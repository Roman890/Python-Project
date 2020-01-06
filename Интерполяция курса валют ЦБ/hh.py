# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets, QtCore
import pyqtgraph as pg
import numpy as np
import sqlite3
import datetime
import urllib.request
from xml.dom import minidom
import pyopencl as cl
import matplotlib.pyplot as plt
import numpy
import math
# определить дату сегодня
now = datetime.datetime.today()
now = str(now.strftime("%d/%m/%Y"))
print(now)


# фунция замены запятых на точки и перевод строки в float
def numbers(s):
    return float(s.replace(',', '.'))

# фунция замены точек на / в дате
def change(s):
    return s.replace('.', '/')

# функция отправения смс-сообщения если курс валюты превышен некоторого значения за сегодня
def sendsms(value):
    connection = sqlite3.connect('Money.db')
    query = 'Select count(nom) from Number'
    result = connection.execute(query)
    row = result.fetchall()
    if (row[0][0] != 0):
        url = "https://sms.ru/sms/send?api_id=182C58A8-7AB9-1389-14D7-23D2088B228B&to=79202550189"
        for i in range(row[0][0]):
            query = 'Select * from Number where id=' + str(i+1) + ''
            result = connection.execute(query)
            row = result.fetchall()
            print(i)
            url1 = ',' + str(row[0][1])
            url += url1
        url += "&msg=increase+the+value+of+the+course+"
        url += str(value)
        url += "&json=1"
        res = urllib.request.urlopen(url)
        print (url)
        print("sms отправлена получателям")
    else :
        url = "https://sms.ru/sms/send?api_id=182C58A8-7AB9-1389-14D7-23D2088B228B&to=79202550189&msg=increase+the+value+of+the+course+"
        url += str(value)
        url += "&json=1"
        res = urllib.request.urlopen(url)
        print("sms отправлена только владельцу приложения")
        print(url)


class Ui_Dia1(QtWidgets.QDialog):
    def d(self, date):
        self.ff.data1.setText(date.toString("dd/MM/yyyy"))

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.ff = root
        self.arg = kwargs
        calendarWidget = QtWidgets.QCalendarWidget()
        calendarWidget.setGeometry(QtCore.QRect(0, 0, 291, 191))
        self.setFixedSize(291, 191)
        self.setWindowTitle('Календарь')
        calendarWidget.clicked.connect(self.d)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(calendarWidget)
        self.setLayout(layout)


