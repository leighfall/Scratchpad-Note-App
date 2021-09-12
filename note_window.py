# pylint: disable=no-name-in-module
#Note Application Window
import sys
import os
from note_widget import Note_Widget
from calendar import CWindow
from search import Search
from PyQt5.QtCore import Qt, QSize, QObject
from PyQt5.QtWidgets import QMainWindow, QComboBox, QTabWidget, QVBoxLayout, QColorDialog, QWidget, QMessageBox, QCalendarWidget, QHBoxLayout, QTabBar
from PyQt5.QtWidgets import QToolBar, QFontComboBox
from PyQt5.QtWidgets import QAction, QMenu, QToolButton
from PyQt5.QtGui import QIcon, QClipboard, QColor, QTextListFormat
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import *

nwinqss = open(os.path.join(sys.path[0], "nwin.qss")).read()
    
class Note_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        global noteindex
        if 'noteindex' not in globals():
            noteindex = {}
        
        
        self.setStyleSheet(nwinqss)
        self.setWindowTitle('Scratchpad')

        #Setting Widget in the center of window
        
        
        #Creation of Tabs
     #  self.setTabs
        self.path = None
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        #self.tab2 = QWidget()
        self.tabs.tabBar().setTabsClosable(True)
        self.tabs.setTabShape(QTabWidget.Rounded)
        
        self.tabs.addTab(self.tab1, "New Note")
        #self.tabs.addTab(self.tab2, "+")
        
        self.tabButton = QToolButton()
        self.tabButton.setText('+')
        font = self.tabButton.font()
        font.setBold(True)
        self.tabButton.setFont(font)
        self.tabs.setCornerWidget(self.tabButton)
        self.tabButton.clicked.connect(self.newtab)
        
        
        
       # addatab = QAction(self)
       # ----------self.tabs.currentChanged.connect(self.tabtest)
        #self.tab2.addAction(addatab)
      #  if self.tabs.tabBar().currentIndex() == self.tabs.tabBar().count() - 1:
      #      print("j")
      #      self.newtab()
            
        noteindex[self.tabs.currentIndex()] = Note_Widget()
        
        
        self.tab1.layout = QVBoxLayout()
        self.tab1.layout.addWidget(noteindex[self.tabs.currentIndex()])
        
        self.tab1.setLayout(self.tab1.layout)
       # mainlayout = QVBoxLayout()

        #widget = QWidget()
       # widget.setLayout(mainlayout)
        #self.setCentralWidget(self.table_widget)
        self.setCentralWidget(self.tabs)
        
        

        self.tabs.tabBar().tabCloseRequested.connect(self.closetab)

       # toolbarlayout = QHBoxLayout()
       # mainlayout.addLayout( toolbarlayout )
      #  mainlayout.addWidget(Note_Widget())
        
        #Adding Menu Option and Toolbar

        menu = self.menuBar()
        
        toolbar = QToolBar("Quick Access Menu")
        toolbar.setIconSize(QSize(50,50))
        self.addToolBar(toolbar)
        toolbar.setFloatable(False)
        toolbar.setMovable(False)
        toolbar.toggleViewAction().setEnabled(False)
        file_menu = menu.addMenu('File')
        edit_menu = menu.addMenu('Edit')
        format_menu = menu.addMenu('Format')
        search_menu = menu.addMenu('Search')
       # reminder_menu = menu.addMenu('Reminders')

        
        
        
        open_icon = QIcon('icons/open.png')
        open_toolbar = QAction(open_icon, "Open", self)
        open_toolbar.setStatusTip("Open File")
        open_toolbar.setShortcut('Ctrl+O')
        open_toolbar.triggered.connect(self.open_file)
        #open_toolbar.setCheckable(True)
        toolbar.addAction(open_toolbar)

        save_icon = QIcon('icons/diskette.png')
        save_toolbar = QAction(save_icon, "Save", self)
        save_toolbar.setStatusTip("Save Current File")
        save_toolbar.setShortcut('Ctrl+S')
        save_toolbar.triggered.connect(self.save_file_as)
        #save_toolbar.setCheckable(True)
        toolbar.addAction(save_toolbar)
        
        toolbar.addSeparator()
        
        font = QFontComboBox()
        font.setEditable(True)
        font.currentFontChanged.connect(self.fontselection)
        toolbar.addWidget(font)
        
        self.fontSize = QComboBox()
        self.fontSize.insertItems(1,['8', '9', '10', '11', '12', '14', '16', '18', '20', '22', '24', '26', '28', '36', '48', '72'])
        self.fontSize.setEditable(True)
        self.fontSize.setCurrentIndex(3)
        self.fontSize.setMinimumContentsLength(5)
        self.fontSize.activated.connect(self.size)
        toolbar.addWidget(self.fontSize)
        
        fontColor_icon = QIcon('icons/fontcolor.png')
        fontColor = QAction(fontColor_icon, 'Font Color', self)
        fontColor.triggered.connect(self.color_selection)
        toolbar.addAction(fontColor)
        
        toolbar.addSeparator()
        
        left_just_icon = QIcon('icons/left-align.png')
        left_just = QAction(left_just_icon, "Left", self)
        left_just.setShortcut('Ctrl+Shift+L')
        left_just.setStatusTip("Left Justification")
        left_just.triggered.connect(self.left)
       # left_just.setCheckable(True)
        toolbar.addAction(left_just)
        
        center_just_icon = QIcon('icons/center-alignment.png')
        center_just = QAction(center_just_icon, "Center", self)
        center_just.setShortcut('Ctrl+Shift+E')
        center_just.setStatusTip("Center Justification")
        center_just.triggered.connect(self.center)
       # center_just.setCheckable(True)
        toolbar.addAction(center_just)
        
        right_just_icon = QIcon('icons/right-alignment.png')
        right_just = QAction(right_just_icon, "Right", self)
        right_just.setShortcut('Ctrl+Shift+R')
        right_just.setStatusTip("Right Justification")
        right_just.triggered.connect(self.right)
        #right_just.setCheckable(True)
        toolbar.addAction(right_just)
                
        toolbar.addSeparator()
        
        bold_icon = QIcon('icons/boldcolor.png')
        self.bold = QAction(bold_icon, "Bold", self)
        self.bold.setStatusTip("Make Font Bold")
        self.bold.triggered.connect(self.boldstate)
        self.bold.setCheckable(True)
        toolbar.addAction(self.bold)
        
        italics_icon = QIcon('icons/italics.png')
        self.italics = QAction(italics_icon, "Italics", self)
        self.italics.setStatusTip("Make Font Italic")
        self.italics.triggered.connect(self.italicsstate)
        self.italics.setCheckable(True)
        toolbar.addAction(self.italics)
        
        underline_icon = QIcon('icons/underline.png')
        self.underline = QAction(underline_icon, "Underline", self)
        self.underline.setStatusTip("Underlines Current Text")
        self.underline.triggered.connect(self.underlinestate)
        self.underline.setCheckable(True)
        toolbar.addAction(self.underline)
        
        toolbar.addSeparator()
        
        makebullets_icon = QIcon('icons/list.png')
        self.makebullets = QAction(makebullets_icon, "Bulletpoints", self)
        self.makebullets.setStatusTip("Add Bulletpoints")
        self.makebullets.triggered.connect(self.bulletstate)
        self.makebullets.setCheckable(True)
        toolbar.addAction(self.makebullets)
        
        self.bulletstyle = QTextListFormat().ListDisc  #Set Default Bullet type
        
        
        
        dedent_icon = QIcon('icons/left-indent.png')
        self.dedent = QAction(dedent_icon, "Left Indent", self)
        self.dedent.setStatusTip("Undo Text Indention")
        self.dedent.setShortcut('Ctrl+[')
        self.dedent.triggered.connect(self.calldedent)
        toolbar.addAction(self.dedent)
        
        indent_icon = QIcon('icons/right-indent.png')
        self.indent = QAction(indent_icon, "Right Indent", self)
        self.indent.setStatusTip("Indent Text")
        self.dedent.setShortcut('Ctrl+]')
        self.indent.triggered.connect(self.callindent)
        toolbar.addAction(self.indent)

        
        

        #toolBar = self.addToolBar('Text Color')
        #toolBar.toggleViewAction().setEnabled(False)
        
    
        
        #toolbarlayout.addWidget(toolBar)
        
       # toolbar.addWidget(self.combo)
       # self.combo.insertItems(1,["Black","Red","Green","Blue","Purple"])
       # self.combo.activated.connect(self.changecolor)








        
        
        #Adding Menu Options

        exit_icon = QIcon.fromTheme('application-exit') #Currently does nothing
        exit_button = QAction(exit_icon, 'Quit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.triggered.connect(self.close)       #Connecting actions to save_file function
        
       
        copy_icon = QIcon('icons/copy.png')                 #Icon Placeholder
        copy_button = QAction(copy_icon, 'Copy', self)  #Setting an action
        copy_button.setShortcut('Ctrl+C')
        copy_button.setStatusTip('Copy')           
        copy_button.triggered.connect(self.copy)   #Connecting actions to copy_file function
    
        paste_icon = QIcon('icons/paste.png')                 #Icon Placeholder
        paste_button = QAction(paste_icon, 'Paste', self)  #Setting an action
        paste_button.setShortcut('Ctrl+V')
        paste_button.setStatusTip('Paste')           
        paste_button.triggered.connect(self.paste)   #Connecting actions to paste_file function
        
        cut_icon = QIcon('icons/cut.png')                 #Icon Placeholder
        cut_button = QAction(cut_icon, 'Cut', self)  #Setting an action
        cut_button.setShortcut('Ctrl+X')
        cut_button.setStatusTip('Cut')           
        cut_button.triggered.connect(self.cut)   #Connecting actions to copy_file function
        
        text_format = QMenu('Text', self)  #Setting an action
        text_format.setStatusTip('Edit Your Text Formatting')
        
        align_indent = QMenu('Align and Indent', self)
        align_indent.setStatusTip('Set Text Alignment')
        
        bullet_number = QMenu('Bullets and Numbering', self)
        bullet_number.setStatusTip('Set Bullet Style')
        
        bullet_style = QMenu('Bullet Style', self)
        bullet_style.setStatusTip('Set Bullet Style Type')
        
        bold_format = QAction(bold_icon, 'Bold', self)
        bold_format.setShortcut('Ctrl+B')
        bold_format.setStatusTip('Make Your Text Bold')  
        bold_format.triggered.connect(self.boldmenu)     
       # text_format.triggered.connect(self.cut) 
       
        italics_format = QAction(italics_icon, 'Italics', self)
        italics_format.setShortcut('Ctrl+I')
        italics_format.setStatusTip('Make Your Text Italics')  
        italics_format.triggered.connect(self.italicsmenu)
        
        underline_format = QAction(underline_icon, 'Underline', self)
        underline_format.setShortcut('Ctrl+U')
        underline_format.setStatusTip('Underline your text')  
        underline_format.triggered.connect(self.underlinemenu) 
        
        addbullets = QAction(makebullets_icon, 'Add Bulletpoint', self)
        addbullets.setStatusTip('Add Bulletpoints')
        addbullets.triggered.connect(self.bulletmenu)
        
        disc = QAction('Disc', self)
        disc.triggered.connect(self.changedisc)
        

        circle = QAction('Circle', self)
        circle.triggered.connect(self.changedcircle)
        
        square = QAction('Square', self)
        square.triggered.connect(self.changedsquare)
        
        decimal = QAction('Decimal', self)
        decimal.triggered.connect(self.changeddecimal)
        
        la = QAction('Lowercase Alphabet', self)
        la.triggered.connect(self.changedlowlatin)
        
        ua = QAction('Uppercase Alphabet', self)
        ua.triggered.connect(self.changedhighlatin)
        
        lr = QAction('Lowercase Roman Numerals', self)
        lr.triggered.connect(self.changedlowroman)
        

        ur = QAction('Uppercase Roman Numerals', self)
        ur.triggered.connect(self.changedhighroman)
        
        
        #reminder_icon = QIcon()                 #Icon Placeholder
        #add_reminder_button = QAction(reminder_icon, 'Create New Reminder', self)  #Setting an action
        #add_reminder_button.setShortcut('Ctrl+R')
        #add_reminder_button.setStatusTip('Create New Reminder')           
        #add_reminder_button.triggered.connect(self.cremind) 

        searchAction = QAction(QIcon('icons/loupe.png'), "Find Word", self)	
        searchAction.setShortcut("Ctrl+F")	
        searchAction.setStatusTip("Search words in document")	
        searchAction.triggered.connect(self.Search)
        
        
        #Adding Functions as Actions
        file_menu.addAction(open_toolbar)
        file_menu.addAction(save_toolbar)
        file_menu.addAction(exit_button)
        
        edit_menu.addAction(cut_button)
        edit_menu.addAction(copy_button)
        edit_menu.addAction(paste_button)
        #edit_menu.addAction(searchAction)
        
        format_menu.addMenu(text_format)
        format_menu.addMenu(align_indent)
        format_menu.addMenu(bullet_number)
        
        text_format.addAction(bold_format)
        text_format.addAction(italics_format)
        text_format.addAction(underline_format)
        
        align_indent.addAction(left_just)
        align_indent.addAction(center_just)
        align_indent.addAction(right_just)
        
        align_indent.addSeparator()
        
        align_indent.addAction(self.indent)
        align_indent.addAction(self.dedent)
        
        
        bullet_number.addAction(addbullets)
        bullet_number.addMenu(bullet_style)
        
        bullet_style.addAction(disc)
        bullet_style.addAction(circle)
        bullet_style.addAction(square)
        bullet_style.addAction(decimal)
        bullet_style.addAction(la)
        bullet_style.addAction(ua)
        bullet_style.addAction(lr)
        bullet_style.addAction(ur)
        
        search_menu.addAction(searchAction)
        #format_menu.addAction

        
        #reminder_menu.addAction(add_reminder_button)
             


    #Used for Unit Testing
    def returncurrenttextbox(self):
        box = noteindex[self.tabs.currentIndex()]
        return box.textbox
        
        
    def show_Saved(self):
        self.statusBar().showMessage('Saved')
        
    #Open File Function    
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "HTML documents (*.html);;Text documents (*.txt);;All files (*.*)")
        
        try:
            with open(path, 'rU') as file:
                text = file.read()
        except Exception:
            return
            
        else:
            openedtab = self.newtab()
            self.path = path
            openedtab.textbox.setText(text)
            
            for i in range(len(path) - 1, -1, -1):
                if path[i] == '/':
                    startindex = i + 1
                    break
            name = path[startindex:len(path)]
            self.tabs.setTabText(self.tabs.count() - 1, name)
      #  name = QFileDialog.getOpenFileName(self, 'Open File')   #Opening File Dialog
        
       # if name[0] != '':
            
        #    file = open(name[0], 'r')                               #Opening and Reading File
        
            #Setting Opened File as New Widget
         #   openedtab = self.newtab()
            #self.central_Widget = Note_Widget()                     #Reassigning Central Widget Variable to New Widget
            #self.setCentralWidget(self.central_Widget)
          #  with file:
           #     text = file.read()
            #    openedtab.textbox.setText(text) #Putting Text from File in New Widget Textbox
           # self.tabs.setTabText(self.tabs.count() - 1, name[0])

    #Save File Function 
    def save_file(self):
       if self.path is None:
           self.save_file_as()
           return
       text = noteindex[self.tabs.currentIndex()].textbox.toHtml()
       
       try:
           with open(self.path, 'w') as file:
               file.write(text)
       except Exception:
            return
       
       
       
       
       
       option=QFileDialog.Options()
        
        #Opening Save File Dialog
       # namee = QFileDialog.getSaveFileName(self, 'Save File', "untitled", "All Files (*)", options=option)
        
       # if namee[0] != '':
       #     file = open(namee[0], 'w')                              #Creating and Writing to New File
       #     text = noteindex[self.tabs.currentIndex()].textbox.toHtml()        #Retrieving Text From Widget
       #     file.write(text)                                        #Writing to File  
       #     self.statusBar().showMessage('Saved')
       #     self.tabs.setTabText(self.tabs.currentIndex(), namee[0]) 
           # self.setWindowTitle(namee[0])               
       #     file.close()
    def save_file_as(self):
        option=QFileDialog.Options()
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "HTML documents (*.html);; Text documents (*.txt);; All files (*.*)", options=option)
        
        if not path:
            return
        text = noteindex[self.tabs.currentIndex()].textbox.toHtml() 
        
        try:
            with open(path, 'w') as file:
                file.write(text)
        except Exception:
            return
        
        else:
            self.path = path
            
            for i in range(len(path) - 1, -1, -1):
                if path[i] == '/':
                    startindex = i + 1
                    break
            name = path[startindex:len(path)]
            self.tabs.setTabText(self.tabs.currentIndex(), name)
            
    def cut(self): 
        noteindex[self.tabs.currentIndex()].cut_text()
        self.statusBar().showMessage('Cut')   
        
    def copy(self): 
        noteindex[self.tabs.currentIndex()].copy_text()
    
    def copiedmessage(self):
        self.statusBar().showMessage('Copied') 
        
    def paste(self):
        noteindex[self.tabs.currentIndex()].paste_text()
        self.statusBar().showMessage('Pasted') 
    
    def cremind(self):
        calendar = CWindow(self)
        calendar.show()
        
    def color_selection(self):
        noteindex[self.tabs.currentIndex()].setcolor()
        
        
    def changecolor(self): 
        textcolor = self.combo.currentText()
        
        if textcolor == "Red":
            redcolor = QColor(255, 0, 0)
            noteindex[self.tabs.currentIndex()].textbox.setTextColor(redcolor)
        elif textcolor == "Green":
            greencolor = QColor(0, 255, 0)
            noteindex[self.tabs.currentIndex()].textbox.setTextColor(greencolor)
        elif textcolor == "Blue":
            bluecolor = QColor(0, 0, 255)
            noteindex[self.tabs.currentIndex()].textbox.setTextColor(bluecolor)
        elif textcolor == "Black":
            blackcolor = QColor(0, 0, 0)
            noteindex[self.tabs.currentIndex()].setTextColor(blackcolor)
        elif textcolor == "Purple":
            purplecolor = QColor(102, 0, 204)
            noteindex[self.tabs.currentIndex()].setTextColor(purplecolor)
        #print("Something Something") 
    
    def newtab(self):
        #if self.tabs.currentIndex() == self.tabs.count() - 1:
          # current_location = self.tabs.count()
           self.NewTab = QWidget()
          # print("HOWDY")
           # new_tab_location = self.tabs.insertTab(current_location,self.NewTab,"New Note")
           
           self.NewTab.layout = QVBoxLayout()
           noteindex[self.tabs.count()] = Note_Widget()
           self.NewTab.layout.addWidget(noteindex[self.tabs.count()])
           self.NewTab.setLayout(self.NewTab.layout)
           self.tabs.addTab(self.NewTab, 'New Note')
           self.tabs.setCurrentIndex(self.tabs.count() - 1)
           return noteindex[self.tabs.count() - 1]
    
           # self.tabs.tabBar().moveTab(new_tab_location, current_location)
           # print(current_location)
           # print(new_tab_location)
            #Add new tab funtionality goes here
    
    def closetab(self, indeX):
        if indeX == 0 and self.tabs.count() == 1:
            self.close()
        notewidgetbeingdeleted =  noteindex[indeX]
        del notewidgetbeingdeleted
        for key in range(indeX + 1, len(noteindex.keys()), 1):
           # print("Deleted index" , indeX)
           #print("Current key is " , key , " out of " , len(noteindex.keys()))
           # if int(key) > indexofdeleted:
            tempwid = noteindex[key]
            noteindex[key - 1] = tempwid
        del noteindex[len(noteindex.keys()) - 1]
        self.tabs.removeTab(indeX)
        
        
               # noteindex[newkey] = tempwid
        

    def tabtest(self):
        print(self.tabs.count())
        print(self.tabs.currentIndex())
        
    def left(self):
       
       # note = self.tab1.layout.children().textbox.setAlignment(Qt.AlignLeft)
        notew = noteindex[self.tabs.currentIndex()]
        notew.textbox.setAlignment(Qt.AlignLeft)
        
    def right(self):
       
       # note = self.tab1.layout.children().textbox.setAlignment(Qt.AlignLeft)
        notew = noteindex[self.tabs.currentIndex()]
        notew.textbox.setAlignment(Qt.AlignRight)
        #textbox.setAlignment(Qt.AlignLeft)
        
    def center(self):
       
       # note = self.tab1.layout.children().textbox.setAlignment(Qt.AlignLeft)
        notew = noteindex[self.tabs.currentIndex()]
        notew.textbox.setAlignment(Qt.AlignCenter)
    
    def bulletstate(self):
        if self.makebullets.isChecked():
            
            noteindex[self.tabs.currentIndex()].createbullet(self.bulletstyle)
        else:
            noteindex[self.tabs.currentIndex()].removebullet()
    
    def italicsstate(self):
        if self.italics.isChecked():
            noteindex[self.tabs.currentIndex()].makeitalics()
        else:
            noteindex[self.tabs.currentIndex()].undoitalics()
    
    def boldstate(self):
        if self.bold.isChecked():
            noteindex[self.tabs.currentIndex()].makebold()
        else:
            noteindex[self.tabs.currentIndex()].undobold()
            
    def underlinestate(self):
        if self.underline.isChecked():
            noteindex[self.tabs.currentIndex()].makeunderline()
        else:
            noteindex[self.tabs.currentIndex()].undounderline()
                 
    def boldmenu(self):
        noteindex[self.tabs.currentIndex()].bold()
    
    def italicsmenu(self):
        noteindex[self.tabs.currentIndex()].italics()
        
    def underlinemenu(self):
        noteindex[self.tabs.currentIndex()].underline()
    
    def bulletmenu(self):
        noteindex[self.tabs.currentIndex()].createbullet(self.bulletstyle)
    
    def changedisc(self):
        self.bulletstyle = QTextListFormat().ListDisc
        
    def changedcircle(self):
        self.bulletstyle = QTextListFormat().ListCircle
        
    def changedsquare(self):
        self.bulletstyle = QTextListFormat().ListSquare
        
    def changeddecimal(self):
        self.bulletstyle = QTextListFormat().ListDecimal
        
    def changedlowlatin(self):
        self.bulletstyle = QTextListFormat().ListLowerAlpha
        
    def changedhighlatin(self):
        self.bulletstyle = QTextListFormat().ListUpperAlpha
        
    def changedlowroman(self):
        self.bulletstyle = QTextListFormat().ListLowerRoman
        
    def changedhighroman(self):
        self.bulletstyle = QTextListFormat().ListUpperRoman
    
    def fontselection(self, font):
        noteindex[self.tabs.currentIndex()].setfont(font)
        self.size()
    
    
    
            
    def size(self):
       inputsize = self.fontSize.currentText()
       try:
           float(inputsize)
       except ValueError:
           return
       noteindex[self.tabs.currentIndex()].setfontsize(inputsize)
       
    def callindent(self):
        noteindex[self.tabs.currentIndex()].indent()
        
    def calldedent(self):
        noteindex[self.tabs.currentIndex()].undoindent()
    
    def Search(self, *args):
        global f
        	
        search = Search(self)
        search.show()

        def handle_search():

            f = search.text.toPlainText()
            print(f)
            noteindex[self.tabs.currentIndex()].textbox.find(f)

            
        search.button.clicked.connect(handle_search)

