# OT_Game_2024 - Game Design Document - SK
Tento repozitár obsahuje implementáciu prototypu hry v Pygame, ktorá bola vytvorená ako súčasť štúdia objektovo-orientovaných technológií. Hra demonštruje základné herné mechaniky, ako sú práca s hernými objektmi, kolízie, spracovanie udalostí a interakcia so zvukmi. Tento repozitár môže slúžiť ako základný vzor alebo inšpirácia pre vývoj vlastných hier v Pygame.
#### Autor: Artsiom Ladziata
#### Vybraná téma: Farba ako herná mechanika

## 1 Uvod
Vytvorená hra je určená na demonštráciu v rámci predmetu „Objektové technológie“ a predstavuje funkčný prototyp projektu na záverečné hodnotenie. V tejto hre hráč ovláda kôš a snaží sa chytať padajúce lopty rôznych farieb, pričom sa vyhýba prekážkam a negatívnym efektom. Hra zahŕňa prvky ako správa času, bodov a bonusov, ako aj možnosť prepínania farieb koša na interakciu s loptami. Projekt demonštruje základy mechaník arkádových hier a môže slúžiť ako základ pre ďalší vývoj.

### 1.1 Inšpirácia
Catch the Ball

Catch the Ball je hra, v ktorej hráč ovláda kôš a snaží sa chytať padajúce lopty rôznych farieb, pričom musí preukázať rýchle reflexy a strategické myslenie. Koncept hry je založený na súboji hráča proti herným mechanikám, kde správne načasovanie a farba koša zohrávajú kľúčovú úlohu. Hráč môže získať body za chytené lopty, vyhýbať sa negatívnym efektom čiernych lôpt a využívať zlaté lopty na dočasné bonusy. Hra obsahuje rôzne prekážky, ktoré zvyšujú náročnosť, a umožňuje hráčovi zdokonaľovať sa postupným zvyšovaním skóre.
<br/>

![image](https://github.com/user-attachments/assets/b5e59f8f-45e4-45c2-86b9-fad6ed4c37a6)
<br/>
Obrázok 1 : Ukážka hry Catch the Ball

### 1.2 Herný zážitok
Cieľom hry Catch the Ball je, aby hráč získal čo najvyššie skóre počas obmedzeného časového intervalu. Hráč ovláda kôš, ktorým musí chytať farebné lopty padajúce zhora. Každá lopta prináša body, avšak nesprávne chytenie môže skóre znížiť alebo spôsobiť negatívny efekt. Hráč sa musí vyhýbať čiernym loptám, ktoré dočasne znemožnia ovládanie koša, a využívať špeciálne zlaté lopty, ktoré mu pomôžu v boji o čo najlepšie skóre. Rýchlosť hry sa postupne zvyšuje, čo vyžaduje rýchle reflexy a strategické rozhodovanie.

### 1.3 Vývojový softvér
__Pygame-CE:__ zvolený programovací jazyk.
__PyCharm 2024.1:__ vybrané IDE.

## Koncept
### 2.1 Prehľad hry
Hráč ovláda kôš a jeho úlohou je chytať farebné lopty, ktoré padajú z vrchu obrazovky. Každá lopta má svoju farbu a hráč musí prepínať farbu koša tak, aby zodpovedala farbe lopty, ktorú chce chytiť. Chytenie správnej lopty prináša body, zatiaľ čo nesprávne chytenie alebo premeškanie lopty vedie k strate bodov alebo iným penalizáciám. Cieľom je získať čo najviac bodov v obmedzenom časovom intervale.

### 2.2 Interpretácia témy (Catch the Ball)
"Catching the Ball" - Hráč čelí neustálemu prísunu lôpt, ktoré padajú rôznou rýchlosťou a z rôznych smerov. Úlohou hráča je správne prepínať farby koša, aby chytil čo najviac lôpt správnej farby. Hra obsahuje rôzne typy lôpt, ktoré môžu pridávať bonusové body, spôsobovať penalizácie alebo ovplyvňovať dynamiku hry (napr. spomalenie alebo zrýchlenie).

### 2.3 Základné mechaniky
Prepínanie farby koša: Hráč môže prepínať medzi dostupnými farbami koša stlačením klávesy, čím prispôsobuje kôš aktuálne padajúcej lopte.
Prekážky: Na obrazovke sa môžu objaviť prekážky, ktoré ovplyvňujú pohyb lôpt alebo hráča, čím pridávajú výzvu do hry.
Bonusové lopty: Zber špeciálnych lôpt môže hráčovi priniesť výhody, ako napríklad zvýšenie bodov, spomalenie hry, alebo naopak zrýchlenie v prípade penalizácie.
Časový limit: Hra je obmedzená na určitý časový interval, počas ktorého sa hráč snaží získať čo najviac bodov.
Dynamická obtiažnosť: S postupom hry sa zvyšuje rýchlosť lôpt, ich množstvo alebo sa pridávajú nové herné prvky, ako napríklad pohyblivé prekážky.

### 2.4 Návrh tried
* __Game:__ Trieda, ktorá obsahuje hlavnú hernú logiku (menu, hernú slučku, vyhodnotenie hry). Spravuje komunikáciu medzi ostatnými triedami, ako aj riadenie času a zvyšovanie obtiažnosti.
* __Basket:__ Trieda reprezentujúca kôš. Obsahuje mechaniku prepínania farieb, pohyb koša a detekciu kolízií s loptami.
* __Ball:__ Trieda zodpovedná za správu lôpt. Obsahuje generovanie lôpt, ich pohyb, interakciu s košom a efekty, ktoré jednotlivé lopty spôsobujú.
* __HUD:__ Trieda spravujúca užívateľské rozhranie. Zobrazuje skóre, čas, rekordy a iné dôležité informácie počas hry.
* __Obstacle:__ Trieda pre prekážky na hernej mape. Obsahuje logiku pre umiestnenie prekážok, ktoré ovplyvňujú pohyb lôpt a hráča, čím hra získava viac stratégií a výziev.
* __Level:__ Trieda, ktorá spravuje nastavenia jednotlivých úrovní (pozadie, počet a rýchlosť lôpt, umiestnenie prekážok). Zodpovedá za postupné zvyšovanie obtiažnosti hry.
* __Sounds:__ Trieda, ktorá spravuje zvukové efekty a hudbu. Obsahuje funkcie na prehrávanie zvukov pri interakciách (napr. chytenie lopty, premeškanie lopty, prepínanie farieb) a riadenie hudby na pozadí.



















