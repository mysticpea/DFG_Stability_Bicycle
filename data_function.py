import mysql.connector
from mysql.connector import RefreshOption
import openpyxl
import os
import numpy as np


class Segment:
    def __init__(self, segment_ID, time, speed, angle, exercise_ID,direction):
        self.segment_ID = segment_ID
        self.time = time
        self.speed = speed
        self.angle = angle
        self.exercise_ID = exercise_ID
        self.direction = direction

class exercise:
    def __init__(self, exercise_ID, exercise_name, description, time):
        self.exercise_ID = exercise_ID
        self.exercise_name = exercise_name
        self.description = description
        self.time = time

class user:
    def __init__(self, user_id, gender, age, name,):
        self.user_id = user_id
        self.gender = gender
        self.age = age
        self.name = name
         



def connect_myc():
    db = mysql.connector.connect(
     host="localhost",
    user="root",
    passwd="1995",
    database="dfg"
    )
    refresh = RefreshOption.LOG
    db.cmd_refresh(refresh)
    myc = db.cursor()
    return db, myc


def get_exercise_progrems(myc, exercise_ID): # get the exercise progrems from the database

    myc.execute( f"SELECT * FROM exercise_sement WHERE exercise_ID = {exercise_ID} ORDER BY segment_time")    
    myresult = myc.fetchall()
    Segment_list = []
    for row in myresult:
        s = Segment(row[0], row[1], row[2], row[3], row[4], row[5])
        Segment_list.append(s)
        #print("ID", segment.segment_ID,"time", segment.time,"speed", segment.speed,"angle", segment.angle,"exercise_ID",  segment.exercise_ID,"direction",  segment.direction)
    myc.execute( f"SELECT * FROM exercise_progrems WHERE exercise_ID = {exercise_ID}")
    myresult = myc.fetchall()

    exercise_progrem = exercise(myresult[0][0], myresult[0][1], myresult[0][2], myresult[0][3])
    print("ID", exercise_progrem.exercise_ID,"name", exercise_progrem.exercise_name,"description", exercise_progrem.description,"time",  exercise_progrem.time)

    return Segment_list, exercise_progrem

def get_user(myc, user_id): # get the user from the database
    myc.execute( f"SELECT * FROM users WHERE user_id = {user_id}")
    myresult = myc.fetchall()
    user1 = user(myresult[0][0], myresult[0][1], myresult[0][2], myresult[0][3])
    print("ID", user1.user_id,"name", user1.name)
    return user1
    




def calibrate_body_angle(sheet):
    # take all the angel of the body from the exel file and calculate the average
    shoulder = []
    torso_RL = []
    torso_BF = []
    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=2, max_col=4, values_only=True):
        shoulder.append(row[0])
        torso_RL.append(row[1])
        torso_BF.append(row[2])
    # calculate the average of the angel
    shoulder_avg = sum(shoulder) / len(shoulder)
    torso_RL_avg = sum(torso_RL) / len(torso_RL)
    torso_BF_avg = sum(torso_BF) / len(torso_BF)
    return shoulder_avg, torso_RL_avg, torso_BF_avg


def create_chart(sheet):
        #create the chart in the excel file time will be the x axis and the angel will be the y axis
    chart = openpyxl.chart.LineChart()
    chart.style = 10
    chart.y_axis.title = "Angel"
    chart.x_axis.title = "Time"
    chart.title = "Angel over time"
    data = openpyxl.chart.Reference(sheet, min_col=2, min_row=1, max_row=sheet.max_row, max_col=sheet.max_column)
    chart.add_data(data, titles_from_data=True)

    sheet.add_chart(chart, "F1")


def create_user_directory(user_name):
    directory_path = os.path.join(os.getcwd(), user_name)
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory '{directory_path}' created successfully.")
    except Exception as e:
        print(f"Failed to create directory '{directory_path}'. Error: {e}")
    return directory_path

def create_plot():
    # create the plot for the angel
    import matplotlib.pyplot as plt
    plt.ion()
    plt.show()
    plt.title('Angel over time')
    plt.xlabel('Time')
    plt.ylabel('Angel')
    plt.grid()
    plt.plot([], [], 'ro', label='shoulder')
    plt.plot([], [], 'bo', label='torso_RL')
    plt.plot([], [], 'go', label='torso_BF')
    plt.ylim(-20, 20)

    plt.legend()

    return plt

def save_plot(plt, shoulder, torso_RL, torso_BF):
    # save the plot to the directory
    plt.plot(shoulder, label='shoulder')
    plt.plot(torso_RL, label='torso_RL')
    plt.plot(torso_BF, label='torso_BF')
    plt.xlabel('Time')
    plt.ylabel('Angel')
    plt.legend()
    plt.savefig('plot.png')
    plt.pause(0.05)
    plt.clf()

def update_plot(plt, timer, shoulder, torso_RL, torso_BF, platform_angle_BF, platform_angle_RL, shoulder_avg, torso_RL_avg, torso_BF_avg):
    # update the plot with the new data
    plt.plot(timer, shoulder, 'ro')
    plt.plot(timer, torso_RL, 'bo')
    plt.plot(timer, torso_BF, 'go')
    plt.pause(0.0000005)

    # save only the last 100 points
    if timer > 3:
        plt.xlim(timer - 3, timer)
        # delete the first point
        plt.gca().lines[0].remove()
        plt.gca().lines[1].remove()
        plt.gca().lines[2].remove()


    else:
        plt.xlim(0, 3)
