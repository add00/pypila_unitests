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
        return True
    return False


def add_dot(words=None):
    if words is None:
        words = ['example', 'sentence']
    words += ['.']
    return ' '.join(words)


def count_letters(words):
    return {word: len(word) for word in words}


def multiply_by_2(number):
    return number * 2
