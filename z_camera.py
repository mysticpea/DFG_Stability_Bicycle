import csv
import cv2
import sys
import pyzed.sl as sl
import cv_viewer.tracking_viewer as cv_viewer
import numpy as np
import math as m
import time
import socket
from ctypes import *
import random
import ogl_viewer.viewer as gl
class CameraData:
    def __init__(self, display_resolution, image_scale, body_runtime_param, bodies, image):
        self.display_resolution = display_resolution
        self.image_scale = image_scale
        self.body_runtime_param = body_runtime_param
        self.bodies = bodies
        self.image = image

def stert_camera_recorded():
    zed = sl.Camera()  # Create a Camera object
   
    # Path of .svo2 file captured by ZED for testing
    input_path = "C:/Users/owner/Documents/ZED/HD2K_SN28318474_10-30-32.svo2"
    # Create a InitParameters object and set configuration parameters
    
    init_params = sl.InitParameters()
    init_params.set_from_svo_file(input_path)
    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    # Enable Positional tracking (mandatory for object detection)
    positional_tracking_parameters = sl.PositionalTrackingParameters()
    # If the camera is static, uncomment the following line to have better performances
    positional_tracking_parameters.set_as_static = True
    zed.enable_positional_tracking(positional_tracking_parameters)

    body_param = sl.BodyTrackingParameters()
    body_param.enable_tracking = True  # Track people across images flow
    body_param.enable_body_fitting = True  # Smooth skeleton move
    body_param.detection_model = sl.BODY_TRACKING_MODEL.HUMAN_BODY_FAST
    body_param.body_format = sl.BODY_FORMAT.BODY_34  # Choose the BODY_FORMAT you wish to use
    display_resolution = sl.Resolution(min(zed.get_camera_information().camera_configuration.resolution.width, 1280), min(zed.get_camera_information().camera_configuration.resolution.height, 720))
    image_scale = [display_resolution.width / zed.get_camera_information().camera_configuration.resolution.width
                 , display_resolution.height / zed.get_camera_information().camera_configuration.resolution.height]
    body_runtime_param = sl.BodyTrackingRuntimeParameters()
    body_runtime_param.detection_confidence_threshold = 40
    bodies = sl.Bodies()
    image = sl.Mat()
    camera_data = CameraData(
    display_resolution,  # דוגמה לרזולוציית תצוגה
    image_scale,  # דוגמה לסקייל של התמונה
    body_runtime_param,  # דוגמה לפרמטרים של גוף בזמן ריצה
    bodies,  # דוגמה לרשימת גופים
    image  # דוגמה לתמונה (יכול להיות אובייקט תמונה בפועל)
)
    # Enable Object Detection module
    zed.enable_body_tracking(body_param)
    return zed, camera_data    


def stert_camera_live():
    zed = sl.Camera()  # Create a Camera object
   
    # Create a InitParameters object and set configuration parameters
    
    init_params = sl.InitParameters()
    #init_params.set_from_svo_file(input_path)
    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(1)

    # Enable Positional tracking (mandatory for object detection)
    positional_tracking_parameters = sl.PositionalTrackingParameters()
    # If the camera is static, uncomment the following line to have better performances
    positional_tracking_parameters.set_as_static = True
    zed.enable_positional_tracking(positional_tracking_parameters)

    body_param = sl.BodyTrackingParameters()
    body_param.enable_tracking = True  # Track people across images flow
    body_param.enable_body_fitting = False  # Smooth skeleton move
    body_param.detection_model = sl.BODY_TRACKING_MODEL.HUMAN_BODY_FAST
    body_param.body_format = sl.BODY_FORMAT.BODY_34  # Choose the BODY_FORMAT you wish to use
    display_resolution = sl.Resolution(min(zed.get_camera_information().camera_configuration.resolution.width, 1280), min(zed.get_camera_information().camera_configuration.resolution.height, 720))
    image_scale = [display_resolution.width / zed.get_camera_information().camera_configuration.resolution.width
                 , display_resolution.height / zed.get_camera_information().camera_configuration.resolution.height]
    body_runtime_param = sl.BodyTrackingRuntimeParameters()
    body_runtime_param.detection_confidence_threshold = 40
    bodies = sl.Bodies()
    image = sl.Mat()
    camera_data = CameraData(
    display_resolution,  # דוגמה לרזולוציית תצוגה
    image_scale,  # דוגמה לסקייל של התמונה
    body_runtime_param,  # דוגמה לפרמטרים של גוף בזמן ריצה
    bodies,  # דוגמה לרשימת גופים
    image  # דוגמה לתמונה (יכול להיות אובייקט תמונה בפועל)
)
    # Enable Object Detection module
    zed.enable_body_tracking(body_param)
    return zed, camera_data    

def camera_work(zed, camera_data):
    key_wait = 10

    if zed.grab() == sl.ERROR_CODE.SUCCESS:
        # Retrieve left image
        zed.retrieve_image(camera_data.image, sl.VIEW.LEFT, sl.MEM.CPU, camera_data.display_resolution)
        # Retrieve bodies            
        zed.retrieve_bodies(camera_data.bodies, camera_data.body_runtime_param)
            # Update GL view
        #viewer.update_view(image, bodies)
            # Update OCV view
        image_left_ocv = camera_data.image.get_data()
        
        cv_viewer.render_2D(image_left_ocv,camera_data.image_scale, camera_data.bodies.body_list, True, sl.BODY_FORMAT.BODY_34)
        # image_left_ocv = cv2.resize(image_left_ocv, (0,0),fx=2,fy=2)                        
        cv2.imshow("ZED | 2D View", image_left_ocv)
         
        key = cv2.waitKey(key_wait)
        if key == 113:  # for 'q' key
                print("Exiting...")
                key_wait=0
            
        # if key == 109:  # for 'm' key
        #     if (key_wait > 0):
        #             print("Pause")
        #             key_wait = 0
        #     else:
        #         print("Restart")
        #         key_wait = 10
    return key_wait            
 
def take_co(bodies):
    keypoint = []
    obj_array=bodies.body_list
    for i in range(len(obj_array)):
        obj_data = obj_array[i]
        position = obj_data.head_position
        bounding_box = obj_data.bounding_box
        keypoint = obj_data.keypoint
    return keypoint

def angel_analsis(keypoint):
     shoulder=0
     torso_RL=0
     torso_BF=0
     neck = keypoint[3]
     pelvis = keypoint[0]
     L_shoulder = keypoint[5]
     R_shoulder = keypoint[12]
     shoulder = np.around(m.degrees(m.atan2(L_shoulder[0] - R_shoulder[0], L_shoulder[1] -R_shoulder[1]))-90, decimals=2)
     torso_RL = np.around(m.degrees(m.atan2(pelvis[0] - neck[0], pelvis[1] -neck[1])), decimals=2)
     torso_BF = np.around(m.degrees(m.atan2(pelvis[1] - neck[1], pelvis[2] -neck[2]))-90, decimals=2)
     all_angel=[shoulder,torso_RL,torso_BF]
     #print("torso_R-L=", torso_RL,"/// torso_B-F=" , torso_BF,  "/// shoulder=", shoulder)
     return all_angel
     


if __name__ == '__main__':
    zed, camera_data=stert_camera_recorded()
    key_wait = 10
    ##################################### the mian loop  ###################################
    while key_wait==10 :
        key_wait = camera_work(zed,camera_data)
        keypoint = take_co(camera_data.bodies)
        if len(keypoint)!=0:
         angel = angel_analsis(keypoint)
        


