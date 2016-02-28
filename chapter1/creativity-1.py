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