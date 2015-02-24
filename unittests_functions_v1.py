def is_even(number):
    return not number % 2


def square(number):
    return number**2


def is_palindrom(word):
    return word == word[::-1]


def is_prime(number):
    for i in xrange(2, number):
        if not number % i:
            break
    else:
        return number > 1
    return False


def add_dot(words_list=None):
    if words_list is None:
        words_list = ['example', 'sentence']
    words_list += ['.']
    return ' '.join(words_list)


def count_letters(words_list):
    return {word: len(word) for word in words_list}


def multiply_by_2(number):
    return number * 2
