# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacejdnWkN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import time
import os
import datetime
import sys
import pytesseract
from PIL import Image
import cv2
import numpy as np
from pdf2image import convert_from_path
import tabula

import pandas as pd

import sqlite3
import requests


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget

import QSS_Resources_rc

class Ui_MainWindow(object):
    
    ch_fac = 0
    ch = 0
    ch_title = 0

    UP = []
    KPVR = []
    OP = []
    AnnRPOP = []
    RPD = []
    RPV = []
    PP = []
    MiD = []

    UPn = []
    KPVRn = []
    OPn = []
    AnnRPOPn = []
    RPDn = []
    RPVn = []
    PPn = []
    MiDn = []


    title = []


    def addTitle(self):
        bd_name = "OTHENASHKOTORYNANEBESAH.db"
        bd = os.path.join("resources", bd_name )
        conn = sqlite3.connect(bd)
        cursor = conn.cursor() 
        cursor.execute(f'SELECT TITLE_OP FROM OP')
        results = cursor.fetchall()
        conn.close()
        self.title = [row[0].replace('"',"'") for row in results]
        conn.close()
        dataBTN = [self.SP_1, self.SP_2, self.SP_3, self.SP_4, self.SP_5, self.SP_6, self.SP_7, self.SP_8, self.SP_9, self.SP_10, self.SP_11, self.SP_12, self.SP_13]
        for i in range(len(self.title)):
                dataBTN[i].setText(self.title[i])

    def setaboutOP(self, i):
        self.ch = i
        bd_name = "OTHENASHKOTORYNANEBESAH.db"
        bd = os.path.join("resources", bd_name )
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()
        cursor.execute(f'SELECT INFORMATION FROM ABOUT_OP WHERE id_OP = {i} ')
        results = cursor.fetchall()
        text = '\n'.join([result[0] for result in results])
        self.textEdit_3.setPlainText(text)
        conn.close()
        self.insertFILES(i)


    def insertFILES(self, i):
        self.spiskiclear()
        bd_name = "OTHENASHKOTORYNANEBESAH.db"
        bd = os.path.join("resources", bd_name )
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()
        cursor.execute(f'SELECT FILE_NAME FROM FILES_OP WHERE id_ABOUT_OP = {i} ')
        f_name = [row[0] for row in cursor.fetchall()] 
        cursor.execute(f'SELECT FILE_LINK FROM FILES_OP WHERE id_ABOUT_OP = {i} ')
        f_links = [row[0] for row in cursor.fetchall()]
        conn.close()
        for j in range(0, len(f_name)):
            if '09.03.0' in f_name[j] and '20' in f_name[j] and len(f_name[j])  < 27:
                self.UP.append(f_links[j])
                self.UPn.append(f_name[j])

            if ('АННОТ' in f_name[j] or 'Аннот' in f_name[j]) and ('практ' not in f_name[j] or 'Практ' not in f_name[j]) and '20' in f_name[j]:
                self.AnnRPOP.append(f_links[j])
                self.AnnRPOPn.append(f_name[j])

            if ('План' in f_name[j] or 'план' in f_name[j])  and ('Восп' in f_name[j] or 'восп' in f_name[j]) and ('Раб' in f_name[j] or 'раб' in f_name[j]):
                self.KPVR.append(f_links[j])
                self.KPVRn.append(f_name[j])

            if ( ((('Раб' in f_name[j] or 'раб' in f_name[j]) and ('Прогр' in f_name[j] or 'прогр' in f_name[j])) or 'РП' in f_name[j] )  and ('Восп' in f_name[j] or 'восп' in f_name[j])):
                self.RPV.append(f_links[j])
                self.RPVn.append(f_name[j])

            if (('Раб' in f_name[j] or 'раб' in f_name[j]) and ('Прогр' in f_name[j] or 'прогр' in f_name[j]))  and ('практ' not in f_name[j] or 'Практ' not in f_name[j] or 'П_' not in f_name[j] ) and ('Восп' not in f_name[j] or 'восп' not in f_name[j]):
                self.RPD.append(f_links[j])
                self.RPDn.append(f_name[j])

            if (('Раб' in f_name[j] or 'раб' in f_name[j]) and ('Прогр' in f_name[j] or 'прогр' in f_name[j])) and ('практ'  in f_name[j] or 'Практ'  in f_name[j] or 'П_'  in f_name[j]  or 'П__'  in f_name[j])   and '20' in f_name[j]:
                self.PP.append(f_links[j])
                self.PPn.append(f_name[j])

            if 'ОПОП' in f_name[j] and 'план' not in f_name[j] and 'Раб' not in f_name[j] and 'РП' not in f_name[j] :
                self.OP.append(f_links[j])
                self.OPn.append(f_name[j])

            if ('MP' in f_name[j] or 'МУ' in f_name[j] or 'пос' in f_name[j] or 'УП' in f_name[j] or 'metodic' in f_name[j] or 'УМП' in f_name[j] or ('Практикум' in f_name[j] or 'практикум' in f_name[j]) or 'Сборник' in f_name[j] or 'методич' in f_name[j]  or 'Руков' in f_name[j]):
                self.MiD.append(f_links[j])
                self.MiDn.append(f_name[j])

    def spiskiclear(self):
        self.UP.clear()
        self.AnnRPOP.clear()
        self.KPVR.clear()
        self.RPD.clear()
        self.RPV.clear()
        self.PP.clear()
        self.OP.clear()
        self.MiD.clear()

    def downloadFiles(self,i):
        path =[]
        parent = self.title[self.ch - 1]
        file_op_path = os.path.join("resources",parent)
        # outLOGs.file_path = os.path.join("logs",  outLOGs.file_name)
        url = [self.UP, self.AnnRPOP,self.KPVR,self.RPD,self.RPV,self.PP,self.OP,self.MiD ]
        nam = [self.UPn, self.AnnRPOPn,self.KPVRn,self.RPDn,self.RPVn,self.PPn,self.OPn,self.MiDn ]
        name_papkf = ['УЧЕБНЫЙ ПЛАН',
                      'АННОТАЦИИ К РАБОЧИМ ПРОГРАММАМ ДИСЦИПЛИН И ПРАКТИКИ',
                      'КАЛЕНДАРНЫЙ ПЛАН ВОСПИТАТЕЛЬНОЙ РАБОТЫ',
                      'РАБОЧАЯ ПРОГРАММА ДИСЦИПЛИН',
                      'РАБОЧАЯ ПРОГРАММА ВОСПИТАНИЯ',
                      'ПРОГРАММЫ ПРАКТИК',
                      'ОБРАЗОВАТЕЛЬНАЯ ПРОГРАММА',
                      'МЕТОДИЧЕСКИЕ И ИНЫЕ ДОКУМЕНТЫ']

        if os.path.exists("resources"):
            if not os.path.exists(file_op_path):
                os.makedirs(file_op_path)
                file_op_path = os.path.join(file_op_path,name_papkf[i-1])
                if not os.path.exists(file_op_path):
                        os.makedirs(file_op_path)
                        for ii in range(0, len(url[i-1])):
                                t = os.path.join(file_op_path, nam[i-1][ii] )
                                response = requests.get(url[i-1][ii])
                                if response.status_code == 200 and not os.path.exists(t):
                                        with open(os.path.join(file_op_path, nam[i-1][ii] ), 'wb') as file:
                                                for chunk in response.iter_content(chunk_size=1024):
                                                        file.write(chunk)
                                                time.sleep(1)
                                                print(f" { name_papkf[i-1]} ЗАГРУЗКА ({ii+1} / {len(url[i-1])})")                                      
                                else:
                                      print("ФАЙЛ УЖЕ ЗАГРУЖЕН!")
                                      print(F"АНАЛИЗ ({ii+1} / {len(url[i-1])}) ")
                                      self.convert(os.path.join(file_op_path, nam[i-1][ii]))
                                      return
                else: 
                      for ii in range(0, len(url[i-1])):
                                t = os.path.join(file_op_path, nam[i-1][ii] )
                                response = requests.get(url[i-1][ii])
                                if response.status_code == 200 and not os.path.exists(t):
                                        with open(os.path.join(file_op_path, nam[i-1][ii] ), 'wb') as file:
                                                for chunk in response.iter_content(chunk_size=1024):
                                                        file.write(chunk)
                                                time.sleep(1)
                                                print(f" { name_papkf[i-1]} ЗАГРУЗКА ({ii+1} / {len(url[i-1])})") 
                                else:
                                      print("ФАЙЛ УЖЕ ЗАГРУЖЕН!")
                                      print(F"АНАЛИЗ ({ii+1} / {len(url[i-1])}) ")
                                      self.convert(os.path.join(file_op_path, nam[i-1][ii]))
                                      return 
            else: 
                file_op_path = os.path.join(file_op_path,name_papkf[i-1])
                if not os.path.exists(file_op_path):
                        os.makedirs(file_op_path)
                        for ii in range(0, len(url[i-1])):
                                t = os.path.join(file_op_path, nam[i-1][ii] )
                                response = requests.get(url[i-1][ii])
                                if response.status_code == 200 and not os.path.exists(t):
                                        with open(os.path.join(file_op_path, nam[i-1][ii] ), 'wb') as file:
                                                for chunk in response.iter_content(chunk_size=1024):
                                                        file.write(chunk)
                                                time.sleep(1)
                                                print(f" { name_papkf[i-1]} ЗАГРУЗКА ({ii+1} / {len(url[i-1])})") 
                                else:
                                      print("ФАЙЛ УЖЕ ЗАГРУЖЕН!")
                                      print(F"АНАЛИЗ ({ii+1} / {len(url[i-1])}) ")
                                      self.convert(os.path.join(file_op_path, nam[i-1][ii]))
                                      return
                else: 
                      for ii in range(0, len(url[i-1])):
                                t = os.path.join(file_op_path, nam[i-1][ii] )
                                response = requests.get(url[i-1][ii])
                                if response.status_code == 200 and not os.path.exists(t):
                                        with open(os.path.join(file_op_path, nam[i-1][ii] ), 'wb') as file:
                                                for chunk in response.iter_content(chunk_size=1024):
                                                        file.write(chunk)
                                                time.sleep(1)
                                                print(f" { name_papkf[i-1]} ЗАГРУЗКА ({ii+1} / {len(url[i-1])})") 
                                else:
                                      print("ФАЙЛ УЖЕ ЗАГРУЖЕН!")
                                      print(F"АНАЛИЗ ({ii+1} / {len(url[i-1])}) ")
                                      self.convert( os.path.join(file_op_path, nam[i-1][ii]))
                                      
        file_op_path = ''
        parent = ''

    def convert(self, file_op_path):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_op_path)
        title = []
         # нащвание раздела с документами(учеьный план)
        img = convert_from_path(file_path)
        text = []
        for iI, image in enumerate(img):
                image_path = f"page_{iI}.jpg"
                image.save(image_path, 'JPEG')
                lines = pytesseract.image_to_string(Image.open(image_path), lang='rus')
                os.remove(image_path)
                title.append(lines.replace('\n\n', ''))
                break

        tables_file = tabula.read_pdf(file_path, pages='3', multiple_tables= False, lattice= True) 
        aatable = tables_file[0]

        aatable.columns = aatable.iloc[0]
        uch_plan = aatable.loc[:, ['Наименование', 'По\rплану']]
        print(uch_plan.columns)

        bd_name = "OTHENASHKOTORYNANEBESAH.db"
        bd = os.path.join("resources", bd_name )
        conn = sqlite3.connect(bd)
        cursor = conn.cursor()
        cursor.execute(f'SELECT FILE_NAME FROM FILES_OP WHERE id_ABOUT_OP = {self.ch} ')
        f_name = [row[0] for row in cursor.fetchall()] 
        conn.close()
        for i in f_name:
              if i == os.path.basename(file_path):
                        print(i == os.path.basename(file_path))
                        conn = sqlite3.connect(bd)
                        cursor = conn.cursor()
                        cursor.execute('''
                                UPDATE  FILES_OP
                                SET TITLE_FILE = ? 
                                WHERE FILE_NAME = ? ;
                                ''', (  title[0]  , i ))
                        conn.commit()
                        conn.close()
                

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1415, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Lucida Console")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: rgb(91, 88, 66) ;\n"
"font-family: \"Lucida Console\";\n"
"font-size: 10pt;\n"
"	}\n"
"#centralwidget{background-color: rgb(248, 242, 179); border:10px solid #000000; border-radius: 5px;}\n"
"\n"
"#label{border-right: 1px solid  #000000; font-size: 14pt;}\n"
"#leftmenu {border-right: 1px solid #000000;}\n"
"#rightmenu{border-left: 1px solid #000000;}\n"
"#mainbody{border-top: 1px solid #000000;}\n"
"#frame_10{border-top: 1px solid #000000; border-bottom: 1px solid #000000;}\n"
"#frame_11, #frame_12, #frame_13{border-top: 1px solid #000000; border-bottom: 1px solid #000000;}\n"
"\n"
"\n"
"#uchplans , #annotrabprogrdiscpra, #obrprogr  , #rabochprogrdicsmodul , #kalendplanvr  , #rabprogrvosp ,#metodichdocum , #progrprakt{border-right: 1px solid #000000; border-left: 1px solid #000000; }\n"
"#uchplansBTN , #annotrabprogrdiscpraBTN, #obrprogrBTN  , #rabochprogrdicsmodulBTN , #kalendpl"
                        "anvrBTN  , #rabprogrvospBTN ,#metodichdocumBTN , #progrpraktBTN{text-align: center; font-size: 8pt; }\n"
