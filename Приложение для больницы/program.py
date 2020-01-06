# -*- coding: utf-8 -*-

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random


person = 0
table = [0,0]

# ----------------класс даты ввода информации-------------------
class Ui_Dia2(QtWidgets.QDialog):
    def d(self, date):
        self.ff.data.setText(date.toString("dd/MM/yy"))

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.ff = root

        calendarWidget = QtWidgets.QCalendarWidget()
        calendarWidget.setGeometry(QtCore.QRect(0, 0, 291, 191))
        self.setFixedSize(291, 191)
        self.setWindowTitle('Календарь')
        calendarWidget.clicked.connect(self.d)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(calendarWidget)
        self.setLayout(layout)


# ----------------класс для личных данных пациента-------------------
class Ui_Form_person(QtWidgets.QDialog):
    def openA1(self):
        if (self.number.text() == '' or self.number.text() == None):

            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка!!!")
            error_message.showMessage("Номер у пациента должен быть обязательно!")
        else:
            self.main.t1 = str(self.number.text())
            self.main.t2 = str(self.fullname.text())
            self.main.t3 = str(self.diagnos.text())
            self.main.t4 = str(self.ageBox.currentText())
            buf = 0
            if (self.sexBox.currentText() == "мужской"):
                buf = 1
            if (self.sexBox.currentText() == "женский"):
                buf = 2
            self.main.t5 = str(buf)
            self.main.t6 = str(self.school.text())
            self.main.t7 = str(self.classBox.currentText())
            if (self.levelBox.currentText() == '1 ступень  (1-4класс)'):
                buf = 1
            if (self.levelBox.currentText() == '2 ступень  (5-8класс)'):
                buf = 2
            if (self.levelBox.currentText() == '3 ступень  (9-11класс)'):
                buf = 3
            self.main.t8 = str(buf)
            self.main.t9 = str(self.data.text())

            self.main.ans_1.setEnabled(True)
            self.main.pushButton.setEnabled(False)
            self.main.tabWidget.setEnabled(True)
            self.close()

    def cl(self):
        self.close()

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root
        self.dialog2 = Ui_Dia2(self)

        self.setGeometry(200, 50, 331, 372)
        self.setFixedSize(331, 372)
        self.setWindowTitle('Личные данные')
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setStyleSheet("")

        self.label_1 = QtWidgets.QLabel('Личные данные пациента', self).setGeometry(QtCore.QRect(40, 10, 221, 16))
        self.label_2 = QtWidgets.QLabel('Номер пациента', self).setGeometry(QtCore.QRect(40, 50, 141, 16))
        self.label_3 = QtWidgets.QLabel('ФИО пациента', self).setGeometry(QtCore.QRect(40, 80, 121, 16))
        self.label_5 = QtWidgets.QLabel('Диагноз(если есть)', self).setGeometry(QtCore.QRect(40, 110, 160, 16))
        self.label_6 = QtWidgets.QLabel('Возраст', self).setGeometry(QtCore.QRect(40, 140, 71, 16))
        self.label_7 = QtWidgets.QLabel('Пол', self).setGeometry(QtCore.QRect(40, 170, 41, 16))
        self.label_8 = QtWidgets.QLabel('Школа', self).setGeometry(QtCore.QRect(40, 200, 61, 16))
        self.label_9 = QtWidgets.QLabel('Класс', self).setGeometry(QtCore.QRect(40, 230, 51, 16))
        self.label_10 = QtWidgets.QLabel('Ступень обучения', self).setGeometry(QtCore.QRect(40, 260, 151, 16))
        self.label_11 = QtWidgets.QLabel('Дата', self).setGeometry(QtCore.QRect(40, 290, 51, 16))


        self.number = QtWidgets.QLineEdit(self)
        self.number.setGeometry(QtCore.QRect(200, 50, 113, 20))
        self.fullname = QtWidgets.QLineEdit(self)
        self.fullname.setGeometry(QtCore.QRect(200, 80, 113, 20))
        self.diagnos = QtWidgets.QLineEdit(self)
        self.diagnos.setGeometry(QtCore.QRect(200, 110, 113, 20))
        self.data = QtWidgets.QLineEdit(self)
        self.data.setGeometry(QtCore.QRect(100, 290, 71, 20))

        #self.data1button = QtWidgets.QPushButton('найти', self)
        #self.data1button.setGeometry(QtCore.QRect(250, 110, 51, 23))
        #font = QtGui.QFont()
        #font.setFamily("Arial")
        #font.setWeight(20)
        #self.data1button.setFont(font)
        #self.data1button.clicked.connect(self.dialog1.exec)

        self.data2button = QtWidgets.QPushButton('найти', self)
        self.data2button.setGeometry(QtCore.QRect(170, 290, 51, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setWeight(20)
        self.data2button.setFont(font)
        self.data2button.clicked.connect(self.dialog2.exec)

        self.sexBox = QtWidgets.QComboBox(self)
        self.sexBox.setGeometry(QtCore.QRect(90, 170, 91, 22))
        self.sexBox.addItems(["мужской","женский"])

        self.school = QtWidgets.QSpinBox(self)
        self.school.setGeometry(QtCore.QRect(110, 200, 51, 22))
        self.school.setMaximum(1000)

        self.classBox = QtWidgets.QComboBox(self)
        self.classBox.setGeometry(QtCore.QRect(110, 230, 61, 22))
        self.classBox.addItems(['1','2','3','4','5','6','7','8','9','10','11'])

        self.levelBox = QtWidgets.QComboBox(self)
        self.levelBox.setGeometry(QtCore.QRect(200, 260, 120, 22))
        self.levelBox.addItems(["1 ступень  (1-4класс)","2 ступень  (5-8класс)","3 ступень  (9-11класс)"])

        self.ageBox = QtWidgets.QComboBox(self)
        self.ageBox.setGeometry(QtCore.QRect(120, 140, 61, 22))
        self.ageBox.addItems(["5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])

        self.savebutton = QtWidgets.QPushButton('Сохранить', self)
        self.savebutton.setGeometry(QtCore.QRect(150, 340, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setWeight(20)
        self.savebutton.setFont(font)
        self.savebutton.clicked.connect(self.openA1)

        self.cleanbutton = QtWidgets.QPushButton('Отмена', self)
        self.cleanbutton.setGeometry(QtCore.QRect(240, 340, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setWeight(20)
        self.cleanbutton.setFont(font)
        self.cleanbutton.clicked.connect(self.cl)


# ----------------класс анкеты для родителя и учителя-------------------
class Ui_Anketa1(QtWidgets.QDialog):
    def saveA1(self):
        if(person == 1):
            nametable = 'Children'
        elif(person == 2):
            nametable = 'Children2'

        connection = sqlite3.connect('Anketa1.db')
        query = 'CREATE TABLE IF NOT EXISTS ' + nametable + ' (Number TEXT,Fullname TEXT,Date TEXT,Age INTEGER,class INTEGER,school INTEGER,' + \
                'Diagnos TEXT,Sex INTEGER,Level INTEGER,answer1 INTEGER,answer2 INTEGER,answer3 INTEGER,answer4 INTEGER,answer5 INTEGER,' + \
                'answer6 INTEGER,answer7 INTEGER,answer8 INTEGER,answer9 INTEGER,answer10 INTEGER,answer11 INTEGER,answer12 INTEGER,' + \
                'answer13 INTEGER,answer14 INTEGER,answer15 INTEGER,answer16 INTEGER,answer17 INTEGER,answer18 INTEGER,answer19 INTEGER,' + \
                'answer20 INTEGER,answer21 INTEGER,answer22 INTEGER,answer23 INTEGER,answer24 INTEGER,answer25 INTEGER,answer26 INTEGER,' + \
                'answer27 INTEGER,answer28 INTEGER,answer29 INTEGER,answer30 INTEGER,answer31 INTEGER,answer32 INTEGER,answer33 INTEGER,' + \
                'answer34 INTEGER,answer35 INTEGER,answer36 INTEGER,answer37 INTEGER,answer38 INTEGER,answer39 INTEGER,answer40 INTEGER,' + \
                'answer41 INTEGER,answer42 INTEGER,answer43 INTEGER,answer44 INTEGER,answer45 INTEGER,answer46 INTEGER,answer47 INTEGER,' + \
                'answer48 INTEGER)'

        connection.execute(query)
        query = 'INSERT INTO ' + nametable + ' (Number,FullName,Date,Age,class,school,Diagnos,Sex,Level,answer1,answer2,answer3,answer4,' + \
                'answer5,answer6,answer7,answer8,answer9,answer10,answer11,answer12,answer13,answer14,answer15,answer16,answer17,' + \
                'answer18,answer19,answer20,answer21,answer22,answer23,answer24,answer25,answer26,answer27,answer28,answer29,' + \
                'answer30,answer31,answer32,answer33,answer34,answer35,answer36,answer37,answer38,answer39,answer40,answer41,' + \
                'answer42,answer43,answer44,answer45,answer46,answer47,answer48) ' + \
                'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

        connection.execute(query, (
            self.t1, self.t2, self.t9, self.t4, self.t7, self.t6, self.t3, self.t5, self.t8,
            self.ans_1.currentIndex(), self.ans_2.currentIndex(), self.ans_3.currentIndex(), self.ans_4.currentIndex(), self.ans_5.currentIndex(),
            self.ans_6.currentIndex(), self.ans_7.currentIndex(), self.ans_8.currentIndex(), self.ans_9.currentIndex(), self.ans_10.currentIndex(),
            self.ans_11.currentIndex(), self.ans_12.currentIndex(), self.ans_13.currentIndex(), self.ans_14.currentIndex(), self.ans_15.currentIndex(),
            self.ans_16.currentIndex(),self.ans_17.currentIndex(), self.ans_18.currentIndex(), self.ans_19.currentIndex(), self.ans_20.currentIndex(),
            self.ans_21.currentIndex(), self.ans_22.currentIndex(), self.ans_23.currentIndex(), self.ans_24.currentIndex(), self.ans_25.currentIndex(),
            self.ans_26.currentIndex(),self.ans_27.currentIndex(),self.ans_28.currentIndex(), self.ans_29.currentIndex(), self.ans_30.currentIndex(),
            self.ans_31.currentIndex(), self.ans_32.currentIndex(), self.ans_33.currentIndex(), self.ans_34.currentIndex(),self.ans_35.currentIndex(),
            self.ans_36.currentIndex(), self.ans_37.currentIndex(),self.ans_38.currentIndex(),self.ans_39.currentIndex(), self.ans_40.currentIndex(),
            self.ans_41.currentIndex()+1, self.ans_42.currentIndex()+1, self.ans_43.currentIndex()+1, self.ans_44.currentIndex()+1, self.ans_45.currentIndex()+1,
            self.ans_46.currentIndex()+1, self.ans_47.currentIndex()+1, self.ans_48.currentIndex()+1))
        connection.commit()
        connection.close()
        self.close()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = Ui_Form_person(self)
        self.setGeometry(200, 50, 1080, 700)
        self.setFixedSize(1080, 700)
        self.setStyleSheet("")
        if (person == 1):
            self.setWindowTitle('ПЕРВИЧНОЕ анкетирование (Родители ребенка)')
        elif(person == 2):
            self.setWindowTitle('ПЕРВИЧНОЕ анкетирование (Учитель)')
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(40, 80, 941, 611))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setEnabled(False)

        self.tab = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab, "1 страница анкеты")
        self.tab_2 = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab_2, "2 страница анкеты")
        self.tab_3 = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab_3, "3 страница анкеты")

        self.label1 = QtWidgets.QLabel('1) Неспособен внимательно следить за деталями, делает нелепые ошибки', self.tab).setGeometry(QtCore.QRect(100, 20, 700, 16))
        self.label2 = QtWidgets.QLabel('2) Имеет трудности в выполнении заданий или игровой деятельности, которые требуют соредоточенности',self.tab).setGeometry(QtCore.QRect(100, 50, 850, 16))
        self.label3 = QtWidgets.QLabel('3) Не слушает, когда к нему обращаются', self.tab).setGeometry(QtCore.QRect(100, 80, 350, 16))
        self.label4 = QtWidgets.QLabel('4) Не заканчивает начатого занятия (непреднамеренно)', self.tab).setGeometry(QtCore.QRect(100, 110, 700, 16))
        self.label5 = QtWidgets.QLabel('5) Несобран, неорганизован', self.tab).setGeometry(QtCore.QRect(100, 140, 300, 16))
        self.label6 = QtWidgets.QLabel('6) Избегает, не любит или не хочет соглашаться выполнять задания, которые требуют повышенного внимания', self.tab).setGeometry(QtCore.QRect(100, 170, 850, 16))
        self.label7 = QtWidgets.QLabel('7) Путает расписание, теряет вещи, необходимые для выполнения заданий',self.tab).setGeometry(QtCore.QRect(100, 200, 800, 16))
        self.label8 = QtWidgets.QLabel('8) Легко отвлекается на все, что происходит вокруг', self.tab).setGeometry(QtCore.QRect(100, 230, 500, 16))
        self.label9 = QtWidgets.QLabel('9) Забывает выполнять каждодневные процедуры (почистить зубы и т.п.)', self.tab).setGeometry(QtCore.QRect(100, 260, 550, 16))
        self.label10 = QtWidgets.QLabel('10) Беспокойно двигает руками или ногами, ерзает на месте', self.tab).setGeometry(QtCore.QRect(100, 290, 500, 16))
        self.label11 = QtWidgets.QLabel('11) Покидает свое место в классе или в другом месте, не может усидеть', self.tab).setGeometry(QtCore.QRect(100, 320, 550, 16))
        self.label12 = QtWidgets.QLabel('12) Начинает бегать и карабкаться куда-то, когда это неуместно', self.tab).setGeometry(QtCore.QRect(100, 350, 550, 16))
        self.label13 = QtWidgets.QLabel('13) Не может тихо играть, неадекватно шумен', self.tab).setGeometry(QtCore.QRect(100, 380, 500, 16))
        self.label14 = QtWidgets.QLabel('14) Действует как «заведенный», как будто к нему приделан «моторчик»', self.tab).setGeometry(QtCore.QRect(100, 410, 550, 16))
        self.label15 = QtWidgets.QLabel('15) Чрезмерно разговорчивый, без учета социальных ограничений', self.tab).setGeometry(QtCore.QRect(100, 440, 520, 16))
        self.label16 = QtWidgets.QLabel('16) Выпаливает ответы до того, как завершены вопросы', self.tab).setGeometry(QtCore.QRect(100, 470, 500, 16))
        self.label17 = QtWidgets.QLabel('17) Не способен стоять в очередях, дожидаться своей очереди', self.tab).setGeometry(QtCore.QRect(100, 500, 520, 16))
        self.label18 = QtWidgets.QLabel('18) Перебивает других или вмешивается в разговоры или занятия других', self.tab).setGeometry(QtCore.QRect(100, 530, 550, 16))
        self.label19 = QtWidgets.QLabel('19) Вступает в конфликты со взрослыми', self.tab).setGeometry(QtCore.QRect(100, 560, 400, 16))
        self.label20 = QtWidgets.QLabel('20) Теряет самоконтроль, склонен к эмоциональным «взрывам»', self.tab_2).setGeometry(QtCore.QRect(100, 20, 500, 16))
        self.label21 = QtWidgets.QLabel('21) Не слушается и отказывается подчиняться установленным правилам взрослых', self.tab_2).setGeometry(QtCore.QRect(100, 50, 700, 16))
        self.label22 = QtWidgets.QLabel('22) Поступает наперекор другим', self.tab_2).setGeometry(QtCore.QRect(100, 80, 300, 16))
        self.label23 = QtWidgets.QLabel('23) Обвиняет других в своих ошибках и поведенческих проблемах', self.tab_2).setGeometry(QtCore.QRect(100, 110, 500, 16))
        self.label24 = QtWidgets.QLabel('24) Стремится добиться своего, легко «выходит из себя»', self.tab_2).setGeometry(QtCore.QRect(100, 140, 450, 16))
        self.label25 = QtWidgets.QLabel('25) Злой и раздражительный', self.tab_2).setGeometry(QtCore.QRect(100, 170, 250, 16))
        self.label26 = QtWidgets.QLabel('26) Не забывает обид, стремится отомстить', self.tab_2).setGeometry(QtCore.QRect(100, 200, 390, 16))
        self.label27 = QtWidgets.QLabel('27) Угрожает и запугивает других', self.tab_2).setGeometry(QtCore.QRect(100, 230, 300, 16))
        self.label28 = QtWidgets.QLabel('28) Грубит взрослым и употребляет нецензурные слова', self.tab_2).setGeometry(QtCore.QRect(100, 260, 450, 16))
        self.label29 = QtWidgets.QLabel('29) Обманывает, чтобы избежать наказания', self.tab_2).setGeometry(QtCore.QRect(100, 290, 350, 16))
        self.label30 = QtWidgets.QLabel('30) Пропускает уроки без разрешения', self.tab_2).setGeometry(QtCore.QRect(100, 320, 300, 16))
        self.label31 = QtWidgets.QLabel('31) Жестокий, драчливый, склонен к физической расправе', self.tab_2).setGeometry(QtCore.QRect(100, 350, 800, 16))
        self.label32 = QtWidgets.QLabel('32) Намеренно портит свои вещи и вещи других', self.tab_2).setGeometry(QtCore.QRect(100, 380, 450, 16))
        self.label33 = QtWidgets.QLabel('33) Имеет серьезные поведенческие проступки (кражи, нападения, вынос вещей из дома и т.п.)', self.tab_2).setGeometry(QtCore.QRect(100, 410, 800, 16))
        self.label34 = QtWidgets.QLabel('34) Робкий, боязливый, тревожный', self.tab_2).setGeometry(QtCore.QRect(100, 470, 300, 16))
        self.label35 = QtWidgets.QLabel('35) Боится пробовать делать что-то новое из-за страха, что не получится или совершит ошибку', self.tab_2).setGeometry(QtCore.QRect(100, 500, 800, 16))
        self.label36 = QtWidgets.QLabel('36) Чувсивует себя бесполезным, ощущает себя хуже других', self.tab_2).setGeometry(QtCore.QRect(100, 530, 700, 16))
        self.label37 = QtWidgets.QLabel('37) Обвиняет себя, чувствует себя виноватым', self.tab_2).setGeometry(QtCore.QRect(100, 560, 450, 16))
        self.label38 = QtWidgets.QLabel('38) Ощущает себя ненужным, жалуется «никто не любит меня»', self.tab_3).setGeometry(QtCore.QRect(100, 20, 500, 16))
        self.label39 = QtWidgets.QLabel('39) Грустный, несчастливый или удрученный', self.tab_3).setGeometry(QtCore.QRect(100, 50, 450, 16))
        self.label40 = QtWidgets.QLabel('40) Застенчивый или легко смущающийся', self.tab_3).setGeometry(QtCore.QRect(100, 80, 440, 16))

        self.help1 = QtWidgets.QLabel('Симптомы', self.tab)
        self.help1.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help2 = QtWidgets.QLabel('Симптомы', self.tab_2)
        self.help2.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help3 = QtWidgets.QLabel('Другие поведенческие проступки (укажите сами при их наличии)', self.tab_2)
        self.help3.setGeometry(QtCore.QRect(210, 440, 531, 20))
        self.help4 = QtWidgets.QLabel('Симптомы', self.tab_3)
        self.help4.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help5 = QtWidgets.QLabel('Успешность', self.tab_3)
        self.help5.setGeometry(QtCore.QRect(410, 120, 101, 21))
        self.help6 = QtWidgets.QLabel(
            "Инструкция: Пожалуйста, оцените поведение ребенка с помощью приведенного\nопросника. "
            "При оценке ориентируйтесь на наиболее типичное поведение ребенка\nв течение последних "
            "шести месяцев в сравнении с поведением сверстников.", self).setGeometry(QtCore.QRect(450, 10, 620, 51))
        self.help7 = QtWidgets.QLabel('(внимательно просмотрите значения для ввода)', self.tab_3).setGeometry(QtCore.QRect(280, 140, 400, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.help1.setFont(font)
        self.help2.setFont(font)
        self.help3.setFont(font)
        self.help4.setFont(font)
        self.help5.setFont(font)

        if (person == 1):
            self.label41 = QtWidgets.QLabel('41) Следование школьным правилам', self.tab_3).setGeometry(QtCore.QRect(100, 170, 400, 16))
            self.label42 = QtWidgets.QLabel('42) Чтение', self.tab_3).setGeometry(QtCore.QRect(100, 200, 100, 13))
            self.label43 = QtWidgets.QLabel('43) Письмо', self.tab_3).setGeometry(QtCore.QRect(100, 230, 100, 13))
            self.label44 = QtWidgets.QLabel('44) Математика', self.tab_3).setGeometry(QtCore.QRect(100, 260, 150, 16))
            self.label45 = QtWidgets.QLabel('45) Отношения с родителями', self.tab_3).setGeometry(QtCore.QRect(100, 290, 300, 16))
            self.label46 = QtWidgets.QLabel('46) Отношения с братьями /сестрами', self.tab_3).setGeometry(QtCore.QRect(100, 320, 300, 16))
            self.label47 = QtWidgets.QLabel('47) Отношения со сверстниками', self.tab_3).setGeometry(QtCore.QRect(100, 350, 300, 16))
            self.label48 = QtWidgets.QLabel('48) Участие в организованных мероприятиях (командная работа)',self.tab_3).setGeometry(QtCore.QRect(100, 380, 800, 16))
        elif(person == 2):
            self.label41 = QtWidgets.QLabel('41) Чтение', self.tab_3).setGeometry(QtCore.QRect(100, 170, 100, 16))
            self.label42 = QtWidgets.QLabel('42) Математика', self.tab_3).setGeometry(QtCore.QRect(100, 200, 150, 13))
            self.label43 = QtWidgets.QLabel('43) Письмо', self.tab_3).setGeometry(QtCore.QRect(100, 230, 100, 13))
            self.label44 = QtWidgets.QLabel('44) Отношения со сверстниками', self.tab_3).setGeometry(QtCore.QRect(100, 260, 300, 16))
            self.label45 = QtWidgets.QLabel('45) Следование инструкциям', self.tab_3).setGeometry(QtCore.QRect(100, 290, 300, 16))
            self.label46 = QtWidgets.QLabel('46) Нарушение порядка на занятиях', self.tab_3).setGeometry(QtCore.QRect(100, 320, 300, 16))
            self.label47 = QtWidgets.QLabel('47) Завершенность действий', self.tab_3).setGeometry(QtCore.QRect(100, 350, 300, 16))
            self.label48 = QtWidgets.QLabel('48) Организационные навыки',self.tab_3).setGeometry(QtCore.QRect(100, 380, 300, 16))


        self.ans_1 = QtWidgets.QComboBox(self.tab)
        self.ans_1.setGeometry(QtCore.QRect(0, 20, 91, 22))
        self.ans_1.addItems(["0","1","2","3"])

        self.ans_2 = QtWidgets.QComboBox(self.tab)
        self.ans_2.setGeometry(QtCore.QRect(0, 50, 91, 22))
        self.ans_2.addItems(["0","1","2","3"])

        self.ans_3 = QtWidgets.QComboBox(self.tab)
        self.ans_3.setGeometry(QtCore.QRect(0, 80, 91, 22))
        self.ans_3.addItems(["0","1","2","3"])

        self.ans_4 = QtWidgets.QComboBox(self.tab)
        self.ans_4.setGeometry(QtCore.QRect(0, 110, 91, 22))
        self.ans_4.addItems(["0","1","2","3"])

        self.ans_5 = QtWidgets.QComboBox(self.tab)
        self.ans_5.setGeometry(QtCore.QRect(0, 140, 91, 22))
        self.ans_5.addItems(["0","1","2","3"])

        self.ans_6 = QtWidgets.QComboBox(self.tab)
        self.ans_6.setGeometry(QtCore.QRect(0, 170, 91, 22))
        self.ans_6.addItems(["0","1","2","3"])

        self.ans_7 = QtWidgets.QComboBox(self.tab)
        self.ans_7.setGeometry(QtCore.QRect(0, 200, 91, 22))
        self.ans_7.addItems(["0","1","2","3"])

        self.ans_8 = QtWidgets.QComboBox(self.tab)
        self.ans_8.setGeometry(QtCore.QRect(0, 230, 91, 22))
        self.ans_8.addItems(["0","1","2","3"])

        self.ans_9 = QtWidgets.QComboBox(self.tab)
        self.ans_9.setGeometry(QtCore.QRect(0, 260, 91, 22))
        self.ans_9.addItems(["0","1","2","3"])

        self.ans_10 = QtWidgets.QComboBox(self.tab)
        self.ans_10.setGeometry(QtCore.QRect(0, 290, 91, 22))
        self.ans_10.addItems(["0","1","2","3"])

        self.ans_11 = QtWidgets.QComboBox(self.tab)
        self.ans_11.setGeometry(QtCore.QRect(0, 320, 91, 22))
        self.ans_11.addItems(["0","1","2","3"])

        self.ans_12 = QtWidgets.QComboBox(self.tab)
        self.ans_12.setGeometry(QtCore.QRect(0, 350, 91, 22))
        self.ans_12.addItems(["0","1","2","3"])

        self.ans_13 = QtWidgets.QComboBox(self.tab)
        self.ans_13.setGeometry(QtCore.QRect(0, 380, 91, 22))
        self.ans_13.addItems(["0","1","2","3"])

        self.ans_14 = QtWidgets.QComboBox(self.tab)
        self.ans_14.setGeometry(QtCore.QRect(0, 410, 91, 22))
        self.ans_14.addItems(["0","1","2","3"])

        self.ans_15 = QtWidgets.QComboBox(self.tab)
        self.ans_15.setGeometry(QtCore.QRect(0, 440, 91, 22))
        self.ans_15.addItems(["0","1","2","3"])

        self.ans_16 = QtWidgets.QComboBox(self.tab)
        self.ans_16.setGeometry(QtCore.QRect(0, 470, 91, 22))
        self.ans_16.addItems(["0","1","2","3"])

        self.ans_17 = QtWidgets.QComboBox(self.tab)
        self.ans_17.setGeometry(QtCore.QRect(0, 500, 91, 22))
        self.ans_17.addItems(["0","1","2","3"])

        self.ans_18 = QtWidgets.QComboBox(self.tab)
        self.ans_18.setGeometry(QtCore.QRect(0, 530, 91, 22))
        self.ans_18.addItems(["0","1","2","3"])

        self.ans_19 = QtWidgets.QComboBox(self.tab)
        self.ans_19.setGeometry(QtCore.QRect(0, 560, 91, 22))
        self.ans_19.addItems(["0","1","2","3"])

        self.ans_20 = QtWidgets.QComboBox(self.tab_2)
        self.ans_20.setGeometry(QtCore.QRect(0, 20, 91, 22))
        self.ans_20.addItems(["0","1","2","3"])

        self.ans_21 = QtWidgets.QComboBox(self.tab_2)
        self.ans_21.setGeometry(QtCore.QRect(0, 50, 91, 22))
        self.ans_21.addItems(["0","1","2","3"])

        self.ans_22 = QtWidgets.QComboBox(self.tab_2)
        self.ans_22.setGeometry(QtCore.QRect(0, 80, 91, 22))
        self.ans_22.addItems(["0","1","2","3"])

        self.ans_23 = QtWidgets.QComboBox(self.tab_2)
        self.ans_23.setGeometry(QtCore.QRect(0, 110, 91, 22))
        self.ans_23.addItems(["0","1","2","3"])

        self.ans_24 = QtWidgets.QComboBox(self.tab_2)
        self.ans_24.setGeometry(QtCore.QRect(0, 140, 91, 22))
        self.ans_24.addItems(["0","1","2","3"])

        self.ans_25 = QtWidgets.QComboBox(self.tab_2)
        self.ans_25.setGeometry(QtCore.QRect(0, 170, 91, 22))
        self.ans_25.addItems(["0","1","2","3"])

        self.ans_26 = QtWidgets.QComboBox(self.tab_2)
        self.ans_26.setGeometry(QtCore.QRect(0, 200, 91, 22))
        self.ans_26.addItems(["0","1","2","3"])

        self.ans_27 = QtWidgets.QComboBox(self.tab_2)
        self.ans_27.setGeometry(QtCore.QRect(0, 230, 91, 22))
        self.ans_27.addItems(["0","1","2","3"])

        self.ans_28 = QtWidgets.QComboBox(self.tab_2)
        self.ans_28.setGeometry(QtCore.QRect(0, 260, 91, 22))
        self.ans_28.addItems(["0","1","2","3"])

        self.ans_29 = QtWidgets.QComboBox(self.tab_2)
        self.ans_29.setGeometry(QtCore.QRect(0, 290, 91, 22))
        self.ans_29.addItems(["0","1","2","3"])

        self.ans_30 = QtWidgets.QComboBox(self.tab_2)
        self.ans_30.setGeometry(QtCore.QRect(0, 320, 91, 22))
        self.ans_30.addItems(["0", "1", "2", "3"])

        self.ans_31 = QtWidgets.QComboBox(self.tab_2)
        self.ans_31.setGeometry(QtCore.QRect(0, 350, 91, 22))
        self.ans_31.addItems(["0","1","2","3"])

        self.ans_32 = QtWidgets.QComboBox(self.tab_2)
        self.ans_32.setGeometry(QtCore.QRect(0, 380, 91, 22))
        self.ans_32.addItems(["0","1","2","3"])

        self.ans_33 = QtWidgets.QComboBox(self.tab_2)
        self.ans_33.setGeometry(QtCore.QRect(0, 410, 91, 22))
        self.ans_33.addItems(["0","1","2","3"])

        self.ans_34 = QtWidgets.QComboBox(self.tab_2)
        self.ans_34.setGeometry(QtCore.QRect(0, 470, 91, 22))
        self.ans_34.addItems(["0","1","2","3"])

        self.ans_35 = QtWidgets.QComboBox(self.tab_2)
        self.ans_35.setGeometry(QtCore.QRect(0, 500, 91, 22))
        self.ans_35.addItems(["0","1","2","3"])

        self.ans_36 = QtWidgets.QComboBox(self.tab_2)
        self.ans_36.setGeometry(QtCore.QRect(0, 530, 91, 22))
        self.ans_36.addItems(["0","1","2","3"])

        self.ans_37 = QtWidgets.QComboBox(self.tab_2)
        self.ans_37.setGeometry(QtCore.QRect(0, 560, 91, 22))
        self.ans_37.addItems(["0","1","2","3"])

        self.ans_38 = QtWidgets.QComboBox(self.tab_3)
        self.ans_38.setGeometry(QtCore.QRect(0, 20, 91, 22))
        self.ans_38.addItems(["0","1","2","3"])

        self.ans_39 = QtWidgets.QComboBox(self.tab_3)
        self.ans_39.setGeometry(QtCore.QRect(0, 50, 91, 22))
        self.ans_39.addItems(["0","1","2","3"])

        self.ans_40 = QtWidgets.QComboBox(self.tab_3)
        self.ans_40.setGeometry(QtCore.QRect(0, 80, 91, 22))
        self.ans_40.addItems(["0","1","2","3"])

        self.ans_41 = QtWidgets.QComboBox(self.tab_3)
        self.ans_41.setGeometry(QtCore.QRect(0, 170, 91, 22))
        self.ans_41.addItems(["1","2","3","4","5"])

        self.ans_42 = QtWidgets.QComboBox(self.tab_3)
        self.ans_42.setGeometry(QtCore.QRect(0, 200, 91, 22))
        self.ans_42.addItems(["1","2","3","4","5"])

        self.ans_43 = QtWidgets.QComboBox(self.tab_3)
        self.ans_43.setGeometry(QtCore.QRect(0, 230, 91, 22))
        self.ans_43.setMaxVisibleItems(5)
        self.ans_43.addItems(["1","2","3","4","5"])

        self.ans_44 = QtWidgets.QComboBox(self.tab_3)
        self.ans_44.setGeometry(QtCore.QRect(0, 260, 91, 22))
        self.ans_44.addItems(["1","2","3","4","5"])

        self.ans_45 = QtWidgets.QComboBox(self.tab_3)
        self.ans_45.setGeometry(QtCore.QRect(0, 290, 91, 22))
        self.ans_45.addItems(["1","2","3","4","5"])

        self.ans_46 = QtWidgets.QComboBox(self.tab_3)
        self.ans_46.setGeometry(QtCore.QRect(0, 320, 91, 22))
        self.ans_46.addItems(["1","2","3","4","5"])

        self.ans_47 = QtWidgets.QComboBox(self.tab_3)
        self.ans_47.setGeometry(QtCore.QRect(0, 350, 91, 22))
        self.ans_47.addItems(["1","2","3","4","5"])

        self.ans_48 = QtWidgets.QComboBox(self.tab_3)
        self.ans_48.setGeometry(QtCore.QRect(0, 380, 91, 22))
        self.ans_48.addItems(["1","2","3","4","5"])

        self.pushButton = QtWidgets.QPushButton("Личные данные ", self)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 391, 51))
        self.pushButton.clicked.connect(self.dialog.exec)

        self.save1pushButton = QtWidgets.QPushButton('Сохранить', self)
        self.save1pushButton.setGeometry(QtCore.QRect(900, 70, 161, 31))
        self.save1pushButton.clicked.connect(self.saveA1)

        self.tabWidget.setCurrentIndex(0)
        self.t1 = ''
        self.t2 = ''
        self.t3 = ''
        self.t4 = ''
        self.t5 = ''
        self.t6 = ''
        self.t7 = ''
        self.t8 = ''
        self.t9 = ''


# ----------------класс анализа данных анкеты родителей и учителя-------------------
class Ui_windowFind1(QtWidgets.QDialog):
    def summa(self):
        if(person == 1):
            nametable = 'Children'
        elif(person == 2):
            nametable = 'Children2'

        connection = sqlite3.connect('Anketa1.db')
        query = 'select * from ' + nametable + ' where Number = ' + chr(34) + self.numberofpat.currentText() + chr(34)
        result = connection.execute(query)
        row = result.fetchall()
        if (row):
            self.label_11.setText('-----------------------')
            self.label_12.setText('-----------------------')
            self.label_13.setText('-----------------------')
            self.label_14.setText('-----------------------')
            self.label_15.setText('-----------------------')
            self.label_16.setText('-----------------------')
            j1 = j2 = j7 = j4 = j5 = j6 = flag = 0

            # ---------------------------социальная адаптация--------------------------------------
            summ7 = summ237 = 0;
            # for i in [49,50,51,52,53,54,55,56,57,58]:
            #   if (row[0][i] == None  or row[0][i] == '') :
            #        summ7 = 0
            #        continue
            #   summ7 = summ7 + row[0][i]
            #  if(row[0][i] == 4 or row[0][i] == 5):
            #      j7=j7+1
            #   summ237 = summ237 + row[0][i]
            # if(j7 >= 1):
            #      flag = 100;
            self.su7.setText(str(summ7))
            self.su_7.setText(str(summ237))

            # --------------------------дефицит внимания------------------------
            summ1 = summ231 = 0;
            for i in [9, 10, 11, 12, 13, 14, 15, 16, 17]:
                if (row[0][i] == None or row[0][i] == ''):
                    summ1 = 0
                    continue
                summ1 = summ1 + row[0][i]
                if (row[0][i] == 2 or row[0][i] == 3):
                    j1 = j1 + 1
                    summ231 = summ231 + row[0][i]
                # if(j1 >= 6 and flag == 100):
                if (j1 >= 6):
                    j1 = 100;
                    self.label_11.setText('симптом выявлен')
            self.su1.setText(str(summ1))
            self.su_1.setText(str(summ231))
            # --------------------------гиперактивность и импульсивность------------------------
            summ2 = summ232 = 0;
            for i in [18, 19, 20, 21, 22, 23, 24, 25, 26]:
                if (row[0][i] == None or row[0][i] == ''):
                    summ2 = 0
                    continue
                summ2 = summ2 + row[0][i]
                if (row[0][i] == 2 or row[0][i] == 3):
                    j2 = j2 + 1
                    summ232 = summ232 + row[0][i]
                # if(j2 >= 6 and flag == 100):
                if (j2 >= 6):
                    j2 = 100;
                    self.label_12.setText('симптом выявлен')
            self.su2.setText(str(summ2))
            self.su_2.setText(str(summ232))

            # --------------------------внимание и гиперактивность------------------------
            summ3 = summ1 + summ2
            summ233 = summ232 + summ231
            # if(j1 == 100 and j2 == 100 and flag == 100):
            if (j1 == 100 and j2 == 100):
                self.label_13.setText('симптом выявлен')
            self.su3.setText(str(summ3))
            self.su_3.setText(str(summ233))

            # --------------------------реакции протеста--------------------------
            summ4 = summ234 = 0;
            for i in [27, 28, 29, 30, 31, 32, 33, 34]:
                if (row[0][i] == None or row[0][i] == ''):
                    summ4 = 0
                    continue
                summ4 = summ4 + row[0][i]
                if (row[0][i] == 2 or row[0][i] == 3):
                    j4 = j4 + 1
                    summ234 = summ234 + row[0][i]
                # if(j4 >= 4 and flag == 100):
                if (j4 >= 4):
                    self.label_14.setText('симптом выявлен')
            self.su4.setText(str(summ4))
            self.su_4.setText(str(summ234))

            # --------------------------поведенческие проблемы--------------------------
            summ5 = summ235 = 0;
            for i in [35, 36, 37, 38, 39, 40, 41]:
                if (row[0][i] == None or row[0][i] == ''):
                    summ5 = 0
                    continue
                summ5 = summ5 + row[0][i]
                if (row[0][i] == 2 or row[0][i] == 3):
                    j5 = j5 + 1
                    summ235 = summ235 + row[0][i]
                # if(j5 >= 3 and flag == 100):
                if (j5 >= 3):
                    self.label_15.setText('симптом выявлен')
            self.su5.setText(str(summ5))
            self.su_5.setText(str(summ235))

            # --------------------------тревожно-депрессивная симптоматика--------------------------
            summ6 = summ236 = 0;
            for i in [42, 43, 44, 45, 46, 47, 48]:
                if (row[0][i] == None or row[0][i] == ''):
                    summ6 = 0
                    continue
                summ6 = summ6 + row[0][i]
                if (row[0][i] == 2 or row[0][i] == 3):
                    j6 = j6 + 1
                    summ236 = summ236 + row[0][i]
                # if(j6 >= 3 and flag == 100):
                if (j6 >= 3):
                    self.label_16.setText('симптом выявлен')
            self.su6.setText(str(summ6))
            self.su_6.setText(str(summ236))

            # --------------------------------------------------------------------------------

            connection.close()

        else:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Ошибка!!!")
            error_message.showMessage("Некорректный ввод данных или нет данного пациента в базе.")

    def cleaner(self):
        self.su1.setText("")
        self.su2.setText("")
        self.su3.setText("")
        self.su4.setText("")
        self.su5.setText("")
        self.su6.setText("")
        self.su7.setText("")
        self.su_1.setText("")
        self.su_2.setText("")
        self.su_3.setText("")
        self.su_4.setText("")
        self.su_5.setText("")
        self.su_6.setText("")
        self.su_7.setText("")

    def saver(self):
        f = QtWidgets.QFileDialog.getSaveFileName(self)
        filename = f[0]
        if f[0] != '':
            openedfile = open(filename, "w")
            text = "Номер пациента: " + self.numberofpat.currentText() + "\t\t\t\tКлиническая форма\n\n"
            text += "субшкала дефицита внимания = " + self.su1.text() + "\t\t" + self.label_11.text() + "\n"
            text += "субшкала гиперактивности и импульсивности = " + self.su2.text() + "\t\t\t" + self.label_12.text() + "\n"
            text += "субшкала невнимательности и гиперакивности = " + self.su3.text() + "\t\t\t" + self.label_13.text() + "\n"
            text += "субшкала реакций оппозиции (протеста) = " + self.su4.text() + "\t" + self.label_14.text() + "\n"
            text += "субшкала др. поведенческих проблем = " + self.su5.text() + "\n"
            text += "субшкала тревожно-депрессивной симптоматики = " + self.su6.text() + "\n"
            text += "субшкала социальной адаптации = " + self.su7.text() + "\n\n\n\n\n\n\n\n\n\n"
            text += "\t\t\t\tПодпись врача______________\n\t\t\t\tДата_________"
            openedfile.write(text)
            openedfile.close()

    def printer(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        text1 = "Заключение по исследованию пациента\n\n"
        text1 += "Номер пациента: " + self.numberofpat.currentText() + "\t\t\t\tКлиническая форма\n\n"
        text1 += "1.Cубшкала дефицита внимания: " + self.su1.text() + "\t\t" + self.label_11.text() + "\n"
        text1 += "2.Cубшкала гиперактивности и импульсивности: " + self.su2.text() + "\t\t\t" + self.label_12.text() + "\n"
        text1 += "3.Cубшкала невнимательности и гиперактивности: " + self.su3.text() + "\t\t\t" + self.label_13.text() + "\n"
        text1 += "4.Cубшкала реакций оппозиции (протеста): " + self.su4.text() + "\t" + self.label_14.text() + "\n"
        text1 += "5.Cубшкала др. поведенческих проблем: " + self.su5.text() + "\n"
        text1 += "6.Cубшкала тревожно-депрессивной симптоматики: " + self.su6.text() + "\n"
        text1 += "7.Cубшкала социальной адаптации:    " + self.su7.text() + "\n\n\n\n\n\n\n\n\n\n"
        text1 += "\t\t\t\tПодпись врача______________\n\t\t\t\tДата_________"
        self.textPrint.setText(text1)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textPrint.print_(printer)

    def saverBD(self):
        if(person == 1):
            nametable = 'Children'
            nametable2 = 'StatusRelatives'
        elif(person == 2):
            nametable = 'Children2'
            nametable2 = 'StatusTeacher'
        connection = sqlite3.connect('Anketa1.db')
        query = 'select * from ' + nametable + ' where Number = ' + chr(34) + self.numberofpat.currentText() + chr(34)
        result = connection.execute(query)
        row = result.fetchall()
        if (row):
            query = 'CREATE TABLE IF NOT EXISTS ' + nametable2 + ' (Number TEXT,Age INTEGER,class INTEGER, Sex INTEGER, Level INTEGER,' + \
                    ' Sum1 INTEGER, Sum2 INTEGER, Sum3 INTEGER,Sum4 INTEGER,Sum5 INTEGER,Sum6 INTEGER,Sum7 INTEGER,' + \
                    ' Status1 TEXT, Status2 TEXT, Status3 TEXT, Status4 TEXT, Status5 TEXT, Status6 TEXT, Status7 TEXT )'
            connection.execute(query)

            query = 'select * from ' + nametable2 + ' where Number = ' + chr(34) + self.numberofpat.currentText() + chr(34)
            result = connection.execute(query)
            row1 = result.fetchall()
            if (row1):
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Сообщение")
                error_message.showMessage("Пациент уже существует в базе, поэтому обновляем.")
                rr = 'DELETE from ' + nametable2 + ' where Number=' + chr(34) + self.numberofpat.currentText() + chr(34)
                connection.execute(rr)
                connection.commit()

                query = 'INSERT INTO ' + nametable2 + ' (Number,Age,class, Sex, Level, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7,Status1,Status2,Status3,' + \
                        'Status4, Status5, Status6, Status7) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

                connection.execute(query, (
                self.numberofpat.currentText(), row[0][3], row[0][4], row[0][7], row[0][8], self.su1.text(), self.su2.text(),
                self.su3.text(), self.su4.text(), self.su5.text(), self.su6.text(), self.su7.text(),
                self.label_11.text(), self.label_12.text(), self.label_13.text(), self.label_14.text(),
                self.label_15.text(), self.label_16.text(), self.label_17.text()))
                connection.commit()
            else:
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Сообщение")
                error_message.showMessage("Такого пациента еще нет в базе, поэтому добавляем.")

                query = 'INSERT INTO ' + nametable2 + ' (Number,Age,class, Sex, Level, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7,Status1,Status2,Status3,' + \
                        'Status4, Status5, Status6, Status7) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                print(query)
                connection.execute(query, (
                self.numberofpat.currentText(), row[0][3], row[0][4], row[0][7], row[0][8], int(self.su1.text()),
                int(self.su2.text()), int(self.su3.text()), int(self.su4.text()), int(self.su5.text()),
                int(self.su6.text()), int(self.su7.text()), self.label_11.text(), self.label_12.text(),
                self.label_13.text(), self.label_14.text(), self.label_15.text(), self.label_16.text(),
                self.label_17.text()))
                connection.commit()
        connection.close()

    def saverSumm(self):
        if(person == 1):
            nametable = 'Children'
            nametable2 = 'SUMMBOTH'
        elif(person == 2):
            nametable = 'Children2'
            nametable2 = 'SUMMBOTH2'
        connection = sqlite3.connect('Anketa1.db')
        query = 'select * from ' + nametable + ' where Number = ' + chr(34) + self.numberofpat.currentText() + chr(34)
        result = connection.execute(query)
        row = result.fetchall()
        if (row):
            query = 'CREATE TABLE IF NOT EXISTS ' + nametable2 + ' (Number TEXT,Age INTEGER,class INTEGER, Sex INTEGER, Level INTEGER,' + \
                    ' Sum1 INTEGER, Sum2 INTEGER, Sum3 INTEGER,Sum4 INTEGER,Sum5 INTEGER,Sum6 INTEGER,Sum7 INTEGER,' + \
                    ' Sum21 INTEGER, Sum22 INTEGER, Sum23 INTEGER,Sum24 INTEGER,Sum25 INTEGER,Sum26 INTEGER,Sum27 INTEGER )'
            connection.execute(query)

            query = 'select * from ' + nametable2 + ' where Number = ' + chr(34) + self.numberofpat.currentText() + chr(34)
            result = connection.execute(query)
            row1 = result.fetchall()
            if (row1):
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Сообщение")
                error_message.showMessage("Пациент уже существует в базе, поэтому обновляем.")
                rr = 'DELETE from ' + nametable2 + ' where Number=' + chr(34) + self.numberofpat.currentText() + chr(34)
                connection.execute(rr)
                connection.commit()

                query = 'INSERT INTO ' + nametable2 + ' (Number,Age,class, Sex, Level, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7,Sum21, Sum22, Sum23,' + \
                        'Sum24, Sum25, Sum26, Sum27) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

                connection.execute(query, (
                self.numberofpat.currentText(), row[0][3], row[0][4], row[0][7], row[0][8], self.su1.text(), self.su2.text(),
                self.su3.text(), self.su4.text(), self.su5.text(), self.su6.text(), self.su7.text(), self.su_1.text(),
                self.su_2.text(), self.su_3.text(), self.su_4.text(), self.su_5.text(), self.su_6.text(),
                self.su_7.text()))
                connection.commit()
            else:
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Сообщение")
                error_message.showMessage("Такого пациента еще нет в базе, поэтому добавляем.")

                query = 'INSERT INTO ' + nametable2 + ' (Number,Age,class, Sex, Level, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7,Sum21, Sum22, Sum23,' + \
                        'Sum24, Sum25, Sum26, Sum27) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                connection.execute(query, (
                self.numberofpat.currentText(), row[0][3], row[0][4], row[0][7], row[0][8], int(self.su1.text()),
                int(self.su2.text()), int(self.su3.text()), int(self.su4.text()), int(self.su5.text()),
                int(self.su6.text()), int(self.su7.text()), int(self.su_1.text()), int(self.su_2.text()),
                int(self.su_3.text()), int(self.su_4.text()), int(self.su_5.text()), int(self.su_6.text()),
                int(self.su_7.text())))
                connection.commit()
        connection.close()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if(person == 1):
            self.setWindowTitle("Оценка ПЕРВИЧНОЙ анкеты (Родители ребенка)")
        elif(person == 2):
            self.setWindowTitle("Оценка ПЕРВИЧНОЙ анкеты (Учитель)")

        self.setGeometry(500, 300, 800, 400)
        self.setFixedSize(800, 400)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setStyleSheet("")

        self.label = QtWidgets.QLabel('Номер пациента', self).setGeometry(QtCore.QRect(30, 10, 141, 21))
        self.label_2 = QtWidgets.QLabel('Субшкала невнимательности ', self).setGeometry(QtCore.QRect(70, 90, 261, 21))
        self.label_3 = QtWidgets.QLabel('Субшкала гиперактивности + импульсивности', self).setGeometry(QtCore.QRect(70, 120, 400, 21))
        self.label_4 = QtWidgets.QLabel('Субшкала невнимательности + гиперактивности', self).setGeometry(QtCore.QRect(70, 150, 400, 21))
        self.label_5 = QtWidgets.QLabel('Субшкала реакций оппозиции (протеста) ', self).setGeometry(QtCore.QRect(70, 180, 351, 21))
        self.label_6 = QtWidgets.QLabel('Субшкала др. поведенческих проблем', self).setGeometry(QtCore.QRect(70, 210, 321, 21))
        self.label_7 = QtWidgets.QLabel('Субшкала тревожно-депрессивной симптоматики ', self).setGeometry(QtCore.QRect(70, 240, 421, 21))
        self.label_8 = QtWidgets.QLabel('Субшкала социальной адаптации', self).setGeometry(QtCore.QRect(70, 270, 291, 21))
        self.label_9 = QtWidgets.QLabel('Сумма 2,3 баллов|Сумма всех', self).setGeometry(QtCore.QRect(380, 60, 250, 21))
        self.label_10 = QtWidgets.QLabel('|      Статус ', self).setGeometry(QtCore.QRect(620, 60, 170, 21))


        self.label_11 = QtWidgets.QLabel('-----------------------', self)
        self.label_11.setGeometry(QtCore.QRect(640, 90, 180, 21))

        self.label_12 = QtWidgets.QLabel('-----------------------', self)
        self.label_12.setGeometry(QtCore.QRect(640, 120, 180, 21))

        self.label_13 = QtWidgets.QLabel('-----------------------', self)
        self.label_13.setGeometry(QtCore.QRect(640, 150, 180, 21))

        self.label_14 = QtWidgets.QLabel('-----------------------', self)
        self.label_14.setGeometry(QtCore.QRect(640, 180, 180, 21))

        self.label_15 = QtWidgets.QLabel('-----------------------', self)
        self.label_15.setGeometry(QtCore.QRect(640, 210, 180, 21))

        self.label_16 = QtWidgets.QLabel('-----------------------', self)
        self.label_16.setGeometry(QtCore.QRect(640, 240, 180, 21))

        self.label_17 = QtWidgets.QLabel('-----------------------', self)
        self.label_17.setGeometry(QtCore.QRect(640, 270, 180, 21))


        self.massiv = []
        self.numberofpat = QtWidgets.QComboBox(self)
        self.numberofpat.setGeometry(QtCore.QRect(180, 10, 121, 20))
        if(person == 1):
            nametable = 'Children'
        elif(person == 2):
            nametable = 'Children2'
        connection = sqlite3.connect('Anketa1.db')
        query = 'select count(Number) from ' + nametable + ' '
        result = connection.execute(query)
        row = result.fetchall()
        n = row[0][0]
        query = 'select Number from ' + nametable + ' '
        result = connection.execute(query)
        row = result.fetchall()
        for row_number in range(n):
            self.massiv.append(str(row[row_number][0]))
        self.numberofpat.addItems(self.massiv)

        self.su1 = QtWidgets.QLineEdit(self)
        self.su1.setGeometry(QtCore.QRect(530, 90, 41, 20))

        self.su2 = QtWidgets.QLineEdit(self)
        self.su2.setGeometry(QtCore.QRect(530, 120, 41, 20))

        self.su3 = QtWidgets.QLineEdit(self)
        self.su3.setGeometry(QtCore.QRect(530, 150, 41, 20))

        self.su4 = QtWidgets.QLineEdit(self)
        self.su4.setGeometry(QtCore.QRect(530, 180, 41, 20))

        self.su5 = QtWidgets.QLineEdit(self)
        self.su5.setGeometry(QtCore.QRect(530, 210, 41, 20))

        self.su6 = QtWidgets.QLineEdit(self)
        self.su6.setGeometry(QtCore.QRect(530, 240, 41, 20))

        self.su7 = QtWidgets.QLineEdit(self)
        self.su7.setGeometry(QtCore.QRect(530, 270, 41, 20))

        self.su_1 = QtWidgets.QLineEdit(self)
        self.su_1.setGeometry(QtCore.QRect(480, 90, 41, 20))

        self.su_2 = QtWidgets.QLineEdit(self)
        self.su_2.setGeometry(QtCore.QRect(480, 120, 41, 20))

        self.su_3 = QtWidgets.QLineEdit(self)
        self.su_3.setGeometry(QtCore.QRect(480, 150, 41, 20))

        self.su_4 = QtWidgets.QLineEdit(self)
        self.su_4.setGeometry(QtCore.QRect(480, 180, 41, 20))

        self.su_5 = QtWidgets.QLineEdit(self)
        self.su_5.setGeometry(QtCore.QRect(480, 210, 41, 20))

        self.su_6 = QtWidgets.QLineEdit(self)
        self.su_6.setGeometry(QtCore.QRect(480, 240, 41, 20))

        self.su_7 = QtWidgets.QLineEdit(self)
        self.su_7.setGeometry(QtCore.QRect(480, 270, 41, 20))

        self.findsumma = QtWidgets.QPushButton('Поиск', self)
        self.findsumma.setGeometry(QtCore.QRect(300, 9, 91, 23))
        self.findsumma.clicked.connect(self.summa)

        self.sbros = QtWidgets.QPushButton('Сброс', self)
        self.sbros.setGeometry(QtCore.QRect(550, 310, 100, 23))
        self.sbros.clicked.connect(self.cleaner)

        self.save = QtWidgets.QPushButton('Cохранить в файл', self)
        self.save.setGeometry(QtCore.QRect(30, 310, 160, 23))
        self.save.clicked.connect(self.saver)

        self.print = QtWidgets.QPushButton('Печать', self)
        self.print.setGeometry(QtCore.QRect(655, 310, 100, 23))
        self.print.clicked.connect(self.printer)

        self.savebd = QtWidgets.QPushButton('Сохранить в базе', self)
        self.savebd.setGeometry(QtCore.QRect(195, 310, 160, 23))
        self.savebd.clicked.connect(self.saverBD)

        self.savesum = QtWidgets.QPushButton('Сохранить суммы', self)
        self.savesum.setGeometry(QtCore.QRect(360, 310, 160, 23))
        self.savesum.clicked.connect(self.saverSumm)

        self.textPrint = QtWidgets.QTextEdit(self)
        self.textPrint.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textPrint.setFont(font)


# ----------------класс для удаления данных пациента из анкеты №1-------------------
class Ui_Delete(QtWidgets.QDialog):

    def deleteform(self):
        if (person == 1):
            nametable = 'Children'
        elif (person == 2):
            nametable = 'Children2'
        elif (table[0] == 1):
            nametable = 'ChildrenAgain'
        elif (table[1] == 1):
            nametable = 'StatusRelatives'
        elif (table[0] == 2):
            nametable = 'ChildrenAgain2'
        elif(table[1] == 2):
            nametable = 'StatusTeacher'
        connection = sqlite3.connect('Anketa1.db')
        rr = 'DELETE from ' + nametable + ' where Number=' + chr(34) + self.numberofpat.text() + chr(34)
        connection.execute(rr)
        connection.commit()
        connection.close()
        self.numberofpat.setText("")
        self.close()

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.ff = root

        self.setWindowTitle("Удаление записи")
        self.resize(400, 149)
        self.setFixedSize(400, 149)

        self.label = QtWidgets.QLabel('Номер пациента', self).setGeometry(QtCore.QRect(40, 40, 131, 21))
        self.massiv = []
        self.numberofpat = QtWidgets.QLineEdit(self)
        self.numberofpat.setGeometry(QtCore.QRect(190, 40, 131, 20))
        self.delete_2 = QtWidgets.QPushButton('Удалить', self)
        self.delete_2.setGeometry(QtCore.QRect(260, 110, 121, 23))
        self.delete_2.clicked.connect(self.deleteform)


# ----------------класс для изменения данных пациента из анкеты №1-------------------
class Ui_Update(QtWidgets.QDialog):
    def changeform(self):
        if (person == 1):
            nametable = 'Children'
        elif (person == 2):
            nametable = 'Children2'
        elif (table[0] == 1):
            nametable = 'ChildrenAgain'
        elif (table[0] == 2):
            nametable = 'ChildrenAgain2'

        connection = sqlite3.connect('Anketa1.db')

        if (str(self.comboBox.currentText()) == 'Номер пациента'): s = 'Number'
        if (str(self.comboBox.currentText()) == 'ФИО пациента'): s = 'Fullname'
        if (str(self.comboBox.currentText()) == 'Дата ввода'): s = 'Date'
        if (str(self.comboBox.currentText()) == 'Дата рождения'): s = 'Birth'
        if (str(self.comboBox.currentText()) == 'Возраст'): s = 'Age'
        if (str(self.comboBox.currentText()) == 'Школа'): s = 'school'
        if (str(self.comboBox.currentText()) == 'Класс'): s = 'class'
        if (str(self.comboBox.currentText()) == 'Пол'): s = 'Sex'
        if (str(self.comboBox.currentText()) == 'Ступень обучения'): s = 'Level'
        if (str(self.comboBox.currentText()) == 'Ответ1'): s = 'answer1'
        if (str(self.comboBox.currentText()) == 'Ответ2'): s = 'answer2'
        if (str(self.comboBox.currentText()) == 'Ответ3'): s = 'answer3'
        if (str(self.comboBox.currentText()) == 'Ответ4'): s = 'answer4'
        if (str(self.comboBox.currentText()) == 'Ответ5'): s = 'answer5'
        if (str(self.comboBox.currentText()) == 'Ответ6'): s = 'answer6'
        if (str(self.comboBox.currentText()) == 'Ответ7'): s = 'answer7'
        if (str(self.comboBox.currentText()) == 'Ответ8'): s = 'answer8'
        if (str(self.comboBox.currentText()) == 'Ответ9'): s = 'answer9'
        if (str(self.comboBox.currentText()) == 'Ответ10'): s = 'answer10'
        if (str(self.comboBox.currentText()) == 'Ответ11'): s = 'answer11'
        if (str(self.comboBox.currentText()) == 'Ответ12'): s = 'answer12'
        if (str(self.comboBox.currentText()) == 'Ответ13'): s = 'answer13'
        if (str(self.comboBox.currentText()) == 'Ответ14'): s = 'answer14'
        if (str(self.comboBox.currentText()) == 'Ответ15'): s = 'answer15'
        if (str(self.comboBox.currentText()) == 'Ответ16'): s = 'answer16'
        if (str(self.comboBox.currentText()) == 'Ответ17'): s = 'answer17'
        if (str(self.comboBox.currentText()) == 'Ответ18'): s = 'answer18'
        if (str(self.comboBox.currentText()) == 'Ответ19'): s = 'answer19'
        if (str(self.comboBox.currentText()) == 'Ответ20'): s = 'answer20'
        if (str(self.comboBox.currentText()) == 'Ответ21'): s = 'answer21'
        if (str(self.comboBox.currentText()) == 'Ответ22'): s = 'answer22'
        if (str(self.comboBox.currentText()) == 'Ответ23'): s = 'answer23'
        if (str(self.comboBox.currentText()) == 'Ответ24'): s = 'answer24'
        if (str(self.comboBox.currentText()) == 'Ответ25'): s = 'answer25'
        if (str(self.comboBox.currentText()) == 'Ответ26'): s = 'answer26'
        if (str(self.comboBox.currentText()) == 'Ответ27'): s = 'answer27'
        if (str(self.comboBox.currentText()) == 'Ответ28'): s = 'answer28'
        if (str(self.comboBox.currentText()) == 'Ответ29'): s = 'answer29'
        if (str(self.comboBox.currentText()) == 'Ответ30'): s = 'answer30'
        if (str(self.comboBox.currentText()) == 'Ответ31'): s = 'answer31'
        if (str(self.comboBox.currentText()) == 'Ответ32'): s = 'answer32'
        if (str(self.comboBox.currentText()) == 'Ответ33'): s = 'answer33'
        if (str(self.comboBox.currentText()) == 'Ответ34'): s = 'answer34'
        if (str(self.comboBox.currentText()) == 'Ответ35'): s = 'answer35'
        if (str(self.comboBox.currentText()) == 'Ответ36'): s = 'answer36'
        if (str(self.comboBox.currentText()) == 'Ответ37'): s = 'answer37'
        if (str(self.comboBox.currentText()) == 'Ответ38'): s = 'answer38'
        if (str(self.comboBox.currentText()) == 'Ответ39'): s = 'answer39'
        if (str(self.comboBox.currentText()) == 'Ответ40'): s = 'answer40'
        if (str(self.comboBox.currentText()) == 'Ответ41'): s = 'answer41'
        if (str(self.comboBox.currentText()) == 'Ответ42'): s = 'answer42'
        if (str(self.comboBox.currentText()) == 'Ответ43'): s = 'answer43'
        if (str(self.comboBox.currentText()) == 'Ответ44'): s = 'answer44'
        if (str(self.comboBox.currentText()) == 'Ответ45'): s = 'answer45'
        if (str(self.comboBox.currentText()) == 'Ответ46'): s = 'answer46'
        if (str(self.comboBox.currentText()) == 'Ответ47'): s = 'answer47'
        if (str(self.comboBox.currentText()) == 'Ответ48'): s = 'answer48'
        if (str(self.comboBox.currentText()) == 'Описание'): s = 'problems'

        rr = 'UPDATE ' + nametable + ' set ' + s + '=' + chr(34) + self.new_2.text() + chr(34) + ' where Number=' + chr(34) + self.numberofpat.text() + chr(34)
        connection.execute(rr)
        connection.commit()
        connection.close()
        self.new_2.setText("")
        self.numberofpat.setText("")

        self.close()

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.ff = root

        self.resize(414, 207)
        self.setFixedSize(414, 207)
        self.setStyleSheet("")
        self.setWindowTitle("Внесение изменений")

        self.label = QtWidgets.QLabel('Номер пациента', self).setGeometry(QtCore.QRect(40, 50, 131, 21))
        self.label_3 = QtWidgets.QLabel('Поле для изменения', self).setGeometry(QtCore.QRect(40, 80, 171, 21))
        self.label_4 = QtWidgets.QLabel('Новое значение', self).setGeometry(QtCore.QRect(40, 110, 141, 21))
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(200, 80, 121, 22))
        self.comboBox.setObjectName("comboBox")
        if (person == 1):
            nametable = 'Children'
            self.comboBox.addItems(
                ["Номер пациента", "ФИО пациента", "Дата ввода", "Дата рождения", "Возраст", "Школа", "Класс", "Пол",
                 "Ступень обучения",
                 "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6", "Ответ7", "Ответ8", "Ответ9", "Ответ10",
                 "Ответ11", "Ответ12",
                 "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17", "Ответ18", "Ответ19", "Ответ20", "Ответ21",
                 "Ответ22", "Ответ23",
                 "Ответ24", "Ответ25", "Ответ26", "Ответ27", "Ответ28", "Ответ29", "Ответ30", "Ответ31", "Ответ32",
                 "Ответ33", "Ответ34",
                 "Ответ35", "Ответ36", "Ответ37", "Ответ38", "Ответ39", "Ответ40", "Ответ41", "Ответ42", "Ответ43",
                 "Ответ44", "Ответ45",
                 "Ответ46", "Ответ47", "Ответ48", "Ответ49", "Ответ50"])
        elif (person == 2):
            nametable = 'Children2'
            self.comboBox.addItems(
                ["Номер пациента", "ФИО пациента", "Дата ввода", "Дата рождения", "Возраст", "Школа", "Класс", "Пол",
                 "Ступень обучения",
                 "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6", "Ответ7", "Ответ8", "Ответ9", "Ответ10",
                 "Ответ11", "Ответ12",
                 "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17", "Ответ18", "Ответ19", "Ответ20", "Ответ21",
                 "Ответ22", "Ответ23",
                 "Ответ24", "Ответ25", "Ответ26", "Ответ27", "Ответ28", "Ответ29", "Ответ30", "Ответ31", "Ответ32",
                 "Ответ33", "Ответ34",
                 "Ответ35", "Ответ36", "Ответ37", "Ответ38", "Ответ39", "Ответ40", "Ответ41", "Ответ42", "Ответ43",
                 "Ответ44", "Ответ45",
                 "Ответ46", "Ответ47", "Ответ48", "Ответ49", "Ответ50"])
        elif (table[0] == 1):
            nametable = 'ChildrenAgain'
            self.comboBox.addItems(
                ["Номер пациента", "ФИО пациента", "Дата ввода", "Дата рождения", "Возраст", "Школа", "Класс", "Пол",
                 "Ступень обучения",
                 "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6", "Ответ7", "Ответ8", "Ответ9", "Ответ10",
                 "Ответ11", "Ответ12",
                 "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17", "Ответ18", "Ответ19", "Ответ20", "Ответ21",
                 "Ответ22", "Ответ23",
                 "Ответ24", "Ответ25", "Ответ26", "Ответ27", "Описание"])
        elif (table[0] == 2):
            nametable = 'ChildrenAgain2'
            self.comboBox.addItems(
                ["Номер пациента", "ФИО пациента", "Дата ввода", "Дата рождения", "Возраст", "Школа", "Класс", "Пол",
                 "Ступень обучения",
                 "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6", "Ответ7", "Ответ8", "Ответ9", "Ответ10",
                 "Ответ11", "Ответ12",
                 "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17", "Ответ18", "Ответ19", "Ответ20", "Ответ21",
                 "Ответ22", "Ответ23",
                 "Ответ24", "Ответ25", "Ответ26", "Ответ27","Описание"])


        self.change = QtWidgets.QPushButton('Изменить', self)
        self.change.setGeometry(QtCore.QRect(220, 160, 121, 23))
        self.change.clicked.connect(self.changeform)

        self.new_2 = QtWidgets.QLineEdit(self)
        self.new_2.setGeometry(QtCore.QRect(190, 110, 131, 20))

        self.numberofpat = QtWidgets.QLineEdit(self)
        self.numberofpat.setGeometry(QtCore.QRect(190, 50, 131, 20))


# ----------------класс для работы с бд анкеты №1-------------------
class Ui_Show1(QtWidgets.QDialog):

    def load(self):
        if (person == 1):
            nametable = 'Children'
        elif (person == 2):
            nametable = 'Children2'
        elif (table[0] == 1):
            nametable = 'ChildrenAgain'
        elif (table[1] == 1):
            nametable = 'StatusRelatives'
        elif (table[0] == 2):
            nametable = 'ChildrenAgain2'
        elif(table[1] == 2):
            nametable = 'StatusTeacher'

        connection = sqlite3.connect('Anketa1.db')
        query = 'SELECT * from ' + nametable + ''
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.delete1 = Ui_Delete(self)


        self.resize(897, 570)
        self.setFixedSize(897, 570)
        self.setStyleSheet("")

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(250, 0, 641, 571))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setRowCount(20)
        self.sho = QtWidgets.QPushButton('Просмотр базы данных', self)
        self.sho.setGeometry(QtCore.QRect(20, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.sho.setFont(font)
        self.sho.clicked.connect(self.load)


        self.delete_2 = QtWidgets.QPushButton('Удаление записи', self)
        self.delete_2.setGeometry(QtCore.QRect(20, 50, 211, 31))
        self.delete_2.setFont(font)
        self.delete_2.clicked.connect(self.delete1.exec)

        if (person == 1):
            self.update1 = Ui_Update(self)
            self.setWindowTitle("База данных первичной анкеты (Родители ребенка)")
            self.tableWidget.setColumnCount(57)
            self.update = QtWidgets.QPushButton('Внесение изменений', self)
            self.update.setGeometry(QtCore.QRect(20, 90, 211, 31))
            self.update.setFont(font)
            self.update.clicked.connect(self.update1.exec)
            self.tableWidget.setHorizontalHeaderLabels(["Номер пациента", "ФИО пацианта", "Дата заполнения", "Возраст",
                                                        "Класс", "Школа", "Дата рождения", "Пол", "Ступень обучения",
                                                        "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6",
                                                        "Ответ7", "Ответ8", "Ответ9", "Ответ10", "Ответ11", "Ответ12",
                                                        "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17",
                                                        "Ответ18",
                                                        "Ответ19", "Ответ20", "Ответ21", "Ответ22", "Ответ23",
                                                        "Ответ24", "Ответ25", "Ответ26", "Ответ27", "Ответ28",
                                                        "Ответ29",
                                                        "Ответ30", "Ответ31", "Ответ32", "Ответ33", "Ответ34",
                                                        "Ответ35", "Ответ36", "Ответ37", "Ответ38", "Ответ39",
                                                        "Ответ40",
                                                        "Ответ41", "Ответ42", "Ответ43", "Ответ44", "Ответ45",
                                                        "Ответ46", "Ответ47", "Ответ48"])
        elif (person == 2):
            self.update1 = Ui_Update(self)
            self.tableWidget.setColumnCount(57)
            self.update = QtWidgets.QPushButton('Внесение изменений', self)
            self.update.setGeometry(QtCore.QRect(20, 90, 211, 31))
            self.update.setFont(font)
            self.update.clicked.connect(self.update1.exec)
            self.setWindowTitle("База данных первичной анкеты (Учитель)")
            self.tableWidget.setHorizontalHeaderLabels(["Номер пациента", "ФИО пацианта", "Дата заполнения", "Возраст",
                                                        "Класс", "Школа", "Дата рождения", "Пол", "Ступень обучения",
                                                        "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6",
                                                        "Ответ7", "Ответ8", "Ответ9", "Ответ10", "Ответ11", "Ответ12",
                                                        "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17",
                                                        "Ответ18",
                                                        "Ответ19", "Ответ20", "Ответ21", "Ответ22", "Ответ23",
                                                        "Ответ24", "Ответ25", "Ответ26", "Ответ27", "Ответ28",
                                                        "Ответ29",
                                                        "Ответ30", "Ответ31", "Ответ32", "Ответ33", "Ответ34",
                                                        "Ответ35", "Ответ36", "Ответ37", "Ответ38", "Ответ39",
                                                        "Ответ40",
                                                        "Ответ41", "Ответ42", "Ответ43", "Ответ44", "Ответ45",
                                                        "Ответ46", "Ответ47", "Ответ48", "Ответ49", "Ответ50"])
        elif (table[0] == 1):
            self.update1 = Ui_Update(self)
            self.tableWidget.setColumnCount(36)
            self.update = QtWidgets.QPushButton('Внесение изменений', self)
            self.update.setGeometry(QtCore.QRect(20, 90, 211, 31))
            self.update.setFont(font)
            self.update.clicked.connect(self.update1.exec)
            self.setWindowTitle("База данных вторичной анкеты (Родители ребенка)")
            self.tableWidget.setHorizontalHeaderLabels(["Номер пациента", "ФИО пацианта", "Дата заполнения", "Возраст",
                                                        "Класс", "Школа", "Дата рождения", "Пол", "Ступень обучения",
                                                        "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6",
                                                        "Ответ7", "Ответ8", "Ответ9", "Ответ10", "Ответ11", "Ответ12",
                                                        "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17",
                                                        "Ответ18",
                                                        "Ответ19", "Ответ20", "Ответ21", "Ответ22", "Ответ23",
                                                        "Ответ24", "Ответ25", "Ответ26", "Описание побочных симптомов"])
        elif (table[1] == 1):
            self.tableWidget.setColumnCount(19)
            self.setWindowTitle("Выявленные дети по данным первичной анкеты (Родители ребенка)")
            self.tableWidget.setHorizontalHeaderLabels(["Номер пациента", "Возраст", "Класс", "Пол", "Ступень обучения",
            "Сумма ответов по шкале 1", "Сумма ответов по шкале 2", "Сумма ответов по шкале 3", "Сумма ответов по шкале 4",
            "Сумма ответов по шкале 5", "Сумма ответов по шкале 6", "Сумма ответов по шкале 7", "Cубшкала дефицита внимания",
             "Субшкала гиперактивности + импульсивности","Субшкала невнимательности + гиперактивности",
             "Субшкала реакций оппозиции(протеста)","Субшкала др. поведенческих проблем","Субшкала тревожно-депрессивной симптоматики",
                "Субшкала социальной адаптации"])
        elif (table[0] == 2):
            self.update1 = Ui_Update(self)
            self.tableWidget.setColumnCount(36)
            self.setWindowTitle("База данных вторичной анкеты (Учитель)")
            self.update = QtWidgets.QPushButton('Внесение изменений', self)
            self.update.setGeometry(QtCore.QRect(20, 90, 211, 31))
            self.update.setFont(font)
            self.update.clicked.connect(self.update1.exec)
            self.tableWidget.setHorizontalHeaderLabels(["Номер пациента", "ФИО пацианта", "Дата заполнения", "Возраст",
                                                        "Класс", "Школа", "Дата рождения", "Пол", "Ступень обучения",
                                                        "Ответ1", "Ответ2", "Ответ3", "Ответ4", "Ответ5", "Ответ6",
                                                        "Ответ7", "Ответ8", "Ответ9", "Ответ10", "Ответ11", "Ответ12",
                                                        "Ответ13", "Ответ14", "Ответ15", "Ответ16", "Ответ17",
                                                        "Ответ18",
                                                        "Ответ19", "Ответ20", "Ответ21", "Ответ22", "Ответ23",
                                                        "Ответ24", "Ответ25", "Ответ26", "Описание побочных симптомов"])
        elif (table[1] == 2):
            self.tableWidget.setColumnCount(19)
            self.setWindowTitle("Выявленные дети по данным первичной анкеты (Учитель)")
            self.tableWidget.setHorizontalHeaderLabels(["Номер пациента", "Возраст", "Класс", "Пол", "Ступень обучения",
                                                        "Сумма ответов по шкале 1", "Сумма ответов по шкале 2",
                                                        "Сумма ответов по шкале 3", "Сумма ответов по шкале 4",
                                                        "Сумма ответов по шкале 5", "Сумма ответов по шкале 6",
                                                        "Сумма ответов по шкале 7", "Cубшкала дефицита внимания",
                                                        "Субшкала гиперактивности + импульсивности",
                                                        "Субшкала невнимательности + гиперактивности",
                                                        "Субшкала реакций оппозиции(протеста)",
                                                        "Субшкала др. поведенческих проблем",
                                                        "Субшкала тревожно-депрессивной симптоматики",
                                                        "Субшкала социальной адаптации"])


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)



# ----------------класс для личных данных пациента укороченный для статистики-------------------
class Ui_S(QtWidgets.QDialog):
    def openA1(self):
        self.main.t3 = self.ageBox1.currentText()
        self.main.t4 = self.ageBox2.currentText()
        text2 = ''
        buf = 0
        if (self.sexBox.currentText() == "все"):
            buf = 0
            text2 = "Общее количество муж. + жен. "
        if (self.sexBox.currentText() == "мужской"):
            buf = 1
            text2 = "Только муж. "
        if (self.sexBox.currentText() == "женский"):
            buf = 2
            text2 = "Только жен. "
        self.main.t5 = str(buf)

        self.main.t7 = str(self.classBox.currentText())
        buf1 = ""
        if (self.levelBox.currentText() == '1 ступень  (1-4класс)'):
            buf1 = 1
        if (self.levelBox.currentText() == '2 ступень  (5-8класс)'):
            buf1 = 2
        if (self.levelBox.currentText() == '3 ступень  (9-11класс)'):
            buf1 = 3
        self.main.t8 = str(buf1)

        flag = 0
        connection = sqlite3.connect('Anketa1.db')
        query = 'Select count(*) from Children '
        if (buf == 1 or buf == 2):
            query += 'where Sex='
            query += str(buf)
            flag = 1
        if (self.main.t3 == '' or self.main.t4 == ''): query += ''
        r1 = self.main.t3
        r2 = self.main.t4
        if (r1 > r2):
            b = self.t3
            self.main.t3 = self.main.t4
            self.main.t4 = b
            if (flag == 0):
                query += "where Age between "
            else:
                query += ' and Age between '
            query += self.main.t3
            query += ' and '
            query += self.main.t4
        if (r1 < r2):
            if (flag == 0):
                query += "where Age between "
            else:
                query += ' and Age between '
            query += self.main.t3
            query += ' and '
            query += self.main.t4

        if (self.main.t7 == ''): query += ''
        if (self.main.t7 != ''):
            if (flag == 0):
                query += "where class="
            else:
                query += ' and class='
            query += self.main.t7

        if (self.main.t8 == ''): query += ''
        if (self.main.t8 == '1'):
            if (flag == 0):
                query += 'where Level=1'
            else:
                query += ' and Level=1'

        if (self.main.t8 == '2'):
            if (flag == 0):
                query += 'where Level=2'
            else:
                query += ' and Level=2'

        if (self.main.t8 == '3'):
            if (flag == 0):
                query += 'where Level=3'
            else:
                query += ' and Level=3'
        print(query)
        result = connection.execute(query)
        row = result.fetchall()
        sq1 = row[0][0]
        query = 'Select count(*) from Children '
        # if( buf == 1 or buf == 2 ):
        #     query += 'where Sex='
        #     query += str(buf)
        print(query)
        result = connection.execute(query)
        row = result.fetchall()
        sq2 = row[0][0]
        sq1 = (sq1 * 100) / sq2
        text2 += str(sq1)
        text2 += "%"
        self.main.descrip.setText(text2)
        self.close()

    def cl(self):
        self.close()

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

        self.setGeometry(200, 50, 331, 372)
        self.setFixedSize(340, 200)
        self.setWindowTitle('Дополнительные параметры')

        self.label_7 = QtWidgets.QLabel('Пол', self).setGeometry(QtCore.QRect(40, 20, 41, 16))
        self.label_10 = QtWidgets.QLabel('Ступень обучения', self).setGeometry(QtCore.QRect(40, 110, 151, 16))
        self.label_6 = QtWidgets.QLabel('Возраст от', self).setGeometry(QtCore.QRect(40, 50, 90, 16))
        self.label_6 = QtWidgets.QLabel('до', self).setGeometry(QtCore.QRect(200, 50, 71, 16))
        self.label_9 = QtWidgets.QLabel('Класс', self).setGeometry(QtCore.QRect(40, 80, 51, 16))


        self.classBox = QtWidgets.QComboBox(self)
        self.classBox.setGeometry(QtCore.QRect(110, 80, 61, 22))
        self.classBox.addItems(["","1","2","3","4","5","6","7","8","9","10","11"])

        self.levelBox = QtWidgets.QComboBox(self)
        self.levelBox.setGeometry(QtCore.QRect(200, 110, 120, 22))
        self.levelBox.addItems(["","1 ступень  (1-4класс)","2 ступень  (5-8класс)","3 ступень  (9-11класс)"])

        self.sexBox = QtWidgets.QComboBox(self)
        self.sexBox.setGeometry(QtCore.QRect(90, 20, 81, 22))
        self.sexBox.addItems(["все", "мужской", "женский"])

        self.ageBox1 = QtWidgets.QComboBox(self)
        self.ageBox1.setGeometry(QtCore.QRect(140, 50, 51, 22))
        self.ageBox1.addItems(["","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])

        self.ageBox2 = QtWidgets.QComboBox(self)
        self.ageBox2.setGeometry(QtCore.QRect(240, 50, 51, 22))
        self.ageBox2.addItems(["","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])

        self.savebutton = QtWidgets.QPushButton('Добавить', self)
        self.savebutton.setGeometry(QtCore.QRect(160, 150, 81, 23))
        self.savebutton.clicked.connect(self.openA1)

        self.cleanbutton = QtWidgets.QPushButton('Отмена', self)
        self.cleanbutton.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.cleanbutton.clicked.connect(self.cl)


# ----------------класс статистики 1-------------------
class Ui_Stat1(QtWidgets.QDialog):
    def hh(self, answer, number):
        if (person == 1):
            nametable = 'Children'
        elif (person == 2):
            nametable = 'Children2'
        connection = sqlite3.connect('Anketa1.db')
        query1 = 'Select count(' + answer + ') from ' + nametable + ' where ' + answer + '=' + str(number)
        if (self.t5 == '0'): query1 += ''
        if (self.t5 == '1'): query1 += ' and Sex=1'
        if (self.t5 == '2'): query1 += ' and Sex=2'
        if (self.t3 == '' or self.t4 == ''): query1 += ''
        r1 = self.t3
        r2 = self.t4
        if (r1 > r2):
            b = self.t3
            self.t3 = self.t4
            self.t4 = b
            query1 += ' and Age between '
            query1 += self.t3
            query1 += ' and '
            query1 += self.t4
        if (r1 < r2):
            query1 += ' and Age between '
            query1 += self.t3
            query1 += ' and '
            query1 += self.t4

        if (self.t7 == ''): query1 += ''
        if (self.t7 != ''):
            query1 += ' and class='
            query1 += self.t7

        if (self.t8 == ''): query1 += ''
        if (self.t8 == '1'): query1 += ' and Level=1'
        if (self.t8 == '2'): query1 += ' and Level=2'
        if (self.t8 == '3'): query1 += ' and Level=3'

        result = connection.execute(query1)
        row = result.fetchall()
        connection.commit()
        connection.close()
        return row[0][0]

    def s(self):

        # ---------------------------Вопрос1----------------------------------------
        part = [self.hh('answer1', 0), self.hh('answer1', 1), self.hh('answer1', 2), self.hh('answer1', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin11.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin12.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin13.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin14.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос2----------------------------------------
        part = [self.hh('answer2', 0), self.hh('answer2', 1), self.hh('answer2', 2), self.hh('answer2', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin21.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin22.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin23.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin24.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос3----------------------------------------
        part = [self.hh('answer3', 0), self.hh('answer3', 1), self.hh('answer3', 2), self.hh('answer3', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin31.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin32.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin33.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin34.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос4----------------------------------------
        part = [self.hh('answer4', 0), self.hh('answer4', 1), self.hh('answer4', 2), self.hh('answer4', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin41.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin42.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin43.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin44.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос5----------------------------------------
        part = [self.hh('answer5', 0), self.hh('answer5', 1), self.hh('answer5', 2), self.hh('answer5', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin51.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin52.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin53.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin54.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос6----------------------------------------
        part = [self.hh('answer6', 0), self.hh('answer6', 1), self.hh('answer6', 2), self.hh('answer6', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin61.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin62.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin63.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin64.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос7----------------------------------------
        part = [self.hh('answer7', 0), self.hh('answer7', 1), self.hh('answer7', 2), self.hh('answer7', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin71.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin72.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin73.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin74.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос8----------------------------------------
        part = [self.hh('answer8', 0), self.hh('answer8', 1), self.hh('answer8', 2), self.hh('answer8', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin81.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin82.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin83.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin84.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос9----------------------------------------
        part = [self.hh('answer9', 0), self.hh('answer9', 1), self.hh('answer9', 2), self.hh('answer9', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin91.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin92.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin93.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin94.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос10----------------------------------------
        part = [self.hh('answer10', 0), self.hh('answer10', 1), self.hh('answer10', 2), self.hh('answer10', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin101.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin102.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin103.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin104.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос11----------------------------------------
        part = [self.hh('answer11', 0), self.hh('answer11', 1), self.hh('answer11', 2), self.hh('answer11', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin111.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin112.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin113.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin114.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос12----------------------------------------
        part = [self.hh('answer12', 0), self.hh('answer12', 1), self.hh('answer12', 2), self.hh('answer12', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin121.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin122.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin123.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin124.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос13----------------------------------------
        part = [self.hh('answer13', 0), self.hh('answer13', 1), self.hh('answer13', 2), self.hh('answer13', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin131.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin132.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin133.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin134.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос14----------------------------------------
        part = [self.hh('answer14', 0), self.hh('answer14', 1), self.hh('answer14', 2), self.hh('answer14', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin141.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin142.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin143.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin144.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос15----------------------------------------
        part = [self.hh('answer15', 0), self.hh('answer15', 1), self.hh('answer15', 2), self.hh('answer15', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin151.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin152.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin153.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin154.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос16----------------------------------------
        part = [self.hh('answer16', 0), self.hh('answer16', 1), self.hh('answer16', 2), self.hh('answer16', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin161.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin162.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin163.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin164.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос17----------------------------------------
        part = [self.hh('answer17', 0), self.hh('answer17', 1), self.hh('answer17', 2), self.hh('answer17', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin171.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin172.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin173.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin174.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос18----------------------------------------
        part = [self.hh('answer18', 0), self.hh('answer18', 1), self.hh('answer18', 2), self.hh('answer18', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin181.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin182.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin183.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin184.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос19----------------------------------------
        part = [self.hh('answer19', 0), self.hh('answer19', 1), self.hh('answer19', 2), self.hh('answer19', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin191.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin192.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin193.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin194.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос20----------------------------------------
        part = [self.hh('answer20', 0), self.hh('answer20', 1), self.hh('answer20', 2), self.hh('answer20', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin201.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin202.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin203.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin204.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос21----------------------------------------
        part = [self.hh('answer21', 0), self.hh('answer21', 1), self.hh('answer21', 2), self.hh('answer21', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin211.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin212.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin213.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin214.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос22----------------------------------------
        part = [self.hh('answer22', 0), self.hh('answer22', 1), self.hh('answer22', 2), self.hh('answer22', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin221.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin222.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin223.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin224.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос23----------------------------------------
        part = [self.hh('answer23', 0), self.hh('answer23', 1), self.hh('answer23', 2), self.hh('answer23', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin231.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin232.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin233.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin234.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос24----------------------------------------
        part = [self.hh('answer24', 0), self.hh('answer24', 1), self.hh('answer24', 2), self.hh('answer24', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin241.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin242.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin243.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin244.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос25----------------------------------------
        part = [self.hh('answer25', 0), self.hh('answer25', 1), self.hh('answer25', 2), self.hh('answer25', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin251.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin252.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin253.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin254.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос26----------------------------------------
        part = [self.hh('answer26', 0), self.hh('answer26', 1), self.hh('answer26', 2), self.hh('answer26', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin261.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin262.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin263.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin264.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос27----------------------------------------
        part = [self.hh('answer27', 0), self.hh('answer27', 1), self.hh('answer27', 2), self.hh('answer27', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin271.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin272.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin273.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin274.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос28----------------------------------------
        part = [self.hh('answer28', 0), self.hh('answer28', 1), self.hh('answer28', 2), self.hh('answer28', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin281.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin282.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin283.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin284.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос29----------------------------------------
        part = [self.hh('answer29', 0), self.hh('answer29', 1), self.hh('answer29', 2), self.hh('answer29', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin291.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin292.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin293.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin294.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос30----------------------------------------
        part = [self.hh('answer30', 0), self.hh('answer30', 1), self.hh('answer30', 2), self.hh('answer30', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin301.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin302.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin303.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin304.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос31----------------------------------------
        part = [self.hh('answer31', 0), self.hh('answer31', 1), self.hh('answer31', 2), self.hh('answer31', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin311.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin312.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin313.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin314.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос32----------------------------------------
        part = [self.hh('answer32', 0), self.hh('answer32', 1), self.hh('answer32', 2), self.hh('answer32', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin321.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin322.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin323.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin324.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос33----------------------------------------
        part = [self.hh('answer33', 0), self.hh('answer33', 1), self.hh('answer33', 2), self.hh('answer33', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin331.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin332.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin333.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin334.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос34----------------------------------------
        part = [self.hh('answer34', 0), self.hh('answer34', 1), self.hh('answer34', 2), self.hh('answer34', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin341.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin342.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin343.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin344.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос35----------------------------------------
        part = [self.hh('answer35', 0), self.hh('answer35', 1), self.hh('answer35', 2), self.hh('answer35', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin351.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin352.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin353.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin354.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос36----------------------------------------
        part = [self.hh('answer36', 0), self.hh('answer36', 1), self.hh('answer36', 2), self.hh('answer36', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin361.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin362.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin363.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin364.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос37----------------------------------------
        part = [self.hh('answer37', 0), self.hh('answer37', 1), self.hh('answer37', 2), self.hh('answer37', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin371.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin372.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin373.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin374.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос38----------------------------------------
        part = [self.hh('answer38', 0), self.hh('answer38', 1), self.hh('answer38', 2), self.hh('answer38', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin381.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin382.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin383.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin384.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос39----------------------------------------
        part = [self.hh('answer39', 0), self.hh('answer39', 1), self.hh('answer39', 2), self.hh('answer39', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin391.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin392.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin393.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin394.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос40----------------------------------------
        part = [self.hh('answer40', 0), self.hh('answer40', 1), self.hh('answer40', 2), self.hh('answer40', 3)]
        summa = part[0] + part[1] + part[2] + part[3]
        self.lin401.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin402.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin403.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin404.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос41----------------------------------------
        part = [self.hh('answer41', 1), self.hh('answer41', 2), self.hh('answer41', 3), self.hh('answer41', 4),
                self.hh('answer41', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin411.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin412.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin413.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin414.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin415.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос42----------------------------------------
        part = [self.hh('answer42', 1), self.hh('answer42', 2), self.hh('answer42', 3), self.hh('answer42', 4),
                self.hh('answer42', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin421.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin422.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin423.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin424.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin425.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос43----------------------------------------
        part = [self.hh('answer43', 1), self.hh('answer43', 2), self.hh('answer43', 3), self.hh('answer43', 4),
                self.hh('answer43', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin431.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin432.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin433.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin434.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin435.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос44----------------------------------------
        part = [self.hh('answer44', 1), self.hh('answer44', 2), self.hh('answer44', 3), self.hh('answer44', 4),
                self.hh('answer44', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin441.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin442.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin443.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin444.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin445.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос45----------------------------------------
        part = [self.hh('answer45', 1), self.hh('answer45', 2), self.hh('answer45', 3), self.hh('answer45', 4),
                self.hh('answer45', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin451.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin452.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin453.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin454.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin455.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос46----------------------------------------
        part = [self.hh('answer46', 1), self.hh('answer46', 2), self.hh('answer46', 3), self.hh('answer46', 4),
                self.hh('answer46', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin461.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin462.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin463.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin464.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin465.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос47----------------------------------------
        part = [self.hh('answer47', 1), self.hh('answer47', 2), self.hh('answer47', 3), self.hh('answer47', 4),
                self.hh('answer47', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin471.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin472.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin473.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin474.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin475.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")
        # ---------------------------Вопрос48----------------------------------------
        part = [self.hh('answer48', 1), self.hh('answer48', 2), self.hh('answer48', 3), self.hh('answer48', 4),
                self.hh('answer48', 5)]
        summa = part[0] + part[1] + part[2] + part[3] + part[4]
        self.lin481.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%")
        self.lin482.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%")
        self.lin483.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%")
        self.lin484.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%")
        self.lin485.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = Ui_S(self)

        self.setGeometry(200, 50, 1020, 700)
        self.setFixedSize(1020, 700)
        self.setStyleSheet("")
        if (person == 1):
            self.setWindowTitle('Общая статистика первичного анкетирования по симптомам (Родители ребенка)')
        elif (person == 2):
            self.setWindowTitle('Общая статистика первичного анкетирования по симптомам (Учитель)')

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(40, 70, 960, 620))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        # self.tabWidget.setEnabled(False)

        self.tab = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab, "1 страница")
        self.tab_2 = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab_2, "2 страница")
        self.tab_3 = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab_3, "3 страница")

        self.label1 = QtWidgets.QLabel('1) Неспособен внимательно следить за деталями, делает нелепые ошибки', self.tab).setGeometry(QtCore.QRect(10, 20, 700, 16))
        self.label2 = QtWidgets.QLabel('2) Имеет трудности в выполнении заданий или игровой деятельности...',self.tab).setGeometry(QtCore.QRect(10, 50, 850, 16))
        self.label3 = QtWidgets.QLabel('3) Не слушает, когда к нему обращаются', self.tab).setGeometry(QtCore.QRect(10, 80, 350, 16))
        self.label4 = QtWidgets.QLabel('4) Не заканчивает начатого занятия (непреднамеренно)', self.tab).setGeometry(QtCore.QRect(10, 110, 700, 16))
        self.label5 = QtWidgets.QLabel('5) Несобран, неорганизован', self.tab).setGeometry(QtCore.QRect(10, 140, 300, 16))
        self.label6 = QtWidgets.QLabel('6) Избегает, не любит или не хочет соглашаться выполнять задания...', self.tab).setGeometry(QtCore.QRect(10, 170, 850, 16))
        self.label7 = QtWidgets.QLabel('7) Путает расписание, теряет вещи, необходимые для выполнения заданий',self.tab).setGeometry(QtCore.QRect(10, 200, 800, 16))
        self.label8 = QtWidgets.QLabel('8) Легко отвлекается на все, что происходит вокруг', self.tab).setGeometry(QtCore.QRect(10, 230, 500, 16))
        self.label9 = QtWidgets.QLabel('9) Забывает выполнять каждодневные процедуры (почистить зубы и т.п.)', self.tab).setGeometry(QtCore.QRect(10, 260, 550, 16))
        self.label10 = QtWidgets.QLabel('10) Беспокойно двигает руками или ногами, ерзает на месте', self.tab).setGeometry(QtCore.QRect(10, 290, 500, 16))
        self.label11 = QtWidgets.QLabel('11) Покидает свое место в классе или в другом месте, не может усидеть', self.tab).setGeometry(QtCore.QRect(10, 320, 550, 16))
        self.label12 = QtWidgets.QLabel('12) Начинает бегать и карабкаться куда-то, когда это неуместно', self.tab).setGeometry(QtCore.QRect(10, 350, 550, 16))
        self.label13 = QtWidgets.QLabel('13) Не может тихо играть, неадекватно шумен', self.tab).setGeometry(QtCore.QRect(10, 380, 500, 16))
        self.label14 = QtWidgets.QLabel('14) Действует как «заведенный», как будто к нему приделан «моторчик»', self.tab).setGeometry(QtCore.QRect(10, 410, 550, 16))
        self.label15 = QtWidgets.QLabel('15) Чрезмерно разговорчивый, без учета социальных ограничений', self.tab).setGeometry(QtCore.QRect(10, 440, 520, 16))
        self.label16 = QtWidgets.QLabel('16) Выпаливает ответы до того, как завершены вопросы', self.tab).setGeometry(QtCore.QRect(10, 470, 500, 16))
        self.label17 = QtWidgets.QLabel('17) Не способен стоять в очередях, дожидаться своей очереди', self.tab).setGeometry(QtCore.QRect(10, 500, 520, 16))
        self.label18 = QtWidgets.QLabel('18) Перебивает других или вмешивается в разговоры или занятия других', self.tab).setGeometry(QtCore.QRect(10, 530, 550, 16))
        self.label19 = QtWidgets.QLabel('19) Вступает в конфликты со взрослыми', self.tab).setGeometry(QtCore.QRect(10, 560, 400, 16))
        self.label20 = QtWidgets.QLabel('20) Теряет самоконтроль, склонен к эмоциональным «взрывам»', self.tab_2).setGeometry(QtCore.QRect(10, 20, 500, 16))
        self.label21 = QtWidgets.QLabel('21) Не слушается и отказывается подчиняться установленным правилам взрослых', self.tab_2).setGeometry(QtCore.QRect(10, 50, 700, 16))
        self.label22 = QtWidgets.QLabel('22) Поступает наперекор другим', self.tab_2).setGeometry(QtCore.QRect(10, 80, 300, 16))
        self.label23 = QtWidgets.QLabel('23) Обвиняет других в своих ошибках и поведенческих проблемах', self.tab_2).setGeometry(QtCore.QRect(10, 110, 500, 16))
        self.label24 = QtWidgets.QLabel('24) Стремится добиться своего, легко «выходит из себя»', self.tab_2).setGeometry(QtCore.QRect(10, 140, 450, 16))
        self.label25 = QtWidgets.QLabel('25) Злой и раздражительный', self.tab_2).setGeometry(QtCore.QRect(10, 170, 250, 16))
        self.label26 = QtWidgets.QLabel('26) Не забывает обид, стремится отомстить', self.tab_2).setGeometry(QtCore.QRect(10, 200, 390, 16))
        self.label27 = QtWidgets.QLabel('27) Угрожает и запугивает других', self.tab_2).setGeometry(QtCore.QRect(10, 230, 300, 16))
        self.label28 = QtWidgets.QLabel('28) Грубит взрослым и употребляет нецензурные слова', self.tab_2).setGeometry(QtCore.QRect(10, 260, 450, 16))
        self.label29 = QtWidgets.QLabel('29) Обманывает, чтобы избежать наказания', self.tab_2).setGeometry(QtCore.QRect(10, 290, 350, 16))
        self.label30 = QtWidgets.QLabel('30) Пропускает уроки без разрешения', self.tab_2).setGeometry(QtCore.QRect(10, 320, 300, 16))
        self.label31 = QtWidgets.QLabel('31) Жестокий, драчливый, склонен к физической расправе', self.tab_2).setGeometry(QtCore.QRect(10, 350, 800, 16))
        self.label32 = QtWidgets.QLabel('32) Намеренно портит свои вещи и вещи других', self.tab_2).setGeometry(QtCore.QRect(10, 380, 450, 16))
        self.label33 = QtWidgets.QLabel('33) Имеет серьезные поведенческие проступки ...', self.tab_2).setGeometry(QtCore.QRect(10, 410, 800, 16))
        self.label34 = QtWidgets.QLabel('34) Робкий, боязливый, тревожный', self.tab_2).setGeometry(QtCore.QRect(10, 470, 300, 16))
        self.label35 = QtWidgets.QLabel('35) Боится пробовать делать что-то новое из-за страха...', self.tab_2).setGeometry(QtCore.QRect(10, 500, 800, 16))
        self.label36 = QtWidgets.QLabel('36) Чувсивует себя бесполезным, ощущает себя хуже других', self.tab_2).setGeometry(QtCore.QRect(10, 530, 700, 16))
        self.label37 = QtWidgets.QLabel('37) Обвиняет себя, чувствует себя виноватым', self.tab_2).setGeometry(QtCore.QRect(10, 560, 450, 16))
        self.label38 = QtWidgets.QLabel('38) Ощущает себя ненужным, жалуется «никто не любит меня»', self.tab_3).setGeometry(QtCore.QRect(10, 20, 500, 16))
        self.label39 = QtWidgets.QLabel('39) Грустный, несчастливый или удрученный', self.tab_3).setGeometry(QtCore.QRect(10, 50, 450, 16))
        self.label40 = QtWidgets.QLabel('40) Застенчивый или легко смущающийся', self.tab_3).setGeometry(QtCore.QRect(10, 80, 440, 16))

        self.help1 = QtWidgets.QLabel('Симптомы', self.tab)
        self.help1.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help2 = QtWidgets.QLabel('Симптомы', self.tab_2)
        self.help2.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help3 = QtWidgets.QLabel('Другие поведенческие проступки', self.tab_2)
        self.help3.setGeometry(QtCore.QRect(390, 440, 531, 20))
        self.help4 = QtWidgets.QLabel('Симптомы', self.tab_3)
        self.help4.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help5 = QtWidgets.QLabel('Успешность', self.tab_3)
        self.help5.setGeometry(QtCore.QRect(390, 120, 101, 21))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.help1.setFont(font)
        self.help2.setFont(font)
        self.help3.setFont(font)
        self.help4.setFont(font)
        self.help5.setFont(font)

        if (person == 1):
            self.label41 = QtWidgets.QLabel('41) Следование школьным правилам', self.tab_3).setGeometry(QtCore.QRect(10, 170, 400, 16))
            self.label42 = QtWidgets.QLabel('42) Чтение', self.tab_3).setGeometry(QtCore.QRect(10, 200, 100, 13))
            self.label43 = QtWidgets.QLabel('43) Письмо', self.tab_3).setGeometry(QtCore.QRect(10, 230, 100, 13))
            self.label44 = QtWidgets.QLabel('44) Математика', self.tab_3).setGeometry(QtCore.QRect(10, 260, 150, 16))
            self.label45 = QtWidgets.QLabel('45) Отношения с родителями', self.tab_3).setGeometry(QtCore.QRect(10, 290, 300, 16))
            self.label46 = QtWidgets.QLabel('46) Отношения с братьями /сестрами', self.tab_3).setGeometry(QtCore.QRect(10, 320, 300, 16))
            self.label47 = QtWidgets.QLabel('47) Отношения со сверстниками', self.tab_3).setGeometry(QtCore.QRect(10, 350, 300, 16))
            self.label48 = QtWidgets.QLabel('48) Участие в организованных мероприятиях ...',self.tab_3).setGeometry(QtCore.QRect(10, 380, 800, 16))
        elif(person == 2):
            self.label41 = QtWidgets.QLabel('41) Чтение', self.tab_3).setGeometry(QtCore.QRect(10, 170, 100, 16))
            self.label42 = QtWidgets.QLabel('42) Математика', self.tab_3).setGeometry(QtCore.QRect(10, 200, 150, 13))
            self.label43 = QtWidgets.QLabel('43) Письмо', self.tab_3).setGeometry(QtCore.QRect(10, 230, 100, 13))
            self.label44 = QtWidgets.QLabel('44) Отношения со сверстниками', self.tab_3).setGeometry(QtCore.QRect(10, 260, 300, 16))
            self.label45 = QtWidgets.QLabel('45) Следование инструкциям', self.tab_3).setGeometry(QtCore.QRect(10, 290, 300, 16))
            self.label46 = QtWidgets.QLabel('46) Нарушение порядка на занятиях', self.tab_3).setGeometry(QtCore.QRect(10, 320, 300, 16))
            self.label47 = QtWidgets.QLabel('47) Завершенность действий', self.tab_3).setGeometry(QtCore.QRect(10, 350, 300, 16))
            self.label48 = QtWidgets.QLabel('48) Организационные навыки',self.tab_3).setGeometry(QtCore.QRect(10, 380, 300, 16))


        self.pushButton = QtWidgets.QPushButton("Критерии вычисления", self)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 180, 31))
        self.pushButton.clicked.connect(self.dialog.exec)

        self.save1pushButton = QtWidgets.QPushButton('Вывести результат', self)
        self.save1pushButton.setGeometry(QtCore.QRect(500, 10, 161, 31))
        self.save1pushButton.clicked.connect(self.s)

        self.descrip = QtWidgets.QLabel('Общее количество муж. + жен.', self)
        self.descrip.setGeometry(QtCore.QRect(230, 15, 400, 16))


        self.tabWidget.setCurrentIndex(0)
        # ---------------------------------------------------------------------------------------------------
        self.never = QtWidgets.QLabel('Никогда', self.tab).setGeometry(QtCore.QRect(650, 0, 70, 16))
        self.never = QtWidgets.QLabel('Иногда', self.tab).setGeometry(QtCore.QRect(730, 0, 70, 16))
        self.never = QtWidgets.QLabel('Часто', self.tab).setGeometry(QtCore.QRect(800, 0, 70, 16))
        self.never = QtWidgets.QLabel('Очень часто', self.tab).setGeometry(QtCore.QRect(855, 0, 120, 16))

        self.lin11 = QtWidgets.QLineEdit(self.tab)
        self.lin11.setGeometry(QtCore.QRect(650, 20, 70, 20))

        self.lin12 = QtWidgets.QLineEdit(self.tab)
        self.lin12.setGeometry(QtCore.QRect(720, 20, 70, 20))

        self.lin13 = QtWidgets.QLineEdit(self.tab)
        self.lin13.setGeometry(QtCore.QRect(790, 20, 70, 20))

        self.lin14 = QtWidgets.QLineEdit(self.tab)
        self.lin14.setGeometry(QtCore.QRect(860, 20, 70, 20))

        self.lin21 = QtWidgets.QLineEdit(self.tab)
        self.lin21.setGeometry(QtCore.QRect(650, 50, 70, 20))

        self.lin22 = QtWidgets.QLineEdit(self.tab)
        self.lin22.setGeometry(QtCore.QRect(720, 50, 70, 20))

        self.lin23 = QtWidgets.QLineEdit(self.tab)
        self.lin23.setGeometry(QtCore.QRect(790, 50, 70, 20))

        self.lin24 = QtWidgets.QLineEdit(self.tab)
        self.lin24.setGeometry(QtCore.QRect(860, 50, 70, 20))

        self.lin31 = QtWidgets.QLineEdit(self.tab)
        self.lin31.setGeometry(QtCore.QRect(650, 80, 70, 20))

        self.lin32 = QtWidgets.QLineEdit(self.tab)
        self.lin32.setGeometry(QtCore.QRect(720, 80, 70, 20))

        self.lin33 = QtWidgets.QLineEdit(self.tab)
        self.lin33.setGeometry(QtCore.QRect(790, 80, 70, 20))

        self.lin34 = QtWidgets.QLineEdit(self.tab)
        self.lin34.setGeometry(QtCore.QRect(860, 80, 70, 20))

        self.lin41 = QtWidgets.QLineEdit(self.tab)
        self.lin41.setGeometry(QtCore.QRect(650, 110, 70, 20))

        self.lin42 = QtWidgets.QLineEdit(self.tab)
        self.lin42.setGeometry(QtCore.QRect(720, 110, 70, 20))

        self.lin43 = QtWidgets.QLineEdit(self.tab)
        self.lin43.setGeometry(QtCore.QRect(790, 110, 70, 20))

        self.lin44 = QtWidgets.QLineEdit(self.tab)
        self.lin44.setGeometry(QtCore.QRect(860, 110, 70, 20))

        self.lin51 = QtWidgets.QLineEdit(self.tab)
        self.lin51.setGeometry(QtCore.QRect(650, 140, 70, 20))

        self.lin52 = QtWidgets.QLineEdit(self.tab)
        self.lin52.setGeometry(QtCore.QRect(720, 140, 70, 20))

        self.lin53 = QtWidgets.QLineEdit(self.tab)
        self.lin53.setGeometry(QtCore.QRect(790, 140, 70, 20))

        self.lin54 = QtWidgets.QLineEdit(self.tab)
        self.lin54.setGeometry(QtCore.QRect(860, 140, 70, 20))

        self.lin61 = QtWidgets.QLineEdit(self.tab)
        self.lin61.setGeometry(QtCore.QRect(650, 170, 70, 20))

        self.lin62 = QtWidgets.QLineEdit(self.tab)
        self.lin62.setGeometry(QtCore.QRect(720, 170, 70, 20))

        self.lin63 = QtWidgets.QLineEdit(self.tab)
        self.lin63.setGeometry(QtCore.QRect(790, 170, 70, 20))

        self.lin64 = QtWidgets.QLineEdit(self.tab)
        self.lin64.setGeometry(QtCore.QRect(860, 170, 70, 20))

        self.lin71 = QtWidgets.QLineEdit(self.tab)
        self.lin71.setGeometry(QtCore.QRect(650, 200, 70, 20))

        self.lin72 = QtWidgets.QLineEdit(self.tab)
        self.lin72.setGeometry(QtCore.QRect(720, 200, 70, 20))

        self.lin73 = QtWidgets.QLineEdit(self.tab)
        self.lin73.setGeometry(QtCore.QRect(790, 200, 70, 20))

        self.lin74 = QtWidgets.QLineEdit(self.tab)
        self.lin74.setGeometry(QtCore.QRect(860, 200, 70, 20))

        self.lin81 = QtWidgets.QLineEdit(self.tab)
        self.lin81.setGeometry(QtCore.QRect(650, 230, 70, 20))

        self.lin82 = QtWidgets.QLineEdit(self.tab)
        self.lin82.setGeometry(QtCore.QRect(720, 230, 70, 20))

        self.lin83 = QtWidgets.QLineEdit(self.tab)
        self.lin83.setGeometry(QtCore.QRect(790, 230, 70, 20))

        self.lin84 = QtWidgets.QLineEdit(self.tab)
        self.lin84.setGeometry(QtCore.QRect(860, 230, 70, 20))

        self.lin91 = QtWidgets.QLineEdit(self.tab)
        self.lin91.setGeometry(QtCore.QRect(650, 260, 70, 20))

        self.lin92 = QtWidgets.QLineEdit(self.tab)
        self.lin92.setGeometry(QtCore.QRect(720, 260, 70, 20))

        self.lin93 = QtWidgets.QLineEdit(self.tab)
        self.lin93.setGeometry(QtCore.QRect(790, 260, 70, 20))

        self.lin94 = QtWidgets.QLineEdit(self.tab)
        self.lin94.setGeometry(QtCore.QRect(860, 260, 70, 20))

        self.lin101 = QtWidgets.QLineEdit(self.tab)
        self.lin101.setGeometry(QtCore.QRect(650, 290, 70, 20))

        self.lin102 = QtWidgets.QLineEdit(self.tab)
        self.lin102.setGeometry(QtCore.QRect(720, 290, 70, 20))

        self.lin103 = QtWidgets.QLineEdit(self.tab)
        self.lin103.setGeometry(QtCore.QRect(790, 290, 70, 20))

        self.lin104 = QtWidgets.QLineEdit(self.tab)
        self.lin104.setGeometry(QtCore.QRect(860, 290, 70, 20))

        self.lin111 = QtWidgets.QLineEdit(self.tab)
        self.lin111.setGeometry(QtCore.QRect(650, 320, 70, 20))

        self.lin112 = QtWidgets.QLineEdit(self.tab)
        self.lin112.setGeometry(QtCore.QRect(720, 320, 70, 20))

        self.lin113 = QtWidgets.QLineEdit(self.tab)
        self.lin113.setGeometry(QtCore.QRect(790, 320, 70, 20))

        self.lin114 = QtWidgets.QLineEdit(self.tab)
        self.lin114.setGeometry(QtCore.QRect(860, 320, 70, 20))

        self.lin121 = QtWidgets.QLineEdit(self.tab)
        self.lin121.setGeometry(QtCore.QRect(650, 350, 70, 20))

        self.lin122 = QtWidgets.QLineEdit(self.tab)
        self.lin122.setGeometry(QtCore.QRect(720, 350, 70, 20))

        self.lin123 = QtWidgets.QLineEdit(self.tab)
        self.lin123.setGeometry(QtCore.QRect(790, 350, 70, 20))

        self.lin124 = QtWidgets.QLineEdit(self.tab)
        self.lin124.setGeometry(QtCore.QRect(860, 350, 70, 20))

        self.lin131 = QtWidgets.QLineEdit(self.tab)
        self.lin131.setGeometry(QtCore.QRect(650, 380, 70, 20))

        self.lin132 = QtWidgets.QLineEdit(self.tab)
        self.lin132.setGeometry(QtCore.QRect(720, 380, 70, 20))

        self.lin133 = QtWidgets.QLineEdit(self.tab)
        self.lin133.setGeometry(QtCore.QRect(790, 380, 70, 20))

        self.lin134 = QtWidgets.QLineEdit(self.tab)
        self.lin134.setGeometry(QtCore.QRect(860, 380, 70, 20))

        self.lin141 = QtWidgets.QLineEdit(self.tab)
        self.lin141.setGeometry(QtCore.QRect(650, 410, 70, 20))

        self.lin142 = QtWidgets.QLineEdit(self.tab)
        self.lin142.setGeometry(QtCore.QRect(720, 410, 70, 20))

        self.lin143 = QtWidgets.QLineEdit(self.tab)
        self.lin143.setGeometry(QtCore.QRect(790, 410, 70, 20))

        self.lin144 = QtWidgets.QLineEdit(self.tab)
        self.lin144.setGeometry(QtCore.QRect(860, 410, 70, 20))

        self.lin151 = QtWidgets.QLineEdit(self.tab)
        self.lin151.setGeometry(QtCore.QRect(650, 440, 70, 20))

        self.lin152 = QtWidgets.QLineEdit(self.tab)
        self.lin152.setGeometry(QtCore.QRect(720, 440, 70, 20))

        self.lin153 = QtWidgets.QLineEdit(self.tab)
        self.lin153.setGeometry(QtCore.QRect(790, 440, 70, 20))

        self.lin154 = QtWidgets.QLineEdit(self.tab)
        self.lin154.setGeometry(QtCore.QRect(860, 440, 70, 20))

        self.lin161 = QtWidgets.QLineEdit(self.tab)
        self.lin161.setGeometry(QtCore.QRect(650, 470, 70, 20))

        self.lin162 = QtWidgets.QLineEdit(self.tab)
        self.lin162.setGeometry(QtCore.QRect(720, 470, 70, 20))

        self.lin163 = QtWidgets.QLineEdit(self.tab)
        self.lin163.setGeometry(QtCore.QRect(790, 470, 70, 20))

        self.lin164 = QtWidgets.QLineEdit(self.tab)
        self.lin164.setGeometry(QtCore.QRect(860, 470, 70, 20))

        self.lin171 = QtWidgets.QLineEdit(self.tab)
        self.lin171.setGeometry(QtCore.QRect(650, 500, 70, 20))

        self.lin172 = QtWidgets.QLineEdit(self.tab)
        self.lin172.setGeometry(QtCore.QRect(720, 500, 70, 20))

        self.lin173 = QtWidgets.QLineEdit(self.tab)
        self.lin173.setGeometry(QtCore.QRect(790, 500, 70, 20))

        self.lin174 = QtWidgets.QLineEdit(self.tab)
        self.lin174.setGeometry(QtCore.QRect(860, 500, 70, 20))

        self.lin181 = QtWidgets.QLineEdit(self.tab)
        self.lin181.setGeometry(QtCore.QRect(650, 530, 70, 20))

        self.lin182 = QtWidgets.QLineEdit(self.tab)
        self.lin182.setGeometry(QtCore.QRect(720, 530, 70, 20))

        self.lin183 = QtWidgets.QLineEdit(self.tab)
        self.lin183.setGeometry(QtCore.QRect(790, 530, 70, 20))

        self.lin184 = QtWidgets.QLineEdit(self.tab)
        self.lin184.setGeometry(QtCore.QRect(860, 530, 70, 20))

        self.lin191 = QtWidgets.QLineEdit(self.tab)
        self.lin191.setGeometry(QtCore.QRect(650, 560, 70, 20))

        self.lin192 = QtWidgets.QLineEdit(self.tab)
        self.lin192.setGeometry(QtCore.QRect(720, 560, 70, 20))

        self.lin193 = QtWidgets.QLineEdit(self.tab)
        self.lin193.setGeometry(QtCore.QRect(790, 560, 70, 20))

        self.lin194 = QtWidgets.QLineEdit(self.tab)
        self.lin194.setGeometry(QtCore.QRect(860, 560, 70, 20))

        self.never = QtWidgets.QLabel('Никогда', self.tab_2).setGeometry(QtCore.QRect(650, 0, 70, 16))
        self.never = QtWidgets.QLabel('Иногда', self.tab_2).setGeometry(QtCore.QRect(730, 0, 70, 16))
        self.never = QtWidgets.QLabel('Часто', self.tab_2).setGeometry(QtCore.QRect(800, 0, 70, 16))
        self.never = QtWidgets.QLabel('Очень часто', self.tab_2).setGeometry(QtCore.QRect(855, 0, 120, 16))

        self.lin201 = QtWidgets.QLineEdit(self.tab_2)
        self.lin201.setGeometry(QtCore.QRect(650, 20, 70, 20))

        self.lin202 = QtWidgets.QLineEdit(self.tab_2)
        self.lin202.setGeometry(QtCore.QRect(720, 20, 70, 20))

        self.lin203 = QtWidgets.QLineEdit(self.tab_2)
        self.lin203.setGeometry(QtCore.QRect(790, 20, 70, 20))

        self.lin204 = QtWidgets.QLineEdit(self.tab_2)
        self.lin204.setGeometry(QtCore.QRect(860, 20, 70, 20))

        self.lin211 = QtWidgets.QLineEdit(self.tab_2)
        self.lin211.setGeometry(QtCore.QRect(650, 50, 70, 20))

        self.lin212 = QtWidgets.QLineEdit(self.tab_2)
        self.lin212.setGeometry(QtCore.QRect(720, 50, 70, 20))

        self.lin213 = QtWidgets.QLineEdit(self.tab_2)
        self.lin213.setGeometry(QtCore.QRect(790, 50, 70, 20))

        self.lin214 = QtWidgets.QLineEdit(self.tab_2)
        self.lin214.setGeometry(QtCore.QRect(860, 50, 70, 20))

        self.lin221 = QtWidgets.QLineEdit(self.tab_2)
        self.lin221.setGeometry(QtCore.QRect(650, 80, 70, 20))

        self.lin222 = QtWidgets.QLineEdit(self.tab_2)
        self.lin222.setGeometry(QtCore.QRect(720, 80, 70, 20))

        self.lin223 = QtWidgets.QLineEdit(self.tab_2)
        self.lin223.setGeometry(QtCore.QRect(790, 80, 70, 20))

        self.lin224 = QtWidgets.QLineEdit(self.tab_2)
        self.lin224.setGeometry(QtCore.QRect(860, 80, 70, 20))

        self.lin231 = QtWidgets.QLineEdit(self.tab_2)
        self.lin231.setGeometry(QtCore.QRect(650, 110, 70, 20))

        self.lin232 = QtWidgets.QLineEdit(self.tab_2)
        self.lin232.setGeometry(QtCore.QRect(720, 110, 70, 20))

        self.lin233 = QtWidgets.QLineEdit(self.tab_2)
        self.lin233.setGeometry(QtCore.QRect(790, 110, 70, 20))

        self.lin234 = QtWidgets.QLineEdit(self.tab_2)
        self.lin234.setGeometry(QtCore.QRect(860, 110, 70, 20))

        self.lin241 = QtWidgets.QLineEdit(self.tab_2)
        self.lin241.setGeometry(QtCore.QRect(650, 140, 70, 20))

        self.lin242 = QtWidgets.QLineEdit(self.tab_2)
        self.lin242.setGeometry(QtCore.QRect(720, 140, 70, 20))

        self.lin243 = QtWidgets.QLineEdit(self.tab_2)
        self.lin243.setGeometry(QtCore.QRect(790, 140, 70, 20))

        self.lin244 = QtWidgets.QLineEdit(self.tab_2)
        self.lin244.setGeometry(QtCore.QRect(860, 140, 70, 20))

        self.lin251 = QtWidgets.QLineEdit(self.tab_2)
        self.lin251.setGeometry(QtCore.QRect(650, 170, 70, 20))

        self.lin252 = QtWidgets.QLineEdit(self.tab_2)
        self.lin252.setGeometry(QtCore.QRect(720, 170, 70, 20))

        self.lin253 = QtWidgets.QLineEdit(self.tab_2)
        self.lin253.setGeometry(QtCore.QRect(790, 170, 70, 20))

        self.lin254 = QtWidgets.QLineEdit(self.tab_2)
        self.lin254.setGeometry(QtCore.QRect(860, 170, 70, 20))

        self.lin261 = QtWidgets.QLineEdit(self.tab_2)
        self.lin261.setGeometry(QtCore.QRect(650, 200, 70, 20))

        self.lin262 = QtWidgets.QLineEdit(self.tab_2)
        self.lin262.setGeometry(QtCore.QRect(720, 200, 70, 20))

        self.lin263 = QtWidgets.QLineEdit(self.tab_2)
        self.lin263.setGeometry(QtCore.QRect(790, 200, 70, 20))

        self.lin264 = QtWidgets.QLineEdit(self.tab_2)
        self.lin264.setGeometry(QtCore.QRect(860, 200, 70, 20))

        self.lin271 = QtWidgets.QLineEdit(self.tab_2)
        self.lin271.setGeometry(QtCore.QRect(650, 230, 70, 20))

        self.lin272 = QtWidgets.QLineEdit(self.tab_2)
        self.lin272.setGeometry(QtCore.QRect(720, 230, 70, 20))

        self.lin273 = QtWidgets.QLineEdit(self.tab_2)
        self.lin273.setGeometry(QtCore.QRect(790, 230, 70, 20))

        self.lin274 = QtWidgets.QLineEdit(self.tab_2)
        self.lin274.setGeometry(QtCore.QRect(860, 230, 70, 20))

        self.lin281 = QtWidgets.QLineEdit(self.tab_2)
        self.lin281.setGeometry(QtCore.QRect(650, 260, 70, 20))

        self.lin282 = QtWidgets.QLineEdit(self.tab_2)
        self.lin282.setGeometry(QtCore.QRect(720, 260, 70, 20))

        self.lin283 = QtWidgets.QLineEdit(self.tab_2)
        self.lin283.setGeometry(QtCore.QRect(790, 260, 70, 20))

        self.lin284 = QtWidgets.QLineEdit(self.tab_2)
        self.lin284.setGeometry(QtCore.QRect(860, 260, 70, 20))

        self.lin291 = QtWidgets.QLineEdit(self.tab_2)
        self.lin291.setGeometry(QtCore.QRect(650, 290, 70, 20))

        self.lin292 = QtWidgets.QLineEdit(self.tab_2)
        self.lin292.setGeometry(QtCore.QRect(720, 290, 70, 20))

        self.lin293 = QtWidgets.QLineEdit(self.tab_2)
        self.lin293.setGeometry(QtCore.QRect(790, 290, 70, 20))

        self.lin294 = QtWidgets.QLineEdit(self.tab_2)
        self.lin294.setGeometry(QtCore.QRect(860, 290, 70, 20))

        self.lin301 = QtWidgets.QLineEdit(self.tab_2)
        self.lin301.setGeometry(QtCore.QRect(650, 320, 70, 20))

        self.lin302 = QtWidgets.QLineEdit(self.tab_2)
        self.lin302.setGeometry(QtCore.QRect(720, 320, 70, 20))

        self.lin303 = QtWidgets.QLineEdit(self.tab_2)
        self.lin303.setGeometry(QtCore.QRect(790, 320, 70, 20))

        self.lin304 = QtWidgets.QLineEdit(self.tab_2)
        self.lin304.setGeometry(QtCore.QRect(860, 320, 70, 20))

        self.lin311 = QtWidgets.QLineEdit(self.tab_2)
        self.lin311.setGeometry(QtCore.QRect(650, 350, 70, 20))

        self.lin312 = QtWidgets.QLineEdit(self.tab_2)
        self.lin312.setGeometry(QtCore.QRect(720, 350, 70, 20))

        self.lin313 = QtWidgets.QLineEdit(self.tab_2)
        self.lin313.setGeometry(QtCore.QRect(790, 350, 70, 20))

        self.lin314 = QtWidgets.QLineEdit(self.tab_2)
        self.lin314.setGeometry(QtCore.QRect(860, 350, 70, 20))

        self.lin321 = QtWidgets.QLineEdit(self.tab_2)
        self.lin321.setGeometry(QtCore.QRect(650, 380, 70, 20))

        self.lin322 = QtWidgets.QLineEdit(self.tab_2)
        self.lin322.setGeometry(QtCore.QRect(720, 380, 70, 20))

        self.lin323 = QtWidgets.QLineEdit(self.tab_2)
        self.lin323.setGeometry(QtCore.QRect(790, 380, 70, 20))

        self.lin324 = QtWidgets.QLineEdit(self.tab_2)
        self.lin324.setGeometry(QtCore.QRect(860, 380, 70, 20))

        self.lin331 = QtWidgets.QLineEdit(self.tab_2)
        self.lin331.setGeometry(QtCore.QRect(650, 410, 70, 20))

        self.lin332 = QtWidgets.QLineEdit(self.tab_2)
        self.lin332.setGeometry(QtCore.QRect(720, 410, 70, 20))

        self.lin333 = QtWidgets.QLineEdit(self.tab_2)
        self.lin333.setGeometry(QtCore.QRect(790, 410, 70, 20))

        self.lin334 = QtWidgets.QLineEdit(self.tab_2)
        self.lin334.setGeometry(QtCore.QRect(860, 410, 70, 20))

        self.lin341 = QtWidgets.QLineEdit(self.tab_2)
        self.lin341.setGeometry(QtCore.QRect(650, 470, 70, 20))

        self.lin342 = QtWidgets.QLineEdit(self.tab_2)
        self.lin342.setGeometry(QtCore.QRect(720, 470, 70, 20))

        self.lin343 = QtWidgets.QLineEdit(self.tab_2)
        self.lin343.setGeometry(QtCore.QRect(790, 470, 70, 20))

        self.lin344 = QtWidgets.QLineEdit(self.tab_2)
        self.lin344.setGeometry(QtCore.QRect(860, 470, 70, 20))

        self.lin351 = QtWidgets.QLineEdit(self.tab_2)
        self.lin351.setGeometry(QtCore.QRect(650, 500, 70, 20))

        self.lin352 = QtWidgets.QLineEdit(self.tab_2)
        self.lin352.setGeometry(QtCore.QRect(720, 500, 70, 20))

        self.lin353 = QtWidgets.QLineEdit(self.tab_2)
        self.lin353.setGeometry(QtCore.QRect(790, 500, 70, 20))

        self.lin354 = QtWidgets.QLineEdit(self.tab_2)
        self.lin354.setGeometry(QtCore.QRect(860, 500, 70, 20))

        self.lin361 = QtWidgets.QLineEdit(self.tab_2)
        self.lin361.setGeometry(QtCore.QRect(650, 530, 70, 20))

        self.lin362 = QtWidgets.QLineEdit(self.tab_2)
        self.lin362.setGeometry(QtCore.QRect(720, 530, 70, 20))

        self.lin363 = QtWidgets.QLineEdit(self.tab_2)
        self.lin363.setGeometry(QtCore.QRect(790, 530, 70, 20))

        self.lin364 = QtWidgets.QLineEdit(self.tab_2)
        self.lin364.setGeometry(QtCore.QRect(860, 530, 70, 20))

        self.lin371 = QtWidgets.QLineEdit(self.tab_2)
        self.lin371.setGeometry(QtCore.QRect(650, 560, 70, 20))

        self.lin372 = QtWidgets.QLineEdit(self.tab_2)
        self.lin372.setGeometry(QtCore.QRect(720, 560, 70, 20))

        self.lin373 = QtWidgets.QLineEdit(self.tab_2)
        self.lin373.setGeometry(QtCore.QRect(790, 560, 70, 20))

        self.lin374 = QtWidgets.QLineEdit(self.tab_2)
        self.lin374.setGeometry(QtCore.QRect(860, 560, 70, 20))

        self.never = QtWidgets.QLabel('Никогда', self.tab_3).setGeometry(QtCore.QRect(650, 0, 70, 16))
        self.never = QtWidgets.QLabel('Иногда', self.tab_3).setGeometry(QtCore.QRect(730, 0, 70, 16))
        self.never = QtWidgets.QLabel('Часто', self.tab_3).setGeometry(QtCore.QRect(800, 0, 70, 16))
        self.never = QtWidgets.QLabel('Очень часто', self.tab_3).setGeometry(QtCore.QRect(855, 0, 120, 16))

        self.lin381 = QtWidgets.QLineEdit(self.tab_3)
        self.lin381.setGeometry(QtCore.QRect(650, 20, 70, 20))

        self.lin382 = QtWidgets.QLineEdit(self.tab_3)
        self.lin382.setGeometry(QtCore.QRect(720, 20, 70, 20))

        self.lin383 = QtWidgets.QLineEdit(self.tab_3)
        self.lin383.setGeometry(QtCore.QRect(790, 20, 70, 20))

        self.lin384 = QtWidgets.QLineEdit(self.tab_3)
        self.lin384.setGeometry(QtCore.QRect(860, 20, 70, 20))

        self.lin391 = QtWidgets.QLineEdit(self.tab_3)
        self.lin391.setGeometry(QtCore.QRect(650, 50, 70, 20))

        self.lin392 = QtWidgets.QLineEdit(self.tab_3)
        self.lin392.setGeometry(QtCore.QRect(720, 50, 70, 20))

        self.lin393 = QtWidgets.QLineEdit(self.tab_3)
        self.lin393.setGeometry(QtCore.QRect(790, 50, 70, 20))

        self.lin394 = QtWidgets.QLineEdit(self.tab_3)
        self.lin394.setGeometry(QtCore.QRect(860, 50, 70, 20))

        self.lin401 = QtWidgets.QLineEdit(self.tab_3)
        self.lin401.setGeometry(QtCore.QRect(650, 80, 70, 20))

        self.lin402 = QtWidgets.QLineEdit(self.tab_3)
        self.lin402.setGeometry(QtCore.QRect(720, 80, 70, 20))

        self.lin403 = QtWidgets.QLineEdit(self.tab_3)
        self.lin403.setGeometry(QtCore.QRect(790, 80, 70, 20))

        self.lin404 = QtWidgets.QLineEdit(self.tab_3)
        self.lin404.setGeometry(QtCore.QRect(860, 80, 70, 20))

        self.never = QtWidgets.QLabel('Отлично', self.tab_3)
        self.never.setGeometry(QtCore.QRect(450, 130, 70, 40))

        self.never = QtWidgets.QLabel('Хорошо', self.tab_3)
        self.never.setGeometry(QtCore.QRect(530, 130, 70, 40))

        self.never = QtWidgets.QLabel('Удовлетворительно', self.tab_3)
        self.never.setGeometry(QtCore.QRect(620, 130, 180, 40))

        self.never = QtWidgets.QLabel('Иногда\nтрудности', self.tab_3)
        self.never.setGeometry(QtCore.QRect(770, 130, 120, 40))

        self.never = QtWidgets.QLabel('Большие\nтрудности', self.tab_3)
        self.never.setGeometry(QtCore.QRect(860, 130, 120, 40))

        self.lin411 = QtWidgets.QLineEdit(self.tab_3)
        self.lin411.setGeometry(QtCore.QRect(450, 170, 70, 20))

        self.lin412 = QtWidgets.QLineEdit(self.tab_3)
        self.lin412.setGeometry(QtCore.QRect(530, 170, 70, 20))

        self.lin413 = QtWidgets.QLineEdit(self.tab_3)
        self.lin413.setGeometry(QtCore.QRect(650, 170, 70, 20))

        self.lin414 = QtWidgets.QLineEdit(self.tab_3)
        self.lin414.setGeometry(QtCore.QRect(775, 170, 70, 20))

        self.lin415 = QtWidgets.QLineEdit(self.tab_3)
        self.lin415.setGeometry(QtCore.QRect(865, 170, 70, 20))

        self.lin421 = QtWidgets.QLineEdit(self.tab_3)
        self.lin421.setGeometry(QtCore.QRect(450, 200, 70, 20))

        self.lin422 = QtWidgets.QLineEdit(self.tab_3)
        self.lin422.setGeometry(QtCore.QRect(530, 200, 70, 20))

        self.lin423 = QtWidgets.QLineEdit(self.tab_3)
        self.lin423.setGeometry(QtCore.QRect(650, 200, 70, 20))

        self.lin424 = QtWidgets.QLineEdit(self.tab_3)
        self.lin424.setGeometry(QtCore.QRect(775, 200, 70, 20))

        self.lin425 = QtWidgets.QLineEdit(self.tab_3)
        self.lin425.setGeometry(QtCore.QRect(865, 200, 70, 20))

        self.lin431 = QtWidgets.QLineEdit(self.tab_3)
        self.lin431.setGeometry(QtCore.QRect(450, 230, 70, 20))

        self.lin432 = QtWidgets.QLineEdit(self.tab_3)
        self.lin432.setGeometry(QtCore.QRect(530, 230, 70, 20))

        self.lin433 = QtWidgets.QLineEdit(self.tab_3)
        self.lin433.setGeometry(QtCore.QRect(650, 230, 70, 20))

        self.lin434 = QtWidgets.QLineEdit(self.tab_3)
        self.lin434.setGeometry(QtCore.QRect(775, 230, 70, 20))

        self.lin435 = QtWidgets.QLineEdit(self.tab_3)
        self.lin435.setGeometry(QtCore.QRect(865, 230, 70, 20))

        self.lin441 = QtWidgets.QLineEdit(self.tab_3)
        self.lin441.setGeometry(QtCore.QRect(450, 260, 70, 20))

        self.lin442 = QtWidgets.QLineEdit(self.tab_3)
        self.lin442.setGeometry(QtCore.QRect(530, 260, 70, 20))

        self.lin443 = QtWidgets.QLineEdit(self.tab_3)
        self.lin443.setGeometry(QtCore.QRect(650, 260, 70, 20))

        self.lin444 = QtWidgets.QLineEdit(self.tab_3)
        self.lin444.setGeometry(QtCore.QRect(775, 260, 70, 20))

        self.lin445 = QtWidgets.QLineEdit(self.tab_3)
        self.lin445.setGeometry(QtCore.QRect(865, 260, 70, 20))

        self.lin451 = QtWidgets.QLineEdit(self.tab_3)
        self.lin451.setGeometry(QtCore.QRect(450, 290, 70, 20))

        self.lin452 = QtWidgets.QLineEdit(self.tab_3)
        self.lin452.setGeometry(QtCore.QRect(530, 290, 70, 20))

        self.lin453 = QtWidgets.QLineEdit(self.tab_3)
        self.lin453.setGeometry(QtCore.QRect(650, 290, 70, 20))

        self.lin454 = QtWidgets.QLineEdit(self.tab_3)
        self.lin454.setGeometry(QtCore.QRect(775, 290, 70, 20))

        self.lin455 = QtWidgets.QLineEdit(self.tab_3)
        self.lin455.setGeometry(QtCore.QRect(865, 290, 70, 20))

        self.lin461 = QtWidgets.QLineEdit(self.tab_3)
        self.lin461.setGeometry(QtCore.QRect(450, 320, 70, 20))

        self.lin462 = QtWidgets.QLineEdit(self.tab_3)
        self.lin462.setGeometry(QtCore.QRect(530, 320, 70, 20))

        self.lin463 = QtWidgets.QLineEdit(self.tab_3)
        self.lin463.setGeometry(QtCore.QRect(650, 320, 70, 20))

        self.lin464 = QtWidgets.QLineEdit(self.tab_3)
        self.lin464.setGeometry(QtCore.QRect(775, 320, 70, 20))

        self.lin465 = QtWidgets.QLineEdit(self.tab_3)
        self.lin465.setGeometry(QtCore.QRect(865, 320, 70, 20))

        self.lin471 = QtWidgets.QLineEdit(self.tab_3)
        self.lin471.setGeometry(QtCore.QRect(450, 350, 70, 20))

        self.lin472 = QtWidgets.QLineEdit(self.tab_3)
        self.lin472.setGeometry(QtCore.QRect(530, 350, 70, 20))

        self.lin473 = QtWidgets.QLineEdit(self.tab_3)
        self.lin473.setGeometry(QtCore.QRect(650, 350, 70, 20))

        self.lin474 = QtWidgets.QLineEdit(self.tab_3)
        self.lin474.setGeometry(QtCore.QRect(775, 350, 70, 20))

        self.lin475 = QtWidgets.QLineEdit(self.tab_3)
        self.lin475.setGeometry(QtCore.QRect(865, 350, 70, 20))

        self.lin481 = QtWidgets.QLineEdit(self.tab_3)
        self.lin481.setGeometry(QtCore.QRect(450, 380, 70, 20))

        self.lin482 = QtWidgets.QLineEdit(self.tab_3)
        self.lin482.setGeometry(QtCore.QRect(530, 380, 70, 20))

        self.lin483 = QtWidgets.QLineEdit(self.tab_3)
        self.lin483.setGeometry(QtCore.QRect(650, 380, 70, 20))

        self.lin484 = QtWidgets.QLineEdit(self.tab_3)
        self.lin484.setGeometry(QtCore.QRect(775, 380, 70, 20))

        self.lin485 = QtWidgets.QLineEdit(self.tab_3)
        self.lin485.setGeometry(QtCore.QRect(865, 380, 70, 20))


        self.t3 = 0
        self.t4 = 0
        self.t5 = '0'
        self.t7 = ''
        self.t8 = ''
        self.t9 = ''
        self.t10 = ''

        self.pushButton2 = QtWidgets.QPushButton('Сохранить', self)
        self.pushButton2.setGeometry(QtCore.QRect(671, 10, 161, 31))

        self.pushButton3 = QtWidgets.QPushButton('Печать', self)
        self.pushButton3.setGeometry(QtCore.QRect(842, 10, 161, 31))


# ----------------класс повторной анкеты для родителя и учителя-------------------
class Ui_AnketaAgain(QtWidgets.QDialog):

    def saveA2(self):
        if(person == 1):
            nametable = 'ChildrenAgain'
        elif(person == 2):
            nametable = 'ChildrenAgain2'

        problems = self.textDescr.toPlainText()

        connection = sqlite3.connect('Anketa1.db')
        query = 'CREATE TABLE IF NOT EXISTS ' + nametable + ' (Number TEXT,Fullname TEXT,Date TEXT,Age INTEGER,class INTEGER,school INTEGER,' + \
                'Diagnos TEXT,Sex INTEGER,Level INTEGER,answer1 INTEGER,answer2 INTEGER,answer3 INTEGER,answer4 INTEGER,answer5 INTEGER,' + \
                'answer6 INTEGER,answer7 INTEGER,answer8 INTEGER,answer9 INTEGER,answer10 INTEGER,answer11 INTEGER,answer12 INTEGER,' + \
                'answer13 INTEGER,answer14 INTEGER,answer15 INTEGER,answer16 INTEGER,answer17 INTEGER,answer18 INTEGER,answer19 INTEGER, ' + \
                'answer20 INTEGER, answer21 INTEGER, answer22 INTEGER, answer23 INTEGER, answer24 INTEGER,answer25 INTEGER,answer26 INTEGER, problems TEXT)'

        connection.execute(query)
        query = 'INSERT INTO ' + nametable + ' (Number,FullName,Date,Age,class,school,Diagnos,Sex,Level,answer1,answer2,answer3,answer4,' + \
                'answer5,answer6,answer7,answer8,answer9,answer10,answer11,answer12,answer13,answer14,answer15,answer16,answer17,' + \
                'answer18,answer19,answer20,answer21,answer22,answer23,answer24,answer25,answer26, problems) ' + \
                'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

        connection.execute(query, (
            self.t1, self.t2, self.t9, self.t4, self.t7, self.t6, self.t3, self.t5, self.t8,
            self.ans_1.currentIndex(), self.ans_2.currentIndex(), self.ans_3.currentIndex(), self.ans_4.currentIndex(),self.ans_5.currentIndex(),
            self.ans_6.currentIndex(), self.ans_7.currentIndex(), self.ans_8.currentIndex(), self.ans_9.currentIndex(),self.ans_10.currentIndex(),
            self.ans_11.currentIndex(), self.ans_12.currentIndex(), self.ans_13.currentIndex(),self.ans_14.currentIndex(), self.ans_15.currentIndex(),
            self.ans_16.currentIndex(), self.ans_17.currentIndex(), self.ans_18.currentIndex(),self.ans_41.currentIndex() + 1, self.ans_42.currentIndex() + 1, self.ans_43.currentIndex() + 1,
            self.ans_44.currentIndex() + 1, self.ans_45.currentIndex() + 1,self.ans_46.currentIndex() + 1, self.ans_47.currentIndex() + 1, self.ans_48.currentIndex() + 1, problems))
        connection.commit()
        connection.close()
        self.close()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = Ui_Form_person(self)

        global person
        self.setGeometry(200, 50, 1080, 700)
        self.setFixedSize(1080, 700)
        self.setStyleSheet("")
        if (person == 1):
            self.setWindowTitle('ПОВТОРНОЕ анкетирование (Родители ребенка)')
        elif (person == 2):
            self.setWindowTitle('ПОВТОРНОЕ анкетирование (Учитель)')
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(40, 80, 941, 611))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setEnabled(False)

        self.tab = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab, "1 страница анкеты")
        self.tab_2 = QtWidgets.QWidget(self)
        self.tabWidget.addTab(self.tab_2, "2 страница анкеты")


        self.help1 = QtWidgets.QLabel('Опишите побочные симптомы(головные боли, тошнота, потеря аппетита и др.) если таковы присутствуют.',self.tab_2)
        self.help1.setGeometry(QtCore.QRect(0, 320, 900, 16))
        self.help2 = QtWidgets.QLabel('Симптомы', self.tab)
        self.help2.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help3 = QtWidgets.QLabel('Успешность', self.tab_2)
        self.help3.setGeometry(QtCore.QRect(390, 0, 101, 16))
        self.help4 = QtWidgets.QLabel(
            "Инструкция: Пожалуйста, оцените поведение ребенка с помощью приведенного\nопросника. "
            "При оценке ориентируйтесь на наиболее типичное поведение ребенка\nв течение последних "
            "шести месяцев в сравнении с поведением сверстников.", self).setGeometry(QtCore.QRect(450, 10, 620, 51))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.help1.setFont(font)
        self.help2.setFont(font)
        self.help3.setFont(font)

        self.textDescr = QtWidgets.QTextEdit(self.tab_2)
        self.textDescr.setGeometry(QtCore.QRect(10, 350, 700, 200))

        self.label1 = QtWidgets.QLabel('1) Неспособен внимательно следить за деталями, делает нелепые ошибки', self.tab).setGeometry(QtCore.QRect(100, 20, 700, 16))
        self.label2 = QtWidgets.QLabel('2) Имеет трудности в выполнении заданий или игровой деятельности, которые требуют соредоточенности',self.tab).setGeometry(QtCore.QRect(100, 50, 850, 16))
        self.label3 = QtWidgets.QLabel('3) Не слушает, когда к нему обращаются', self.tab).setGeometry(QtCore.QRect(100, 80, 350, 16))
        self.label4 = QtWidgets.QLabel('4) Не заканчивает начатого занятия (непреднамеренно)', self.tab).setGeometry(QtCore.QRect(100, 110, 700, 16))
        self.label5 = QtWidgets.QLabel('5) Несобран, неорганизован', self.tab).setGeometry(QtCore.QRect(100, 140, 300, 16))
        self.label6 = QtWidgets.QLabel('6) Избегает, не любит или не хочет соглашаться выполнять задания, которые требуют повышенного внимания', self.tab).setGeometry(QtCore.QRect(100, 170, 850, 16))
        self.label7 = QtWidgets.QLabel('7) Путает расписание, теряет вещи, необходимые для выполнения заданий',self.tab).setGeometry(QtCore.QRect(100, 200, 800, 16))
        self.label8 = QtWidgets.QLabel('8) Легко отвлекается на все, что происходит вокруг', self.tab).setGeometry(QtCore.QRect(100, 230, 500, 16))
        self.label9 = QtWidgets.QLabel('9) Забывает выполнять каждодневные процедуры (почистить зубы и т.п.)', self.tab).setGeometry(QtCore.QRect(100, 260, 550, 16))
        self.label10 = QtWidgets.QLabel('10) Беспокойно двигает руками или ногами, ерзает на месте', self.tab).setGeometry(QtCore.QRect(100, 290, 500, 16))
        self.label11 = QtWidgets.QLabel('11) Покидает свое место в классе или в другом месте, не может усидеть', self.tab).setGeometry(QtCore.QRect(100, 320, 550, 16))
        self.label12 = QtWidgets.QLabel('12) Начинает бегать и карабкаться куда-то, когда это неуместно', self.tab).setGeometry(QtCore.QRect(100, 350, 550, 16))
        self.label13 = QtWidgets.QLabel('13) Не может тихо играть, неадекватно шумен', self.tab).setGeometry(QtCore.QRect(100, 380, 500, 16))
        self.label14 = QtWidgets.QLabel('14) Действует как «заведенный», как будто к нему приделан «моторчик»', self.tab).setGeometry(QtCore.QRect(100, 410, 550, 16))
        self.label15 = QtWidgets.QLabel('15) Чрезмерно разговорчивый, без учета социальных ограничений', self.tab).setGeometry(QtCore.QRect(100, 440, 520, 16))
        self.label16 = QtWidgets.QLabel('16) Выпаливает ответы до того, как завершены вопросы', self.tab).setGeometry(QtCore.QRect(100, 470, 500, 16))
        self.label17 = QtWidgets.QLabel('17) Не способен стоять в очередях, дожидаться своей очереди', self.tab).setGeometry(QtCore.QRect(100, 500, 520, 16))
        self.label18 = QtWidgets.QLabel('18) Перебивает других или вмешивается в разговоры или занятия других', self.tab).setGeometry(QtCore.QRect(100, 530, 550, 16))

        if (person == 1):
            self.label19 = QtWidgets.QLabel('19) Следование школьным правилам', self.tab_2).setGeometry(QtCore.QRect(100, 20, 400, 16))
            self.label20 = QtWidgets.QLabel('20) Чтение', self.tab_2).setGeometry(QtCore.QRect(100, 50, 100, 13))
            self.label21 = QtWidgets.QLabel('21) Письмо', self.tab_2).setGeometry(QtCore.QRect(100, 80, 100, 13))
            self.label22 = QtWidgets.QLabel('22) Математика', self.tab_2).setGeometry(QtCore.QRect(100, 110, 150, 16))
            self.label23 = QtWidgets.QLabel('23) Отношения с родителями', self.tab_2).setGeometry(QtCore.QRect(100, 140, 300, 16))
            self.label24 = QtWidgets.QLabel('24) Отношения с братьями /сестрами', self.tab_2).setGeometry(QtCore.QRect(100, 170, 400, 16))
            self.label25 = QtWidgets.QLabel('25) Отношения со сверстниками',  self.tab_2).setGeometry(QtCore.QRect(100, 200, 300, 16))
            self.label26 = QtWidgets.QLabel('26) Участие в организованных мероприятиях (командная работа)',self.tab_2).setGeometry(QtCore.QRect(100, 230, 800, 16))
        elif(person == 2):
            self.label19 = QtWidgets.QLabel('19) Чтение', self.tab_2).setGeometry(QtCore.QRect(100, 20, 100, 16))
            self.label20 = QtWidgets.QLabel('20) Математика', self.tab_2).setGeometry(QtCore.QRect(100, 50, 150, 13))
            self.label21 = QtWidgets.QLabel('21) Письмо', self.tab_2).setGeometry(QtCore.QRect(100, 80, 100, 13))
            self.label22 = QtWidgets.QLabel('22) Отношения со сверстниками', self.tab_2).setGeometry(QtCore.QRect(100, 110, 300, 16))
            self.label23 = QtWidgets.QLabel('23) Следование инструкциям', self.tab_2).setGeometry(QtCore.QRect(100, 140, 300, 16))
            self.label24 = QtWidgets.QLabel('24) Нарушение порядка на занятиях', self.tab_2).setGeometry(QtCore.QRect(100, 170, 300, 16))
            self.label25 = QtWidgets.QLabel('25) Завершенность действий', self.tab_2).setGeometry(QtCore.QRect(100, 200, 300, 16))
            self.label26 = QtWidgets.QLabel('26) Организационные навыки',self.tab_2).setGeometry(QtCore.QRect(100, 230, 300, 16))


        self.ans_1 = QtWidgets.QComboBox(self.tab)
        self.ans_1.setGeometry(QtCore.QRect(0, 20, 91, 22))
        self.ans_1.addItems(["0","1","2","3"])

        self.ans_2 = QtWidgets.QComboBox(self.tab)
        self.ans_2.setGeometry(QtCore.QRect(0, 50, 91, 22))
        self.ans_2.addItems(["0", "1", "2", "3"])

        self.ans_3 = QtWidgets.QComboBox(self.tab)
        self.ans_3.setGeometry(QtCore.QRect(0, 80, 91, 22))
        self.ans_3.addItems(["0", "1", "2", "3"])

        self.ans_4 = QtWidgets.QComboBox(self.tab)
        self.ans_4.setGeometry(QtCore.QRect(0, 110, 91, 22))
        self.ans_4.addItems(["0", "1", "2", "3"])

        self.ans_5 = QtWidgets.QComboBox(self.tab)
        self.ans_5.setGeometry(QtCore.QRect(0, 140, 91, 22))
        self.ans_5.addItems(["0", "1", "2", "3"])

        self.ans_6 = QtWidgets.QComboBox(self.tab)
        self.ans_6.setGeometry(QtCore.QRect(0, 170, 91, 22))
        self.ans_6.addItems(["0", "1", "2", "3"])

        self.ans_7 = QtWidgets.QComboBox(self.tab)
        self.ans_7.setGeometry(QtCore.QRect(0, 200, 91, 22))
        self.ans_7.addItems(["0", "1", "2", "3"])

        self.ans_8 = QtWidgets.QComboBox(self.tab)
        self.ans_8.setGeometry(QtCore.QRect(0, 230, 91, 22))
        self.ans_8.addItems(["0", "1", "2", "3"])

        self.ans_9 = QtWidgets.QComboBox(self.tab)
        self.ans_9.setGeometry(QtCore.QRect(0, 260, 91, 22))
        self.ans_9.addItems(["0", "1", "2", "3"])

        self.ans_10 = QtWidgets.QComboBox(self.tab)
        self.ans_10.setGeometry(QtCore.QRect(0, 290, 91, 22))
        self.ans_10.addItems(["0", "1", "2", "3"])

        self.ans_11 = QtWidgets.QComboBox(self.tab)
        self.ans_11.setGeometry(QtCore.QRect(0, 320, 91, 22))
        self.ans_11.addItems(["0", "1", "2", "3"])

        self.ans_12 = QtWidgets.QComboBox(self.tab)
        self.ans_12.setGeometry(QtCore.QRect(0, 350, 91, 22))
        self.ans_12.addItems(["0", "1", "2", "3"])

        self.ans_13 = QtWidgets.QComboBox(self.tab)
        self.ans_13.setGeometry(QtCore.QRect(0, 380, 91, 22))
        self.ans_13.addItems(["0", "1", "2", "3"])

        self.ans_14 = QtWidgets.QComboBox(self.tab)
        self.ans_14.setGeometry(QtCore.QRect(0, 410, 91, 22))
        self.ans_14.addItems(["0", "1", "2", "3"])

        self.ans_15 = QtWidgets.QComboBox(self.tab)
        self.ans_15.setGeometry(QtCore.QRect(0, 440, 91, 22))
        self.ans_15.addItems(["0", "1", "2", "3"])

        self.ans_16 = QtWidgets.QComboBox(self.tab)
        self.ans_16.setGeometry(QtCore.QRect(0, 470, 91, 22))
        self.ans_16.addItems(["0", "1", "2", "3"])

        self.ans_17 = QtWidgets.QComboBox(self.tab)
        self.ans_17.setGeometry(QtCore.QRect(0, 500, 91, 22))
        self.ans_17.addItems(["0", "1", "2", "3"])

        self.ans_18 = QtWidgets.QComboBox(self.tab)
        self.ans_18.setGeometry(QtCore.QRect(0, 530, 91, 22))
        self.ans_18.addItems(["0", "1", "2", "3"])

        self.ans_41 = QtWidgets.QComboBox(self.tab_2)
        self.ans_41.setGeometry(QtCore.QRect(0, 20, 91, 22))
        self.ans_41.addItems(["1", "2", "3", "4", "5"])

        self.ans_42 = QtWidgets.QComboBox(self.tab_2)
        self.ans_42.setGeometry(QtCore.QRect(0, 50, 91, 22))
        self.ans_42.addItems(["1", "2", "3", "4", "5"])

        self.ans_43 = QtWidgets.QComboBox(self.tab_2)
        self.ans_43.setGeometry(QtCore.QRect(0, 80, 91, 22))
        self.ans_43.addItems(["1", "2", "3", "4", "5"])

        self.ans_44 = QtWidgets.QComboBox(self.tab_2)
        self.ans_44.setGeometry(QtCore.QRect(0, 110, 91, 22))
        self.ans_44.addItems(["1", "2", "3", "4", "5"])

        self.ans_45 = QtWidgets.QComboBox(self.tab_2)
        self.ans_45.setGeometry(QtCore.QRect(0, 140, 91, 22))
        self.ans_45.addItems(["1", "2", "3", "4", "5"])

        self.ans_46 = QtWidgets.QComboBox(self.tab_2)
        self.ans_46.setGeometry(QtCore.QRect(0, 170, 91, 22))
        self.ans_46.addItems(["1", "2", "3", "4", "5"])

        self.ans_47 = QtWidgets.QComboBox(self.tab_2)
        self.ans_47.setGeometry(QtCore.QRect(0, 200, 91, 22))
        self.ans_47.addItems(["1", "2", "3", "4", "5"])

        self.ans_48 = QtWidgets.QComboBox(self.tab_2)
        self.ans_48.setGeometry(QtCore.QRect(0, 230, 91, 22))
        self.ans_48.addItems(["1", "2", "3", "4", "5"])

        self.pushButton = QtWidgets.QPushButton("Личные данные ", self)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 391, 51))
        self.pushButton.clicked.connect(self.dialog.exec)

        self.save1pushButton = QtWidgets.QPushButton('Сохранить', self)
        self.save1pushButton.setGeometry(QtCore.QRect(900, 70, 161, 31))
        self.save1pushButton.clicked.connect(self.saveA2)

        self.tabWidget.setCurrentIndex(0)

        self.t1 = ''
        self.t2 = ''
        self.t3 = ''
        self.t4 = ''
        self.t5 = ''
        self.t6 = ''
        self.t7 = ''
        self.t8 = ''
        self.t9 = ''


# ----------------класс для личных данных пациента для другой статистики по симптомам-------------------
class Ui_S1(QtWidgets.QDialog):
    def openA1(self):
        self.main.t3 = self.ageBox1.currentText()
        self.main.t4 = self.ageBox2.currentText()
        buf = 0
        if (self.sexBox.currentText() == "все"):
            buf = 0
            self.main.descrip.setText("Общее количество муж. + жен.")
        if (self.sexBox.currentText() == "мужской"):
            buf = 1
            self.main.descrip.setText("Только муж.")
        if (self.sexBox.currentText() == "женский"):
            buf = 2
            self.main.descrip.setText("Только жен.")
        self.main.t5 = str(buf)

        self.main.t7 = str(self.classBox.currentText())
        buf1 = ""
        if (self.levelBox.currentText() == '1 ступень  (1-4класс)'):
            buf1 = 1
        if (self.levelBox.currentText() == '2 ступень  (5-8класс)'):
            buf1 = 2
        if (self.levelBox.currentText() == '3 ступень  (9-11класс)'):
            buf1 = 3
        self.main.t8 = str(buf1)
        self.close()

    def cl(self):
        self.close()

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

        self.setGeometry(400, 300, 331, 372)
        self.setFixedSize(340, 200)
        self.setWindowTitle('Дополнительные параметры')

        self.label_7 = QtWidgets.QLabel('Пол', self).setGeometry(QtCore.QRect(40, 20, 41, 16))
        self.label_10 = QtWidgets.QLabel('Ступень обучения', self).setGeometry(QtCore.QRect(40, 110, 151, 16))
        self.label_6 = QtWidgets.QLabel('Возраст от', self).setGeometry(QtCore.QRect(40, 50, 90, 16))
        self.label_6 = QtWidgets.QLabel('до', self).setGeometry(QtCore.QRect(210, 50, 71, 16))
        self.label_9 = QtWidgets.QLabel('Класс', self).setGeometry(QtCore.QRect(40, 80, 51, 16))


        self.classBox = QtWidgets.QComboBox(self)
        self.classBox.setGeometry(QtCore.QRect(110, 80, 70, 22))
        self.classBox.addItems(["","1","2","3","4","5","6","7","8","9","10","11"])

        self.levelBox = QtWidgets.QComboBox(self)
        self.levelBox.setGeometry(QtCore.QRect(200, 110, 120, 22))
        self.levelBox.addItems(["","1 ступень  (1-4класс)","2 ступень  (5-8класс)","3 ступень  (9-11класс)"])

        self.sexBox = QtWidgets.QComboBox(self)
        self.sexBox.setGeometry(QtCore.QRect(90, 20, 81, 22))
        self.sexBox.addItems(["все","мужской","женский"])

        self.ageBox1 = QtWidgets.QComboBox(self)
        self.ageBox1.setGeometry(QtCore.QRect(140, 50, 61, 22))
        self.ageBox1.addItems(["","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])

        self.ageBox2 = QtWidgets.QComboBox(self)
        self.ageBox2.setGeometry(QtCore.QRect(240, 50, 61, 22))
        self.ageBox2.addItems(["", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"])

        self.savebutton = QtWidgets.QPushButton('Добавить', self)
        self.savebutton.setGeometry(QtCore.QRect(160, 150, 81, 23))
        self.savebutton.clicked.connect(self.openA1)

        self.cleanbutton = QtWidgets.QPushButton('Отмена', self)
        self.cleanbutton.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.cleanbutton.clicked.connect(self.cl)


# ----------------класс обработки симптомов для данных анкеты 1-------------------
class Ui_Simptom1(QtWidgets.QDialog):
    def hh(self, status):
        if(person == 1):
            nametable = 'StatusRelatives'
        elif(person == 2):
            nametable = 'StatusTeacher'
        connection = sqlite3.connect('Anketa1.db')
        query1 = 'Select count(' + status + ') from ' + nametable + ' where ' + status + '=' + chr(
            34) + 'симптом выявлен' + chr(34) + ' '
        self.buffer = "Критерии выборки: "
        if (self.t5 == '0'):
            query1 += ''
            self.buffer += "мужчины и женщины "
        if (self.t5 == '1'):
            query1 += ' and Sex=1'
            self.buffer += "мужчины "
        if (self.t5 == '2'):
            query1 += ' and Sex=2'
            self.buffer += "женщины "
        if (self.t3 == '' or self.t4 == ''): query1 += ''
        r1 = self.t3
        r2 = self.t4
        if (r1 > r2):
            b = self.t3
            self.t3 = self.t4
            self.t4 = b
            query1 += ' and Age between '
            query1 += self.t3
            query1 += ' and '
            query1 += self.t4
            self.buffer += "возраст от "
            self.buffer += str(self.t3)
            self.buffer += " до "
            self.buffer += str(self.t4)
            self.buffer += " "
        if (r1 < r2):
            query1 += ' and Age between '
            query1 += self.t3
            query1 += ' and '
            query1 += self.t4
            self.buffer += "возраст от "
            self.buffer += str(self.t3)
            self.buffer += " до "
            self.buffer += str(self.t4)
            self.buffer += " "
        if (self.t7 == ''): query1 += ''
        if (self.t7 != ''):
            query1 += ' and class='
            query1 += self.t7
            self.buffer += "класс "
            self.buffer += str(self.t7)
            self.buffer += " "
        if (self.t8 == ''): query1 += ''
        if (self.t8 == '1'):
            query1 += ' and Level=1'
            self.buffer += "уровень "
            self.buffer += str(self.t8)
        if (self.t8 == '2'):
            query1 += ' and Level=2'
            self.buffer += "уровень "
            self.buffer += str(self.t8)
        if (self.t8 == '3'):
            query1 += ' and Level=3'
            self.buffer += "уровень "
            self.buffer += str(self.t8)
        self.buffer += "\n"
        result = connection.execute(query1)
        row = result.fetchall()
        return row[0][0]

    def s(self):
        part = [self.hh('Status1'), self.hh('Status2'), self.hh('Status3'), self.hh('Status4'), self.hh('Status5'),
                self.hh('Status6'), self.hh('Status7')]
        summa = part[0] + part[1] + part[2] + part[3] + part[4] + part[5] + part[6]
        if (summa != 0):
            self.su1.setText(str(part[0]) + "   |" + str(round(((part[0] * 100) / summa), 1)) + "%");
            self.su2.setText(str(part[1]) + "   |" + str(round(((part[1] * 100) / summa), 1)) + "%");
            self.su3.setText(str(part[2]) + "   |" + str(round(((part[2] * 100) / summa), 1)) + "%");
            self.su4.setText(str(part[3]) + "   |" + str(round(((part[3] * 100) / summa), 1)) + "%");
            self.su5.setText(str(part[4]) + "   |" + str(round(((part[4] * 100) / summa), 1)) + "%");
            self.su6.setText(str(part[5]) + "   |" + str(round(((part[5] * 100) / summa), 1)) + "%");
            self.su7.setText(str(part[6]) + "   |" + str(round(((part[6] * 100) / summa), 1)) + "%");
        else:
            self.su1.setText("0")
            self.su2.setText("0")
            self.su3.setText("0")
            self.su4.setText("0")
            self.su5.setText("0")
            self.su6.setText("0")
            self.su7.setText("0")

    def cleaner(self):
        self.su1.setText("0")
        self.su2.setText("0")
        self.su3.setText("0")
        self.su4.setText("0")
        self.su5.setText("0")
        self.su6.setText("0")
        self.su7.setText("0")

    def saver(self):
        f = QtWidgets.QFileDialog.getSaveFileName(self)
        filename = f[0]
        if f[0] != '':
            openedfile = open(filename, "w")
            text1 = "Общая статитстика по субшкалам для всех пациентов, из базы данных\nс подозрением на СДВГ.\n\n"
            text1 += self.buffer
            text1 += "                                               кол-во/проценты\n"
            text1 += "1.Cубшкала дефицита внимания:                  \t" + self.su1.text() + "\n"
            text1 += "2.Cубшкала гиперактивности и импульсивности:   \t" + self.su2.text() + "\n"
            text1 += "3.Cубшкала невнимательности и гиперактивности: \t" + self.su3.text() + "\n"
            text1 += "4.Cубшкала реакций оппозиции (протеста):       \t" + self.su4.text() + "\n"
            text1 += "5.Cубшкала др. поведенческих проблем:          \t" + self.su5.text() + "\n"
            text1 += "6.Cубшкала тревожно-депрессивной симптоматики: \t" + self.su6.text() + "\n"
            text1 += "7.Cубшкала социальной адаптации:               \t" + self.su7.text() + "\n"
            openedfile.write(text1)
            openedfile.close()

    def printer(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        text1 = "Общая статитстика по субшкалам для всех пациентов, из базы данных\nс подозрением на СДВГ.\n\n"
        text1 += self.buffer
        text1 += "                                               кол-во/проценты\n"
        text1 += "1.Cубшкала дефицита внимания:                  \t" + self.su1.text() + "\n"
        text1 += "2.Cубшкала гиперактивности и импульсивности:   \t" + self.su2.text() + "\n"
        text1 += "3.Cубшкала невнимательности и гиперактивности: \t" + self.su3.text() + "\n"
        text1 += "4.Cубшкала реакций оппозиции (протеста):       \t" + self.su4.text() + "\n"
        text1 += "5.Cубшкала др. поведенческих проблем:          \t" + self.su5.text() + "\n"
        text1 += "6.Cубшкала тревожно-депрессивной симптоматики: \t" + self.su6.text() + "\n"
        text1 += "7.Cубшкала социальной адаптации:               \t" + self.su7.text() + "\n"
        self.textPrint.setText(text1)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textPrint.print_(printer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = Ui_S1(self)

        if(person == 1):
            self.setWindowTitle("Статистика по симптомам первичного анкетирования (Родители ребенка)")
        elif(person == 2):
            self.setWindowTitle("Статистика по симптомам первичного анкетирования (Учитель)")

        self.setGeometry(500, 300, 600, 400)
        self.setFixedSize(600, 400)
        self.setStyleSheet("")

        self.descrip = QtWidgets.QLabel('Общее количество муж. + жен.', self)
        self.descrip.setGeometry(QtCore.QRect(350, 15, 400, 16))
        self.label_2 = QtWidgets.QLabel('Субшкала невнимательности ', self).setGeometry(QtCore.QRect(20, 90, 261, 21))
        self.label_3 = QtWidgets.QLabel('Субшкала гиперактивности + импульсивности', self).setGeometry(QtCore.QRect(20, 120, 400, 21))
        self.label_4 = QtWidgets.QLabel('Субшкала невнимательности + гиперактивности', self).setGeometry(QtCore.QRect(20, 150, 400, 21))
        self.label_5 = QtWidgets.QLabel('Субшкала реакций оппозиции (протеста) ', self).setGeometry(QtCore.QRect(20, 180, 351, 21))
        self.label_6 = QtWidgets.QLabel('Субшкала др. поведенческих проблем', self).setGeometry(QtCore.QRect(20, 210, 321, 21))
        self.label_7 = QtWidgets.QLabel('Субшкала тревожно-депрессивной симптоматики ', self).setGeometry(QtCore.QRect(20, 240, 421, 21))
        self.label_8 = QtWidgets.QLabel('Субшкала социальной адаптации', self).setGeometry(QtCore.QRect(20, 270, 291, 21))
        self.label_9 = QtWidgets.QLabel('Количество человек / % ', self).setGeometry(QtCore.QRect(390, 60, 200, 21))

        self.su1 = QtWidgets.QLabel('0', self)
        self.su1.setGeometry(QtCore.QRect(490, 90, 90, 20))

        self.su2 = QtWidgets.QLabel('0', self)
        self.su2.setGeometry(QtCore.QRect(490, 120, 90, 20))

        self.su3 = QtWidgets.QLabel('0', self)
        self.su3.setGeometry(QtCore.QRect(490, 150, 90, 20))

        self.su4 = QtWidgets.QLabel('0', self)
        self.su4.setGeometry(QtCore.QRect(490, 180, 90, 20))

        self.su5 = QtWidgets.QLabel('0', self)
        self.su5.setGeometry(QtCore.QRect(490, 210, 90, 20))

        self.su6 = QtWidgets.QLabel('0', self)
        self.su6.setGeometry(QtCore.QRect(490, 240, 90, 20))

        self.su7 = QtWidgets.QLabel('0', self)
        self.su7.setGeometry(QtCore.QRect(490, 270, 90, 20))

        self.findsumma = QtWidgets.QPushButton('Вывести результат', self)
        self.findsumma.setGeometry(QtCore.QRect(160, 10, 150, 30))
        self.findsumma.clicked.connect(self.s)

        self.sbros = QtWidgets.QPushButton('Сброс', self)
        self.sbros.setGeometry(QtCore.QRect(190, 310, 100, 30))
        self.sbros.clicked.connect(self.cleaner)

        self.save = QtWidgets.QPushButton('Cохранить в файл', self)
        self.save.setGeometry(QtCore.QRect(430, 310, 150, 30))
        self.save.clicked.connect(self.saver)

        self.print = QtWidgets.QPushButton('Печать', self)
        self.print.setGeometry(QtCore.QRect(310, 310, 100, 30))
        self.print.clicked.connect(self.printer)

        self.save = QtWidgets.QPushButton('Критерии оценки', self)
        self.save.setGeometry(QtCore.QRect(10, 10, 150, 30))
        self.save.clicked.connect(self.dialog.exec)

        self.df = Ui_uu(self)
        self.diagram = QtWidgets.QPushButton('Диаграмма', self)
        self.diagram.setGeometry(QtCore.QRect(20, 310, 150, 30))
        self.diagram.clicked.connect(self.df.exec)

        self.textPrint = QtWidgets.QTextEdit(self)
        self.textPrint.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.t3 = 0
        self.t4 = 0
        self.buffer = 'Критерии выборки: '
        self.t5 = '0'
        self.t7 = ''
        self.t8 = ''
        self.t9 = ''
        self.t10 = ''


# ----------------класс диаграммы-------------------
class Ui_uu(QtWidgets.QDialog):
    def showDiagram(self):
        f1 = self.main.su1.text()
        f2 = self.main.su2.text()
        f3 = self.main.su3.text()
        f4 = self.main.su4.text()
        f5 = self.main.su5.text()
        f6 = self.main.su6.text()
        f7 = self.main.su7.text()
        self.ff1 = int(f1.split(' ')[0].strip())
        self.ff2 = int(f2.split(' ')[0].strip())
        self.ff3 = int(f3.split(' ')[0].strip())
        self.ff4 = int(f4.split(' ')[0].strip())
        self.ff5 = int(f5.split(' ')[0].strip())
        self.ff6 = int(f6.split(' ')[0].strip())
        self.ff7 = int(f7.split(' ')[0].strip())
        self.name = self.main.descrip.text()
        self.canvas = Canvas(self, width=5, height=7, dpi=90, f1=self.ff1, f2=self.ff2, f3=self.ff3, f4=self.ff4,
                             f5=self.ff5, f6=self.ff6, f7=self.ff7, name=self.name)
        self.canvas.show()

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root
        self.ff1 = 5
        self.ff2 = 5
        self.ff3 = 5
        self.ff4 = 5
        self.ff5 = 5
        self.ff6 = 5
        self.ff7 = 5
        self.name = ''
        self.setGeometry(200, 50, 600, 600)
        self.setFixedSize(600, 600)
        self.setWindowTitle('Диаграмма')
        self.canvas = None
        self.pushButton = QtWidgets.QPushButton('Построить', self)
        self.pushButton.setGeometry(QtCore.QRect(500, 570, 90, 30))
        self.pushButton.clicked.connect(self.showDiagram)


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=0, height=0, dpi=100, f1=5, f2=0, f3=0, f4=0, f5=0, f6=0, f7=0, name=''):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.f4 = f4
        self.f5 = f5
        self.f6 = f6
        self.f7 = f7
        self.name = name

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        x = [self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7]
        labels = ["1-Cубшкала дефицита внимания", "2-Cубшкала гиперактивности и импульсивности",
                  "3-Cубшкала невнимательности и гиперактивности", "4-Cубшкала реакций оппозиции (протеста)",
                  "5-Субшкала др. поведенческих проблем", "6-Субшкала тревожно-депрессивной симптоматики",
                  "7-Субшкала социальной адаптации"]
        labels_num = ["1", "2", "3", "4", "5", "6", "7"]
        colors = ['b', 'r', 'c', 'm', 'g', 'y', 'orange']
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels_num,
               colors=colors,
               shadow=1,
               startangle=90,
               explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
               autopct='%1.1f%%'
               )
        ax.legend(
            bbox_to_anchor=(-0.16, -0.3, 0.25, 0.25),
            loc='lower left', labels=labels)
        ax.set_title("Диаграмма выявленных симптомов\n" + self.name)

        filename = ''
        for x in range(12):
            filename = filename + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        filename += ".pdf"
        fig.savefig(filename)


# ----------------класс обработки сумм для данных анкеты 1-------------------
class Ui_Summ1(QtWidgets.QDialog):
    def hh(self, summ, number1, number2):
        if(person == 1):
            nametable = 'SUMMBOTH'
        elif(person == 2):
            nametable = 'SUMMBOTH2'
        connection = sqlite3.connect('Anketa1.db')
        query1 = 'Select count(' + summ + ') from ' + nametable + ' where ' + summ + ' between ' + str(number1) + ' and ' + str(
            number2) + ' '
        self.buffer = "Критерии выборки: "
        if (self.t5 == '0'):
            query1 += ''
            self.buffer += "мужчины и женщины "
        if (self.t5 == '1'):
            query1 += ' and Sex=1'
            self.buffer += "мужчины "
        if (self.t5 == '2'):
            query1 += ' and Sex=2'
            self.buffer += "женщины "
        if (self.t3 == '' or self.t4 == ''): query1 += ''
        r1 = self.t3
        r2 = self.t4
        if (r1 > r2):
            b = self.t3
            self.t3 = self.t4
            self.t4 = b
            query1 += ' and Age between '
            query1 += self.t3
            query1 += ' and '
            query1 += self.t4
            self.buffer += "возраст от "
            self.buffer += str(self.t3)
            self.buffer += " до "
            self.buffer += str(self.t4)
            self.buffer += " "
        if (r1 < r2):
            query1 += ' and Age between '
            query1 += self.t3
            query1 += ' and '
            query1 += self.t4
            self.buffer += "возраст от "
            self.buffer += str(self.t3)
            self.buffer += " до "
            self.buffer += str(self.t4)
            self.buffer += " "
        if (self.t7 == ''): query1 += ''
        if (self.t7 != ''):
            query1 += ' and class='
            query1 += self.t7
            self.buffer += "класс "
            self.buffer += str(self.t7)
            self.buffer += " "
        if (self.t8 == ''): query1 += ''
        if (self.t8 == '1'):
            query1 += ' and Level=1'
            self.buffer += "уровень "
            self.buffer += str(self.t8)
        if (self.t8 == '2'):
            query1 += ' and Level=2'
            self.buffer += "уровень "
            self.buffer += str(self.t8)
        if (self.t8 == '3'):
            query1 += ' and Level=3'
            self.buffer += "уровень "
            self.buffer += str(self.t8)
        self.buffer += "\n"
        result = connection.execute(query1)
        row = result.fetchall()
        return row[0][0]

    def s(self):
        part1 = [[self.hh('Sum1', 0, 11), self.hh('Sum1', 12, 18), self.hh('Sum1', 19, 27)],
                 [self.hh('Sum2', 0, 11), self.hh('Sum2', 12, 18), self.hh('Sum2', 19, 27)],
                 [self.hh('Sum3', 0, 23), self.hh('Sum3', 24, 36), self.hh('Sum3', 37, 54)],
                 [self.hh('Sum4', 0, 7), self.hh('Sum4', 8, 12), self.hh('Sum4', 13, 24)],
                 [self.hh('Sum5', 0, 5), self.hh('Sum5', 6, 9), self.hh('Sum5', 10, 21)],
                 [self.hh('Sum6', 0, 5), self.hh('Sum6', 6, 9), self.hh('Sum6', 10, 21)]]
        part2 = [[self.hh('Sum21', 0, 11), self.hh('Sum21', 12, 18), self.hh('Sum21', 19, 27)],
                 [self.hh('Sum22', 0, 11), self.hh('Sum22', 12, 18), self.hh('Sum22', 19, 27)],
                 [self.hh('Sum23', 0, 23), self.hh('Sum23', 24, 36), self.hh('Sum23', 37, 54)],
                 [self.hh('Sum24', 0, 7), self.hh('Sum24', 8, 12), self.hh('Sum24', 13, 24)],
                 [self.hh('Sum25', 0, 5), self.hh('Sum25', 6, 9), self.hh('Sum25', 10, 21)],
                 [self.hh('Sum26', 0, 5), self.hh('Sum26', 6, 9), self.hh('Sum26', 10, 21)]]
        self.su1.setText(str(part1[0][0]) + "      |       " + str(part1[0][1]) + "      |       " + str(part1[0][2]));
        self.su2.setText(str(part1[1][0]) + "      |       " + str(part1[1][1]) + "      |       " + str(part1[1][2]));
        self.su3.setText(str(part1[2][0]) + "      |       " + str(part1[2][1]) + "      |       " + str(part1[2][2]));
        self.su4.setText(str(part1[3][0]) + "      |       " + str(part1[3][1]) + "      |       " + str(part1[3][2]));
        self.su5.setText(str(part1[4][0]) + "      |       " + str(part1[4][1]) + "      |       " + str(part1[4][2]));
        self.su6.setText(str(part1[5][0]) + "      |       " + str(part1[5][1]) + "      |       " + str(part1[5][2]));
        self.su_1.setText(str(part2[0][0]) + "      |       " + str(part2[0][1]) + "      |       " + str(part2[0][2]));
        self.su_2.setText(str(part2[1][0]) + "      |       " + str(part2[1][1]) + "      |       " + str(part2[1][2]));
        self.su_3.setText(str(part2[2][0]) + "      |       " + str(part2[2][1]) + "      |       " + str(part2[2][2]));
        self.su_4.setText(str(part2[3][0]) + "      |       " + str(part2[3][1]) + "      |       " + str(part2[3][2]));
        self.su_5.setText(str(part2[4][0]) + "      |       " + str(part2[4][1]) + "      |       " + str(part2[4][2]));
        self.su_6.setText(str(part2[5][0]) + "      |       " + str(part2[5][1]) + "      |       " + str(part2[5][2]));

    def cleaner(self):
        self.su1.setText("")
        self.su2.setText("")
        self.su3.setText("")
        self.su4.setText("")
        self.su5.setText("")
        self.su6.setText("")
        self.su_1.setText("")
        self.su_2.setText("")
        self.su_3.setText("")
        self.su_4.setText("")
        self.su_5.setText("")
        self.su_6.setText("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = Ui_S1(self)

        if (person == 1):
            self.setWindowTitle("Статистика по суммам первичного анкетирования (Родители ребенка)")
        elif (person == 2):
            self.setWindowTitle("Статистика по суммам первичного анкетирования (Учитель)")
        self.setGeometry(200, 50, 650, 670)
        self.setFixedSize(650, 670)
        self.setStyleSheet("")

        self.descrip = QtWidgets.QLabel('Общее количество муж. + жен.', self)
        self.descrip.setGeometry(QtCore.QRect(370, 15, 400, 16))
        self.label_2 = QtWidgets.QLabel('Субшкала невнимательности ', self).setGeometry(QtCore.QRect(100, 90, 261, 21))
        self.label_3 = QtWidgets.QLabel('Субшкала гиперактивности + импульсивности', self).setGeometry(QtCore.QRect(100, 180, 400, 21))
        self.label_4 = QtWidgets.QLabel('Субшкала невнимательности + гиперактивности', self).setGeometry(QtCore.QRect(100, 270, 400, 21))
        self.label_5 = QtWidgets.QLabel('Субшкала реакций оппозиции (протеста) ', self).setGeometry(QtCore.QRect(100, 360, 351, 21))
        self.label_6 = QtWidgets.QLabel('Субшкала др. поведенческих проблем', self).setGeometry(QtCore.QRect(100, 450, 321, 21))
        self.label_7 = QtWidgets.QLabel('Субшкала тревожно-депрессивной симптоматики ', self).setGeometry(QtCore.QRect(100, 540, 421, 21))

        self.label_str1 = QtWidgets.QLabel('Интервал значений        0-11      12-18      19-27\nОбщая сумма баллов\nСумма баллов (2,3)', self).setGeometry(QtCore.QRect(20, 110, 600, 60))
        self.label_str2 = QtWidgets.QLabel('Интервал значений        0-11      12-18      19-27\nОбщая сумма баллов\nСумма баллов (2,3)', self).setGeometry(QtCore.QRect(20, 200, 600, 60))
        self.label_str3 = QtWidgets.QLabel('Интервал значений        0-23      24-36      37-54\nОбщая сумма баллов\nСумма баллов (2,3)', self).setGeometry(QtCore.QRect(20, 290, 600, 60))
        self.label_str4 = QtWidgets.QLabel('Интервал значений        0-7      8-12      13-24\nОбщая сумма баллов\nСумма баллов (2,3)', self).setGeometry(QtCore.QRect(20, 380, 600, 60))
        self.label_str5 = QtWidgets.QLabel('Интервал значений        0-5      6-9      10-21\nОбщая сумма баллов\nСумма баллов (2,3)', self).setGeometry(QtCore.QRect(20, 470, 600, 60))
        self.label_str6 = QtWidgets.QLabel('Интервал значений        0-5      6-9      10-21\nОбщая сумма баллов\nСумма баллов (2,3)', self).setGeometry(QtCore.QRect(20, 560, 600, 60))

        self.su1 = QtWidgets.QLineEdit(self)
        self.su1.setGeometry(QtCore.QRect(200, 135, 200, 20))

        self.su2 = QtWidgets.QLineEdit(self)
        self.su2.setGeometry(QtCore.QRect(200, 225, 200, 20))

        self.su3 = QtWidgets.QLineEdit(self)
        self.su3.setGeometry(QtCore.QRect(200, 315, 200, 20))

        self.su4 = QtWidgets.QLineEdit(self)
        self.su4.setGeometry(QtCore.QRect(200, 405, 200, 20))

        self.su5 = QtWidgets.QLineEdit(self)
        self.su5.setGeometry(QtCore.QRect(200, 495, 200, 20))

        self.su6 = QtWidgets.QLineEdit(self)
        self.su6.setGeometry(QtCore.QRect(200, 585, 200, 20))

        self.su_1 = QtWidgets.QLineEdit(self)
        self.su_1.setGeometry(QtCore.QRect(200, 155, 200, 20))

        self.su_2 = QtWidgets.QLineEdit(self)
        self.su_2.setGeometry(QtCore.QRect(200, 245, 200, 20))

        self.su_3 = QtWidgets.QLineEdit(self)
        self.su_3.setGeometry(QtCore.QRect(200, 335, 200, 20))

        self.su_4 = QtWidgets.QLineEdit(self)
        self.su_4.setGeometry(QtCore.QRect(200, 425, 200, 20))

        self.su_5 = QtWidgets.QLineEdit(self)
        self.su_5.setGeometry(QtCore.QRect(200, 515, 200, 20))

        self.su_6 = QtWidgets.QLineEdit(self)
        self.su_6.setGeometry(QtCore.QRect(200, 605, 200, 20))

        self.findsumma = QtWidgets.QPushButton('Вывести результат', self)
        self.findsumma.setGeometry(QtCore.QRect(210, 10, 150, 30))
        self.findsumma.clicked.connect(self.s)

        self.sbros = QtWidgets.QPushButton('Сброс', self)
        self.sbros.setGeometry(QtCore.QRect(450, 600, 150, 30))
        self.sbros.clicked.connect(self.cleaner)

        self.save = QtWidgets.QPushButton('Критерии оценки', self)
        self.save.setGeometry(QtCore.QRect(10, 10, 200, 30))
        self.save.clicked.connect(self.dialog.exec)

        self.t3 = 0
        self.t4 = 0
        self.buffer = 'Критерии выборки: '
        self.t5 = '0'
        self.t7 = ''
        self.t8 = ''
        self.t9 = ''
        self.t10 = ''



# ----------------главный класс анкетирование на выбор-------------------
class AnketaChoose(QtWidgets.QWidget):

    def openAnketa1(self):
        global person
        person = 1
        self.A1 = Ui_Anketa1()
        self.A1.show()

    def openAnketaAgain1(self):
        global person
        person = 1
        self.A2 = Ui_AnketaAgain()
        self.A2.show()

    def openAnketa2(self):
        global person
        person = 2
        self.A11 = Ui_Anketa1()
        self.A11.show()

    def openAnketaAgain2(self):
        global person
        person = 2
        self.A12 = Ui_AnketaAgain()
        self.A12.show()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setWindowTitle("АНКЕТИРОВАНИЕ")
        self.resize(500, 280)
        self.setFixedSize(500, 280)

        self.Button_1 = QtWidgets.QPushButton('ПЕРВИЧНОЕ анкетирование \n(Родители ребенка)', self)
        self.Button_1.setGeometry(QtCore.QRect(0, 0, 500, 70))
        self.Button_1.clicked.connect(self.openAnketa1)

        self.Button_2 = QtWidgets.QPushButton('ПОВТОРНОЕ анкетирование \n(Родители ребенка)', self)
        self.Button_2.setGeometry(QtCore.QRect(0, 70, 500, 70))
        self.Button_2.clicked.connect(self.openAnketaAgain1)

        self.Button_3 = QtWidgets.QPushButton('ПЕРВИЧНОЕ анкетирование \n(Учитель)', self)
        self.Button_3.setGeometry(QtCore.QRect(0, 140, 500, 70))
        self.Button_3.clicked.connect(self.openAnketa2)

        self.Button_4 = QtWidgets.QPushButton('ПОВТОРНОЕ анкетирование \n(Учитель)', self)
        self.Button_4.setGeometry(QtCore.QRect(0, 210, 500, 70))
        self.Button_4.clicked.connect(self.openAnketaAgain2)

# ----------------главный класс обработки данных анкет-------------------
class FindFromAnketa(QtWidgets.QWidget):

    def findSimptom1(self):
        global person
        person = 1
        self.ff1 = Ui_windowFind1()
        self.ff1.show()

    def findSimptom2(self):
        global person
        person = 2
        self.ff2 = Ui_windowFind1()
        self.ff2.show()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setWindowTitle("ПЕРВИЧНАЯ ОБРАБОТКА АНКЕТ")
        self.resize(500, 140)
        self.setFixedSize(500, 140)

        self.Button_1 = QtWidgets.QPushButton('Оценка ПЕРВИЧНОЙ анкеты \n(Родители ребенка)', self)
        self.Button_1.setGeometry(QtCore.QRect(0, 0, 500, 70))
        self.Button_1.clicked.connect(self.findSimptom1)

        self.Button_2 = QtWidgets.QPushButton('Оценка ПЕРВИЧНОЙ анкеты \n(Учитель)', self)
        self.Button_2.setGeometry(QtCore.QRect(0, 70, 500, 70))
        self.Button_2.clicked.connect(self.findSimptom2)


#-----------------главный класс статистики ------------------------------
class Statistic(QtWidgets.QWidget):

    def stat1(self):
        global person
        person = 1
        self.st1 = Ui_Stat1()
        self.st1.show()

    def stat1a(self):
        global person
        person = 1
        self.st2 = Ui_Simptom1()
        self.st2.show()

    def statsum1(self):
        global person
        person = 1
        self.st3 = Ui_Summ1()
        self.st3.show()

    def stat2(self):
        global person
        person = 2
        self.st11 = Ui_Stat1()
        self.st11.show()

    def stat2a(self):
        global person
        person = 2
        self.st12 = Ui_Simptom1()
        self.st12.show()

    def statsum2(self):
        global person
        person = 2
        self.st13 = Ui_Summ1()
        self.st13.show()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setWindowTitle("ПОСТРОЕНИЕ СТАТИСТИКИ")
        self.resize(500, 420)
        self.setFixedSize(500, 420)

        self.Button_1 = QtWidgets.QPushButton('Общая статистика первичного анкетирования\n(Родители ребенка)', self)
        self.Button_1.setGeometry(QtCore.QRect(0, 0, 500, 70))
        self.Button_1.clicked.connect(self.stat1)

        self.Button_2 = QtWidgets.QPushButton('Статистика по симптомам первичного анкетирования\n(Родители ребенка)', self)
        self.Button_2.setGeometry(QtCore.QRect(0, 70, 500, 70))
        self.Button_2.clicked.connect(self.stat1a)

        self.Button_3 = QtWidgets.QPushButton('Статистика по суммам первичного анкетирования\n(Родители ребенка)', self)
        self.Button_3.setGeometry(QtCore.QRect(0, 140, 500, 70))
        self.Button_3.clicked.connect(self.statsum1)

        self.Button_11 = QtWidgets.QPushButton('Общая статистика первичного анкетирования\n(Учитель)', self)
        self.Button_11.setGeometry(QtCore.QRect(0, 210, 500, 70))
        self.Button_11.clicked.connect(self.stat2)

        self.Button_12 = QtWidgets.QPushButton('Статистика по симптомам первичного анкетирования\n(Учитель)',self)
        self.Button_12.setGeometry(QtCore.QRect(0, 280, 500, 70))
        self.Button_12.clicked.connect(self.stat2a)

        self.Button_13 = QtWidgets.QPushButton('Статистика по суммам первичного анкетирования\n(Учитель)', self)
        self.Button_13.setGeometry(QtCore.QRect(0, 350, 500, 70))
        self.Button_13.clicked.connect(self.statsum2)

# ----------------главный класс просмотра таблиц данных-------------------
class ShowAllTable(QtWidgets.QWidget):

    def Show1(self):
        global person
        person = 1
        global table
        table[0] = 0
        table[1] = 0
        self.sh1 = Ui_Show1()
        self.sh1.show()

    def Show2(self):
        global person
        person = 0
        global table
        table[0] = 1
        table[1] = 0
        self.sh1 = Ui_Show1()
        self.sh1.show()

    def Show3(self):
        global person
        person = 0
        global table
        table[0] = 0
        table[1] = 1
        self.sh1 = Ui_Show1()
        self.sh1.show()

    def Show11(self):
        global person
        person = 2
        global table
        table[0] = 0
        table[1] = 0
        self.sh2 = Ui_Show1()
        self.sh2.show()

    def Show12(self):
        global person
        person = 0
        global table
        table[0] = 2
        table[1] = 0
        self.sh2 = Ui_Show1()
        self.sh2.show()

    def Show13(self):
        global person
        person = 0
        global table
        table[0] = 0
        table[1] = 2
        self.sh2 = Ui_Show1()
        self.sh2.show()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setWindowTitle("РАБОТА С ТАБЛИЦАМИ ДАННЫХ")
        self.resize(500, 420)
        self.setFixedSize(500, 420)

        self.Button_1 = QtWidgets.QPushButton('База данных первичной анкеты \n(Родители ребенка)', self)
        self.Button_1.setGeometry(QtCore.QRect(0, 0, 500, 70))
        self.Button_1.clicked.connect(self.Show1)

        self.Button_2 = QtWidgets.QPushButton('База данных вторичной анкеты \n(Родители ребенка)', self)
        self.Button_2.setGeometry(QtCore.QRect(0, 70, 500, 70))
        self.Button_2.clicked.connect(self.Show2)

        self.Button_3 = QtWidgets.QPushButton('Выявленные дети по данным первичной анкеты \n(Родители ребенка)', self)
        self.Button_3.setGeometry(QtCore.QRect(0, 140, 500, 70))
        self.Button_3.clicked.connect(self.Show3)


        self.Button_11 = QtWidgets.QPushButton('База данных первичной анкеты \n(Учитель)', self)
        self.Button_11.setGeometry(QtCore.QRect(0, 210, 500, 70))
        self.Button_11.clicked.connect(self.Show11)

        self.Button_12 = QtWidgets.QPushButton('База данных вторичной анкеты \n(Учитель)', self)
        self.Button_12.setGeometry(QtCore.QRect(0, 280, 500, 70))
        self.Button_12.clicked.connect(self.Show12)

        self.Button_13 = QtWidgets.QPushButton('Выявленные дети по данным первичной анкеты \n(Учитель)', self)
        self.Button_13.setGeometry(QtCore.QRect(0, 350, 500, 70))
        self.Button_13.clicked.connect(self.Show13)


# ----------------класс главного окна-------------------
class Ui_MainWindow(QtWidgets.QWidget):

    def Menu1(self):
        self.window1 = AnketaChoose()
        self.window1.show()

    def Menu2(self):
        self.window2 = FindFromAnketa()
        self.window2.show()

    def Menu3(self):
        self.window3 = ShowAllTable()
        self.window3.show()

    def Menu4(self):
        self.window4 = Statistic()
        self.window4.show()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setWindowTitle("Добро пожаловать")
        #self.setGeometry(200, 50, 1020, 700)
        self.resize(700, 500)
        self.setFixedSize(700, 500)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(self)
        self.label = QtWidgets.QLabel('Анализ данных анкет пациентов', self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 0, 400, 31))
        font.setPointSize(10)
        self.label.setFont(font)

        self.Button_1 = QtWidgets.QPushButton('АНКЕТИРОВАНИЕ', self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(100, 60, 500, 70))
        self.Button_1.clicked.connect(self.Menu1)

        self.Button_2 = QtWidgets.QPushButton('ПЕРВИЧНАЯ ОБРАБОТКА АНКЕТ', self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(100, 130, 500, 70))
        self.Button_2.clicked.connect(self.Menu2)

        self.Button_3 = QtWidgets.QPushButton('РАБОТА С ТАБЛИЦАМИ ДАННЫХ', self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(100, 200, 500, 70))
        self.Button_3.clicked.connect(self.Menu3)

        self.Button_4 = QtWidgets.QPushButton('ПОСТРОЕНИЕ СТАТИСТИКИ', self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(100, 270, 500, 70))
        self.Button_4.clicked.connect(self.Menu4)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
