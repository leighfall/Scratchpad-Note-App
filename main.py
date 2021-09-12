# pylint: disable=no-name-in-module

import sys
import os
import unittest
from note_window import Note_Window
from landpage_window import LandingPage_Window
from PyQt5.QtWidgets import QApplication

def main():
    # declare an instance of the application
    note = QApplication(sys.argv)

    
    #landing_page = LandingPage_Window()
    main_window = Note_Window()

    QApplication.clipboard().dataChanged.connect(main_window.copiedmessage)
    #run
    main_window.show()
    #landing_page.show()
    
    sys.exit(note.exec_())
    
    
if __name__ == '__main__':
    main()
 