"\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 3px;}\n"
"\n"
"\n"
" #label_3, #label_6, #label_4{\n"
"				padding: 5px 3px;\n"
"				line-height: 1pt;}\n"
" #label_2, #label_5, #label_7{ font-weight: bold;}\n"
"#bar{	background-color: rgb(0, 0, 0)}\n"
"#label_8{padding-left: 6px; border-radius: 10px;}\n"
"\n"
"#homeBTN{  border-left: 2px solid  rgb(79, 77, 57);\n"
"				   font-weight: bold;}\n"
"\n"
"#SP_1, #SP_2, #SP_3, #SP_4, #SP_5, #SP_6, #SP_7, #SP_8, #SP_9, #SP_10, #SP_11, #SP_12, #SP_13{\n"
"	\n"
"	font: 9pt \"Lucida Console\";\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1415, 630))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 10)
        self.bar = QWidget(self.centralwidget)
        self.bar.setObjectName(u"bar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bar.sizePolicy().hasHeightForWidth())
        self.bar.setSizePolicy(sizePolicy1)
        self.bar.setMinimumSize(QSize(0, 12))
        self.bar.setMaximumSize(QSize(16777215, 11))
        self.horizontalLayout = QHBoxLayout(self.bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.frame = QFrame(self.bar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.collapse = QPushButton(self.frame)
        self.collapse.setObjectName(u"collapse")
        self.collapse.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/toolbar_separator_vertical.png", QSize(), QIcon.Normal, QIcon.Off)
        self.collapse.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.collapse)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close = QPushButton(self.frame)
        self.close.setObjectName(u"close")
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.close)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.bar)

        self.MAIN = QWidget(self.centralwidget)
        self.MAIN.setObjectName(u"MAIN")
        self.verticalLayout_2 = QVBoxLayout(self.MAIN)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.MAIN)
        self.header.setObjectName(u"header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(50)
        sizePolicy2.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy2)
        self.header.setMinimumSize(QSize(0, 100))
        self.header.setMaximumSize(QSize(1400, 150))
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(280, 0))
        self.label.setMaximumSize(QSize(280, 16777215))
        font1 = QFont()
        font1.setFamily(u"Lucida Console")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.header)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(70, 16777215))
        font2 = QFont()
        font2.setFamily(u"Lucida Console")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.header)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(300, 0))
        self.label_3.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.header)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 0))
        self.label_5.setMaximumSize(QSize(70, 16777215))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(300, 0))
        self.label_4.setMaximumSize(QSize(300, 16777215))
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_7 = QLabel(self.header)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(50, 0))
        self.label_7.setMaximumSize(QSize(70, 16777215))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_6 = QLabel(self.header)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(300, 0))
        self.label_6.setMaximumSize(QSize(330, 16777215))

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.header)

        self.mainbody = QWidget(self.MAIN)
        self.mainbody.setObjectName(u"mainbody")
        self.horizontalLayout_4 = QHBoxLayout(self.mainbody)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QCustomSlideMenu(self.mainbody)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setMinimumSize(QSize(0, 500))
        self.leftmenu.setMaximumSize(QSize(0, 1000))
        self.verticalLayout_6 = QVBoxLayout(self.leftmenu)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftmenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(280, 0))
        self.widget.setMaximumSize(QSize(280, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(50, 0, 0, 0)
        self.homeBTN = QPushButton(self.frame_2)
        self.homeBTN.setObjectName(u"homeBTN")
        font3 = QFont()
        font3.setFamily(u"Lucida Console")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.homeBTN.setFont(font3)
        self.homeBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBTN.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.homeBTN)

        self.facultiesBTN = QPushButton(self.frame_2)
        self.facultiesBTN.setObjectName(u"facultiesBTN")
        self.facultiesBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.facultiesBTN)

        self.specialtiesBTN = QPushButton(self.frame_2)
        self.specialtiesBTN.setObjectName(u"specialtiesBTN")
        self.specialtiesBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.specialtiesBTN)

        self.analysisBTN = QPushButton(self.frame_2)
        self.analysisBTN.setObjectName(u"analysisBTN")
        self.analysisBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.analysisBTN)

        self.all_filesBTN = QPushButton(self.frame_2)
        self.all_filesBTN.setObjectName(u"all_filesBTN")
        self.all_filesBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.all_filesBTN)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(50, 0, 0, 0)
        self.signinBTN = QPushButton(self.frame_3)
        self.signinBTN.setObjectName(u"signinBTN")
        self.signinBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.signinBTN)

        self.settingBTN = QPushButton(self.frame_3)
        self.settingBTN.setObjectName(u"settingBTN")
        self.settingBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.settingBTN)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.leftmenu)

        self.mainbodycontent = QWidget(self.mainbody)
        self.mainbodycontent.setObjectName(u"mainbodycontent")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainbodycontent.sizePolicy().hasHeightForWidth())
        self.mainbodycontent.setSizePolicy(sizePolicy4)
        self.mainbodycontent.setMinimumSize(QSize(500, 500))
        self.mainbodycontent.setMaximumSize(QSize(444444, 1000))
        self.verticalLayout_7 = QVBoxLayout(self.mainbodycontent)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomQStackedWidget(self.mainbodycontent)
        self.mainPages.setObjectName(u"mainPages")
        sizePolicy.setHeightForWidth(self.mainPages.sizePolicy().hasHeightForWidth())
        self.mainPages.setSizePolicy(sizePolicy)
        self.mainPages.setMinimumSize(QSize(1, 0))
        self.mainPages.setFont(font2)
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.verticalLayout_8 = QVBoxLayout(self.homepage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 2, 10, 15)
        self.label_8 = QLabel(self.homepage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(1100, 480))
        self.label_8.setMaximumSize(QSize(1488, 496))
        self.label_8.setPixmap(QPixmap(u"QSS/title.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.mainPages.addWidget(self.homepage)
        self.facultiespage = QWidget()
        self.facultiespage.setObjectName(u"facultiespage")
        self.verticalLayout_9 = QVBoxLayout(self.facultiespage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.facultiespage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 165, 690))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 10, 0)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 165))
        self.frame_4.setMaximumSize(QSize(16777215, 165))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fitkbBTN = QPushButton(self.frame_4)
        self.fitkbBTN.setObjectName(u"fitkbBTN")
        self.fitkbBTN.setMinimumSize(QSize(70, 50))
        self.fitkbBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.fitkbBTN.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.fitkbBTN.setCheckable(True)
        self.fitkbBTN.setChecked(True)

        self.horizontalLayout_5.addWidget(self.fitkbBTN)

        self.textEdit = QTextEdit(self.frame_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 165))
        self.textEdit.setMaximumSize(QSize(16777215, 165))

        self.horizontalLayout_5.addWidget(self.textEdit)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 150))
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.faigBTN = QPushButton(self.frame_5)
        self.faigBTN.setObjectName(u"faigBTN")
        self.faigBTN.setMinimumSize(QSize(70, 50))
        self.faigBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.faigBTN.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.faigBTN.setCheckable(True)
        self.faigBTN.setChecked(True)

        self.horizontalLayout_6.addWidget(self.faigBTN)

        self.textEdit_2 = QTextEdit(self.frame_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 150))
        self.textEdit_2.setMaximumSize(QSize(16777215, 150))

        self.horizontalLayout_6.addWidget(self.textEdit_2)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 130))
        self.frame_8.setMaximumSize(QSize(16777215, 130))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.fmatBTN = QPushButton(self.frame_8)
        self.fmatBTN.setObjectName(u"fmatBTN")
        self.fmatBTN.setMinimumSize(QSize(70, 50))
        self.fmatBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.fmatBTN.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.fmatBTN.setCheckable(True)
        self.fmatBTN.setChecked(True)

        self.horizontalLayout_12.addWidget(self.fmatBTN)

        self.textEdit_4 = QTextEdit(self.frame_8)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 130))
        self.textEdit_4.setMaximumSize(QSize(16777215, 130))

        self.horizontalLayout_12.addWidget(self.textEdit_4)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 135))
        self.frame_7.setMaximumSize(QSize(16777215, 135))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.fissBTN = QPushButton(self.frame_7)
        self.fissBTN.setObjectName(u"fissBTN")
        self.fissBTN.setMinimumSize(QSize(70, 50))
        self.fissBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.fissBTN.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.fissBTN.setCheckable(True)
        self.fissBTN.setChecked(True)

        self.horizontalLayout_11.addWidget(self.fissBTN)

        self.textEdit_5 = QTextEdit(self.frame_7)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMinimumSize(QSize(0, 135))
        self.textEdit_5.setMaximumSize(QSize(16777215, 135))

        self.horizontalLayout_11.addWidget(self.textEdit_5)


        self.verticalLayout_10.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 110))
        self.frame_6.setMaximumSize(QSize(16777215, 110))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.rteBTN = QPushButton(self.frame_6)
        self.rteBTN.setObjectName(u"rteBTN")
        self.rteBTN.setMinimumSize(QSize(70, 50))
        self.rteBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.rteBTN.setLocale(QLocale(QLocale.Russian, QLocale.Russia))

        self.horizontalLayout_9.addWidget(self.rteBTN)

        self.textEdit_6 = QTextEdit(self.frame_6)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setMinimumSize(QSize(0, 110))
        self.textEdit_6.setMaximumSize(QSize(16777215, 110))

        self.horizontalLayout_9.addWidget(self.textEdit_6)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_9.addWidget(self.scrollArea_2)

        self.mainPages.addWidget(self.facultiespage)
        self.specialtiespage = QWidget()
        self.specialtiespage.setObjectName(u"specialtiespage")
        self.verticalLayout_11 = QVBoxLayout(self.specialtiespage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.specialtiespage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1120, 823))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.labeeel = QLabel(self.frame_9)
        self.labeeel.setObjectName(u"labeeel")
        self.labeeel.setMinimumSize(QSize(0, 20))
        self.labeeel.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_12.addWidget(self.labeeel)

        self.TITLE_FACULTY_2 = QLabel(self.frame_9)
        self.TITLE_FACULTY_2.setObjectName(u"TITLE_FACULTY_2")

        self.verticalLayout_12.addWidget(self.TITLE_FACULTY_2)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(1120, 0))
        self.frame_10.setMaximumSize(QSize(1400, 400))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 0, 0, 0)
        self.SP_1 = QPushButton(self.frame_10)
        self.SP_1.setObjectName(u"SP_1")
        self.SP_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_1)

        self.SP_2 = QPushButton(self.frame_10)
        self.SP_2.setObjectName(u"SP_2")
        self.SP_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_2)

        self.SP_3 = QPushButton(self.frame_10)
        self.SP_3.setObjectName(u"SP_3")
        self.SP_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_3)

        self.SP_4 = QPushButton(self.frame_10)
        self.SP_4.setObjectName(u"SP_4")
        self.SP_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_4)

        self.SP_5 = QPushButton(self.frame_10)
        self.SP_5.setObjectName(u"SP_5")
        self.SP_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_5)

        self.SP_6 = QPushButton(self.frame_10)
        self.SP_6.setObjectName(u"SP_6")
        self.SP_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_6)

        self.SP_7 = QPushButton(self.frame_10)
        self.SP_7.setObjectName(u"SP_7")
        self.SP_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_7)

        self.SP_8 = QPushButton(self.frame_10)
        self.SP_8.setObjectName(u"SP_8")
        self.SP_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_8)

        self.SP_9 = QPushButton(self.frame_10)
        self.SP_9.setObjectName(u"SP_9")
        self.SP_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_9)

        self.SP_10 = QPushButton(self.frame_10)
        self.SP_10.setObjectName(u"SP_10")
        self.SP_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_10)

        self.SP_11 = QPushButton(self.frame_10)
        self.SP_11.setObjectName(u"SP_11")
        self.SP_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_11)

        self.SP_12 = QPushButton(self.frame_10)
        self.SP_12.setObjectName(u"SP_12")
        self.SP_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_12)

        self.SP_13 = QPushButton(self.frame_10)
        self.SP_13.setObjectName(u"SP_13")
        self.SP_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.SP_13)


        self.verticalLayout_13.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy5)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.uchplans = QWidget(self.frame_12)
        self.uchplans.setObjectName(u"uchplans")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.uchplans.sizePolicy().hasHeightForWidth())
        self.uchplans.setSizePolicy(sizePolicy6)
        self.uchplans.setMinimumSize(QSize(280, 0))
        self.uchplans.setMaximumSize(QSize(357, 16777215))
        self.verticalLayout_27 = QVBoxLayout(self.uchplans)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.uchplansBTN = QPushButton(self.uchplans)
        self.uchplansBTN.setObjectName(u"uchplansBTN")
        sizePolicy5.setHeightForWidth(self.uchplansBTN.sizePolicy().hasHeightForWidth())
        self.uchplansBTN.setSizePolicy(sizePolicy5)
        self.uchplansBTN.setCursor(QCursor(Qt.PointingHandCursor))
        self.uchplansBTN.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_27.addWidget(self.uchplansBTN)


        self.horizontalLayout_7.addWidget(self.uchplans)

        self.obrprogr = QWidget(self.frame_12)
        self.obrprogr.setObjectName(u"obrprogr")
        sizePolicy6.setHeightForWidth(self.obrprogr.sizePolicy().hasHeightForWidth())
        self.obrprogr.setSizePolicy(sizePolicy6)
        self.obrprogr.setMinimumSize(QSize(280, 0))
        self.verticalLayout_28 = QVBoxLayout(self.obrprogr)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.obrprogrBTN = QPushButton(self.obrprogr)
        self.obrprogrBTN.setObjectName(u"obrprogrBTN")
        sizePolicy5.setHeightForWidth(self.obrprogrBTN.sizePolicy().hasHeightForWidth())
        self.obrprogrBTN.setSizePolicy(sizePolicy5)
        self.obrprogrBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_28.addWidget(self.obrprogrBTN)


        self.horizontalLayout_7.addWidget(self.obrprogr)

        self.rabochprogrdicsmodul = QWidget(self.frame_12)
        self.rabochprogrdicsmodul.setObjectName(u"rabochprogrdicsmodul")
        sizePolicy6.setHeightForWidth(self.rabochprogrdicsmodul.sizePolicy().hasHeightForWidth())
        self.rabochprogrdicsmodul.setSizePolicy(sizePolicy6)
        self.rabochprogrdicsmodul.setMinimumSize(QSize(280, 0))
        self.verticalLayout_32 = QVBoxLayout(self.rabochprogrdicsmodul)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.rabochprogrdicsmodulBTN = QPushButton(self.rabochprogrdicsmodul)
        self.rabochprogrdicsmodulBTN.setObjectName(u"rabochprogrdicsmodulBTN")
        sizePolicy5.setHeightForWidth(self.rabochprogrdicsmodulBTN.sizePolicy().hasHeightForWidth())
        self.rabochprogrdicsmodulBTN.setSizePolicy(sizePolicy5)
        self.rabochprogrdicsmodulBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_32.addWidget(self.rabochprogrdicsmodulBTN)


        self.horizontalLayout_7.addWidget(self.rabochprogrdicsmodul)

        self.progrprakt = QWidget(self.frame_12)
        self.progrprakt.setObjectName(u"progrprakt")
        sizePolicy6.setHeightForWidth(self.progrprakt.sizePolicy().hasHeightForWidth())
        self.progrprakt.setSizePolicy(sizePolicy6)
        self.progrprakt.setMinimumSize(QSize(280, 0))
        self.verticalLayout_37 = QVBoxLayout(self.progrprakt)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.progrpraktBTN = QPushButton(self.progrprakt)
        self.progrpraktBTN.setObjectName(u"progrpraktBTN")
        sizePolicy5.setHeightForWidth(self.progrpraktBTN.sizePolicy().hasHeightForWidth())
        self.progrpraktBTN.setSizePolicy(sizePolicy5)
        self.progrpraktBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_37.addWidget(self.progrpraktBTN)


        self.horizontalLayout_7.addWidget(self.progrprakt)


        self.verticalLayout_13.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.annotrabprogrdiscpra = QWidget(self.frame_11)
        self.annotrabprogrdiscpra.setObjectName(u"annotrabprogrdiscpra")
        sizePolicy6.setHeightForWidth(self.annotrabprogrdiscpra.sizePolicy().hasHeightForWidth())
        self.annotrabprogrdiscpra.setSizePolicy(sizePolicy6)
        self.annotrabprogrdiscpra.setMinimumSize(QSize(280, 0))
        self.verticalLayout_30 = QVBoxLayout(self.annotrabprogrdiscpra)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.annotrabprogrdiscpraBTN = QPushButton(self.annotrabprogrdiscpra)
        self.annotrabprogrdiscpraBTN.setObjectName(u"annotrabprogrdiscpraBTN")
        sizePolicy5.setHeightForWidth(self.annotrabprogrdiscpraBTN.sizePolicy().hasHeightForWidth())
        self.annotrabprogrdiscpraBTN.setSizePolicy(sizePolicy5)
        self.annotrabprogrdiscpraBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_30.addWidget(self.annotrabprogrdiscpraBTN)


        self.horizontalLayout_8.addWidget(self.annotrabprogrdiscpra)

        self.kalendplanvr = QWidget(self.frame_11)
        self.kalendplanvr.setObjectName(u"kalendplanvr")
        sizePolicy6.setHeightForWidth(self.kalendplanvr.sizePolicy().hasHeightForWidth())
        self.kalendplanvr.setSizePolicy(sizePolicy6)
        self.kalendplanvr.setMinimumSize(QSize(280, 0))
        self.verticalLayout_29 = QVBoxLayout(self.kalendplanvr)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.kalendplanvrBTN = QPushButton(self.kalendplanvr)
        self.kalendplanvrBTN.setObjectName(u"kalendplanvrBTN")
        sizePolicy5.setHeightForWidth(self.kalendplanvrBTN.sizePolicy().hasHeightForWidth())
        self.kalendplanvrBTN.setSizePolicy(sizePolicy5)
        self.kalendplanvrBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_29.addWidget(self.kalendplanvrBTN)


        self.horizontalLayout_8.addWidget(self.kalendplanvr)

        self.rabprogrvosp = QWidget(self.frame_11)
        self.rabprogrvosp.setObjectName(u"rabprogrvosp")
        sizePolicy6.setHeightForWidth(self.rabprogrvosp.sizePolicy().hasHeightForWidth())
        self.rabprogrvosp.setSizePolicy(sizePolicy6)
        self.rabprogrvosp.setMinimumSize(QSize(280, 0))
        self.verticalLayout_33 = QVBoxLayout(self.rabprogrvosp)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.rabprogrvospBTN = QPushButton(self.rabprogrvosp)
        self.rabprogrvospBTN.setObjectName(u"rabprogrvospBTN")
        sizePolicy5.setHeightForWidth(self.rabprogrvospBTN.sizePolicy().hasHeightForWidth())
        self.rabprogrvospBTN.setSizePolicy(sizePolicy5)
        self.rabprogrvospBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_33.addWidget(self.rabprogrvospBTN)


        self.horizontalLayout_8.addWidget(self.rabprogrvosp)

        self.metodichdocum = QWidget(self.frame_11)
        self.metodichdocum.setObjectName(u"metodichdocum")
        sizePolicy6.setHeightForWidth(self.metodichdocum.sizePolicy().hasHeightForWidth())
        self.metodichdocum.setSizePolicy(sizePolicy6)
        self.metodichdocum.setMinimumSize(QSize(280, 0))
        self.verticalLayout_38 = QVBoxLayout(self.metodichdocum)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.metodichdocumBTN = QPushButton(self.metodichdocum)
        self.metodichdocumBTN.setObjectName(u"metodichdocumBTN")
        sizePolicy5.setHeightForWidth(self.metodichdocumBTN.sizePolicy().hasHeightForWidth())
        self.metodichdocumBTN.setSizePolicy(sizePolicy5)
        self.metodichdocumBTN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_38.addWidget(self.metodichdocumBTN)


        self.horizontalLayout_8.addWidget(self.metodichdocum)


        self.verticalLayout_13.addWidget(self.frame_11)

        self.textEdit_3 = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMinimumSize(QSize(1120, 370))
        self.textEdit_3.setMaximumSize(QSize(1395, 370))
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.textEdit_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.mainPages.addWidget(self.specialtiespage)
        self.analysispage = QWidget()
        self.analysispage.setObjectName(u"analysispage")
        self.verticalLayout_15 = QVBoxLayout(self.analysispage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.vivod = QTextEdit(self.analysispage)
        self.vivod.setObjectName(u"vivod")

        self.verticalLayout_15.addWidget(self.vivod)

        self.mainPages.addWidget(self.analysispage)
        self.alllistfilepage = QWidget()
        self.alllistfilepage.setObjectName(u"alllistfilepage")
        self.verticalLayout_25 = QVBoxLayout(self.alllistfilepage)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.alllistfilepage)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 100, 30))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_25.addWidget(self.scrollArea_3)

        self.mainPages.addWidget(self.alllistfilepage)
        self.signinpage = QWidget()
        self.signinpage.setObjectName(u"signinpage")
        self.label_14 = QLabel(self.signinpage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(740, 220, 131, 16))
        self.mainPages.addWidget(self.signinpage)
        self.sattingpage = QWidget()
        self.sattingpage.setObjectName(u"sattingpage")
        self.label_15 = QLabel(self.sattingpage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(750, 210, 141, 16))
        self.mainPages.addWidget(self.sattingpage)

        self.verticalLayout_7.addWidget(self.mainPages)


        self.horizontalLayout_4.addWidget(self.mainbodycontent)

        self.rightmenu = QWidget(self.mainbody)
        self.rightmenu.setObjectName(u"rightmenu")
        self.rightmenu.setEnabled(True)
        self.rightmenu.setMinimumSize(QSize(0, 200))
        self.rightmenu.setMaximumSize(QSize(0, 1000))

        self.horizontalLayout_4.addWidget(self.rightmenu)


        self.verticalLayout_2.addWidget(self.mainbody)


        self.verticalLayout.addWidget(self.MAIN)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)

        
        # self.fitkbBTN.clicked.connect(lambda: self.ch_fac = 1)
        # self.faigBTN.clicked.connect(lambda: self.ch_fac = 2)
        # self.fmatBTN.clicked.connect(lambda: self.ch_fac = 3)
        # self.fissBTN.clicked.connect(lambda: self.ch_fac = 4)
        # self.rteBTN.clicked.connect(lambda:self.ch_fac = 5)


        self.SP_1.clicked.connect(lambda: self.setaboutOP(1))
        self.SP_2.clicked.connect(lambda: self.setaboutOP(2))
        self.SP_3.clicked.connect(lambda: self.setaboutOP(3))
        self.SP_4.clicked.connect(lambda: self.setaboutOP(4))
        self.SP_5.clicked.connect(lambda: self.setaboutOP(5))
        self.SP_6.clicked.connect(lambda: self.setaboutOP(6))
        self.SP_7.clicked.connect(lambda: self.setaboutOP(7))
        self.SP_8.clicked.connect(lambda: self.setaboutOP(8))
        self.SP_9.clicked.connect(lambda: self.setaboutOP(9))
        self.SP_10.clicked.connect(lambda: self.setaboutOP(10))
        self.SP_11.clicked.connect(lambda: self.setaboutOP(11))
        self.SP_12.clicked.connect(lambda: self.setaboutOP(12))
        self.SP_13.clicked.connect(lambda: self.setaboutOP(13))


        self.uchplansBTN.clicked.connect(lambda: self.downloadFiles(1))
        self.annotrabprogrdiscpraBTN.clicked.connect(lambda: self.downloadFiles(2))
        self.kalendplanvrBTN.clicked.connect(lambda: self.downloadFiles(3))
        self.rabochprogrdicsmodulBTN.clicked.connect(lambda: self.downloadFiles(4))
        self.rabprogrvospBTN.clicked.connect(lambda: self.downloadFiles(5))
        self.progrpraktBTN.clicked.connect(lambda: self.downloadFiles(6))
        self.obrprogrBTN.clicked.connect(lambda: self.downloadFiles(7))
        self.metodichdocumBTN.clicked.connect(lambda: self.downloadFiles(8))



        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.collapse.setText("")
        self.close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"VSTUMAPPER", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  1.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the faculty of state </p><p>of Voronezh State University </p><p>for futher analisys</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  2.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the faculty speciality </p><p>you have chosen </p><p>for analysis</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  3.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select the educational program</p><p>file related to this </p><p>specialty</p></body></html>", None))
        self.homeBTN.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.facultiesBTN.setText(QCoreApplication.translate("MainWindow", u"Faculties", None))
        self.specialtiesBTN.setText(QCoreApplication.translate("MainWindow", u"Specialties", None))
        self.analysisBTN.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.all_filesBTN.setText(QCoreApplication.translate("MainWindow", u"All list files", None))
        self.signinBTN.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.settingBTN.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_8.setText("")
        self.fitkbBTN.setText(QCoreApplication.translate("MainWindow", u" \u0424\u0418\u0422\u041a\u0411", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0418\u0422-\u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439 \u0431\u044b\u043b \u0441\u043e\u0437\u0434\u0430\u043d \u0432 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0435 \u0432 2013 \u0433\u043e\u0434\u0443, \u043e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0432 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0443 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432 \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0438"
                        "\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439. \u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0435\u0442 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u043c &quot;\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430 \u0438 \u0432\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430&quot;, &quot;\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438&quot;, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 &quot;\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u0431\u0435\u0437"
                        "\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c&quot;, &quot;\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u0442\u0435\u043b\u0435\u043a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c&quot; \u0438 &quot;\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c&quot;. </p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f &quot;\u0418\u043d\u0444\u043e\u0440\u043c\u0430"
                        "\u0442\u0438\u043a\u0430 \u0438 \u0432\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u0445\u043d\u0438\u043a\u0430&quot; \u043f\u043e\u043b\u0443\u0447\u0430\u044e\u0442 \u0437\u043d\u0430\u043d\u0438\u044f \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0441\u0435\u0442\u0435\u0439 \u0438 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0430\u043f\u043f\u0430\u0440\u0430\u0442\u043d\u044b\u0445 \u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432 \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c. \u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 &quot;\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442"
                        "\u0435\u043c\u044b \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438&quot; \u043f\u043e\u0434\u0433\u043e\u0442\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432 \u0434\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u0442\u0435\u043e\u0440\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0438 \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0437\u0430\u0434\u0430\u0447 \u0432 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c\u0430\u0445 \u0441 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u0441\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439.</p></body></html>", None))
        self.faigBTN.setText(QCoreApplication.translate("MainWindow", u" \u0424\u0410\u0418\u0413", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0410\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u043d\u044b\u0439 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442, \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0439 \u0432 1972 \u0433\u043e\u0434\u0443, \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043e\u0434\u043d\u0438\u043c \u0438\u0437 \u0432\u0435\u0434\u0443\u0449\u0438\u0445 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u043e\u0432 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0430 \u0438 \u0433\u043e\u0442\u043e\u0432\u0438"
                        "\u0442 \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u043e\u0440\u043e\u0432, \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u043e\u0440\u043e\u0432-\u0434\u0438\u0437\u0430\u0439\u043d\u0435\u0440\u043e\u0432, \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u043e\u0440\u043e\u0432-\u0440\u0435\u0441\u0442\u0430\u0432\u0440\u0430\u0442\u043e\u0440\u043e\u0432, \u0433\u0440\u0430\u0434\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u0435\u0439 \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u043c \u0431\u0430\u043a\u0430\u043b\u0430\u0432\u0440\u0438\u0430\u0442\u0430 \u0438 \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u0443\u0440\u044b \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u044f\u0445 &quot;\u0410\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u0430&quot;, &quot;\u0414\u0438\u0437\u0430\u0439\u043d \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u043d\u043e\u0439 \u0441\u0440\u0435\u0434\u044b&quot;, &quot;\u0420\u0435\u043a\u043e\u043d\u0441"
                        "\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u0438 \u0440\u0435\u0441\u0442\u0430\u0432\u0440\u0430\u0446\u0438\u044f \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u043d\u043e\u0433\u043e \u043d\u0430\u0441\u043b\u0435\u0434\u0438\u044f&quot;, &quot;\u0413\u0440\u0430\u0434\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e&quot;.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0441\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 6 \u043a\u0430\u0444\u0435\u0434\u0440, \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 17 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u043e\u0440\u043e\u0432, \u0432\u043a\u043b\u044e\u0447\u0430\u044f 3 &quot;\u0417\u0430\u0441\u043b\u0443\u0436\u0435\u043d\u043d\u044b\u0445 \u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u043e"
                        "\u0440\u0430 \u0420\u043e\u0441\u0441\u0438\u0438&quot;, \u043b\u0430\u0443\u0440\u0435\u0430\u0442\u043e\u0432 \u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u043f\u0440\u0435\u043c\u0438\u0439 \u0420\u043e\u0441\u0441\u0438\u0438, \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u043e\u0432 \u043d\u0430\u0443\u043a, \u0434\u043e\u0446\u0435\u043d\u0442\u043e\u0432. \u0411\u043e\u043b\u044c\u0448\u0438\u043d\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u044f\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0447\u043b\u0435\u043d\u0430\u043c\u0438 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0445 \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u043a\u0438\u0445 \u0441\u043e\u044e\u0437\u043e\u0432 \u0438 \u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u043c\u0438 \u0432\u043e\u0440\u043e\u043d\u0435\u0436\u0441\u043a\u0438\u043c\u0438 \u0430\u0440\u0445\u0438\u0442"
                        "\u0435\u043a\u0442\u043e\u0440\u0430\u043c\u0438, \u0430\u0432\u0442\u043e\u0440\u0430\u043c\u0438 \u043a\u0440\u0443\u043f\u043d\u044b\u0445 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043a, \u043b\u0430\u0443\u0440\u0435\u0430\u0442\u0430\u043c\u0438 \u043f\u0440\u0435\u043c\u0438\u0439 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0438 \u043c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f.</p></body></html>", None))
        self.fmatBTN.setText(QCoreApplication.translate("MainWindow", u" \u0424\u041c\u0410\u0422", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0431\u044b\u043b \u043e\u0441\u043d\u043e\u0432\u0430\u043d \u043f\u0443\u0442\u0435\u043c \u0441\u043b\u0438\u044f\u043d\u0438\u044f \u0430\u0432\u0438\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e, \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0430\u0446\u0438\u0438 \u0438 \u0440\u043e\u0431\u043e\u0442\u0438\u0437\u0430\u0446\u0438\u0438 \u043c\u0430\u0448\u0438\u043d\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0438 \u0444\u0438\u0437\u0438\u043a\u043e"
                        "-\u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u043e\u0432 \u0412\u043e\u0440\u043e\u043d\u0435\u0436\u0441\u043a\u043e\u0433\u043e \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0430.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0433\u043e\u0442\u043e\u0432\u0438\u0442 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432 \u0434\u043b\u044f \u0430\u0432\u0438\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439, \u0440\u0430\u043a\u0435\u0442\u043d\u043e-\u043a\u043e\u0441\u043c\u0438\u0447\u0435\u0441\u043a\u043e\u0439, \u043d\u0435\u0444\u0442\u0435\u0433\u0430\u0437\u043e"
                        "\u0432\u043e\u0439 \u0438 \u043c\u0430\u0448\u0438\u043d\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043e\u0442\u0440\u0430\u0441\u043b\u0435\u0439. \u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0430 \u043a\u0430\u0434\u0440\u043e\u0432 \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u0432\u044b\u0441\u043e\u043a\u0438\u043c \u0442\u0432\u043e\u0440\u0447\u0435\u0441\u043a\u0438\u043c \u0438 \u043d\u0430\u0443\u0447\u043d\u044b\u043c \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043e\u043c \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u043e\u0440\u0441\u043a\u043e-\u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c\u0441\u043a\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u0430\u0432\u0430 \u043a\u0430\u0444\u0435\u0434\u0440, \u0432\u043a\u043b\u044e\u0447\u0430\u044e\u0449\u0435\u0433\u043e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439 \u0438 \u0432\u0435\u0434\u0443"
                        "\u0449\u0438\u0445 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432 \u0431\u0430\u0437\u043e\u0432\u044b\u0445 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0439 \u0440\u0435\u0433\u0438\u043e\u043d\u0430.  \u041e\u0431\u0443\u0447\u0430\u044f\u0441\u044c \u0443 \u043d\u0430\u0441, \u0432\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0441\u0442\u0430\u0442\u044c \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u043c\u0438 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u0430\u043c\u0438, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0430\u0442 \u0438\u043d\u043d\u043e\u0432\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u0420\u043e\u0441\u0441\u0438\u0438 \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u043c\u043e\u0449\u044c.</p></body></html>", None))
        self.fissBTN.setText(QCoreApplication.translate("MainWindow", u" \u0424\u0418\u0421\u0421", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c \u0438 \u0441\u043e\u043e\u0440\u0443\u0436\u0435\u043d\u0438\u0439 - \u0432\u0435\u0434\u0443\u0449\u0438\u0439 \u043c\u043d\u043e\u0433\u043e\u043f\u0440\u043e\u0444\u0438\u043b\u044c\u043d\u044b\u0439 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442\u0430 \u0441 \u0431\u043e\u0433\u0430\u0442\u043e\u0439 \u0438\u0441"
                        "\u0442\u043e\u0440\u0438\u0435\u0439 \u0438 \u0442\u0440\u0430\u0434\u0438\u0446\u0438\u044f\u043c\u0438. \u041e\u043d \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0435\u0442 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u043c \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u043c \u0438 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044f\u043c, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e, \u043f\u0440\u043e\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u044d\u043a\u0441\u043f\u043b\u0443\u0430\u0442\u0430\u0446\u0438\u044e \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c \u0438 \u0441\u043e\u043e\u0440\u0443\u0436\u0435\u043d\u0438\u0439.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px;\">\u041d\u0430 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u044b \u043a\u0440\u0443\u043f\u043d\u0435\u0439\u0448\u0438\u0435 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0435 \u0446\u0435\u043d\u0442\u0440\u044b, \u043e\u0441\u043d\u0430\u0449\u0435\u043d\u043d\u044b\u0435 \u0441\u043e\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u043c \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u0438 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430\u043c\u0438, \u0447\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0430\u043c \u0430\u043a\u0442\u0438\u0432\u043d\u043e \u0443\u0447\u0430\u0441\u0442\u0432\u043e\u0432\u0430\u0442\u044c \u0432 \u043d\u0430\u0443\u0447\u043d\u043e\u0439 \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0438 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442"
                        "\u043a\u0430\u0445, \u043e\u0441\u043e\u0431\u0435\u043d\u043d\u043e \u0432 \u0443\u0441\u043b\u043e\u0432\u0438\u044f\u0445 \u0438\u043c\u043f\u043e\u0440\u0442\u043e\u0437\u0430\u043c\u0435\u0449\u0435\u043d\u0438\u044f. \u0422\u0430\u043a\u0436\u0435 \u043d\u0430 \u0444\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442\u0435 \u043e\u0442\u043a\u0440\u044b\u0442\u0430 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u044f \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u0440\u0435\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438, \u0433\u0434\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u044b \u0440\u0430\u0437\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u044e\u0442 \u0446\u0438\u0444\u0440\u043e\u0432\u043e\u0439 \u043a\u043e\u043d\u0442\u0435\u043d\u0442 \u0438 \u043f\u043e\u043b\u0443\u0447\u0430\u044e\u0442 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0446\u0438\u0444\u0440\u043e\u0432\u044b\u0435 \u043a\u043e\u043c\u043f\u0435"
                        "\u0442\u0435\u043d\u0446\u0438\u0438.</p></body></html>", None))
        self.rteBTN.setText(QCoreApplication.translate("MainWindow", u" \u0420\u0422\u042d", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0440\u0430\u0434\u0438\u043e\u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u0438 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0438 \u0433\u043e\u0442\u043e\u0432\u0438\u0442 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432 \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0440\u0430\u0434\u0438\u043e\u0442\u0435\u0445\u043d\u0438\u043a\u0438, \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0438, \u0438\u043d\u0444\u043e\u0440\u043c"
                        "\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439, \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u043e\u0439 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438. \u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0438\u043c\u0435\u0435\u0442 \u043a\u0440\u0443\u043f\u043d\u0435\u0439\u0448\u0438\u0435 \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u044b\u0435 \u0446\u0435\u043d\u0442\u0440\u044b, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u044e \u0432\u0438\u0440\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0439 \u0440\u0435\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438. \u0412\u044b\u043f\u0443\u0441\u043a\u043d\u0438\u043a\u0438 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0442 \u0432 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u044b\u0445 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446"
                        "\u0438\u044f\u0445, \u0432\u043a\u043b\u044e\u0447\u0430\u044f \u043a\u0440\u0443\u043f\u043d\u044b\u0435 \u043c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438. \u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0435\u0442 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0431\u0430\u043a\u0430\u043b\u0430\u0432\u0440\u0438\u0430\u0442\u0443, \u043c\u0430\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u0443\u0440\u0435 \u0438 \u0430\u0441\u043f\u0438\u0440\u0430\u043d\u0442\u0443\u0440\u0435, \u0430 \u0442\u0430\u043a\u0436\u0435 \u0432\u043e\u0435\u043d\u043d\u043e\u0435 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435. \u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0438\u043c\u0435\u0435\u0442 \u0431\u043e\u0433\u0430\u0442\u0443\u044e \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u0438 \u0442\u0440\u0430\u0434\u0438\u0446\u0438\u0438, \u0430 \u0435\u0433\u043e \u043f"
                        "\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0438 - \u0430\u0432\u0442\u043e\u0440\u0438\u0442\u0435\u0442\u043d\u044b\u0435 \u0443\u0447\u0435\u043d\u044b\u0435 \u0438 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044b \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0440\u0430\u0434\u0438\u043e\u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u0438 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0438\u043a\u0438.</p></body></html>", None))
        self.labeeel.setText(QCoreApplication.translate("MainWindow", u"  SPECIALTIES", None))
        self.TITLE_FACULTY_2.setText(QCoreApplication.translate("MainWindow", u"  fitkb", None))
        self.SP_1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.SP_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.uchplansBTN.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0427\u0415\u0411\u041d\u042b\u0419 \u041f\u041b\u0410\u041d", None))
        self.obrprogrBTN.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u0420\u0410\u0417\u041e\u0412\u0410\u0422\u0415\u041b\u042c\u041d\u0410\u042f \u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u0410", None))
        self.rabochprogrdicsmodulBTN.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0411\u041e\u0427\u0418\u0415 \u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u042b \n"
