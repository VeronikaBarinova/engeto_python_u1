# Scraper uloha c. 3

## Popis
Slouzi pro stahovani dat z vybranych URL a ukladani do souboru ve formatu CSV. Program je napsan v jazyce Python a pouziva knihovny requests, BeautifulSoup a pandas.

## Instalace knihoven
Pouzite knihovny jsou ulozeny v souboru requirements.txt. Pro jejich instalaci staci spustit nasledujici prikaz:
```bash
$ pip3 install -r requirements.txt
```

## Spuštění programu
Spuštění programu je možné s následujícími argumenty:
```bash
$ python3 scraper.py '<url>' <output_file>
```

Vysledny soubor se ulozi do output_file.

## Ukázka projektu

Výsledky hlasovani pro okres Prosťejov:

1. argument ```https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103```
2. argument ```vylsedky_prostejova.csv```

Spusteni programu:
```python3 scraper.py https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103 vylsedky_prostejova.csv```

Prubeh stahovaní:
```
STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
UKLADAM DATA DO SOUBORU: vylsedky_prostejova.csv
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
529303,Benešov,13 104,8 485,8 437,1 052,10,2,624,3,802,597,109,35,112,6,11,948,3,6,414,2 577,3,21,314,5,58,17,16,682,10
532568,Bernartice,191,148,148,4,0,0,17,0,6,7,1,4,0,0,0,7,0,0,3,39,0,0,37,0,3,0,0,20,0
```