# -*- coding: utf-8 -*-
import pymysql
import os
import sys
sys.path.append('C:/Users/Iga')
import password
print (os.getcwd())

class Husaria_py:
    def __init__(self):
        haslo = password.haslo.hus_admin
        self.conn = pymysql.connect('localhost','hus_admin',haslo,'husaria_py', charset='utf8')
