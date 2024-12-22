from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QComboBox, QCheckBox, QSpinBox, QDoubleSpinBox
from PyQt5.QtWidgets import QAbstractScrollArea, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout, QTabWidget
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import QTimer
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self._main_window = MainWindow
        if self._main_window.objectName():
            self._main_window.setObjectName(u"MainWindow")
        self._main_window.resize(830, 640)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 800, 600))
        
        # Ensure the QTabWidget does not have fixed size constraints
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)

######### THE TABS #########

#Tab 1: START EXERCISE 
        self.Start_exercise = QWidget()
        self.Start_exercise.setObjectName(u"Start_exercise")
        self.tabWidget.addTab(self.Start_exercise, "")

        # Add Delete Participant button
        self.Delete_participant = QPushButton(self.Start_exercise)
        self.Delete_participant.setObjectName(u"Delete_participant")
        self.Delete_participant.setGeometry(QRect(250, 50, 141, 31))
        self.Delete_participant.setFont(font)

        # Add Participant ID label and comboBox
        self.Participant_ID = QLabel(self.Start_exercise)
        self.Participant_ID.setObjectName(u"Participant_ID")
        self.Participant_ID.setGeometry(QRect(0, 0, 251, 61))
        self.Participant_ID.setFont(font)
        self.Participant_ID_label = QComboBox(self.Start_exercise)
        self.Participant_ID_label.setObjectName(u"Participant_ID_label")
        self.Participant_ID_label.setGeometry(QRect(10, 50, 231, 31))
        self.Participant_ID_label.setFont(font)
        
        # Add the table title
        self.exercise_history = QLabel(self.Start_exercise)
        self.exercise_history.setObjectName(u"exercise_history")
        self.exercise_history.setGeometry(QRect(0, 80, 151, 71))
        self.exercise_history.setFont(font)
        
        # Add the table
        self.table_exercise_history_Widget = QTableWidget(self.Start_exercise)
        if (self.table_exercise_history_Widget.columnCount() < 5):
            self.table_exercise_history_Widget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.table_exercise_history_Widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_exercise_history_Widget.setObjectName(u"table_exercise_history_Widget")
        self.table_exercise_history_Widget.setGeometry(QRect(10, 140, 650, 160))
        self.table_exercise_history_Widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_exercise_history_Widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)     # Enable vertical scrolling
        self.table_exercise_history_Widget.verticalHeader().setVisible(False)                   # Hide row numbers

        self.samples = [
        ["1", "2024-12-19", "Type A", "85"],
        ["2", "2024-12-18", "Type B", "90"],
        ["3", "2024-12-17", "Type C", "95"],
        ]
        self.table_exercise_history_Widget.setRowCount(len(self.samples))
        for row, sample in enumerate(self.samples):
                for col, value in enumerate(sample):
                        self.table_exercise_history_Widget.setItem(row, col, QTableWidgetItem(value))
        
        # CheckBox to show the exercise history
        self.show_exercise_history = QCheckBox(self.Start_exercise)
        self.show_exercise_history.setObjectName(u"show_exercise_history")
        self.show_exercise_history.setGeometry(QRect(0, 310, 311, 61))
        self.show_exercise_history.setFont(font)
        
        # Choose the exercise type from the comboBox
        self.exercise_type = QLabel(self.Start_exercise)
        self.exercise_type.setObjectName(u"exercise_type")
        self.exercise_type.setGeometry(QRect(0, 390, 251, 16))
        self.exercise_type.setFont(font)
        self.Exercise_type_label = QComboBox(self.Start_exercise)
        self.Exercise_type_label.setObjectName(u"Exercise_type_label")
        self.Exercise_type_label.setGeometry(QRect(10, 420, 231, 31))
        self.Exercise_type_label.setFont(font)
        
        #button to start the exercise (and the timer to show the running time)
        self.Start_button_tab1 = QPushButton(self.Start_exercise)
        self.Start_button_tab1.setObjectName(u"Start_button_tab1")
        self.Start_button_tab1.setGeometry(QRect(320, 510, 121, 41))
        self.Start_button_tab1.setFont(font)

        # #label to show the total duration of the exercise
        # self.Total_duration = QLabel(self.Start_exercise)
        # self.Total_duration.setObjectName(u"Total_duration")
        # self.Total_duration.setGeometry(QRect(270, 460, 121, 31))
        # font1 = QFont()
        # font1.setPointSize(10)
        # font1.setBold(True)
        # font1.setWeight(75)
        # self.Total_duration.setFont(font1)
        
        # #label to show the running time
        # self.running_time = QLabel(self.Start_exercise)
        # self.running_time.setObjectName(u"running_time")
        # self.running_time.setGeometry(QRect(410, 460, 181, 31))
        # self.running_time.setFont(font1)



