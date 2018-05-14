'''
    Authors: Armando Miguel, Antonin Chantier, and Andrew Lin.
    Course: CST-205
    Title: CST-205 Final Project
    Date: May 14, 2018
    GitHub Link: https://github.com/L-Andrew/CST-205-Team-12.git
    
    ***TO RUN CODE, PUT FILE IN VIRTUAL ENVIRONMENT***
    
    Abstract:
    The purpose of this project was to create a photo editor, that allows user to customize any image they want and save it as a copy.
    The way that this happen is when the user runs the code, a prompt will appear asking the user if they want to make a collage of 2 images
    and edit it or no collage and just edit one image. Based off the user input, a window will open and ask the user to pick the image(s). After picking the
    image(s), a new window will appear with different buttons which will edit the image. The buttons included would be Mirror (left-right),
    Mirror(up-down), Rotate, Red Filter, Green Filter, Blue Filter, and Gray Scale. These button will add changes to the image and display what
    it would look like to the side. There is also a Reset change button that will allow the user to restart their changes all over again. After clicking
    the save button the image will be saved inside the virtual enrviroment folder as a copy under the name "ImageCopy.png".
    '''



# ***Source (Works Cited) for pillow features: https://pillow.readthedocs.io/en/5.1.x/ ***
#Imports
from PIL import Image
import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit,QPushButton,QVBoxLayout, QFileDialog,QComboBox,QLabel,QHBoxLayout, QSlider,QScrollArea, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot


#List of Collage Options (Armando)
NumofImages = ['Pick A Number of images to put in collages','1 Image','2 Images',]
#List of all effects (Antonin)
eff = ["Mirror (left-right)", "Mirror(up-down)", "Rotate", "Red Filter", "Green Filter", "Blue Filter", "Gray Scale", "Reset Changes"]


#*****************************MAIN MENU****************************
#App Class (Armando Miguel)
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.mainmenu() #calls "def mainmenu"
    
    #Creates a window that asks user if they want to make a collage of 1 or 2 images
    def mainmenu(self):
        self.combo = QComboBox()
        self.combo.addItems(NumofImages)
        
        self.btn = QPushButton('Enter')
        vbox = QVBoxLayout()
        vbox.addWidget(self.combo)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)
        self.resize(200,150)
        self.show()
        self.btn.clicked.connect(self.open_win)#calls "def open_win"
    
    def open_win(self):
        i = self.combo.currentIndex()
        if i==1:
            #If user selects "1 image" class "WindowOne" will be called
            self.newWindow = windowOne()
        if i==2:
            #If user selects "2 image" class "WindowTwo" will be called
            self.newWindowTwo = windowTwo()
#*******************************************************************


#*****************************ONE IMAGE****************************
#Class Created by Armando but implimentations create by all three of us.
class windowOne(QWidget):
    def __init__(self):
        super().__init__()
        self.openFileNameDialog()#calls "def openFileNameDialog"
        
        layout = QVBoxLayout()
        self.effects = []
        
        #Create a window with all the button, bind the buttons to the effects(Antonin)
        self.baseImg = self.fileName
        
        for i in range(len(eff)):
            self.effects.append(QPushButton(eff[i]))
            self.effects[i].setCheckable(True)
    
        self.effects[0].clicked.connect(lambda: self.changeEffect(0))
        self.effects[1].clicked.connect(lambda: self.changeEffect(1))
        self.effects[2].clicked.connect(lambda: self.changeEffect(2))
        self.effects[3].clicked.connect(lambda: self.changeEffect(3))
        self.effects[4].clicked.connect(lambda: self.changeEffect(4))
        self.effects[5].clicked.connect(lambda: self.changeEffect(5))
        self.effects[6].clicked.connect(lambda: self.changeEffect(6))
        self.effects[7].clicked.connect(lambda: self.changeEffect(7))
        
        for i in range(len(eff)):
            layout.addWidget(self.effects[i])


self.buttons = QWidget()
self.buttons.setLayout(layout)

#Make the effects scrollable and show the image on the window (Antonin)
self.scroll = QScrollArea()
    self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.scroll.setWidgetResizable(False)
    self.scroll.setWidget(self.buttons)
    self.scroll.setFixedWidth(150)
    
    self.imgLabel = QLabel() #gets the image and displays it on the window
        self.pixmap = QPixmap(self.baseImg)
        self.imgLabel.setPixmap(self.pixmap)
        self.pix = self.pixmap.copy()
        
        VLayout = QVBoxLayout()
        self.savebtn = QPushButton('Save')
        
        VLayout.addWidget(self.imgLabel)
        VLayout.addWidget(self.savebtn)
        
        self.left = QWidget()
        self.left.setLayout(VLayout)
        
        lay = QHBoxLayout()
        lay.addWidget(self.scroll)
        lay.addWidget(self.left)
        self.setLayout(lay)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.setWindowTitle("GUI")
        self.show()

    @pyqtSlot()
    #Called when a button is pressed (Antonin)
