def is_interesting(number, awesome_phrases):
    numbers = [int(number) for number in str(number)]
    print(f'len number {len(numbers)}')
    print(f'len set {len(set(numbers))}')
    print(f'number {number}')
    if len(numbers) == (len(set(numbers)) * len(numbers)):  # Every digit is the same number: 1111
        return 2
    elif sum(numbers)==numbers[0]:  # Any digit followed by all zeros: 100, 90000
        return 2
    elif len(numbers)== len(set(numbers)): #The digits are sequential, incementing †: 01234567890 0 before 1 and after 9
        if numbers==numbers.sort():
            return True
        else:
            print('nok')
    else:
        print('coś')
    print('----------------')



print(is_interesting(9000, []))
print(is_interesting(222, []))
print(is_interesting(12345689, []))
