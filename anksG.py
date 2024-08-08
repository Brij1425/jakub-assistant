from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowState(Qt.WindowMaximized)  # Maximize the window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.input_box1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_box2 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_box = QtWidgets.QTextEdit(self.centralwidget)
        self.speak_button = QtWidgets.QPushButton('Speak Command', self.centralwidget)
        self.stop_button = QtWidgets.QPushButton('Stop', self.centralwidget)
        self.weather_box = QtWidgets.QTextEdit(self.centralwidget)

        # Set font size and bold
        font = QFont()
        font.setPointSize(16)  # Adjust the font size as needed
        font.setBold(True)
        self.input_box1.setFont(font)
        self.input_box2.setFont(font)
        self.output_box.setFont(font)
        self.speak_button.setFont(font)
        self.stop_button.setFont(font)
        self.weather_box.setFont(font)

        # Set colors
        self.centralwidget.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")
        self.input_box1.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.input_box2.setStyleSheet("background-color: #34495e; color: #ecf0f1;")
        self.output_box.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")
        self.speak_button.setStyleSheet("background-color: #3498db; color: #ecf0f1;")
        self.stop_button.setStyleSheet("background-color: #e74c3c; color: #ecf0f1;")
        self.weather_box.setStyleSheet("background-color: #34495e; color: #ecf0f1;")

        # Create layouts
        main_layout = QVBoxLayout(self.centralwidget)
        top_layout = QHBoxLayout()  # Top layout for input boxes and weather box
        bottom_layout = QVBoxLayout()  # Bottom layout for output box and buttons

        # Set fixed heights for the boxes and buttons
        box_height = 100
        button_height = 100
        self.input_box1.setFixedHeight(box_height)
        self.input_box2.setFixedHeight(box_height)
        self.weather_box.setFixedHeight(box_height * 2)
        self.output_box.setFixedHeight(box_height * 5)  # Increased height for the output box
        self.speak_button.setFixedHeight(button_height)
        self.stop_button.setFixedHeight(button_height)

        # Set fixed widths for the input boxes
        box_width = 500
        self.input_box1.setFixedWidth(box_width)
        self.input_box2.setFixedWidth(box_width)

        # Add widgets to layouts
        top_layout.addWidget(self.weather_box)  # Add weather box to the top layout
        top_layout.addWidget(self.input_box1)
        top_layout.addWidget(self.input_box2)

        bottom_layout.addWidget(self.output_box)
        bottom_layout.addWidget(self.speak_button)
        bottom_layout.addWidget(self.stop_button)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtWidgets.QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt GUI Example"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.retranslateUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())