#Tab 2: CREATE EXERCISE 
        self.Creat_exercise = QWidget()
        self.Creat_exercise.setObjectName(u"Creat_exercise")
        self.tabWidget.addTab(self.Creat_exercise, "")
        
        # Add Exercise name
        self.Exercise_name = QLabel(self.Creat_exercise)
        self.Exercise_name.setObjectName(u"Exercise_name")
        self.Exercise_name.setGeometry(QRect(0, 0, 251, 61))
        self.Exercise_name.setFont(font)
        
        self.ExerciseName_label_tab2 = QLineEdit(self.Creat_exercise)
        self.ExerciseName_label_tab2.setObjectName(u"ExerciseName_label_tab2")
        self.ExerciseName_label_tab2.setGeometry(QRect(10, 50, 231, 31))
        self.ExerciseName_label_tab2.setFont(font)    
        
        # Add Total Exercise Duration
        self.TotalExerciseDuration_label_tab2 = QLabel(self.Creat_exercise)
        self.TotalExerciseDuration_label_tab2.setObjectName(u"TotalExerciseDuration_label_tab2")
        self.TotalExerciseDuration_label_tab2.setGeometry(QRect(0, 90, 200, 41))
        self.TotalExerciseDuration_label_tab2.setFont(font)
        self.TotalExerciseDuration_label_tab2.setText(u"")
        
        self.SetTotalExeDuration = QSpinBox(self.Creat_exercise)
        self.SetTotalExeDuration.setObjectName(u"SetTotalExeDuration")
        self.SetTotalExeDuration.setGeometry(QRect(10, 130, 231, 31))
        self.SetTotalExeDuration.setFont(font)

        #checkBox to calculate the total duration of the exercise in order to set the amount of perturbation
        self.LockTime_checkBox = QCheckBox(self.Creat_exercise)
        self.LockTime_checkBox.setObjectName(u"LockTime_checkBox")
        self.LockTime_checkBox.setGeometry(QRect(270, 140, 100, 20))
        self.LockTime_checkBox.setFont(font)

        # This is the labels that presents the total exercise time in seconds after we lock the minutes
        total_duration_seconds_label_font = QFont()
        total_duration_seconds_label_font.setBold(True)
        self.total_duration_seconds_label = QLabel(self.Creat_exercise)
        self.total_duration_seconds_label.setFont(total_duration_seconds_label_font)
        self.total_duration_seconds_label.setStyleSheet("color: red;")
        self.total_duration_seconds_label.setObjectName(u"total_duration_seconds_label")
        self.total_duration_seconds_label.setGeometry(QRect(10, 170, 300, 30))
        self.total_duration_seconds_label.setText("")

        #create perturbation table
        self.SetDesiredPertub_label_tab2 = QLabel(self.Creat_exercise)
        self.SetDesiredPertub_label_tab2.setObjectName(u"SetDesiredPertub_label_tab2")
        self.SetDesiredPertub_label_tab2.setGeometry(QRect(0, 200, 211, 31))
        self.SetDesiredPertub_label_tab2.setFont(font)
        
        self.perturbation_start_time_label = QLabel(self.Creat_exercise)
        self.perturbation_start_time_label.setObjectName(u"perturbation_start_time_label")
        self.perturbation_start_time_label.setGeometry(QRect(0, 250, 200, 24))
        self.perturbation_start_time_label.setFont(font)
        
        self.PertubationType_label_tab2 = QLabel(self.Creat_exercise)
        self.PertubationType_label_tab2.setObjectName(u"PertubationType_label_tab2")
        self.PertubationType_label_tab2.setGeometry(QRect(0, 290, 141, 24))
        self.PertubationType_label_tab2.setFont(font)
        
        self.PertubationDegrees_label_tab2 = QLabel(self.Creat_exercise)
        self.PertubationDegrees_label_tab2.setObjectName(u"PertubationDegrees_label_tab2")
        self.PertubationDegrees_label_tab2.setGeometry(QRect(0, 330, 200, 24))
        self.PertubationDegrees_label_tab2.setFont(font)
        
        self.Speed_label_tab2 = QLabel(self.Creat_exercise)
        
        self.Speed_label_tab2.setObjectName(u"Speed_label_tab2")
        self.Speed_label_tab2.setGeometry(QRect(0, 370, 81, 24))
        self.Speed_label_tab2.setFont(font)
        
        # START OF exercise input fields
        self.SetPertubStartTime = QSpinBox(self.Creat_exercise)
        self.SetPertubStartTime.setObjectName(u"SetPertubStartTime")
        self.SetPertubStartTime.setGeometry(QRect(220, 250, 141, 31))
        self.SetPertubStartTime.setFont(font)
        
        self.Perturbation_type = QComboBox(self.Creat_exercise)
        Perturbation_list = ['-','Left', 'Right', 'Forward','Backward','No perturbations']
        self.Perturbation_type.addItems(Perturbation_list)
        self.Perturbation_type.setObjectName(u"Perturbation_type")
        self.Perturbation_type.setGeometry(QRect(220, 290, 141, 31))
        self.Perturbation_type.setFont(font)
        
        self.Perturbation_degrees = QDoubleSpinBox(self.Creat_exercise)
        self.Perturbation_degrees.setObjectName(u"Perturbation_degrees")
        self.Perturbation_degrees.setGeometry(QRect(220, 330, 141, 31))

        self.Speed = QComboBox(self.Creat_exercise)
        Speed_list = ['-','1','2','3','4','5','6','7','8','9','10']
        self.Speed.addItems(Speed_list)
        self.Speed.setObjectName(u"Speed")
        self.Speed.setGeometry(QRect(220, 370, 141, 31))
        self.Speed.setFont(font)
        
        # END OF exercise input fields

        self.Addpertub_button_tab2 = QPushButton(self.Creat_exercise)
        self.Addpertub_button_tab2.setObjectName(u"Addpertub_button_tab2")
        self.Addpertub_button_tab2.setGeometry(QRect(100, 420, 121, 41))
        self.Addpertub_button_tab2.setFont(font)

        self.AddExercise_button_tab2 = QPushButton(self.Creat_exercise)
        self.AddExercise_button_tab2.setObjectName(u"AddExercise_button_tab2")
        self.AddExercise_button_tab2.setGeometry(QRect(410, 510, 131, 41))
        self.AddExercise_button_tab2.setFont(font)

        self.PertubationtableWidget = QTableWidget(self.Creat_exercise)
        self.PertubationtableWidget.setObjectName(u"PertubationtableWidget")
        self.PertubationtableWidget.setGeometry(QRect(420, 200, 530, 192))
        self.PertubationtableWidget.setColumnCount(4)
        self.PertubationtableWidget.setHorizontalHeaderLabels(["Start Time", "Type", "Degrees", "Speed"])
        self.PertubationtableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.PertubationtableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.PertubationtableWidget.verticalHeader().setVisible(True)
        
        self.ClearTable_button_tab2 = QPushButton(self.Creat_exercise)
        self.ClearTable_button_tab2.setObjectName(u"ClearTable_button_tab2")
        self.ClearTable_button_tab2.setGeometry(QRect(600, 410, 171, 41))
        self.ClearTable_button_tab2.setFont(font)
        
    
        #Tab 3: Add new participant
        self.Add_new_participant = QWidget()
        self.Add_new_participant.setObjectName(u"Add_new_participant")
        self.tabWidget.addTab(self.Add_new_participant, "")

        # Add full name
        self.FullName_label_tab3 = QLabel(self.Add_new_participant)
        self.FullName_label_tab3.setObjectName(u"FullName_label_tab3")
        self.FullName_label_tab3.setGeometry(QRect(0, 10, 161, 41))
        self.FullName_line_tab3 = QLineEdit(self.Add_new_participant)
        self.FullName_line_tab3.setObjectName(u"FullName_line_tab3")
        self.FullName_line_tab3.setGeometry(QRect(10, 50, 261, 31))
        
        # Add Participant ID
        self.ParticipantID_label_tab3 = QLabel(self.Add_new_participant)
        self.ParticipantID_label_tab3.setObjectName(u"ParticipantID_label_tab3")
        self.ParticipantID_label_tab3.setGeometry(QRect(0, 90, 161, 41))
        self.ParticipantID_line_tab3 = QLineEdit(self.Add_new_participant)
        self.ParticipantID_line_tab3.setObjectName(u"ParticipantID_line_tab3")
        self.ParticipantID_line_tab3.setGeometry(QRect(10, 130, 261, 31))

        # Add gender
        self.Gender_label_tab3 = QLabel(self.Add_new_participant)
        self.Gender_label_tab3.setObjectName(u"Gender_label_tab3")
        self.Gender_label_tab3.setGeometry(QRect(0, 170, 161, 41))
        self.Gender = QComboBox(self.Add_new_participant)
        Gender_list = ['-','male','female']
        self.Gender.addItems(Gender_list)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setGeometry(QRect(10, 210, 131, 31))
        
        # Add age
        self.Age_label_tab3 = QLabel(self.Add_new_participant)
        self.Age_label_tab3.setObjectName(u"Age_label_tab3")
        self.Age_label_tab3.setGeometry(QRect(0, 250, 161, 41))
        self.Age_label_tab3.setFont(font)
        self.lineEdit_age = QLineEdit(self.Add_new_participant)
        self.lineEdit_age.setObjectName(u"lineEdit_age")
        self.lineEdit_age.setGeometry(QRect(10, 290, 131, 31))
        self.lineEdit_age.setFont(font)
        
        # Add height
        self.Height_label_tab3 = QLabel(self.Add_new_participant)
        self.Height_label_tab3.setObjectName(u"Height_label_tab3")
        self.Height_label_tab3.setGeometry(QRect(0, 330, 161, 41))
        self.SetHeight = QDoubleSpinBox(self.Add_new_participant)
        self.SetHeight.setObjectName(u"SetHeight")
        self.SetHeight.setGeometry(QRect(10, 370, 131, 31))
        
        # Add weight
        self.Weight_label_tab3 = QLabel(self.Add_new_participant)
        self.Weight_label_tab3.setObjectName(u"Weight_label_tab3")
        self.Weight_label_tab3.setGeometry(QRect(0, 410, 161, 41))
        self.SetWeight = QDoubleSpinBox(self.Add_new_participant)
        self.SetWeight.setObjectName(u"SetWeight")
        self.SetWeight.setGeometry(QRect(10, 450, 131, 31))

        self.AddParticipant_button_tab3 = QPushButton(self.Add_new_participant)
        self.AddParticipant_button_tab3.setObjectName(u"AddParticipant_button_tab3")
        self.AddParticipant_button_tab3.setGeometry(QRect(250, 490, 151, 41))

        ######### DONE WITH THE TABS #########


        #set the current tab to the first tab
        self.tabWidget.setCurrentIndex(0)

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    
   
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", u"MainWindow", None))
        self.Delete_participant.setText(_translate("MainWindow", u"Delete Participant", None))
        self.Participant_ID.setText(_translate("MainWindow", u"Participant ID:", None))
        self.exercise_history.setText(_translate("MainWindow", u"Exercise History:", None))
        self.show_exercise_history.setText(_translate("MainWindow", u"Show exercise history", None))
        self.Start_button_tab1.setText(_translate("MainWindow", u"BEGIN", None))
        ___qtablewidgetitem = self.table_exercise_history_Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(_translate("MainWindow", u"Exercise Number \n"
"", None));
        ___qtablewidgetitem1 = self.table_exercise_history_Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(_translate("MainWindow", u"Date \n"
"", None));
        ___qtablewidgetitem2 = self.table_exercise_history_Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(_translate("MainWindow", u"Exercise type\n"
"", None));
        ___qtablewidgetitem3 = self.table_exercise_history_Widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(_translate("MainWindow", u"Score\n"
"", None));
        ___qtablewidgetitem4 = self.table_exercise_history_Widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(_translate("MainWindow", u"Borg\n"
"", None));
        self.exercise_type.setText(_translate("MainWindow", u"Exercise name:", None))
        #self.Total_duration.setText(_translate("MainWindow", u"Total duration:", None))
        #self.running_time.setText(_translate("MainWindow", u"00:00:00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Start_exercise), _translate("MainWindow", u"Start training ", None))
        self.Exercise_name.setText(_translate("MainWindow", u"Exercise name:", None))
        self.TotalExerciseDuration_label_tab2.setText(_translate("MainWindow", u"Total exercise duration [min]: ", None))
        self.LockTime_checkBox.setText(_translate("MainWindow", u"Lock Time", None))
        self.SetDesiredPertub_label_tab2.setText(_translate("MainWindow", u"Set the desired perturbation:", None))
        self.perturbation_start_time_label.setText(_translate("MainWindow", u"Start Perturbation at [sec]: ", None))
        self.PertubationType_label_tab2.setText(_translate("MainWindow", u"Perturbation type:", None))
        self.PertubationDegrees_label_tab2.setText(_translate("MainWindow", u"Perturbation degrees:", None))
        self.Speed_label_tab2.setText(_translate("MainWindow", u"Speed: ", None))
        self.Addpertub_button_tab2.setText(_translate("MainWindow", u"Add perturbation", None))
        self.AddExercise_button_tab2.setText(_translate("MainWindow", u"Add exercise", None))
        self.ClearTable_button_tab2.setText(_translate("MainWindow", u"Clear perturbation table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Creat_exercise), _translate("MainWindow", u"Create training ", None))
        self.FullName_label_tab3.setText(_translate("MainWindow", u"Participant full name: ", None))
        self.ParticipantID_label_tab3.setText(_translate("MainWindow", u"Participant ID: ", None))
        self.Gender_label_tab3.setText(_translate("MainWindow", u"Gender:", None))
        self.Height_label_tab3.setText(_translate("MainWindow", u"Height [cm]: ", None))
        self.Weight_label_tab3.setText(_translate("MainWindow", u"Weight [Kg]: ", None))
        self.Age_label_tab3.setText(_translate("MainWindow", u"Age: ", None))
        self.AddParticipant_button_tab3.setText(_translate("MainWindow", u"Add participant", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Add_new_participant), _translate("MainWindow", u"Add new participant ", None))
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = 0
        self.ui.tabWidget.currentChanged.connect(self.adjust_tab_size)
       
        #### Connect the buttons to the action - Tab 1 ####
        self.ui.Delete_participant.clicked.connect(self.delete_participant)
        self.ui.Start_button_tab1.clicked.connect(self.start_exercise)
        self.ui.show_exercise_history.stateChanged.connect(self.toggle_table_display)
        
        #### Connect the buttons to the action - Tab 2 ####
        self.ui.LockTime_checkBox.stateChanged.connect(self.update_total_duration_label)
        self.ui.Addpertub_button_tab2.clicked.connect(self.add_perturbation)
        self.ui.ClearTable_button_tab2.clicked.connect(self.clear_perturbation_table)
        self.ui.AddExercise_button_tab2.clicked.connect(self.Add_Exercise)

        #### Connect the buttons to the action - Tab 3 ####
        self.ui.AddParticipant_button_tab3.clicked.connect(self.add_participant)

    def adjust_tab_size(self, index):
        if index == 0:  # Start_exercise tab
            self.setMinimumSize(QSize(800, 650))
            self.setMaximumSize(QSize(800, 650))
            self.resize(800, 650)
        elif index == 1:  # Creat_exercise tab
            self.setMinimumSize(QSize(1000, 650))
            self.setMaximumSize(QSize(1000, 650))
            self.resize(1000, 650)
        elif index == 2:  # Add_new_participant tab
            self.setMinimumSize(QSize(700, 650))
            self.setMaximumSize(QSize(700, 650))
            self.resize(700, 650)
        self.adjustSize()  # Adjust the size of the window to fit the contents


        #### Functions - Tab 1 ####
    def delete_participant(self):
        print("Delete Participant button clicked")

    def start_exercise(self):
        print("Start Exercise button clicked")
        initial_dialog = InitialConfirmationDialog(self)
        if initial_dialog.exec_() == QDialog.Accepted:
            trainee_id = "12345"  # Replace with actual trainee ID
            control_dialog = ExerciseControlDialog(self, trainee_id)
            control_dialog.exec_()
        
    def update_timer(self):
        self.time_elapsed += 1
        print(f"Time elapsed: {self.time_elapsed} seconds")
        # Update the timer display here if needed
        hours, remainder = divmod(self.time_elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.ui.running_time.setText(f"{hours:02}:{minutes:02}:{seconds:02}")

        # Toggle table contents dynamically
    def toggle_table_display(self):
        mock_data = [
                ["6", "2024-12-14", "Type F", "87"],
                ["7", "2024-12-13", "Type G", "89"],
                ["8", "2024-12-12", "Type H", "91"],
        ]
        
        if self.ui.show_exercise_history.isChecked():
                print("Checkbox is checked")
                # Add all samples to the table
                current_row_count = self.ui.table_exercise_history_Widget.rowCount()
                self.ui.table_exercise_history_Widget.setRowCount(current_row_count + len(mock_data))
                for row, sample in enumerate(mock_data):
                        for col, value in enumerate(sample):
                                self.ui.table_exercise_history_Widget.setItem(current_row_count + row, col, QTableWidgetItem(value))
        else:
                print("Checkbox is unchecked")
                # Remove the added rows
                current_row_count = self.ui.table_exercise_history_Widget.rowCount()
                new_row_count = current_row_count - len(mock_data)
                self.ui.table_exercise_history_Widget.setRowCount(new_row_count)

    #### Functions - Tab 2 #### 
    def update_total_duration_label(self):
        if self.ui.LockTime_checkBox.isChecked():
            total_duration_text = self.ui.SetTotalExeDuration.text()
            try:
                total_duration_seconds = float(total_duration_text) * 60  # Assuming the input is in minutes
                self.ui.total_duration_seconds_label.setText(f"Total duration in seconds: {total_duration_seconds}")
            except ValueError:
                self.ui.total_duration_seconds_label.setText("Invalid duration")
        else:
            self.ui.total_duration_seconds_label.setText("")
    
    def add_perturbation(self):
        start_time = self.ui.SetPertubStartTime.text()
        perturbation_type = self.ui.Perturbation_type.currentText()
        perturbation_degrees = self.ui.Perturbation_degrees.text()
        speed = self.ui.Speed.currentText()
        
        row_position = self.ui.PertubationtableWidget.rowCount()
        self.ui.PertubationtableWidget.insertRow(row_position)
        
        self.ui.PertubationtableWidget.setItem(row_position, 0, QTableWidgetItem(start_time))
        self.ui.PertubationtableWidget.setItem(row_position, 1, QTableWidgetItem(perturbation_type))
        self.ui.PertubationtableWidget.setItem(row_position, 2, QTableWidgetItem(perturbation_degrees))
        self.ui.PertubationtableWidget.setItem(row_position, 3, QTableWidgetItem(speed))
    
    def clear_perturbation_table(self):
        self.ui.PertubationtableWidget.clearContents()
        self.ui.PertubationtableWidget.setRowCount(0)

    def Add_Exercise(self):
            print("Add Exercise button clicked")

        #### Functions - Tab 3 ####
    def add_participant(self):
        print("Add Participant button clicked")

class InitialConfirmationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Safety check")
        self.setGeometry(750, 500, 450, 200)

        font = QFont()
        font.setPointSize(10)  # Set the font size
        font.setBold(True)     # Set the font to bold

        self.label = QLabel("Please make sure that the trainee is securely \nconnected to the harness!", self)
        self.label.setGeometry(30, 30, 440, 60)
        self.label.setFont(font)  # Apply the font to the label
        self.continue_button = QPushButton("Continue", self)
        self.continue_button.setGeometry(40, 130, 160, 40)
        self.continue_button.clicked.connect(self.accept)

        self.return_button = QPushButton("Return", self)
        self.return_button.setGeometry(240, 130, 160, 40)
        self.return_button.clicked.connect(self.reject)

class ExerciseControlDialog(QDialog):
    def __init__(self, parent=None, trainee_id=""):
        super().__init__(parent)
        self.setWindowTitle("Exercise Control")
        self.setGeometry(750, 550, 400, 300)

        self.time_label = QLabel("Time elapsed: 0 seconds", self)
        self.time_label.setGeometry(10, 10, 380, 30)

        self.trainee_id_label = QLabel(f"Trainee ID: {trainee_id}", self)
        self.trainee_id_label.setGeometry(10, 50, 380, 30)

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.setGeometry(10, 90, 180, 40)
        self.pause_button.setStyleSheet("background-color: orange")
        self.pause_button.clicked.connect(self.pause_timer)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(200, 90, 180, 40)
        self.stop_button.setStyleSheet("background-color: red")
        self.stop_button.clicked.connect(self.stop_timer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.time_elapsed = 0
        self.timer.start(1000)  # Update every second

    def update_time(self):
        self.time_elapsed += 1
        self.time_label.setText(f"Time elapsed: {self.time_elapsed} seconds")

    def pause_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pause_button.setText("Resume")
        else:
            self.timer.start(1000)
            self.pause_button.setText("Pause")

    def stop_timer(self):
        self.timer.stop()
        self.accept()  # Close the dialog



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())