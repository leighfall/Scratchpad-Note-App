# Landing Page 
import sys
import os
from landpage_widget import LandingPage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class LandingPage_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Landing Page')

        self.central_Widget = LandingPage()
        self.setCentralWidget(self.central_Widget)

        self.statusBar().showMessage('Maybe useful???')
        
        