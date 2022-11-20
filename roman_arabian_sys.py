def from_roman(roman):
    R2M = {'M': 1000, 'i': 900, 'D': 500, 'j': 400, 'C': 100, 'k': 90, 'L': 50, 'l': 40, 'X': 10, 'm': 9, 'V': 5,
           'n': 4, 'I': 1}
    roman = roman.replace('CM', 'i').replace('CD', 'j').replace('XC', 'k').replace('XL', 'l').replace('IX',
                                                                                                      'm').replace('IV',
                                                                                                                   'n')
    return sum(R2M[i] for i in roman)
