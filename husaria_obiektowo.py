# -*- coding: utf-8 -*-
import pymysql
import os
import sys
from datetime import datetime
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
'''        
class Koordynator(User):
    def __init__(self, id, login, imie, nazwisko, data_ur, plec, miasto):
'''        
        
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
                return True
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
            konsola = input('Co chcesz zrobić? \n (1) - moje wyniki \n (2) - pokaż ligę   \n (3) - zmień hasło \n (4) - dodaj zawodnika \n (5) - usuń zawodnika \n (6) - wyloguj ').upper()
            if(konsola == '1'):
                self.mojeWyniki()
            elif(konsola == '2'):
                self.ligaHus()
            elif(konsola == '3'):
                self.zmianaHasla()
            elif(konsola =='4'):
                self.cursor.execute("select rola from logowanie where login = '%s'" % (self.userLogged.login))
                res = self.cursor.fetchall()
                res = ((res[0])[0])                
                if (res != "admin"):
                    print('Nie masz uprawnień')
                else:
                    self.dodajHus()
            elif(konsola =='5'):
                self.cursor.execute("select rola from logowanie where login = '%s'" % (self.userLogged.login))
                res = self.cursor.fetchall()
                res = ((res[0])[0])
                print (res)
                if (res != "admin"):
                    print('Nie masz uprawnień')
                else:
                    self.usunHus()
            elif(konsola =='6'):   
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
        noweHaslo = input('Podaj nowe hasło: ')
        potwHaslo = input('Potwierdź nowe hasło: ')
        if(noweHaslo == potwHaslo):
            self.cursor.execute("update logowanie set haslo='%s' where login='%s'" % (noweHaslo, self.userLogged.login))
            self.conn.commit() 
            print('Hasło zostało zmienione')
        else:
            print('Hasło niezgodne. Spróbuj jeszcze raz.')
    def start(self):
        self.isLogged = hus1.test_log()
        if(self.isLogged):
            self.konsolaUsera()
        else:
            print('Błąd logowania')
    def dodajHus(self):
        imie_log = input('Podaj imię: ')
        nazwisko_log = input('Podaj nazwisko: ')
        data_ur = datetime.strptime(input('Podaj datę urodzenia: '),'%Y/%m/%d').date()
        plec = input('Podaj płeć (K/M): ').upper()
        miasto_zawodnika = input('Podaj miasto zawodnika: ').upper()
        self.cursor.execute("insert into zawodnicy(imie, nazwisko, data_ur, plec, miasto_zawodnika) values ('%s', '%s', '%s', '%s', '%s')" % (imie_log, nazwisko_log, data_ur, plec, miasto_zawodnika))
        self.conn.commit() 
        self.cursor.execute("select id_zawodnika from zawodnicy where imie = '%s' and nazwisko = '%s'" % (imie_log, nazwisko_log))
        id_zawodnika = self.cursor.fetchall()
        lista = int(((id_zawodnika[0])[0]))
        login = input('Podaj login zawodnika: ')
        haslo = input('Podaj hasło zawodnika: ')
        self.cursor.execute("insert into logowanie (id_zawodnika, login, haslo) values ('%i', '%s','%s')" % (lista, login, haslo))
        self.conn.commit()
        print('Zawodnik został dodany')
    def usunHus(self):
        nazwisko_us = input('Podaj nazwisko zawodnika, którego chcesz usunąć? ')
        potwierdzenie = input('Czy na pewno chcesz usunąć zawodnika: ' + (nazwisko_us) +'(T/N) ')
        if potwierdzenie == 'T':
            self.cursor.execute("select id_zawodnika from zawodnicy where nazwisko = '%s'" % nazwisko_us)
            id_zawodnika_us = self.cursor.fetchall()
            id_zawodnika_us = int(((id_zawodnika_us[0])[0]))
            self.cursor.execute("delete from logowanie where logowanie.id_zawodnika = '%i'" % (id_zawodnika_us))
            self.cursor.execute("delete from zawodnicy where nazwisko='%s'" % (nazwisko_us))
            self.conn.commit()
            print('Zawodnik został usunięty')
        else:
            print('Usuwanie się nie powiodło')
            
    def ligaHus(self):
        self.cursor.execute("select id_wyniku, miejsce_open, punkty from wyniki")  
        LH = self.cursor.fetchall()
        for v in LH:
            id_wyniku = v[0]
            miejsce_open= v[1]
            punkty = v[2]
            
            if (v[2] == None):
                if (v[1] == 1):
                    punkty = 100
                elif (v[1] == 2):
                    punkty = 95 
                elif (v[1] == 3):
                    punkty = 90
                elif (v[1] > 3 and v[1] < 11):
                    punkty = 80                
                elif (v[1] > 10 and v[1] <= 70):
                    punkty = 90-v[1]
                else:
                    punkty = 1
                self.waga()        
            self.cursor.execute("update wyniki set punkty = '%d' where id_wyniku= '%i'" % (punkty, id_wyniku));                       
            self.conn.commit()                   
        self.ligaWyniki()       
  
    def waga (self):
        self.cursor.execute("select id_wyniku, dystans_km, nazwa_zawodow, punkty from wyniki_glowna")  
        LW = self.cursor.fetchall()
        wagaKM = 0
        wagaZ = 0
        for v in LW:
            id_wyniku = v[0]
            dystans_km = v[1]
            nazwa_zawodow = v[2]
            punkty =v[3]
            if (v[1] <10):
                wagaKM = 1.0
            elif (v[1] < 20):
                wagaKM = 1.5 
            elif (v[1] > 21):
                wagaKM = 1.9                
            else:
                wagaKM = 1
            punkty = round(punkty * wagaKM,2)
            if (v[2] == "Runmageddon"):
                wagaZ = 1.0 
            elif (v[2] =="Spartan"):
                wagaZ = 1.5               
            elif (v[2] == "Barbarian"):
                wagaZ = 2.0
            punkty = round(punkty * wagaZ,2)
            self.cursor.execute("update wyniki set punkty = '%d' where id_wyniku= '%i'" % (punkty, id_wyniku));
            self.conn.commit()  
            
            
    def ligaWyniki(self):
        self.cursor.execute("select id_zawodnika, imie, nazwisko, sum(punkty) as razem from wyniki_glowna group by id_zawodnika order by razem desc") 
        TG = self.cursor.fetchall()
        print('%10s|%15s|%15s|%15s|' % ('miejsce', 'imie', 'nazwisko', 'punkty'))  
        id=0
        for v in TG:
            id+=1
            imie = v[1]
            nazwisko = v[2]
            punkty =v[3]
            print('%10s|%15s|%15s|%15s|' % (id, imie, nazwisko, punkty))

hus1 = Husaria_py()
hus1.start()
