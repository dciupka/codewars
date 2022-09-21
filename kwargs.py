"""How it works **kwarg"""

user = {'name': 'dawid', 'surname': 'Raccoon', 'age': 32}


def few_key_words_arg(**user):
    return user

few_key_words_arg(**user)