def changeEffect(self, x):
    for i in range(len(self.effects)):
        click = 0
            if i != x:
                self.effects[i].setChecked(False)
        else:
            self.effects[i].setChecked(True)
        #Depending on which button is clicked, it will edit the image or apply a filter (Armando)
        if (x == 0):
            self.img1 = Image.open(self.copyfilename).convert("RGB")
            self.mirrorH(self.img1) #calls "def mirrorH" and takes in the image chosen.
            self.copyfilename = "ImageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen (Armando).
            self.imgLabel.setPixmap(self.pixmap)
if (x == 1):
    self.img1 = Image.open(self.copyfilename).convert("RGB")
    self.mirrorV(self.img1)#calls "def mirrorV" and takes in the image chosen.
    self.copyfilename = "ImageCopy.png"
        self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen (Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 2):
            self.img1 = Image.open(self.copyfilename).convert("RGB")
            self.rotate(self.img1, 90)#calls "def rotate" which will take in the image chosen and rotate it 90 degrees.
            self.copyfilename = "ImageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
    if (x == 3):
        self.img1 = Image.open(self.copyfilename).convert("RGB")
        self.filterR(self.img1,1.5)#calls "def filterR" which will take in the image chosen and the percent of image filter.
        self.copyfilename = "ImageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 4):
            self.img1 = Image.open(self.copyfilename).convert("RGB")
            self.filterG(self.img1,1.5)#calls "def filterG" which will take in the image chosen and the percent of image filter.
            self.copyfilename = "ImageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 5):
            self.img1 = Image.open(self.copyfilename).convert("RGB")
            self.filterB(self.img1,1.5)#calls "def filterB" which will take in the image chosen and the percent of image filter.
            self.copyfilename = "ImageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 6):
            self.img1 = Image.open(self.copyfilename).convert("RGB")
            self.filterGrayscale(self.img1)#calls "def filterR" which will take in the image chosen and gray scale it.
            self.copyfilename = "ImageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
if (x == 7):
    self.img1 = Image.open(self.fileName).convert("RGB")
    self.restart(self.img1)#calls "def restart" which will take in the image chosen and gray scale it.
    self.copyfilename = "ImageCopy.png"
        self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)

#*** Source (Works cited): https://pythonspot.com/pyqt5-file-dialog/ ***
'''This function will open up the file inside of the users computer system kind of like a finder and will allow the user to pick an image
    from their files in their computer to edit. After clicking the image, the image pathway gets save to a variable as well as a to another
    varable which would be the copy of the image.'''
        #Created by (Armando)
        def openFileNameDialog(self):
        options = QFileDialog.Options()#Opens up the computers file
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)#Allows user to pick an image file and sets it as "filename"
        if self.fileName:
            self.copyfilename = self.fileName #creates the image copy and sets it as "copyfilename"
            print(self.fileName) #prints the pathway

#   mirror horizontally - Andrew
def mirrorH(self,source):
    self.new_img = source.copy()
    self.new_img = self.new_img.transpose(Image.FLIP_LEFT_RIGHT)
    self.new_img.save("ImageCopy.png") #saves the copy image (ImageCopy.png) to the filter in addition to other change if applied(Armando).
    return self.new_img
    #   mirror vertically - Andrew
    def mirrorV(self,source):
        self.new_img = source.copy()
        self.new_img = self.new_img.transpose(Image.FLIP_TOP_BOTTOM)
        self.new_img.save("ImageCopy.png") #saves the copy image (ImageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #   rotate by degrees degrees - Andrew
    def rotate(self,source, degrees):
        self.new_img = source.rotate(degrees, expand = True)
        self.new_img.save("ImageCopy.png") #saves the copy image (ImageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #   multiply blue value by percent. 1 being 100% - Andrew
    def filterB(self,source, percent):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                b = int(b * percent)
                self.new_img.putpixel((x,y), (r, g, b))
        self.new_img.save("ImageCopy.png") #saves the copy image (ImageCopy.png) to the filter in addition to other change if applied(Armando)
        return self.new_img
    #   multiply green value by percent. 1 being 100% - Andrew
    def filterG(self,source, percent):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                g = int(g * percent)
                self.new_img.putpixel((x,y), (r, g, b))
        self.new_img.save("ImageCopy.png") #saves the copy image (ImageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #   multiply red value by percent. 1 being 100% - Andrew
    def filterR(self,source, percent):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                r = int(r * percent)
                self.new_img.putpixel((x,y), (r, g, b))
        self.new_img.save("ImageCopy.png")#saves the copy image (ImageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    # greyscale image - Andrew
    def filterGrayscale(self,source):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                avg = int((r + g + b) / 3)
                self.new_img.putpixel((x,y), (avg, avg, avg))
        self.new_img.save("ImageCopy.png") #saves the copy image (ImageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #resets the image copy to the orginal image and then displays it on the window (Armando)
    def restart(self, source):
        self.new_img = source.copy()
        self.new_img.save("ImageCopy.png") #saves the copy image (ImageCopy.png) to the original image(Armando).
