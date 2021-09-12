# pylint: disable=no-name-in-module

import sys 
import os
import time 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

sbqss = open(os.path.join(sys.path[0], "sb.qss")).read()

f = ""

class Search(QDialog):
    def __init__(self,parent = None):
        QDialog.__init__(self, parent)

        self.setWindowTitle('Search')
         
        self.setStyleSheet(sbqss)

        self.initUI()
 
    def initUI(self):
 
        self.label = QLabel("Search: ",self)
        self.label.move(10,10)
 
        self.text = QTextEdit(self)
        self.text.move(10,40)
        self.text.resize(250,25)
 
        self.button = QPushButton("Find",self)
        self.button.move(270,40) 
         
        self.setGeometry(640,200,360,100)
