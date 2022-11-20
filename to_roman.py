'''
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
Examples

RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
class RomanNumerals:

    def to_roman(val):
        return ''

    def from_roman(roman_num):
        return 0

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
'''


def to_roman(val):
    integer_digit_list = [int(ch) for ch in str(val).split()[0]]
    roman_list = []
    for index in range(len(integer_digit_list)):
        # 1-9
        if len(integer_digit_list) == 1:
            if integer_digit_list[0] != 0:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'I')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('I')
                    roman_list.append('V')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('V')
                    roman_list.append((integer_digit_list[index] - 5) * 'I')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('IX')
        # 10-99
        if len(integer_digit_list) == 2:
            if index == 0:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'X')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('X')
                    roman_list.append('L')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('L')
                    roman_list.append((integer_digit_list[index] - 5) * 'X')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('XC')
            if index != 0:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'I')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('I')
                    roman_list.append('V')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('V')
                    roman_list.append((integer_digit_list[index] - 5) * 'I')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('IX')
        # 100-999
        if len(integer_digit_list) == 3:
            if index == 0:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'C')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('C')
                    roman_list.append('D')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('D')
                    roman_list.append((integer_digit_list[index] - 5) * 'C')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('CM')
            if index == 1:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'X')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('X')
                    roman_list.append('L')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('L')
                    roman_list.append((integer_digit_list[index] - 5) * 'X')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('XC')

            if index == 2:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'I')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('I')
                    roman_list.append('V')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('V')
                    roman_list.append((integer_digit_list[index] - 5) * 'I')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('IX')
        # 1000-9999
        if len(integer_digit_list) == 4:
            if index == 0:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'M')

            if index == 1:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'C')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('C')
                    roman_list.append('D')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('D')
                    roman_list.append((integer_digit_list[index] - 5) * 'C')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('CM')
            if index == 2:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'X')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('X')
                    roman_list.append('L')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('L')
                    roman_list.append((integer_digit_list[index] - 5) * 'X')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('XC')

            if index == 3:
                if integer_digit_list[index] > 0 and integer_digit_list[index] < 4:
                    roman_list.append(integer_digit_list[index] * 'I')
                if integer_digit_list[index] > 3 and integer_digit_list[index] < 5:
                    roman_list.append('I')
                    roman_list.append('V')
                if integer_digit_list[index] >= 5 and integer_digit_list[index] < 9:
                    roman_list.append('V')
                    roman_list.append((integer_digit_list[index] - 5) * 'I')
                if integer_digit_list[index] > 8 and integer_digit_list[index] < 10:
                    roman_list.append('IX')
        result = ''
        for e in roman_list:
            result += e
    return result

#TESTY
#numbers  = [90,100,101,102,200,300,400,500,600,700,800,900,1000,1100]
#numbers  = [100,101,111,801,990,999,1000]
#numbers  = [1230]
# numbers = [1,2,3,4,5,6,7,8,9]
#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 40,
#           50, 91, 98, 99, 100]

#for num in numbers:
#    print(f'numer: {num} to rzymskie: {to_roman(num)}')





'''
import codewars_test as test
from solution import RomanNumerals

@test.describe('sample_tests')
def sample_tests():
    @test.it('to roman')
    def sample_tests_to():
        test.assert_equals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        test.assert_equals(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        test.assert_equals(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        test.assert_equals(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')
    @test.it('from roman')
    def sample_tests_from():
        test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        test.assert_equals(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        test.assert_equals(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        test.assert_equals(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')


'''