#***************************************************************************************

#*****************************TWO IMAGES****************************

#Same creation of the window with the buttons (Antonin)
#Class Created by Armando but implimentations create by all three of us.
class windowTwo(QWidget):
    def __init__(self):
        super().__init__()
        self.openFileNameDialog() #calls "def openFileNameDialog"
        self.img1 = Image.open(self.fileNameOne) #set the first image chosen from "def openFileNameDialog" to variable
        self.img2 = Image.open(self.fileNameTwo) #set the second image chosen from "def openFileNameDialog" to variable
        self.collageH(self.img1,self.img2) #calls "def collageH" and takes in two images (img1 and img2) to create a collage
        
        layout = QVBoxLayout()
        self.effects = []
        
        baseImg = "collage.png"
        
        for i in range(len(eff)):
            self.effects.append(QPushButton(eff[i]))
            self.effects[i].setCheckable(True)
    
        self.effects[0].setChecked(True)
        self.effects[0].clicked.connect(lambda: self.changeEffect(0))
        self.effects[1].clicked.connect(lambda: self.changeEffect(1))
        self.effects[2].clicked.connect(lambda: self.changeEffect(2))
        self.effects[3].clicked.connect(lambda: self.changeEffect(3))
        self.effects[4].clicked.connect(lambda: self.changeEffect(4))
        self.effects[5].clicked.connect(lambda: self.changeEffect(5))
        self.effects[6].clicked.connect(lambda: self.changeEffect(6))
        self.effects[7].clicked.connect(lambda: self.changeEffect(7))
        
        for i in range(len(eff)):
            layout.addWidget(self.effects[i])

self.buttons = QWidget()
self.buttons.setLayout(layout)

self.scroll = QScrollArea()
self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
self.scroll.setWidgetResizable(False)
self.scroll.setWidget(self.buttons)
self.scroll.setFixedWidth(150)

self.imgLabel = QLabel()#gets the image and displays it on the window
pixmap = QPixmap(baseImg)
self.imgLabel.setPixmap(pixmap)

VLayout = QVBoxLayout()
self.savebtn = QPushButton('Save')

VLayout.addWidget(self.imgLabel)
VLayout.addWidget(self.savebtn)

self.left = QWidget()
self.left.setLayout(VLayout)

lay = QHBoxLayout()
lay.addWidget(self.scroll)
lay.addWidget(self.left)
self.setLayout(lay)
self.setAutoFillBackground(True)
p = self.palette()
p.setColor(self.backgroundRole(), Qt.black)
self.setPalette(p)
self.setWindowTitle("GUI")
self.show()

@pyqtSlot()
def changeEffect(self, x):
    for i in range(len(self.effects)):
        if i != x:
            self.effects[i].setChecked(False)
            else:
                self.effects[i].setChecked(True)
    #Depending on which button is clicked, it will edit the image or apply a filter (Armando)
    if (x == 0):
        self.img1 = Image.open(self.copyfilename2).convert("RGB")
        self.mirrorH(self.img1)#calls "def mirrorV" and takes in the image chosen.
        self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen (Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 1):
            self.img1 = Image.open(self.copyfilename2).convert("RGB")
            self.mirrorV(self.img1)#calls "def mirrorV" and takes in the image chosen.
            self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen (Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 2):
            self.img1 = Image.open(self.copyfilename2).convert("RGB")
            self.rotate(self.img1, 90)#calls "def rotate" which will take in the image chosen and rotate it 90 degrees.
            self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 3):
            self.img1 = Image.open(self.copyfilename2).convert("RGB")
            self.filterR(self.img1,1.5)#calls "def filterR" which will take in the image chosen and the percent of image filter.
            self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
    if (x == 4):
        self.img1 = Image.open(self.copyfilename2).convert("RGB")
        self.filterG(self.img1,1.5)#calls "def filterG" which will take in the image chosen and the percent of image filter.
        self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 5):
            self.img1 = Image.open(self.copyfilename2).convert("RGB")
            self.filterB(self.img1,1.5)#calls "def filterB" which will take in the image chosen and the percent of image filter.
            self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 6):
            self.img1 = Image.open(self.copyfilename2).convert("RGB")
            self.filterGrayscale(self.img1)#calls "def filterR" which will take in the image chosen and gray scale it.
            self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)
        if (x == 7):
            self.img1 = Image.open(self.copyfilename3).convert("RGB")
            self.restart(self.img1)#calls "def restart" which will take in the image chosen and gray scale it.
            self.copyfilename = "collageCopy.png"
            self.baseImg = self.copyfilename
            self.pixmap = QPixmap(self.baseImg)#get the image copy with the filter and displays it on the windown screen(Armando).
            self.imgLabel.setPixmap(self.pixmap)


