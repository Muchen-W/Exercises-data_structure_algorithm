def reverseList(data):
    data_reversed = list()
    data_len = len(data)
    for i in range(data_len):
        data_reversed.append(data[data_len-1-i])
    return data_reversed


def pair_product_odd(data):
    data_len = len(data)
    for i in range(data_len-1):
        for j in range(i+1, data_len):
            if data[i] & data[j] & 1 == 1:
                return True
    return False


def isDistinct(data):    # slow
    return len(data) == len(set(data))


def is_distinct(data):    # fast
    result = dict()
    for item in data:
        if item in result:
            result[item] += 1
            return False
        else:
            result[item] = 1
    return True


def shuffle(data):
    import random
    data_len = len(data)
    for i in range(data_len-1):
        index = random.randint(i, data_len-1)
        data[i], data[index] = data[index], data[i]
        #print(index, data)
    return data


def reverseLines():
    lines = list()
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    for item in lines[::-1]:
        print(item)


def dotProduct(arrayA, arrayB):
    n = len(arrayA)
    arrayC = list()
    if not (len(arrayB) == n):
        raise TypeError('Two arrays must be same length')
    else:
        arrayC = [arrayA[i]*arrayB[i] for i in range(n)]
        return arrayC


def writeElement(lst, elemt, index):
    try:
        lst[index] = elemt
    except IndexError:
        print('Don’t try buffer overflow attacks in Python!')
    return lst


def countVowels1(str):
    vowels = dict({'a':0, 'e':0, 'i':0, 'o':0, 'u':0})
    for item in str:
        if item in vowels:
            vowels[item] += 1
        else:
            vowels[item] = 1
    return vowels['a']+vowels['e']+vowels['i']+vowels['o']+vowels['u']


def countVowels2(str):
    cnt = 0
    for item in str:
        if item in 'aeiou':
            cnt += 1
    return cnt

# c1-27
def factors(n): # generator that computes factors
    k = 1
    rev_factor = list()
    while k*k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            rev_factor.append(n//k)
        k += 1
    if k*k == n: # special case if n is perfect square
        yield k
    for item in rev_factor[::-1]:
        yield item


# c1-28
def norm(v, p=2):
    return sum([vi**p for vi in v])**(1/p)


if __name__ == '__main__':
    import math
    data_length = 10
    data = [int(10*math.cos(i)) for i in range(data_length)]
    print('original data:', data)
    print(reverseList(data))
    print(reversed(data))
    print(list(reversed(data)))
    print(data[::-1])
    data.reverse()
    print(data)

    print(pair_product_odd(data))

    print(isDistinct(data))
    print(is_distinct(data))

    print(data)
    print(shuffle(data))
    reverseLines()

    print('dot product:', dotProduct(data, reverseList(data)))