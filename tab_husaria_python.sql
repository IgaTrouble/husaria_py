create database husaria_python;
use husaria_python;

# tab_zawodnicy
CREATE TABLE zawodnicy (
    id_zawodnika smallint AUTO_INCREMENT UNIQUE NOT NULL,
    imie VARCHAR(20) NOT NULL,
    nazwisko VARCHAR(35) NOT NULL,
    data_ur DATE NOT NULL,
    plec char not null,
    miasto_zawodnika VARCHAR(15) NOT NULL,
    PRIMARY KEY (id_zawodnika));

# tab_zawody
CREATE TABLE zawody (
    id_zawodow int NOT NULL auto_increment,
    nazwa_zawodow VARCHAR(20) NOT NULL,
    miasto_zawodow varchar(30) not null,
    kraj_zawodow varchar(30) not null,
    data_od date not null,
    data_do date not null,
    PRIMARY KEY (id_zawodow)
);
# tab_dystans
CREATE TABLE dystans (
    id_dystansu INT AUTO_INCREMENT UNIQUE NOT NULL,
    nazwa_dystansu VARCHAR(20) NOT NULL,
    dystans_km DOUBLE,
    l_przeszkod smallint,
    data_biegu DATE NOT NULL,
    id_zawodow int,
    FOREIGN KEY (id_zawodow)
        REFERENCES zawody (id_zawodow),
    PRIMARY KEY (id_dystansu)
);
# tab_wyniki
 CREATE TABLE wyniki (
    id_wyniku INT UNIQUE AUTO_INCREMENT NOT NULL,
    id_zawodnika smallint,
    id_dystansu INT,
    miejsce_open INT NOT NULL,
    miejsce_elite INT default 0,
    miejsce_competitive INT DEFAULT 0,
    miejsce_masters_open INT DEFAULT 0,
    miejsce_masters_elite INT DEFAULT 0,
    czas TIME,
    punkty DOUBLE,
    PRIMARY KEY (id_wyniku),
    FOREIGN KEY (id_zawodnika)
        REFERENCES zawodnicy (id_zawodnika),
    FOREIGN KEY (id_dystansu)
        REFERENCES dystans (id_dystansu)
);
# tab_logowanie
CREATE TABLE logowanie (
    id_zawodnika smallint,
    rola varchar(15) default 'user', 
    login varchar(25) UNIQUE NOT NULL,
    haslo varchar(15) UNIQUE NOT NULL,
    PRIMARY KEY (login),
    FOREIGN KEY (id_zawodnika)
        REFERENCES zawodnicy (id_zawodnika)
);

create view tab_glowna as select imie,
    nazwisko,
    nazwa_dystansu,
    nazwa_zawodow,
    miasto_zawodow,
    miejsce_open,
    miejsce_elite,
    miejsce_competitive,
    czas,
    data_biegu
FROM
    zawodnicy,
    wyniki,
    zawody,
    dystans
WHERE
    zawodnicy.id_zawodnika = wyniki.id_zawodnika
        AND wyniki.id_dystansu = dystans.id_dystansu
        AND dystans.id_zawodow = zawody.id_zawodow;

select * from tab_glowna;