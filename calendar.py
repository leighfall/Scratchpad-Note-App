# pylint: disable=no-name-in-module
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QCalendarWidget, QLayout, QLabel
import sys
from PyQt5 import QtGui


class CWindow(QDialog):
    def __init__(self,parent = None):
        QDialog.__init__(self, parent)
       # super().__init__()
        
        
        self.setWindowTitle("Assign Date")
        self.left = 500
        self.top = 200
        self.width = 600
        self.height = 500
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.Calendar()

    
    def Calendar(self):
        
        #Variable for widget manipulation / places components vertically
        box = QVBoxLayout()
        
        #Declaring the Calender Variable
        self.cal = QCalendarWidget()
        
        #connecting selection changed to function
        self.cal.selectionChanged.connect(self.changeselecteddate)
        
        #Created Space to Display Usable Date
        self.label = QLabel()
        
        box.addWidget(self.cal)
        box.addWidget(self.label)
        
        #Container to hold Calendar
        self.setLayout(box)
    
    #Gets the date the user selects
    def changeselecteddate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date))
        

    
    
        
#App = QApplication(sys.argv)
#window = CWindow()
#sys.exit(App.exec())