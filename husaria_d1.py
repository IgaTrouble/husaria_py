# -*- coding: utf-8 -*-
import pymysql
import os
import sys
sys.path.append('C:/Users/Iga')
import password.haslo
# print (os.getcwd())

class Husaria_py:
    def __init__(self):
        haslo = password.haslo.hus_admin
        self.conn = pymysql.connect('localhost','hus_admin',haslo,'husaria_python', charset='utf8')
        self.cursor = self.conn.cursor()
    def logowanie(self):
        global login
        try:
            login = input('Podaj swój login: ')
            haslo = input('Podaj swoje haslo: ')
            self.cursor.execute("select * from logowanie where login = '%s' and haslo = '%s'" % (login, haslo))
            TG = self.cursor.fetchall()
           # print(TG)
            if(len(TG)==0):
                print('Błędne hasło.')
                return False
            else:
                print('Zalogowałeś się poprawnie.')
                hus1.konsolaUsera()
                return True
        except: 
            print('Błędny format.')
 
    def test_log(self):
        l = 0
        while (l < 3):
            decision = self.logowanie()
            if decision:
                break
            else:
                l += 1
                if(l == 3):
                    print('Podałeś trzykrotnie błędne hasło. Zażyj Bilobil')
    def select(self):
        self.cursor.execute('select * from tab_glowna')
        TG = self.cursor.fetchall()
        print('%10s|%12s|%15s|%15s|%20s|%3i|%3i|%3i|%8s|%10s|)' % ('imię', 'nazwisko', 'dystans', 'bieg', 'miasto', 'miejsce_open', 'miejsce_elite', 'miejsce_competitive', 'czas', 'data biegu'))
        for v in TG:
            imie = v[0]
            nazwisko = v[1]
            nazwa_dystansu = v[2]
            nazwa_zawodow = v[3]
            miasto_zawodow = v[4]
            miejsce_open = v[5]
            miejsce_elite = v[6]
            miejsce_competitive = v[7]
            czas = v[8]
            data_biegu = v[9]
            print('%10s|%12s|%15s|%15s|%20s|%3i|%3i|%3i|%8s|%10s|' % (imie, nazwisko, nazwa_dystansu, nazwa_zawodow, miasto_zawodow, miejsce_open, miejsce_elite, miejsce_competitive, czas, data_biegu))
    def konsolaUsera(self):
        while(self.logowanie):
            konsola = input('Co chcesz zrobić? \n (1) - moje wyniki \n (2) - pokaż ligę   \n (3) - wyloguj ').upper()
            if(konsola == '1'):
                print(login)
                self.mojeWyniki()
            if(konsola == '2'):
                self.ligaHus()
            elif(konsola =='3'):
                print('Powodzenia w dalszych biegach.')
                break
            else:
                break
    def mojeWyniki(self):
        self.cursor.execute("select * from moje_wyniki where login = '%s'" % (login))    
        TG = self.cursor.fetchall()
        print('%10s|%12s|%-15s|%-15s|%-20s|%15s|%15s|%20s|%8s|%10s|' % ('imię', 'nazwisko', 'dystans', 'bieg', 'miasto', 'miejsce_open', 'miejsce_elite', 'miejsce_competitive', 'czas', 'data biegu'))
        for v in TG:
            imie = v[0]
            nazwisko = v[1]
            nazwa_dystansu = v[2]
            nazwa_zawodow = v[3]
            miasto_zawodow = v[4]
            miejsce_open = v[5]
            miejsce_elite = v[6]
            miejsce_competitive = v[7]
            czas = v[8]
            data_biegu = v[9]
            print('%10s|%12s|%-15s|%-15s|%-20s|%15s|%15s|%20s|%8s|%10s|' % (imie, nazwisko, nazwa_dystansu, nazwa_zawodow, miasto_zawodow, miejsce_open, miejsce_elite, miejsce_competitive, czas, data_biegu))              
hus1 = Husaria_py()
hus1.test_log()