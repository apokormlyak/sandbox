import string
import re
import math
from itertools import combinations


def get_count(sentence):
    return sum(1 for c in sentence if c in ['a', 'e', 'i', 'o', 'u'])


def pig_it(text):
    words = text.split(' ')
    for num, word in enumerate(words):
        if re.search("[a-zA-Z]", word):
            for c in string.punctuation:
                if c in word:
                    word = word.replace(c, '')
            new_word_2 = word[1:] + word[0] + 'ay'
            words[num] = word.replace(word, new_word_2)
    new_text = " ".join(words)
    return new_text


def comp(array1, array2):
    if array1 is not None and array2 is not None:

        my_a1 = array1.copy()
        my_a2 = array2.copy()

        if len(array1)==len(array2):
            for el in array1:
                try:
                    my_a1.remove(el)
                    my_a2.remove(el*el)
                except ValueError:
                    return False
            if len(my_a1) == len(my_a1) == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def dig_pow(n, p):
    # your code
    s_n = list(str(n))
    new_d = 0
    for el in s_n:
        el = pow(int(el), p)
        p = p+1
        new_d += int(el)
    print(new_d)
    if (new_d) % n == 0:
        return (new_d) / n
    return -1


def array_diff(a, b):
    for e in set(b):
        while e in a:
            a.remove(e)
    return a


def two_sum(numbers, target):
    my = numbers.copy()
    for n, num in enumerate(numbers):
        for p, my_num in enumerate(my):
            if num+my_num == target:
                return [n,p]


if __name__ == '__main__':
    # print(get_count('Hiiello you'))
    # print(pig_it('O tempora o mores !'))
    # print(comp([], []))
    # print(dig_pow(695,2))
    print(array_diff([1,2,2], [1]))
