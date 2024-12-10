import cv2
import pyzed.sl as sl
import cv_viewer.tracking_viewer as cv_viewer
import numpy as np
import math as m
import time
from ctypes import *
import mysql.connector
from mysql.connector.constants import RefreshOption
import ogl_viewer.viewer as gl
from edcon.edrive.com_modbus import ComModbus
from edcon.edrive.motion_handler import MotionHandler
from edcon.utils.logging import Logging
import motor
import z_camera
import openpyxl
import data_function
import matplotlib.pyplot as plt
import Gui

# function to check if the angel is a good response to the platform angel
def angel_analsis(angel, angel_avg ,platform_angel,direction):
    # angel = [0]=shoulder, [1] = torso_RL, [2] torso_BF
    # angel_avg = [0]=shoulder, [1] = torso_RL, [2] torso_BF
    # platform_angel = [0] = BF, [1] = RL
    # direction = 'f' or 'b' or 'l' or 'r'
    match direction:
        case 'f':
            if angel[2] > angel_avg[2] + 0.8*platform_angel[0]:
                return True
            else:
                return False    
        case 'b':
            if angel[2] < angel_avg[2] - 0.9*platform_angel[0]:
                return True
            else:
                return False
        case 'l':
            if angel[1] > angel_avg[1] + platform_angel[1] or angel[0] > angel_avg[0] + platform_angel[1]:
                return True
            else:
                return False
        case 'r':
            if angel[1] < angel_avg[1] - platform_angel[1] or angel[0] < angel_avg[0] - platform_angel[1]:
                return True
            else:
                return False

if __name__ == '__main__':
    
    # connect to camera
    # zed, camera_data=z_camera.stert_camera_recorded()
    zed, camera_data=z_camera.stert_camera_live()
   
    # connect to data base
    db, myc=data_function.connect_myc()
    Segment_list, exercise_progrem = data_function.get_exercise_progrems(myc, 14)
    user1 = data_function.get_user(myc, 20)
    x=0

    # create excel file for the data 
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['time', 'shoulder', 'torso_RL', 'torso_BF', 'platform_angle_bf', 'platform_angle_rl', 'angle_avg_shoulder', 'angle_avg_torso_RL', 'angle_avg_torso_BF'])

    # create a plot
    plot = data_function.create_plot()

    # connect to motors
    motors = motor.connect()
    motor.move_platform(motors, 'h', 0, 150)


    key_wait = 10
    start_time = time.time()
    timer = round((time.time() - start_time),6)
    segment_time = 0
    platform_angle = [0,0] # [0] = BF, [1] = RL
    angel_avg = [0,0,0] # [0]=shoulder, [1] = torso_RL, [2] torso_BF
    score=[]
    ##################################### the mian loop  ###################################
    while timer<exercise_progrem.time and key_wait==10 :
        timer = round((time.time() - start_time),6)
        print (timer)
        key_wait = z_camera.camera_work(zed, camera_data)
        keypoint = z_camera.take_co(camera_data.bodies)                                                         # 0= pelvis, 3= neck, 5= L_shoulder, 12= R_shoulder

        
        if len(keypoint)!=0:
         angel = z_camera.angel_analsis(keypoint)                                                               # [0]=shoulder, [1] = torso_RL, [2] torso_BF
         sheet.append([timer, angel[0], angel[1], angel[2], platform_angle[0], platform_angle[1], angel_avg[0], angel_avg[1], angel_avg[2]])              

           
            # calibrate the bady angel for 60 sec
        if timer>15 and angel_avg[0]==0:
            angel_avg = data_function.calibrate_body_angle(sheet)                                               

        if segment_time!=0 and (segment_time + 3 < timer or angel_analsis(angel, angel_avg, platform_angle, Segment_list[x-1].direction)):
            motor.move_platform(motors, 'h', 0, 100)
            
            if timer-segment_time<1:
             score_100=+1
             score=100
            elif timer-segment_time<1.5:
             score_70=+1
             score=70
            elif timer-segment_time<2:
             score_50=+1
             score=50
             success=+1
            else:

             score=0
             


            print(score)
            segment_time = 0
            data_function.print_plot(plot, angel, angel_avg, platform_angle, Segment_list[x-1].direction,score)
            platform_angle = [0,0]

        
        if x<len(Segment_list) and timer>Segment_list[x].time:
            motor.move_platform(motors, Segment_list[x].direction, Segment_list[x].angle, Segment_list[x].speed)
            
            if Segment_list[x].direction == 'f' or Segment_list[x].direction == 'b':
                platform_angle[0] =Segment_list[x].angle
            if Segment_list[x].direction == 'r' or Segment_list[x].direction == 'l':
                platform_angle[1] =Segment_list[x].angle
            segment_time = timer
            x=x+1
        # rate_of_success=(success/len(Segment_list))*100



# למעלה זה שמאלה ולמטה זה ימינה


    date = time.strftime("%Y-%m-%d")
    # shutdown all
    data_function.create_chart(sheet)
    exel_file_name = user1.name + "_exercise_" + str(exercise_progrem.exercise_ID) + "_" + date +  ".xlsx"     
    wb.save(exel_file_name)    
    for mot in motors:
        mot.shutdown()
    db.close()
    zed.close()
    cv2.destroyAllWindows()
    print("finish")