#*** Source (Works cited): https://pythonspot.com/pyqt5-file-dialog/ ***
'''This function will open up the file inside of the users computer system kind of like a finder and will allow the user to pick an image
    from their files in their computer to edit. The differnce in this code is that 2 images are going to be picked, the file will open up once
    let the user pick an image and will open up the file again allowing the user to pick another image. After selecting the image the collage function
    will be called and combine both images together into 1.'''
        #Created by (Armando)
        def openFileNameDialog(self):
        optionsOne = QFileDialog.Options()#Opens up the computers file
        optionsOne |= QFileDialog.DontUseNativeDialog
        self.fileNameOne, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=optionsOne)#Allows user to pick an image file and sets it as "fileNameOne"
        if self.fileNameOne:
            print(self.fileNameOne)#prints the pathway
optionsTwo = QFileDialog.Options()
optionsTwo |= QFileDialog.DontUseNativeDialog
    self.fileNameTwo, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=optionsTwo)#Allows user to pick another image file and sets it as "fileNameTwo"
    if self.fileNameTwo:
        print(self.fileNameTwo)#prints the pathway
    
    #--------RESIZES THE IMAGES TO PUT IN COLLAGE --------#
    def resizeImg(self,source, percent):
        size = (int(percent * source.width), int(percent * source.height))
        new_img = Image.new("RGB", size)
        for x in range(size[0]):
            for y in range(size[1]):
                new_img.putpixel((x, y), source.getpixel((int(x / percent), int(y / percent))))
        return new_img
    #-------- CREATES THE COLLAGE --------#
    def collageH(self,source, *sourceList):
        totalX = 0
        sList = list(sourceList)
        for i, img in enumerate(sList):
            if (img.height != source.height):
                img = self.resizeImg(img, source.height/img.height) # CALLS RESIZE
                sList[i] = img
            totalX = totalX + img.width
        self.new_img = Image.new("RGB", (source.width + totalX, source.height))
        for x in range(source.width):
            for y in range(source.height):
                self.new_img.putpixel((x, y), source.getpixel((x, y)))
        offsetX = source.width
        for img in sList:
            for x in range(img.width):
                for y in range(img.height):
                    self.new_img.putpixel((offsetX + x, y), img.getpixel((x, y)))
            offsetX = offsetX + img.width
        self.new_img.save("collage.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
        self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED collageCopy.PNG
        self.copyfilename3 = "collage.png"# this variable stores the orginal image
        self.copyfilename2 = "collageCopy.png"# this variable stores the copy of the images
    
    
    #   mirror horizontally - Andrew
    def mirrorH(self,source):
        self.new_img = source.copy()
        self.new_img = self.new_img.transpose(Image.FLIP_LEFT_RIGHT)
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to the filter in addition to other change if applied (Armando).
        return self.new_img
    #   mirror vertically - Andrew
    def mirrorV(self,source):
        self.new_img = source.copy()
        self.new_img = self.new_img.transpose(Image.FLIP_TOP_BOTTOM)
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #   rotate by degrees degrees - Andrew
    def rotate(self,source, degrees):
        self.new_img = source.rotate(degrees, expand = True)
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #   multiply blue value by percent. 1 being 100% - Andrew
    def filterB(self,source, percent):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                b = int(b * percent)
                self.new_img.putpixel((x,y), (r, g, b))
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #   multiply green value by percent. 1 being 100% - Andrew
    def filterG(self,source, percent):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                g = int(g * percent)
                self.new_img.putpixel((x,y), (r, g, b))
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    #   multiply red value by percent. 1 being 100% - Andrew
    def filterR(self,source, percent):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                r = int(r * percent)
                self.new_img.putpixel((x,y), (r, g, b))
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    # greyscale image - Andrew
    def filterGrayscale(self,source):
        self.new_img = source.copy()
        for x in range(source.width):
            for y in range(source.height):
                r, g, b = source.getpixel((x, y))
                avg = int((r + g + b) / 3)
                self.new_img.putpixel((x,y), (avg, avg, avg))
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to the filter in addition to other change if applied(Armando).
        return self.new_img
    
    #resets the image copy to the orginal image and then displays it on the window (Armando)
    def restart(self, source):
        self.new_img = source.copy()
        self.new_img.save("collageCopy.png") #saves the copy image (collageCopy.png) to original image(Armando).

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