"\u0414\u0418\u0421\u0426\u0418\u041f\u041b\u0418\u041d(\u041c\u041e\u0414\u0423\u041b\u0415\u0419)", None))
        self.progrpraktBTN.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u042b\n"
"\u041f\u0420\u0410\u041a\u0422\u0418\u041a", None))
        self.annotrabprogrdiscpraBTN.setText(QCoreApplication.translate("MainWindow", u"\u0410\u041d\u041d\u041e\u0422\u0410\u0426\u0418\u0418 \u041a \u0420\u0410\u0411\u041e\u0427\u0418\u041c \n"
"\u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u0410\u041c \u0414\u0418\u0421\u0426\u0418\u041f\u041b\u0418\u041d \n"
"\u0418 \u041f\u0420\u0410\u041a\u0422\u0418\u041a\u0418", None))
        self.kalendplanvrBTN.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0410\u041b\u0415\u041d\u0414\u0410\u0420\u041d\u042b\u0419 \u041f\u041b\u0410\u041d \n"
"\u0412\u041e\u0421\u041f\u0418\u0422\u0410\u0422\u0415\u041b\u042c\u041d\u041e\u0419 \u0420\u0410\u0411\u041e\u0422\u042b", None))
        self.rabprogrvospBTN.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0411\u041e\u0427\u0410\u042f \u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u0410\n"
"\u0412\u041e\u0421\u041f\u0418\u0422\u0410\u041d\u0418\u042f", None))
        self.metodichdocumBTN.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0415\u0422\u041e\u0414\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u0418\n"
"\u0418\u041d\u042b\u0415 \u0414\u041e\u041a\u0423\u041c\u0415\u041d\u0422\u042b", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Console'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"signinapi", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"satting", None))
    # retranslateUi

