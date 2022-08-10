from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from PyQt5.uic import loadUiType
import sys
import MySQLdb

ui,_ = loadUiType('booking.ui')
login,_ =  loadUiType('login.ui')

class Login(QWidget , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.Handel_Login)

    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='149209' , db='bus_booking')
        self.cur = self.db.cursor()
        
        username = self.lineEdit_9.text()
        password = self.lineEdit_10.text()

        query = "SELECT * FROM user"
        
        self.cur.execute(query)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[3]:
                print('user match')
                self.window2 = Application()
                self.close()
                self.window2.show()
            else:
                self.label.setText('Invalid Username or Password!')

class Application(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Bus Booking App")
        self.setFixedSize(self.size())
        
        self.pushButton_11.clicked.connect(self.add_user)
        self.pushButton_7.clicked.connect(self.book_ticket)
        self.pushButton_9.clicked.connect(self.show_update_tickets)
        self.pushButton_10.clicked.connect(self.update_selected_ticket)
        self.pushButton_13.clicked.connect(self.show_cancel_tickets)
        self.pushButton_12.clicked.connect(self.cancel_selected_ticket)
        self.pushButton_6.clicked.connect(self.Exit)

        self.dateEdit_2.setDate(QDate.currentDate())
        self.dateEdit_3.setDate(QDate.currentDate())
        self.dateEdit_4.setDate(QDate.currentDate())

        #tab buttons
        self.pushButton.clicked.connect(self.data_tab)
        self.pushButton_2.clicked.connect(self.add_tab)
        self.pushButton_3.clicked.connect(self.update_tab)
        self.pushButton_4.clicked.connect(self.cancel_tab)
        self.pushButton_5.clicked.connect(self.user_tab)
        self.tabWidget.tabBar().setVisible(False)

        #functions
        self.approved_tickets()


    def data_tab(self):
        self.tabWidget.setCurrentIndex(0)
    def add_tab(self):
        self.tabWidget.setCurrentIndex(1)
    def update_tab(self):
        self.tabWidget.setCurrentIndex(2)
    def cancel_tab(self):
        self.tabWidget.setCurrentIndex(3)
    def user_tab(self):
        self.tabWidget.setCurrentIndex(4)

    #button functions

    def approved_tickets(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='149209', db = 'bus_booking')
        self.cur = self.db.cursor()

        query = "SELECT id,name, leaving_from, going_to, date,travelling_with, bus_type, bill_rate, pay_rate , mop FROM book_ticket"

        self.cur.execute(query)

        data = self.cur.fetchall()

        print(data)

        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.insertRow(0)
        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget_7.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_position)

    def book_ticket(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='149209', db = 'bus_booking')
        self.cur = self.db.cursor()

        leaving = self.lineEdit.text()
        going = self.lineEdit_2.text()
        temp_date = self.dateEdit_3.date()
        date = temp_date.toPyDate()
        name = self.lineEdit_3.text()
        travelling = self.comboBox_5.currentText()
        bustype = self.comboBox.currentText()
        bill = self.lineEdit_7.text()
        pay = self.lineEdit_8.text()
        mop = self.comboBox_3.currentText()

        if leaving and going and temp_date and name and travelling and bustype and bill and pay and mop != '':
            try:
                query = "INSERT INTO book_ticket(name, leaving_from, going_to,date, travelling_with, bus_type, bill_rate, pay_rate , mop) VALUES(%s, %s, %s, %s , %s, %s , %s, %s , %s)"
                self.cur.execute(query,(name,leaving,going,date,travelling,bustype,bill,pay,mop))
                self.db.commit()
                self.statusBar().showMessage(' Ticket Booked')
                self.approved_tickets()

            except TypeError:
                print(TypeError)
        else:
            QMessageBox.information(self, "Empty Fields", "Please, fill all input fields!")
        
    
    def show_update_tickets(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='149209', db='bus_booking')
        self.cur = self.db.cursor()

        
        person_id = self.lineEdit_5.text()

        try:
            query  = (f"SELECT name, leaving_from, going_to, date,travelling_with, bus_type, bill_rate, pay_rate , mop FROM book_ticket WHERE id = '{person_id}'")
            self.cur.execute(query)
            result = self.cur.fetchone()

            name = result[0]
            leaving = result[1]
            going = result[2]
            date = result[3]
            travelling = result[4]
            bus = result[5]
            bill = result[6]
            pay = result[7]
            mop = result[8]

            t_name = self.lineEdit_26.setText(name)
            t_leaving = self.lineEdit_20.setText(leaving)
            t_going = self.lineEdit_19.setText(going)
            t_date = self.dateEdit_3.setDate(date)
            t_travelling = self.comboBox_12.setCurrentText(travelling)
            t_bus = self.comboBox_10.setCurrentText(bus) 
            t_bill = self.lineEdit_24.setText(bill)
            t_pay = self.lineEdit_25.setText(pay)
            t_mop = self.comboBox_11.setCurrentText(mop)

        except Exception as e:
            QMessageBox.information(self,"Oops","No Data Found!")
        

    def update_selected_ticket(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='149209', db = 'bus_booking')
        self.cur = self.db.cursor()

        
        ticket_id = self.lineEdit_5.text()

        name = self.lineEdit_26.text()
        leaving = self.lineEdit_20.text()
        going = self.lineEdit_19.text()
        temp_date = self.dateEdit_2.date()
        date = temp_date.toPyDate()
        travelling = self.comboBox_12.currentText()
        bustype = self.comboBox_10.currentText()
        bill = self.lineEdit_24.text()
        pay = self.lineEdit_25.text()
        mop = self.comboBox_11.currentText()

        if leaving and going and temp_date and name and travelling and bustype and bill and pay and mop != '':
            query = "UPDATE book_ticket SET name='%s',leaving_from='%s',going_to='%s',date='%s',travelling_with='%s',bus_type='%s',bill_rate='%s',pay_rate='%s', mop='%s' WHERE id = '%s'"

            self.cur.execute(query%(name,leaving,going,date,travelling,bustype,bill,pay,mop,str(ticket_id)))
            self.db.commit()
            self.statusBar().showMessage('Ticket Updated')
            self.approved_tickets()

        else:
            QMessageBox.information(self,"Empty Fields", "Please, search ticket id!")



    def show_cancel_tickets(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='149209', db='bus_booking')
        self.cur = self.db.cursor()

        ticket_id = self.lineEdit_6.text()

        try:
            query  = (f"SELECT name, leaving_from, going_to, date,travelling_with, bus_type, bill_rate, pay_rate , mop FROM book_ticket WHERE id = '{ticket_id}'")
            self.cur.execute(query)
            result = self.cur.fetchone()

            name = result[0]
            leaving = result[1]
            going = result[2]
            date = result[3]
            travelling = result[4]
            bus = result[5]
            bill = result[6]
            pay = result[7]
            mop = result[8]

            t_name = self.lineEdit_53.setText(name)
            t_leaving = self.lineEdit_22.setText(leaving)
            t_going = self.lineEdit_21.setText(going)
            t_date = self.dateEdit_4.setDate(date)
            t_travelling = self.comboBox_39.setCurrentText(travelling)
            t_bus = self.comboBox_37.setCurrentText(bus) 
            t_bill = self.lineEdit_51.setText(bill)
            t_pay = self.lineEdit_52.setText(pay)
            t_mop = self.comboBox_38.setCurrentText(mop)

        except Exception as e:
            QMessageBox.information(self,"Oops","No Data Found!")


         
        


    def cancel_selected_ticket(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='149209', db = 'bus_booking')
        self.cur = self.db.cursor()

        ticket_id = self.lineEdit_6.text()

        name = self.lineEdit_26.text()
        leaving = self.lineEdit_20.text()
        going = self.lineEdit_19.text()
        temp_date = self.dateEdit_2.date()
        date = temp_date.toPyDate()
        travelling = self.comboBox_12.currentText()
        bustype = self.comboBox_10.currentText()
        bill = self.lineEdit_24.text()
        pay = self.lineEdit_25.text()
        mop = self.comboBox_11.currentText()
        
        if ticket_id != '':
                query = "DELETE  FROM book_ticket WHERE id = %s"
                self.cur.execute(query,[(ticket_id)])
                self.db.commit()
                self.statusBar().showMessage('Ticket Canceled')
                self.approved_tickets()
        else:
             QMessageBox.information(self,"Empty Fields", "Please, search ticket id!")


    def add_user(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='149209', db = 'bus_booking')
        self.cur = self.db.cursor()

        username = self.lineEdit_9.text()
        email = self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password_again = self.lineEdit_12.text()
        if username and email and password and password_again != "":
            if password == password_again :
                query = "INSERT INTO user(username , email , password) VALUES(%s, %s, %s)"
                self.cur.execute(query,(username,email, password))
                self.db.commit()
                self.statusBar().showMessage('New User Added')
            else:
                QMessageBox.information(self, "Password Do Not Match", "Please ensure that password is same!")
        else:
            QMessageBox.information(self, "Empty Fields", "Please, fill all input fields!")

    def Exit(self):
        self.close()


if __name__  == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()