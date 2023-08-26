import sys
import os

from PyQt5 import *
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Python Demo Desktop App'
        self.left = 350
        self.top = 150
        self.width = 700
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox with label Name:
        self.nameLabel_1 = QLabel(self)
        self.nameLabel_1.setText('Name:')
        self.nameLabel_1.move(20, 20)
        self.textbox_1 = QLineEdit(self)
        self.textbox_1.move(95, 20)
        self.textbox_1.resize(260,30)
        self.nameLabel_1.setStyleSheet("font-size: 12pt; font-weight:bold; font-family:Arial;")
        self.textbox_1.setStyleSheet("font-size: 11pt;")

        # Create textbox with label Address:
        self.nameLabel_2 = QLabel(self)
        self.nameLabel_2.setText('Address:')
        self.nameLabel_2.move(20, 60)
        self.textbox_2 = QLineEdit(self)
        self.textbox_2.move(95, 60)
        self.textbox_2.resize(260,30)
        self.nameLabel_2.setStyleSheet("font-size: 12pt; font-weight:bold; font-family:Arial;")
        self.textbox_2.setStyleSheet("font-size: 11pt;")

        # Create upload button
        self.nameLabel_3 = QLabel(self)
        self.nameLabel_3.setText('Upload:')
        self.nameLabel_3.move(20, 100)
        self.upload_btn = QPushButton('Upload CSV File', self)
        self.upload_btn.move(95,100)
        self.upload_btn.resize(120,30)
        self.nameLabel_3.setStyleSheet("font-size: 12pt; font-weight:bold; font-family:Arial;")
        self.upload_btn.setStyleSheet("color:white; background:#1a8cff; font-size: 11pt;")

        # Create a button in the window
        self.button = QPushButton('Click', self)
        self.button.move(95,150)
        self.button.setStyleSheet("background:#00802b; color:#ffffff; font-size:15px;")
        
        # Set an event on upload button click
        self.upload_btn.clicked.connect(self.upload_click)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def upload_click(self):
        fname = QFileDialog.getOpenFileName(None, "Import CSV", "", "Files allowed (*.csv *.xlsx)")
        print(fname[0])
    
    @pyqtSlot()
    def on_click(self):
        text_box_val_1 = self.textbox_1.text()
        text_box_val_2 = self.textbox_2.text()

        if text_box_val_1 != "" or text_box_val_2 != "":
            QMessageBox.question(self, 'Message', "Name:- " + text_box_val_1 + "\n" + "Address:- " + text_box_val_2, QMessageBox.Ok, QMessageBox.Ok)
            self.textbox_1.setText("")   #field will be clear by clicking ok.
            self.textbox_2.setText("")
        else:
            QMessageBox.question(self, 'Message', "Please provide value to all fields!", QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QMessageBox{font-size: 12pt;}")
    ex = App()
    sys.exit(app.exec())