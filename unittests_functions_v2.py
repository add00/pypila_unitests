def is_even(number):
    return not number & 1


def square(number):
    return number * number


def is_palindrom(word):
    if len(word) == 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrom(word[1:-1])
        return False


def is_prime(number):
    for i in xrange(3, number):
        if not number % i:
            return False
    return True


def add_dot(words_list=['example', 'sentence']):
    words_list += ['.']
    return ' '.join(words_list)


def count_letters(words_list):
    result = {}
    for word in words_list:
        result[word] = len(word)
    return result


def multiply_by_2(number):
    return number << 2
