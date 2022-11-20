def from_roman(roman):
    R2M = {'M': 1000, 'i': 900, 'D': 500, 'j': 400, 'C': 100, 'k': 90, 'L': 50, 'l': 40, 'X': 10, 'm': 9, 'V': 5,
           'n': 4, 'I': 1}
    roman = roman.replace('CM', 'i').replace('CD', 'j').replace('XC', 'k').replace('XL', 'l').replace('IX',
                                                                                                      'm').replace('IV',
                                                                                                                   'n')
    return sum(R2M[i] for i in roman)


def to_roman(num):
    R2M = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    string = ''
    for k, v in R2M.items():
        print(f'k,v {k,v}')
        count = num // v        #num sie miesci  w v ile razy?
        print(f'count {count}')
        num %= v              #reszta z dzielenia num prze v 900%1000  == 900
        print(f'num {num}')
        print(f'value {v}')
        string += count * k  # to tworzy nowego str = count *K
        print('-----------------------------------')
    return string

print(to_roman(900))