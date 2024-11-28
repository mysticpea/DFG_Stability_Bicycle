import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1995",
    database="dfg"
)

mycursor = db.cursor()

# הכנסת מידע על משתמש
insert_user_query = """
INSERT INTO users (user_id, name, gender, age)
VALUES (%s, %s, %s, %s)
"""
user_data = (209146216, 'roee zehavi', 'm', 26)

# יצירת טבלת משתמש
create_users_table_query = """
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name CHAR(255),
    gender ENUM('m', 'f'),
    age TINYINT
)
"""

# יצירת טבלת אימונים
create_exercise_progrems_table_query = """
CREATE TABLE exercise_progrems (
    exercise_ID INT PRIMARY KEY,
    exercise_name VARCHAR(50),
    description VARCHAR(50),
    time INT
)
"""

# הכנסת מידע על אימון
insert_exercise_query = """
INSERT INTO exercise_progrems (exercise_ID, exercise_name, description, time)
VALUES (%s, %s, %s, %s)
"""
exercise_data = (2, 'sec', 'sec exercise', 4*60)

# mycursor.execute(insert_exercise_query, exercise_data)


# יצירת טבלת היסטורית אימונים
create_exercise_history_table_query = """
CREATE TABLE exercise_history (
    exercise_Number INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    exercise_ID INT,
    score INT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (exercise_ID) REFERENCES exercise_progrems(exercise_ID)
)
"""


# יצירת טבלת סגמנטים
create_exercise_sement_table_query = """
CREATE TABLE exercise_sement (
    segment_ID INT AUTO_INCREMENT PRIMARY KEY,
    segment_time INT,
    speed INT,
    angle INT,
    exercise_ID INT,
    Direction ENUM('f', 'b', 'l', 'r', 'h'),
    FOREIGN KEY (exercise_ID) REFERENCES exercise_progrems(exercise_ID)
)
"""
#הוספת עומודה בטבלה שנקראת For_test
alter_table_query = f"ALTER TABLE {'exercise_sement'} ADD COLUMN {'For_test'} {'INT'}"

# הכנסת נתונים לטבלת סגמנטים

insert_exercise_sement_query = """
INSERT INTO exercise_sement (segment_time, speed, angle, exercise_ID, Direction)
VALUES (%s, %s, %s, %s, %s)
"""
exercise_ID= 2
sement_data = [(10, 50, 5, exercise_ID, 'h'),(20, 50, 5, exercise_ID, 'f'),(30, 50, 5, exercise_ID, 'b'),(40, 50, 5, exercise_ID, 'l'),(50, 50, 5, exercise_ID, 'r')]
# for i in sement_data:
#     mycursor.execute(insert_exercise_sement_query, i)


# פעולות על טבלאות
# שינוי סוג משתנה בעמודה בטבלה
alter_table_query1 = f"ALTER TABLE {'exercise_progrems'} MODIFY COLUMN {'time'} {'INT'}"         

# הוספת עמודה לטבלה
alter_table_query2 = f"ALTER TABLE {'exercise_progrems'} ADD COLUMN {'time'} {'INT'}"

# מחיקת עמודה מטבלה
alter_table_query3 = f"ALTER TABLE {'exercise_progrems'} DROP COLUMN {'time'}"

# מחיקת טבלה
alter_table_query4 = f"DROP TABLE {'exercise_progrems'}"

# עדכון ערך בטבלה
alter_table_query5 = f"UPDATE {'exercise_progrems'} SET {'time'} = 300 WHERE {'exercise_ID'} = 1"

# מחיקת רשומה מטבלה
alter_table_query6 = f"DELETE FROM {'exercise_progrems'} WHERE {'exercise_ID'} = 1"

# שליפת כל הסגמנטים של אימון מסוים
# alter_table_query7 = f"SELECT * FROM {'exercise_sement'} WHERE {'exercise_ID'} = 1"
# mycursor.execute(alter_table_query7)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# מיין סגמנטים לפי זמן
alter_table_query8 = f"SELECT * FROM {'exercise_sement'} WHERE {'exercise_ID'} = 1 ORDER BY {'segment_time'}"
mycursor.execute(alter_table_query8)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


#             בחירת ביצוע פעולה- לבחור פעולה ואת להוריד את הערה בשורה למטה


mycursor.execute(alter_table_query)
# mycursor.execute(insert_exercise_sement_query, sement_data)
db.commit()
