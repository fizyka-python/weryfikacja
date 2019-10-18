# coding: utf8
import sys
import os

from contextlib import contextmanager
from io import StringIO

import unittest


import karta
import pesel as pesel_module


@contextmanager
def capture_stdout():
    old_out = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_out


class TestPESEL(unittest.TestCase):

    _months = ('stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca',
                'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia')

    def do_test_pesel(self, pesel):
        with capture_stdout() as out:
            ok = pesel_module.check_pesel(pesel)
        self.assertTrue(ok, "Funkcja nie zwróciła True dla poprawnej wartości PESEL")
        birthday = out.getvalue().strip()
        if birthday.startswith('0'): birthday = birthday[1:]
        month = int(pesel[2:4])
        year = int(pesel[0:2])
        century = month // 20
        if century == 4:
            year += 1800
        else:
            year += 1900 + 100 * century
        self.assertEqual(birthday.lower(), f"{int(pesel[4:6])} {self._months[(month%20)-1]} {year}",
                         "Funkcja nie wydrukowała daty urodzenia według wskazanego formatu")

    def test_pesel_poprawny_XX_wiek(self):
        self.do_test_pesel('90090515836')

    def test_pesel_poprawny_XXI_wiek(self):
        self.do_test_pesel('01261051813')

    def test_pesel_poprawny_XIX_wiek(self):
        self.do_test_pesel('87832165181')

    def test_pesel_niepoprawny(self):
        self.assertFalse(pesel_module.check_pesel('90090525836'),
                         "Funkcja nie zwróciła False dla niepoprawnej wartości PESEL")
        self.assertFalse(pesel_module.check_pesel('01261031813'),
                         "Funkcja nie zwróciła False dla niepoprawnej wartości PESEL")
        self.assertFalse(pesel_module.check_pesel('87832165581'),
                         "Funkcja nie zwróciła False dla niepoprawnej wartości PESEL")

    def test_pesel_zbyt_krótki(self):
        self.assertFalse(pesel_module.check_pesel('123456789'),
                         "Funkcja nie zwróciła False dla niepoprawnej i zbyt krótkiej wartości PESEL")

    def test_pesele_w_pliku(self):
        pesel_module.check_pesel_file('data.txt')
        try:
            with open('data.out') as result:
                correct = ['5 września 1990', '21 marca 1887', '-', '10 czerwca 2001', '-']
                self.assertEqual(correct, [line.rstrip() for line in result.readlines()])
        except FileNotFoundError:
            self.fail("Nie znaleziono pliku wynikowego")


class TestCard(unittest.TestCase):

    def test_karta_poprawna_16_cyfr(self):
        self.assertTrue(karta.check_card('4929134138580797'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('4152651010436721'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('4539667947868665'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('4024007164776170'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('4485154991816266'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('5443972305885927'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('5114869172331548'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('5578916533101687'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('5406733474061897'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('5419564871798376'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('6011395236301055'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('6011432269128210'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('6011636118723985'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('6011631220718007'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('6011856166915099'), "Funkcja nie zwróciła True dla poprawnego numeru karty")

    def test_karta_poprawna_15_cyfr(self):
        self.assertTrue(karta.check_card('370594756527911'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('379451233726940'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('341377872063524'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('376766310514015'), "Funkcja nie zwróciła True dla poprawnego numeru karty")
        self.assertTrue(karta.check_card('375692442227519'), "Funkcja nie zwróciła True dla poprawnego numeru karty")

    def test_karta_poprawna_11_cyfr(self):
        self.assertTrue(karta.check_card('79927398713'), "Funkcja nie zwróciła True dla poprawnego numeru karty")

    def test_karta_niepoprawna(self):
        self.assertFalse(karta.check_card('79927398710'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398711'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398712'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398714'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398715'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398716'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398717'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398718'), "Funkcja nie zwróciła False dla błędnego numeru karty")
        self.assertFalse(karta.check_card('79927398719'), "Funkcja nie zwróciła False dla błędnego numeru karty")
