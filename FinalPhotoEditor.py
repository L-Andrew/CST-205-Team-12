#!/usr/bin/python

#!/usr/bin/python
from PIL import Image
import math
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit,QPushButton,QVBoxLayout, QFileDialog,QComboBox,QLabel,QHBoxLayout, QSlider,QScrollArea, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot

NumofImages = [
'Pick A Number of images to put in collages',
'1 Image',
'2 Images',
]
eff = ["Mirror (left-right)", "Mirror(up-down)", "Rotate", "Red Filter", "Green Filter", "Blue Filter", "Gray Scale", "Reset Changes"]

#*****************************MAIN MENU****************************
class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'PyQt5 file dialogs - pythonspot.com'
		self.mainmenu()

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
		self.btn.clicked.connect(self.open_win)

	def open_win(self):
		i = self.combo.currentIndex()
		if i==1:
			self.newWindow = windowOne()
		if i==2:
			self.newWindowTwo = windowTwo()
#*******************************************************************

#*****************************ONE IMAGE****************************
class windowOne(QWidget):
	def __init__(self):
		super().__init__()
		self.openFileNameDialog()
		layout = QVBoxLayout()
		self.effects = []


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

		self.scroll = QScrollArea()
		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.scroll.setWidgetResizable(False)
		self.scroll.setWidget(self.buttons)
		self.scroll.setFixedWidth(150)

		self.imgLabel = QLabel()
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

	def changeEffect(self, x):
		for i in range(len(self.effects)):
			click = 0
			if i != x:
				self.effects[i].setChecked(False)
			else:
				self.effects[i].setChecked(True)
		if (x == 0):
			self.img1 = Image.open(self.copyfilename).convert("RGB")
			self.mirrorH(self.img1)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 1):
			self.img1 = Image.open(self.copyfilename).convert("RGB")
			self.mirrorV(self.img1)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 2):
			self.img1 = Image.open(self.copyfilename).convert("RGB")
			self.rotate(self.img1, 90)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 3):
			self.img1 = Image.open(self.copyfilename).convert("RGB")
			self.filterR(self.img1,1.5)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 4):
			self.img1 = Image.open(self.copyfilename).convert("RGB")
			self.filterG(self.img1,1.5)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 5):
			self.img1 = Image.open(self.copyfilename).convert("RGB")
			self.filterB(self.img1,1.5)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 6):
			self.img1 = Image.open(self.copyfilename).convert("RGB")
			self.filterGrayscale(self.img1)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 7):
			self.img1 = Image.open(self.fileName).convert("RGB")
			self.restart(self.img1)
			self.copyfilename = "ImageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)


	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if self.fileName:
			self.copyfilename = self.fileName
			print(self.fileName)

	#   mirror horizontally - Andrew
	def mirrorH(self,source):
		self.new_img = source.copy()
		self.new_img = self.new_img.transpose(Image.FLIP_LEFT_RIGHT)
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   mirror vertically - Andrew
	def mirrorV(self,source):
		self.new_img = source.copy()
		self.new_img = self.new_img.transpose(Image.FLIP_TOP_BOTTOM)
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   rotate by degrees degrees - Andrew
	def rotate(self,source, degrees):
		self.new_img = source.rotate(degrees, expand = True)
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   multiply blue value by percent. 1 being 100% - Andrew
	def filterB(self,source, percent):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				b = int(b * percent)
				self.new_img.putpixel((x,y), (r, g, b))
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   multiply green value by percent. 1 being 100% - Andrew
	def filterG(self,source, percent):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				g = int(g * percent)
				self.new_img.putpixel((x,y), (r, g, b))
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   multiply red value by percent. 1 being 100% - Andrew
	def filterR(self,source, percent):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				r = int(r * percent)
				self.new_img.putpixel((x,y), (r, g, b))
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    # greyscale image - Andrew
	def filterGrayscale(self,source):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				avg = int((r + g + b) / 3)
				self.new_img.putpixel((x,y), (avg, avg, avg))
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
	def restart(self, source):
		self.new_img = source.copy()
		self.new_img.save("ImageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
#***************************************************************************************

#*****************************TWO IMAGES****************************
class windowTwo(QWidget):
	def __init__(self):
		super().__init__()
		self.openFileNameDialog()
		self.img1 = Image.open(self.fileNameOne)
		self.img2 = Image.open(self.fileNameTwo)
		self.collageH(self.img1,self.img2)
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
		#self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(False)
		self.scroll.setWidget(self.buttons)
		self.scroll.setFixedWidth(150)
		#self.scroll.setFixedSize(150, 300)

		self.imgLabel = QLabel()
		pixmap = QPixmap(baseImg)
		self.imgLabel.setPixmap(pixmap)
		#self.imgLabel.resize(pixmap.width(),pixmap.height())

		VLayout = QVBoxLayout()
#		self.slider = QSlider(Qt.Horizontal)
#		self.slider.setFixedWidth(100)
		self.savebtn = QPushButton('Save')

		VLayout.addWidget(self.imgLabel)
#		VLayout.addWidget(self.slider)
		VLayout.addWidget(self.savebtn)

		self.left = QWidget()
		self.left.setLayout(VLayout)

		lay = QHBoxLayout()
		lay.addWidget(self.scroll)
		lay.addWidget(self.left)
		self.setLayout(lay)
		#self.setFixedSize(350, 320)
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
		if (x == 0):
			self.img1 = Image.open(self.copyfilename2).convert("RGB")
			self.mirrorH(self.img1)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 1):
			self.img1 = Image.open(self.copyfilename2).convert("RGB")
			self.mirrorV(self.img1)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 2):
			self.img1 = Image.open(self.copyfilename2).convert("RGB")
			self.rotate(self.img1, 90)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 3):
			self.img1 = Image.open(self.copyfilename2).convert("RGB")
			self.filterR(self.img1,1.5)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 4):
			self.img1 = Image.open(self.copyfilename2).convert("RGB")
			self.filterG(self.img1,1.5)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 5):
			self.img1 = Image.open(self.copyfilename2).convert("RGB")
			self.filterB(self.img1,1.5)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 6):
			self.img1 = Image.open(self.copyfilename2).convert("RGB")
			self.filterGrayscale(self.img1)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)
		if (x == 7):
			self.img1 = Image.open(self.copyfilename3).convert("RGB")
			self.restart(self.img1)
			self.copyfilename = "collageCopy.png"
			self.baseImg = self.copyfilename
			self.pixmap = QPixmap(self.baseImg)
			self.imgLabel.setPixmap(self.pixmap)


	#_________________________________________________________________
	#-------- THIS CODE GETS THE FILES FROM COMPUTER ---------#
	def openFileNameDialog(self):
		optionsOne = QFileDialog.Options()
		optionsOne |= QFileDialog.DontUseNativeDialog
		self.fileNameOne, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=optionsOne)
		if self.fileNameOne:
			print(self.fileNameOne)
		optionsTwo = QFileDialog.Options()
		optionsTwo |= QFileDialog.DontUseNativeDialog
		self.fileNameTwo, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=optionsTwo)
		if self.fileNameTwo:
			print(self.fileNameTwo)

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
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		self.copyfilename3 = "collage.png"
		self.copyfilename2 = "collageCopy.png"


    #   mirror horizontally - Andrew
	def mirrorH(self,source):
		self.new_img = source.copy()
		self.new_img = self.new_img.transpose(Image.FLIP_LEFT_RIGHT)
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   mirror vertically - Andrew
	def mirrorV(self,source):
		self.new_img = source.copy()
		self.new_img = self.new_img.transpose(Image.FLIP_TOP_BOTTOM)
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   rotate by degrees degrees - Andrew
	def rotate(self,source, degrees):
		self.new_img = source.rotate(degrees, expand = True)
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   multiply blue value by percent. 1 being 100% - Andrew
	def filterB(self,source, percent):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				b = int(b * percent)
				self.new_img.putpixel((x,y), (r, g, b))
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   multiply green value by percent. 1 being 100% - Andrew
	def filterG(self,source, percent):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				g = int(g * percent)
				self.new_img.putpixel((x,y), (r, g, b))
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    #   multiply red value by percent. 1 being 100% - Andrew
	def filterR(self,source, percent):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				r = int(r * percent)
				self.new_img.putpixel((x,y), (r, g, b))
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
    # greyscale image - Andrew
	def filterGrayscale(self,source):
		self.new_img = source.copy()
		for x in range(source.width):
			for y in range(source.height):
				r, g, b = source.getpixel((x, y))
				avg = int((r + g + b) / 3)
				self.new_img.putpixel((x,y), (avg, avg, avg))
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG
		return self.new_img
	def restart(self, source):
		self.new_img = source.copy()
		self.new_img.save("collageCopy.png") # MAKES NEW IMAGE CALLED COLLAGE.PNG

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
