'''
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
 The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

'''


def duplicate_count(text):
    new = []
    res = 0
    for l in text.upper():
        if l not in new:
            new.append(l)
        else:
            if l in new:
                res += 1
    return res


text = "Indivisibilities"

print(duplicate_count(text))
