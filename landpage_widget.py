
import sys
import os
from note_widget import Note_Widget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#TextBox Interface and Settings
class LandingPage(QWidget):
    def __init__(self):
        #Setting Variables for Textbox Size
        super().__init__()

        self.central_layout = QVBoxLayout()
        
        self.grid_layout = QGridLayout()
        self.open_button1 = QPushButton('Open')
        self.open_button1.clicked.connect(self.open_file)
        self.grid_layout.addWidget(self.open_button1)
        
        self.quit_button1 = QPushButton('Quit')
        self.quit_button1.clicked.connect(self.quit_button)
        self.grid_layout.addWidget(self.quit_button1)

        self.central_layout.addLayout(self.grid_layout)

        self.setLayout(self.central_layout)

        # This should be able to show the saved file names 
        #QFileDialog.getSaveFileName()

    def open_file(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')   #Opening File Dialog
        file = open(name[0], 'r')                               #Opening and Reading File
        
        #Setting Opened File as New Widget
        self.central_Widget = Note_Widget()                     #Reassigning Central Widget Variable to New Widget
        self.setCentralWidget(self.central_Widget)
        with file:
            text = file.read()
            self.central_Widget.textbox.setText(text)      #Putting Text from File in New Widget Textbox
        self.setWindowTitle(name[0])
        
    def quit_button(self):
        sys.exit()

   