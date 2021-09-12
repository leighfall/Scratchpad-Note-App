# pylint: disable=no-name-in-module
import sys
import os
import unittest
from note_window import Note_Window
from note_widget import Note_Widget
#from landpage_window import LandingPage_Window
from PyQt5.QtWidgets import QApplication, QFontComboBox
from PyQt5.QtGui import QClipboard, QTextCursor

class TestNoteFunctions(unittest.TestCase):
    def setUp(self):
        self.note = QApplication(sys.argv)
        self.window = Note_Window()
        self.currentbox = self.window.returncurrenttextbox()
        self.currentbox.insertPlainText("Hello ") #Adds Text to box
        self.ital = self.window.italics #Variable to Italics Feature
        QApplication.clipboard().setText("ThIs Is A tEsT.") #Setting Clipboard for testing
        
        
    
    #Skylar's Test Cases

    #Checking Conditions of Italics Feature
    def test_italicsfeature(self):
        #Turning on Italics
        self.ital.setChecked(True) #Toggles Function On
        self.window.italicsstate()  #Calls Italics Function
        self.assertTrue(self.currentbox.fontItalic())
        
        #Turning off Italics
        self.ital.setChecked(False) #Toggles Function Off
        self.window.italicsstate()  #Calls Italics Function
        self.assertFalse(self.currentbox.fontItalic())
    
    #Checking Copy Feature
    def test_copyfeature(self):
        self.currentbox.insertPlainText("World") #Adding World to Current Textbox (Current contains "Hello ")
        self.currentbox.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor) #Setting Cursor At Beginning of Document
        self.currentbox.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor) #Selecting all Text in Document
        self.window.copy()
        self.assertEqual(QApplication.clipboard().text(), "Hello World")
    
    #Checking Paste Feature
    def test_pastefeature(self):
        self.currentbox.clear() #Cleaning the box out
        self.window.paste() #Pastes from clipboard which was set in setup
        self.assertEqual(self.currentbox.toPlainText(), "ThIs Is A tEsT.")

    # Anthony Test Cases

    # Checking search function
    def test_searchfeature(self):
        self.currentbox.clear()
        self.currentbox.insertPlainText("Hello")
        self.window.Search()
        self.assertEqual(self.currentbox.toPlainText(), 'Hello')

    # Making a test to for the push button 
    def test_search_click(self):
        #button = self.window.Search()
        #find_button = button.button(handle_search)
        #QTest.mouseClick(find_button, Qt.LeftButton)
        pass 

    #Autumn's Test Cases

    #Checking Bold Menu
    def test_boldfeature(self):
        self.currentbox.clear()
        self.currentbox.insertPlainText("Hello World")
        self.currentbox.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.currentbox.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
        self.window.boldmenu()
        self.assertEqual(self.currentbox.toPlainText(), "Hello World") 

    #Checking Underline Menu
    def test_underlinefeature(self):
        self.currentbox.clear()
        self.currentbox.insertPlainText("Hello World")
        self.currentbox.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.currentbox.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
        self.window.underlinemenu()
        self.assertEqual(self.currentbox.toPlainText(), "Hello World") 
    
    #Checking Italic Menu
    def test_italicmenufeature(self):
        self.currentbox.clear()
        self.currentbox.insertPlainText("Hello World")
        self.currentbox.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)
        self.currentbox.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
        self.window.italicsmenu()
        self.assertEqual(self.currentbox.toPlainText(), "Hello World")
        
    
    
        