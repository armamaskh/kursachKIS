import os
import sys

from PySide2.QtWidgets import *
from qtpy.QtWidgets import *
from PySide2.QtCore import QTimer
import sqlite3
from parsing import *
from ui_interface import *

settings = QSettings()
from Custom_Widgets.Widgets import *

import threading



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        IC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'QSS')
        self.setWindowIcon(QIcon(os.path.join(IC , 'letter-v_9313273.ico')))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui) 
        self.ui.addTitle()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint )
        
        # self.dobavlenieSpecial()
        self.show()




if __name__ == "__main__":
    outLOGs()
    outLOGs.creating_file( f"[{datetime.datetime.now()}] Проверка наличия папки с базой данных.\n" )
    if not os.path.exists('resources'):
        os.makedirs('resources')
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Папка с базой данных не обнаружена!\n" )
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Проверка наличия базы данных.\n" )
        bazadannix = os.path.join("resources", BD().bd_name)
        if not os.path.exists(bazadannix):
                outLOGs.creating_file( f"[{datetime.datetime.now()}] База данных не обнаружена!\n" )
                outLOGs.creating_file( f"[{datetime.datetime.now()}] Данных нет!\n" )
                BD().create_BD()
                outLOGs.creating_file( f"[{datetime.datetime.now()}] НАЧАЛО ПАРСИНГА!\n" )
                PARSING().fSTAGE() 
                outLOGs.creating_file( f"[{datetime.datetime.now()}] НАЧАЛО РАБОТЫ!\n" )
                app = QApplication(sys.argv)    
                window = MainWindow()
                window.show()
                sys.exit(app.exec_())            
    else:
        bazadannix = os.path.join("resources", BD().bd_name)
        if not os.path.exists(bazadannix):
                outLOGs.creating_file( f"[{datetime.datetime.now()}] База данных не обнаружена!\n" )
                outLOGs.creating_file( f"[{datetime.datetime.now()}] Данных нет!\n" )
                BD().create_BD()
                outLOGs.creating_file( f"[{datetime.datetime.now()}] НАЧАЛО ПАРСИНГА!\n" )
                PARSING().fSTAGE()
        else: 
                outLOGs.creating_file( f"[{datetime.datetime.now()}] НАЧАЛО РАБОТЫ!\n" )
                app = QApplication(sys.argv)    
                window = MainWindow()
                window.show()
                sys.exit(app.exec_())

