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
        self.upload_btn = QPushButton('Upload Files', self)
        self.upload_btn.move(95,100)
        self.upload_btn.resize(100,30)
        self.nameLabel_3.setStyleSheet("font-size: 12pt; font-weight:bold; font-family:Arial;")
        self.upload_btn.setStyleSheet("color:white; background:#1a8cff; font-size: 11pt;")

        self.textbox_3 = QLineEdit(self)
        self.textbox_3.move(95, 132)
        self.textbox_3.resize(260,30)
        self.textbox_3.setStyleSheet("font-size: 11pt; background:#d9d9d9;")
        self.textbox_3.setReadOnly(True)    #Disabled filed for only read. 

        self.textbox_4 = QLineEdit(self)
        self.textbox_4.move(95, 164)
        self.textbox_4.resize(350,30)
        self.textbox_4.setStyleSheet("font-size: 11pt; background:#d9d9d9;")
        self.textbox_4.setReadOnly(True)
        self.textbox_4.hide()

        # Create a button in the window
        self.button = QPushButton('Click', self)
        self.button.move(95,185)
        self.button.setStyleSheet("background:#00802b; color:#ffffff; font-size:15px;")
        
        # Set an event on upload button click
        self.upload_btn.clicked.connect(self.upload_click)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def upload_click(self):
        global file_name
        f_path_name = QFileDialog.getOpenFileName(self, "Import CSV", "", "Files allowed (*.csv *.xlsx)")
        file_name = os.path.basename(f_path_name[0])
        self.textbox_3.setText(str(file_name))
        self.textbox_4.setText(str(f_path_name[0]))
        print(f_path_name[0])
        print("File basename:- " + file_name)
    
    
    @pyqtSlot()
    def on_click(self):
        text_box_val_1 = self.textbox_1.text()
        text_box_val_2 = self.textbox_2.text()
        text_box_val_3 = self.textbox_3.text()
        source_file_path = self.textbox_4.text()
        destination_path = r"C:\Users\abc123\Desktop\python\python desktop app\form_app\upload_folder"

        if text_box_val_1 != "" and text_box_val_2 != "" and text_box_val_3 != "":
            destination_file_path = os.path.join(destination_path, text_box_val_3)
            os.rename(source_file_path, destination_file_path)
            QMessageBox.question(self, 'Message', "Name:- " + text_box_val_1 + "\n" + "Address:- " + text_box_val_2 + "\n" + "File:- " + text_box_val_3, QMessageBox.Ok, QMessageBox.Ok)
            self.textbox_1.setText("")   #field will be clear by clicking ok.
            self.textbox_2.setText("")
            self.textbox_3.setText("")
        else:
            QMessageBox.question(self, 'Message', "Please provide value to all fields!", QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QMessageBox{font-size: 12pt;}")
    ex = App()
    sys.exit(app.exec())
