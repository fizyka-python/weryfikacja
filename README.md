# PESEL

Powszechny Elektroniczny System Ewidencji Ludności (PESEL) to centralny zbiór danych prowadzony w Polsce przez
Ministerstwo Informatyzacji na mocy ustawy o ewidencji ludności. Rejestr służy do gromadzenia podstawowych informacji
identyfikujących tożsamość i status administracyjno-prawny obywateli polskich oraz cudzoziemców zamieszkujących
na terenie Rzeczypospolitej Polskiej.

Każdy wpis w rejestrze jest określany unikatowym symbolem jednoznacznie identyfikującym osobę fizyczną. Potocznie
 mianem PESEL określa się również numer ewidencyjny osoby fizycznej wykorzystywany w tym rejestrze.

Numer PESEL jest to 11-cyfrowy stały symbol numeryczny jednoznacznie identyfikujący określoną osobę fizyczną.

Zbudowany jest z następujących elementów:
- zakodowanej daty urodzenia,
- liczby porządkowej,
- zakodowanej płci
- cyfry kontrolnej.

Przykładowa postać: `440514` `0145` `8`
- cyfry 1-6 (`440514`) – data urodzenia z określeniem stulecia urodzenia
- cyfry 7-10 (`0145`) – numer serii z oznaczeniem płci
- cyfra 10 (`5`) – płeć (parzysta: kobieta, nieparzysta: mężczyzna)
- cyfra 11 (`8`) – cyfra kontrolna

### Data urodzenia

Numeryczny zapis daty urodzenia przedstawiony jest w następującym porządku: dwie ostatnie cyfry roku, miesiąc i dzień.
Dla odróżnienia poszczególnych stuleci przyjęto następującą metodę kodowania:

- dla osób urodzonych w latach 1900 do 1999 – miesiąc zapisywany jest w sposób naturalny, tzn. dwucyfrowo od 01 do 12

- dla osób urodzonych w innych latach niż 1900–1999 dodawane są do numeru miesiąca następujące wielkości:
  - dla lat 1800–1899 – 80
  - dla lat 2000–2099 – 20
  - dla lat 2100–2199 – 40
  - dla lat 2200–2299 – 60.

Przyjęta metoda kodowania miesiąca urodzenia pozwala na rozróżnienie 5 stuleci.

### Cyfra kontrolna

Jedenasta cyfra jest cyfrą kontrolną, służącą do wychwytywania przekłamań numeru. Jest ona generowana na podstawie
pierwszych dziesięciu cyfr. Aby sprawdzić czy dany numer PESEL jest prawidłowy, należy, zakładając, że litery
*a*-*j* to kolejne cyfry numeru od lewej, obliczyć wyrażenie:

9×*a* + 7×*b* + 3×*c* + 1×*d* + 9×*e* + 7×*f* + 3×*g* + 1×*h* + 9×*i* + 7×*j*

Jeżeli ostatnia cyfra otrzymanego wyniku nie jest równa cyfrze kontrolnej, to znaczy, że numer zawiera błąd[18].

Przykład dla numeru PESEL `44051401358`:

    9×4 + 7×4 + 3×0 + 1×5 + 9×1 + 7×4 + 3×0 + 1×1 + 9×3 + 7×5 = 169

Wyznaczamy resztę z dzielenia sumy przez 10:

    169 % 10 = 9

Wynik 9 nie jest równy ostatniej cyfrze numeru PESEL, czyli 8, więc numer jest błędny.

#### Metoda równoważna

Powyższa metoda sprowadza się do obliczenia sumy:

1×*a* + 3×*b* + 7×*c* + 9×*d* + 1×*e* + 3×*f* + 7×*g* + 9×*h* + 1×*i* + 3×*j*

(gdzie litery oznaczają kolejne cyfry numeru), a następnie sprawdzenia czy reszta z dzielenia przez 10 jest zerem.
Innymi słowy, jeśli ostatnia cyfra otrzymanej sumy jest zerem, to numer PESEL jest formalnie poprawny, w przeciwnym
razie numer jest błędny.

## Zadanie

Napisz funkcję o nazwie `check_pesel` weryfikującą numer PESEL oraz podający datę urodzenia osoby, która ten numer
posiada.

Funkcja ma przyjmować numer PESEL jako łańcuch tekstowy oraz zwracać wartość `True` bądź `False` w zależności od
poprawności numeru PESEL. Ponadto funkcja ma drukować ekranie datę urodzenia w formacie *dzień miesiąc rok*,
na przykład: `14 maja 1944`.

Każde odstępstwo od specyfikacji spowoduje niezaliczenie zadania.




# Sprawdzanie poprawności numeru karty kredytowej

Algorytm Luhna, zwany także jako algorytm ”mod 10” jest przykładem prostej sumy kontrolnej wykorzystywany do walidacji
różnych numerów, takich jak numery kart płatniczych, numery IMEI. Nazwa algorytmu pochodzi od nazwiska jego twórcy
Hansa Petera Luhna, niemieckiego naukowca, pracownika IBM.

Algorytm wykrywa wszelkie pomyłki zamiany pojedynczej cyfry, jak również większości zamian kolejności sąsiednich cyfr.
 Nie wykrywa on jednak zamiany sekwencji 09 na 90 (i  na odwrót). Wykrywa 7 z 10 możliwych błędów bliźniaczych
 (nie wykryje 22 ↔ 55, 33 ↔ 66 lub 44 ↔ 77).


Sprawdzenie numeru karty płatniczej - algorytm:
1. Obliczenia rozpoczynamy od cyfry, która jest najbardziej na prawo i przesuwając się w lewo podwajamy co drugą cyfrę.
2. Jeśli w wyniku podwojenia otrzymamy liczbę dwucyfrową, dodajemy do siebie cyfry otrzymując liczbę jednocyfrową
   np. 14 zapisujemy jako 5 (1+4)
3. Dodajemy do siebie wszystkie cyfry, podwojone i niepodwojone.
4. Jeśli suma mod 10 równa jest 0, numer jest prawidłowy.

### Przykład

Numer karty płatniczej: `4417123456789113`

- Podwajamy co drugą cyfrę zaczynając od prawej (w nawiasie kwadratowym podano indeks pozycji):

  - [15] 2 × 4 = 8
  - [14] 1 × 4 = 4
  - [13] 2 × 1 = 2
  - [12] 1 × 7 = 7
  - [11] 2 × 1 = 2
  - [10] 1 × 2 = 2
  - [9] 2 × 3 = 6
  - [8] 1 × 4 = 4
  - [7] 2 × 5 = 10 (suma cyfr: 1)
  - [6] 1 × 6 = 6
  - [5] 2 × 7 = 14 (suma cyfr: 5)
  - [4] 1 × 8 = 8
  - [3] 2 × 9 = 18 (suma cyfr: 9)
  - [2] 1 × 1 = 1
  - [1] 2 × 1 = 2
  - [0] 1 × 3 = 3
    
- Dodajemy otrzymane liczby do siebie: `8 + 4 + 2 + 7 + 2 + 2 + 6 + 4 + 1 + 6 + 5 + 8 + 9 + 1 + 2 + 3 = 70`

- Wykonujemy operację mod 10: `70 % 10 = 0`

- Otrzymany wynik jest zerem czyli numer karty jest poprawny


## Zadanie

Napisz funkcję o nazwie `check_card` weryfikującą numer karty kredytowej. Funkcja ma przyjmować numer karty jako
łańcuch tekstowy i zwracać `True` (numer poprawny) bądź `False` (numer zły).
