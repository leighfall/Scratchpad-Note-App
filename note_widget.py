# pylint: disable=no-name-in-module
#
#Note Widget

import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTextEdit, QLineEdit, QPushButton, QColorDialog
from PyQt5.QtGui import QTextListFormat, QTextCursor, QFont


nwidqss = open(os.path.join(sys.path[0], "nwid.qss")).read()

#TextBox Interface and Settings
class Note_Widget(QWidget):
    def __init__(self):
        
        #Setting Variables for Textbox Size
            super().__init__()
            
            self.setStyleSheet(nwidqss)

            self.boxsize()
            
    def boxsize(self):
        
        #Creating PlainText Editor
        self.textbox = QTextEdit(self)
        self.textbox.setPlaceholderText("Insert Note...\n")
        self.textbox.setFontPointSize(11)
    
      
        #self.textbox.move(10,10)
        
    def indent(self):
        cursor = self.textbox.textCursor()
        
        if cursor.hasSelection():
            beginning = cursor.blockNumber()
            cursor.setPosition(cursor.selectionEnd())
            totalrange = cursor.blockNumber() - beginning
            
            for i in range(totalrange + 1):
                cursor.movePosition(QTextCursor.StartOfLine)
                cursor.insertText("\t")
                cursor.movePosition(QTextCursor.Up)
        else:
            cursor.insertText("\t")
            
    def undoindent(self):
        cursor = self.textbox.textCursor()
        
        if cursor.hasSelection():
            beginning = cursor.blockNumber()
            cursor.setPosition(cursor.selectionEnd())
            totalrange = cursor.blockNumber() - beginning
            
            for i in range(totalrange + 1):
                self.performunindent(cursor)
                cursor.movePosition(QTextCursor.Up)
        else:
            self.performunindent(cursor)
        
    def performunindent(self, cur):
        cur.movePosition(QTextCursor.StartOfLine)
        currentposition = cur.block().text()
        
        if currentposition.startswith("\t"):
            cur.deleteChar()
        else:
            for char in currentposition[:8]:
                if  char != " ":
                    break
                cur.deleteChar()
                
    def createbullet(self, style):
        cursor = self.textbox.textCursor()
        listForm = QTextListFormat()
        listForm.setStyle(style)
        listForm.setIndent(3)
        cursor.createList(listForm)
      #  cursor.insertText("one")
       # print("What")
        #self.textbox.AutoFormatting(QTextEdit.AutoBulletList)
        
    def removebullet(self):
        cursor = self.textbox.textCursor()
        list = cursor.currentList()
        
        if list:
            listform = QTextListFormat()
            listform.setIndent(0)
            listform.setStyle(0)
            list.setFormat(listform)
            
            for i in range(list.count() - 1, 0, -1):
                list.removeItem(i)
            
            
    
    def italics(self):
        if self.textbox.fontItalic() != True:
            self.textbox.setFontItalic(True)
        else:
            self.textbox.setFontItalic(False)
        
    def makeitalics(self):
        self.textbox.setFontItalic(True)
    
    def undoitalics(self):
        self.textbox.setFontItalic(False)
        
    def bold(self):
        if self.textbox.fontWeight() != 75:
            self.textbox.setFontWeight(75)
        else:
            self.textbox.setFontWeight(50)
            
            
    def makebold(self):
        self.textbox.setFontWeight(75)
        
    def undobold(self):
        self.textbox.setFontWeight(50)
        
    def underline(self):
        if self.textbox.fontUnderline() != True:
            self.textbox.setFontUnderline(True)
        else:
            self.textbox.setFontUnderline(False)
    
    def makeunderline(self):
        self.textbox.setFontUnderline(True)
    
    def undounderline(self):
        self.textbox.setFontUnderline(False)
    
    def copy_text(self):
        self.textbox.copy()
    
    def cut_text(self):
        self.textbox.cut()
    
    def paste_text(self):
        self.textbox.paste()
    
    def setcolor(self):
        color = QColorDialog.getColor()
        self.textbox.setTextColor(color)
    
    def setfontsize(self, size):
        self.textbox.setFontPointSize(float(size))
        #print(float(size))
        
    def setfont(self, font):
        self.textbox.setCurrentFont(font)
    
        



        