def convert_Allexcel_toSQL():
    file_paths =[
        r"C:\Users\owner\ProjectDFG\calib\dikla_clib_date_14_2024-12-08_1733639663.xlsx",
        r"C:\Users\owner\ProjectDFG\calib\dikla_clib_date_14_2024-12-10_1733822747.xlsx",
        r'C:\Users\owner\ProjectDFG\calib\elia_clib_date_14_2024-12-09_1733742208.xlsx',
        r'C:\Users\owner\ProjectDFG\calib\INBER_clib_date_14_2024-12-09_1733739044.xlsx',
        r'C:\Users\owner\ProjectDFG\calib\michael_clib_date_14_2024-12-09_1733764406.xlsx',
        r'C:\Users\owner\ProjectDFG\calib\noa_clib_date_14_2024-12-09_1733751972.xlsx',
        r'C:\Users\owner\ProjectDFG\calib\ran_clib_date_14_2024-12-09_1733748868.xlsx',
        r'C:\Users\owner\ProjectDFG\calib\roee zehavi_clib_date_14_2024-12-09_1733740868.xlsx',
        r'C:\Users\owner\ProjectDFG\calib\shahar yosefi_clib_date_14_2024-12-09_1733744784.xlsx',
        ]
    db,myc = connect_myc()
    for i in file_paths:#loop to change each workbook that was already created
        wb = openpyxl.load_workbook(i)
        sheet = wb["Sheet"]
        flag = 1
        quality = []
        for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column, values_only=True):
                timer = row[0]
                success = 1
                if row [4] != 0 or row[5] != 0:
                     quality.append(abs(row[1]-row[6] - row[5]+row[5])/(row[5]+row[6]))
                if (row [4] != 0 or row[5] != 0) and flag == 1:
                    max_reaction = 0
                    time_to_max = 0
                    prtobetion = abs(row[4]+row[5]) #one will always be 0 if there is prtobetion
                    quility = []
                    flag = 0 # already got the data for the first pertobetion
                    if row [4] !=0:# check if the prtobetion is in the right or left or back or front by the angel.
                        if row[4] > 0 : #postive angel is front pertobetion
                            direction = 'f'
                        else:
                            direction = 'b'
                    if row [5] !=0:
                        if row[5] < 0: #negative angel is right pertobetion
                            direction = 'r'
                        else:
                            direction = 'l'
                    perto_time = timer # the time of the pertobetion
                if flag == 0 and (row[4] != 0 or row[5] != 0):
                    if abs(row[1] - row[6]) > max_reaction:
                        max_reaction = abs(row[1] - row[6])
                        time_to_max = timer - perto_time
                 
                        
                if row[4] == 0 and row[5] == 0 and flag == 0: #finsihs the prtobetion
                    reaction =  timer - perto_time# total pertobtion time
                    sum_of_quality = 0
                    flag = 1 #can go and check for the next pertobation
                    for i in quality:
                        sum_of_quality += i
                    sum_of_quality = sum_of_quality/len(quality)
                    if reaction < 0.7:#scoring the reaction
                      score =100
                    if reaction > 0.7 and reaction <2:
                        score = 70
                    else:
                        score = 50
                    if reaction > 5:
                        success = 0
                    query = """INSERT INTO exercise_history (score, date, direction, angle, time, response_angle, reaction_time,quality,success_rate) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"""
                    values = (score, '2024-12-09', direction, prtobetion, perto_time, max_reaction, time_to_max, sum_of_quality,success)
                    myc.execute(query, values)
                    db.commit()
                   

def score_plot(save_directory):
    db,myc=connect_myc()
    import matplotlib.pyplot as plt
    direaction = ['l','r','f','b']
    save_directory = r'C:\Users\owner\ProjectDFG\calib\Matlab plots' 
    for d in direaction:
        max_angel =[]
        time_to_max = []
        pertobation = []
        myc.execute(f"SELECT * FROM exercise_history WHERE Direction = '{d}'")
        for i in myc:
            pertobation.append(abs(i[6]))
            max_angel.append(i[8])
            time_to_max.append(i[9])
        reaction_avg = np.mean(time_to_max)
        angel_avg = np.mean(max_angel)
        plt.figure(figsize=(10,10))
        plt.subplot(2,1,1)
        plt.plot(pertobation,time_to_max,'o',linestyle='none',color ='blue')
        plt.axhline(y=reaction_avg, color='green', linestyle='--', label=f'Average Reaction Time: {reaction_avg:.2f}')
        plt.xlabel('Pertobation')
        plt.ylabel('Time to Max')
        plt.title(f'{d} time to max reaction')
        plt.grid(True)
        plt.subplot(2,1,2)
        plt.plot(pertobation,max_angel,'o',linestyle='none',color = 'red')
        plt.axhline(y=angel_avg, color='green', linestyle='--', label=f'Average Max angel: {angel_avg:.2f}')
        plt.xlabel('Pertobation')
        plt.ylabel('Max Angel')
        plt.title(f'{d} Max angel')
        plt.grid(True)
        try:
            plt.savefig(os.path.join(save_directory,f'{d}_reaction_plot.pdf'))
        except:
            print('failed to save to target directory, saved to the Project directory instead')
            plt.savefig((f'{d}_reaction_plot.pdf'))
        plt.show()
        plt.close()


