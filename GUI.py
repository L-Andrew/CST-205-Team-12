# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSlider, QPushButton, QScrollArea, QLabel

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        eff = ["Effect 1", "Effect 2", "Effect 3", "Effect 4", "Effect 5", "Effect 6", "Effect 7", "Effect 8", "Effect 9"]
        layout = QVBoxLayout()
        self.effects = []
        
        baseImg = "PUT YOUR IMAGE HERE"
        
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
        self.effects[8].clicked.connect(lambda: self.changeEffect(8))
        
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
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFixedWidth(100)
        VLayout.addWidget(self.imgLabel)
        VLayout.addWidget(self.slider)
        VLayout.setAlignment(Qt.AlignCenter)
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
        
    @pyqtSlot() 
    def changeEffect(self, x):
        for i in range(len(self.effects)):
            if i != x:
                self.effects[i].setChecked(False)
            else:
                self.effects[i].setChecked(True)
        
app = QApplication(sys.argv)
ex = GUI()
ex.show()
sys.exit(app.exec_())

"""
self.slider = QSlider(Qt.Horizontal)
self.scroll = QScrollBar()
layout.addWidget(self.slider)
layout.addWidget(self.scroll)
"""