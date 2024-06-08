import time
import os
import datetime
import sys

import numpy as np
import sqlite3


import requests
from bs4 import BeautifulSoup


class outLOGs:
    a = True
    file_name = ''
    file_path = ''
    def __init__(self):
        return
    def creating_file(text):
        if not os.path.exists('logs'):
            print('создание папки с логами')
            os.makedirs('logs')
        if(outLOGs.a == True): 
            outLOGs.file_name = "LOG_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
            outLOGs.file_path = os.path.join("logs",  outLOGs.file_name)
        outLOGs.a = False
        if not  os.path.exists( outLOGs.file_path):
            outLOGs.write_text_to_file( outLOGs.file_name,  outLOGs.file_path, ("НАЧАЛО РАБОТЫ ПРИЛОЖЕНИЯ FITCBuddy(Faculty of Information Technology and Cybersecurity helper): " + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "\n") )
            outLOGs.write_text_to_file( outLOGs.file_name,  outLOGs.file_path, "_поставте пять пж\n\n")
        outLOGs.write_text_to_file( outLOGs.file_name,  outLOGs.file_path, text)

    def write_text_to_file(file_name, file_path, rec_text):
        try:
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(rec_text)
            print(f"запись успешно добавлена в файл {file_name}")
        except IOError as e:
            print(f"Ошибка при записи в файл: {e}")
    

class PARSING(outLOGs):
    def __init__(self):
        return 
    
    def fSTAGE(self):
        url = "https://cchgeu.ru/education/programms/index.php"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"} 
        resp = requests.get(url, headers=headers).text
        soup = BeautifulSoup(resp, "lxml")
        tabl_class = soup.find(class_="table")
        line = tabl_class.find_all("tr")
        outLOGs.creating_file( f"[{datetime.datetime.now()}] СПИСОК специальностей факультета ФИТКБ получен.\n")
        name_OP = []
        address = []
        for i in range(21,34): ##ФИТКБ
            name_OP.append(line[i].find('a').text)
            address.append("https://cchgeu.ru" +line[i].find('a')["href"])
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Названия и ссылки на специальности факультета ФИТКБ получены.\n")
        BD.filling_BD_OP(name_OP,address)
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Сохранение в базу данных.\n")

        PARSING.sSTAGE(address)

        name_OP.clear()
        address.clear()

    def sSTAGE(address):
        url = address

        s_address = []
        s_title = []
        s_information = []

        for i in range(len(url)):
            information = []
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
            resp = requests.get(url[i], headers=headers).text
            soup = BeautifulSoup(resp, "lxml")
            about_us = soup.find(class_ = 'bring-left')
            line = about_us.find_all('a')[-1]
            s_address.append("https://cchgeu.ru" + line['href'])
            s_title.append(line.text)
            about_us = soup.find(class_ = 'program-detail')
            inf = about_us.find_all('p')
            for j in inf:
                predl = []
                if(len(j.text) > 100): 
                    predl.append(j.text.replace('\n', '').replace('\t', '').replace('\xa0', ' ').replace('\r ', '') )
                else: continue
                information.append(predl)
            time.sleep(7)
            combined_text = '\n'.join(' '.join(i) for i in information)
            s_information.append(combined_text)

        outLOGs.creating_file( f"[{datetime.datetime.now()}] Название, ссылка на сайт с файлами и информация об специальности получены.\n")
        BD.filling_BD_ABOUT_OP(s_title, s_address, s_information)
        PARSING.thSTAGE(s_address)
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Сохранение в базу данных.\n")
        s_address.clear()
        s_title.clear()
        s_information.clear()

    def thSTAGE(address):
        url = address
        for ii in range(len(url)):
            result = []
            th_title = []
            th_name = []
            th_address = []
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
            resp = requests.get(url[ii], headers=headers).text
            soup = BeautifulSoup(resp, "lxml")
            file = soup.find(class_ = 'program-detail')
            
            title = file.find_all('h5')
            for j in title:
                th_title.append(j.text) 
            adres = soup.find_all(class_ = 'wb-ba')
            for i in adres:
                th_name.append(i.text)
            if ii == 0:
                t = file.find('h5')
                sss = t.find_next('a')
                th_address.append("https://cchgeu.ru" + sss['href'])
            for i in adres:
                th_address.append("https://cchgeu.ru" +i['href'])
            BD.filling_BD_FILES_OP(ii,th_title,th_name,th_address)
            th_title.clear()
            th_name.clear()
            th_address.clear()
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Раздел файлов, название каждого опубликованного файла и его ссылка для скачивания получены.\n")
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Сохранение в базу данных.\n")


class BD(outLOGs):
    bd_name = "OTHENASHKOTORYNANEBESAH.db"
    bd = os.path.join("resources", bd_name )
    def __init__(self):
        return
    def create_BD(self):
        conn = sqlite3.connect(BD.bd)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS OP (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            TITLE_OP TEXT,
            LINK_OP TEXT
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ABOUT_OP (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_OP INTEGER,
            TITLE_OP TEXT,
            LINK_OP TEXT,
            INFORMATION TEXT,
            FOREIGN KEY (id_OP) REFERENCES OP(id)
        )""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS FILES_OP (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_ABOUT_OP INTEGER,                       
            TITLE_OP TEXT NULL,
            FILE_NAME TEXT,
            FILE_LINK TEXT,
            TITLE_FILE TEXT ,
            BASIS_FILE TEXT ,
            FOREIGN KEY (id_ABOUT_OP) REFERENCES ABOUT_OP(id)
        )""")
        outLOGs.creating_file( f"[{datetime.datetime.now()}] Создание новой директориии добавление в нее базу данных({BD.bd})\n")
        conn.commit()
        conn.close()
        return


    def filling_BD_OP(address, name):
        conn = sqlite3.connect(BD.bd)
        cursor = conn.cursor()
        for i in range(len(address)):
            cursor.execute('''
                    INSERT OR REPLACE INTO OP(TITLE_OP,LINK_OP)
                    VALUES (?, ?)
                    ''', (address[i], name[i]))
            conn.commit()
        conn.close()
        return
    
    def filling_BD_ABOUT_OP(s_name, s_address,  s_information):
        conn = sqlite3.connect(BD.bd)
        cursor = conn.cursor()
        for i in range(len(s_name)):
            cursor.execute('''
                INSERT OR REPLACE INTO ABOUT_OP(id_OP,TITLE_OP,LINK_OP, INFORMATION)
                VALUES (?, ?, ?, ?)
                ''', (i+1, s_name[i], s_address[i], s_information[i]))
            conn.commit()
        conn.close()
        return
    
    def filling_BD_FILES_OP(i, th_title, th_name,  th_address):
        conn = sqlite3.connect(BD.bd)
        cursor = conn.cursor()
        for j in range (len(th_name)):
            cursor.execute('''
                INSERT OR REPLACE INTO FILES_OP(id_ABOUT_OP, TITLE_OP, FILE_NAME, FILE_LINK, TITLE_FILE, BASIS_FILE)
                VALUES (?, ?, ?, ?,?,?)
                ''', (i+1 ,'', th_name[j], th_address[j], '', ''))
        conn.commit()

                # if '09.03.0' in th_name[j] and '20' in th_name[j] and len(th_name[j])  < 25:

        conn.close()
        return

   
