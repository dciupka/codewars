import unittest
from roman_arabian_sys import from_roman


class TestNums(unittest.TestCase):

    def test_one_digit(self):
        roman_num = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        roman_res = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for rom in roman_num:
            res = from_roman(rom)
            self.assertEqual(res, roman_res[roman_num.index(rom)])
            print(f'TEST: {rom}, równy {roman_res[roman_num.index(rom)]}')

    def test_two_digit(self):
        roman_num = ['X', 'XIV', 'XL', 'L', 'LX', 'XI', 'XIX', 'XXXIX','XC','XCIV','XCIX']
        roman_res = [10, 14, 40, 50, 60, 11, 19, 39,90,94,99]
        for rom in roman_num:
            res = from_roman(rom)
            self.assertEqual(res, roman_res[roman_num.index(rom)])
            print(f'TEST: {rom}, równy {roman_res[roman_num.index(rom)]}')

    def test_three_digit(self):
        roman_num = ['C','CI','CIV','CVII','CIX','CXIX','CXXIX','CXLIX','D','CMXCIX']
        roman_res = [100,101,104,107,109,119,129,149,500,999]
        for rom in roman_num:
            res = from_roman(rom)
            self.assertEqual(res, roman_res[roman_num.index(rom)])
            print(f'TEST: {rom}, równy {roman_res[roman_num.index(rom)]}')



if __name__ == '__main__':
    unittest.main()
