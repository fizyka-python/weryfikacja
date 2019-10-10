# coding: utf8
"""
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
"""


def check_card(number):
    pass
