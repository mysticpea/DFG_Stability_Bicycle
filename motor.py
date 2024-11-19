from edcon.edrive.com_modbus import ComModbus
from edcon.edrive.motion_handler import MotionHandler
from edcon.utils.logging import Logging
import time
import data_function
import openpyxl


def move_platform(mots, dirction, angel,speed):
    # mots=connect()
    step=angel*9000
    match dirction:
        case 'f':
            # move forward
            position_0=step
            position_1=step
            pass
        case 'b':
            # move backward
            position_0=(-step)
            position_1=(-step)
            pass
        case 'l':
            # move left
            position_0=(-step)
            position_1=step
            pass
        case 'r':
            # move right
            position_0=step
            position_1=(-step)
            pass
        case 'h':
            # move home
            position_0=0
            position_1=0
            pass
    
    mots[0].position_task(position_0, speed, absolute=True, nonblocking=True)
    mots[1].position_task(position_1, speed, absolute=True, nonblocking=True)
    target_positions_reached = [mot.target_position_reached() for mot in mots]
    while True:
        target_positions_reached = [mot.target_position_reached() for mot in mots]
        if all(target_positions_reached):
            break

def connect():
    coms = [ComModbus(ip_address='192.168.0.11'),   # Right motor
            ComModbus(ip_address='192.168.0.3')]    # Left motor
    
    for com in coms:
       if not com.connected():
        exit()
    mots = [MotionHandler(com) for com in coms]

    for mot in mots:
       mot.acknowledge_faults()
       mot.enable_powerstage()
       if not mot.referenced():
        mot.referencing_task()
    return mots

# if __name__ == "__main__":
#     mots = connect()
#     db ,myc = data_function.connect_myc()
#     Segment_list, exercise_progrem = data_function.get_exercise_progrems(myc, 2)
#     user1 = data_function.get_user(myc, 209146216)

#     x=0

#     move_platform(mots, 'h', 0, 200)
    
#     start_time = time.time()
#     timer = round((time.time() - start_time),6)
#     segment_time = 0
#     platform_angle = [0,0] # [0] = BF, [1] = RL

#     while timer<exercise_progrem.time:
#         timer = round((time.time() - start_time),6)
#         print (timer)
#         if x<len(Segment_list) and timer>Segment_list[x].time:
#             move_platform(mots, Segment_list[x].direction, Segment_list[x].angle, Segment_list[x].speed)
#             segment_time = round(Segment_list[x].time)
#             x+=1
#         if segment_time!=0 and segment_time + 5 < timer:
#             move_platform(mots, 'h', 0, 200)
#             segment_time = 0
            
             
#     for mot in mots:
#         mot.shutdown()