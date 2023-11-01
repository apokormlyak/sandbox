from itertools import groupby
from functools import reduce
from math import sqrt, ceil


def sort_array(source_array):
    sorted_array = source_array[:]
    min_i = 0
    odd_arr = list(filter(lambda x: x % 2 != 0, source_array))
    for n, i in enumerate(source_array):
        if odd_arr:
            min_i = min(odd_arr)
        if i % 2 != 0:
            sorted_array[n] = min_i
            odd_arr.remove(min_i)
    return sorted_array


def solution(number):
    # if number < 0:
    #     return 0
    # else:
    #     mul = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(number)))
    #     return sum(mul)
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


def duplicate_encode(word):
    #your code here
    word = word.lower()
    new_word = ''
    for n, let in enumerate(word):
        if let in word[:n] or let in word[n+1:]:
            new_word += ')'
        else:
            new_word += '('
    return new_word
    # return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


def duplicate_count(text):
    # Your code goes here
    return len(set(''.join([c if text.lower().count(c) > 1 else "" for c in text.lower()])))


def digital_root(n):
    # n = list(str(n))
    # while len(n)>1:
    #     new_n = 0
    #     for i in n:
    #         new_n += (int(i))
    #     n = list(str(new_n))
    # return new_n

    #alternative
    while n > 9:
        n = sum(map(int, str(n)))
    return n


def unique_in_order(sequence):
    if len(sequence) > 0:
        new_s = [n for i, n in enumerate(sequence) if i != len(sequence)-1 and n != sequence[i+1]]
        new_s.append(sequence[-1])
        return new_s
    else:
        return []


#kata
def sum_for_list(lst):
    primes = get_primes_for_lst(lst)
    res = [(i, num) for i in primes for num in lst if num % i == 0]
    sum_for_i = []
    for k, item in groupby(res, lambda x: x[0]):
        n = [k, sum(e[1] for e in list(item) if e[1] is not None)]
        sum_for_i.append(n)

    print(sum_for_i)
    return sum_for_i


def get_primes_for_lst(lst):
    abs_lst = list(map(lambda x: abs(x), lst))
    primes = [2]
    for k in range(2, max(abs_lst)):
        for j in range(2, ceil(sqrt(k))+1):
            if k % j == 0:
                break
            elif j == ceil(sqrt(k)):
                primes.append(k)
    print(sorted(set(primes)))
    return sorted(set(primes))



if __name__ == '__main__':
    # print(sort_array([5, 3, 2, 8, 1, 4]))
    # print(solution(10))
    # print(duplicate_encode('zqKcPeE)XqqzhY!OtakM(QJEVyGbU'))
    # print(duplicate_count('hRHeello'))
    # print(digital_root(942))
    # print(unique_in_order([1, 2, 2, 3, 3, 4, 4, 4, 6, 6]))
    sum_for_list([43630, -104189, -248973, -208168, -488266, 99068, -334695, -970931, -934295, -855636, 529939, -640595, -678072, -469501])