class Ui_Dia2(QtWidgets.QDialog):
    def d(self, date):
        self.ff.data2.setText(date.toString("dd/MM/yyyy"))

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.ff = root
        self.arg = kwargs
        calendarWidget = QtWidgets.QCalendarWidget()
        calendarWidget.setGeometry(QtCore.QRect(0, 0, 291, 191))
        self.setFixedSize(291, 191)
        self.setWindowTitle('Календарь')
        calendarWidget.clicked.connect(self.d)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(calendarWidget)
        self.setLayout(layout)


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.dialog1 = Ui_Dia1(self)
        self.dialog2 = Ui_Dia2(self)
        self.setWindowTitle("Курс валют")
        layout = QtWidgets.QGridLayout(self)
        self.setLayout(layout)
        self.buf = self.first = 0

        self.array1 = []
        self.array2 = []
        self.view = view = pg.PlotWidget()
        self.curve = view.plot()
        self.curve1 = view.plot()
        self.view.showGrid(x=True, y=True)
        self.view.setLabel('left', 'Значения')
        self.view.setLabel('bottom', 'Дата')




        self.name = 'money2'
        self.btn2 = QtWidgets.QPushButton('Индийский рупий')
        self.btn2.clicked.connect(self.plot2)
        self.btn2.setStyleSheet("background-color:  #87CEEB")
        self.name = 'money3'
        self.btn3 = QtWidgets.QPushButton('Бразильский реал')
        self.btn3.clicked.connect(self.plot3)
        self.btn3.setStyleSheet("background-color:  #87CEEB")

        self.saveP = QtWidgets.QPushButton('Загрузить данные из сети в базу данных')
        self.saveP.clicked.connect(self.savePlot)
        self.saveP.setStyleSheet("background-color:  #87CEEB")
        self.clear = QtWidgets.QPushButton('Очистить')
        self.clear.clicked.connect(self.clr)
        self.clear.setStyleSheet("background-color:  #87CEEB")

        self.data1button = QtWidgets.QPushButton('дата поиска от', self)
        self.data1button.clicked.connect(self.dialog1.exec)
        self.data1button.setStyleSheet("background-color:  #87CEEB")
        self.data2button = QtWidgets.QPushButton('дата поиска до', self)
        self.data2button.clicked.connect(self.dialog2.exec)
        self.data2button.setStyleSheet("background-color:  #87CEEB")

        self.text1 = QtWidgets.QLineEdit()
        self.text1.setStyleSheet("background-color:  white")
        self.data1 = QtWidgets.QLineEdit()
        self.data1.setStyleSheet("background-color:  white")
        self.data2 = QtWidgets.QLineEdit()
        self.data2.setStyleSheet("background-color:  white")
        self.saveNumber = QtWidgets.QPushButton('Добавить номер телефона')
        self.saveNumber.clicked.connect(self.saveNum)
        self.saveNumber.setStyleSheet("background-color:  #87CEEB")



        layout.addWidget(self.view, 1,2,7,2)
        layout.addWidget(self.btn2, 0, 2)
        layout.addWidget(self.btn3, 0, 3)
        layout.addWidget(self.data1button, 9, 2)
        layout.addWidget(self.data2button, 9, 3)
        layout.addWidget(self.data1, 10, 2)
        layout.addWidget(self.data2, 10, 3)
        layout.addWidget(self.saveP, 11, 2)
        layout.addWidget(self.clear, 11, 3)
        layout.addWidget(self.text1, 1, 0)
        layout.addWidget(self.saveNumber, 0, 0)


    def find(self, base):
        self.array2 = []
        self.array1 = []
        connection = sqlite3.connect('Money.db')
        query = 'Select count(Date) from ' + base
        result = connection.execute(query)
        row = result.fetchall()
        if (row[0][0] != 0):
            for i in range(row[0][0]):
                query = 'Select * from ' + base + ' where id=' + str(i) + ''
                result = connection.execute(query)
                row = result.fetchall()
                self.array2.append(numbers(row[0][2]))
                self.array1.append(i)
            self.buf = 1
            self.curve.setData(self.array2, pen='b', symbol='o', symbolPen='b', symbolBrush=0.2)

            size = len(self.array1)
            print(size)
            self.ctx = cl.create_some_context()
            self.queue = cl.CommandQueue(self.ctx)
            # read in the OpenCL source file as a string
            f = open("kernel.cl", 'r')
            fstr = "".join(f.readlines())
            # create the program
            self.program = cl.Program(self.ctx, fstr).build()
            mf = cl.mem_flags

            xnew1 = []
            # initialize client side (CPU) arrays
            self.a = numpy.array(self.array1).astype(numpy.float32)
            self.b = numpy.array(self.array2).astype(numpy.float32)
            number_part = math.ceil(size/5)

            self.xnew = numpy.linspace(numpy.min(self.a), numpy.max(self.a), 100).astype(numpy.float32)

            # create OpenCL buffers
            self.a_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.a)
            self.b_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.b)
            self.xnew_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=self.xnew)
            self.dest_buf = cl.Buffer(self.ctx, mf.WRITE_ONLY, self.xnew.nbytes)
            self.program.part1(self.queue, (100,), (size,), numpy.int32(size), self.a_buf, self.b_buf, self.dest_buf,
                             self.xnew_buf)
            self.c = numpy.zeros(100, dtype=numpy.float32)
            cl.enqueue_copy(self.queue, self.c, self.dest_buf).wait()
            self.curve1.setData(self.xnew, self.c, pen='r')
        else:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Error")
            error_message.showMessage("База данных пуста")


    def plot2(self):
        self.find('money2')

    def plot3(self):
        self.find('money3')

    def savePlot(self):
        if (self.data2.text() != '' and self.data1.text() != ''):
            self.loadBD('money2', 'Indian+rupee', 'R01270', 90)
            self.loadBD('money3', 'Brazilian+real', 'R01115', 16)
        else:
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Error")
            error_message.showMessage("Для начала необходимо задать даты ")

    def loadBD(self, base, name_momey, name_money_cbr, value_money):
        self.array1 = []
        self.array2 = []
        buf = "http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=" + self.data1.text() + "&date_req2=" + self.data2.text() + "&VAL_NM_RQ=" + name_money_cbr
        print(buf)
        url = buf
        webFile = urllib.request.urlopen(url)
        data = webFile.read()
        FileName = 'first.xml'
        with open(FileName, "wb") as localFile:
            localFile.write(data)
            webFile.close()

        doc = minidom.parse(FileName)
        currency = doc.getElementsByTagName("Record")
        yy=0

        for rate in currency:
            value = rate.getElementsByTagName("Value")[0]
            date = rate.getAttribute('Date')
            date = change(date)
            if (numbers(value.firstChild.data) > value_money and yy == 0 ): #and date == now):
                #print("зашли")
                sendsms(name_momey)
                yy =9
            self.array2.append(value.firstChild.data)
            self.array1.append(date)

        print(self.array2)
        print(self.array1)

        n = len(self.array2)
        connection = sqlite3.connect('Money.db')
        query = 'DROP TABLE IF EXISTS ' + base
        connection.execute(query)
        connection.commit()
        connection = sqlite3.connect('Money.db')
        query = 'CREATE TABLE IF NOT EXISTS ' + base +' (id INTEGER, Date TEXT, ValueM TEXT)'
        connection.execute(query)
        for i in range(n):
            query = 'INSERT INTO ' + base + ' (id, Date,ValueM) VALUES(?,?,?)'
            connection.execute(query, (i, self.array1[i], numbers(self.array2[i])))
        connection.commit()


    def saveNum(self):
        connection = sqlite3.connect('Money.db')
        t = self.text1.text()
        query = 'CREATE TABLE IF NOT EXISTS number (id INTEGER PRIMARY KEY, nom TEXT, descr TEXT)'
        connection.execute(query)
        query = 'INSERT INTO number (nom, descr) VALUES(?, ?)'
        connection.execute(query, (t, 'превышено значение'))
        connection.commit()
        self.text1.setText('')

    def clr(self):
        mass = [0]
        self.curve.setData(mass)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.setStyleSheet("background-color: #1E90FF ")
    w.show()
    app.exec()

