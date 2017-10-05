# -*- coding: utf-8 -*-
import pymysql
import os
import sys
sys.path.append('C:/Users/Iga')
import password.haslo
# print (os.getcwd())


class User:
    def __init__(self, id, login, imie, nazwisko, data_ur, plec, miasto):
        self.id = id
        self.login = login
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_ur = data_ur
        self.plec = plec
        self.miasto = miasto       
       
class Husaria_py:
    userLogged = None
    isLogged = False
    def __init__(self):
        haslo = password.haslo.hus_admin
        self.conn = pymysql.connect('localhost','hus_admin',haslo,'husaria_python', charset='utf8')
        self.cursor = self.conn.cursor()
    def logowanie(self):
        try:
            login = input('Podaj swój login: ')
            haslo = input('Podaj swoje haslo: ')
            self.cursor.execute("select l.id_zawodnika, l.login, z.imie, z.nazwisko, z.data_ur, z.plec, z.miasto_zawodnika from logowanie l join zawodnicy z on l.id_zawodnika=z.id_zawodnika  where l.login = '%s' and l.haslo = '%s'" % (login, haslo))
            TG = self.cursor.fetchall()
            if(len(TG)==0):
                print('Błędne hasło.')
                return False
            else:
                print('Zalogowałeś się poprawnie.')
                for col in TG:
                    self.userLogged = User(col[0], col[1], col[2], col[3], col[4], col[5], col[6])
               # hus1.konsolaUsera()
                return login
        except: 
            print('Błędny format.')
    def test_log(self):
        l = 0
        while (l < 3):
            decision = self.logowanie()
            if decision:
                return True
            else:
                l += 1
                if(l == 3):
                    print('Podałeś trzykrotnie błędne hasło. Zażyj Bilobil')
                    return False
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
        while(self.isLogged):
            konsola = input('Co chcesz zrobić? \n (1) - moje wyniki \n (2) - pokaż ligę   \n (3) - zmień hasło \n (4) - wyloguj ').upper()
            if(konsola == '1'):
                self.mojeWyniki()
            if(konsola == '2'):
                self.ligaHus()
            if(konsola == '3'):
                self.zmianaHasla()
            elif(konsola =='4'):
                print('Powodzenia w dalszych biegach.')
                break
            else:
                break
    def mojeWyniki(self):
        self.cursor.execute("select * from moje_wyniki where login = '%s'" % (self.userLogged.login))    
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
    def zmianaHasla(self):
        while(True):
            noweHaslo = input('Podaj nowe hasło: ')
            potwHaslo = input('Potwierdź nowe hasło: ')
            if(noweHaslo == potwHaslo):
                print('Hasło zostało zmienione')
                self.test_log
                break
            else:
                print('Hasło niezgodne. Spróbuj jeszcze raz.')
                self.zmianaHasla
            self.cursor.execute("update logowanie set haslo='%s' where login='%s'" % (noweHaslo, self.userLogged.login))
            self.conn.commit()
            break
    def start(self):
        self.isLogged = hus1.test_log()
        if(self.isLogged):
            self.konsolaUsera()
        else:
            print('Błąd logowania')        
        
hus1 = Husaria_py()
hus1.start()

