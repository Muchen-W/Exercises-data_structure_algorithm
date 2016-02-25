def is_multiple(n, m):
    return n % m == 0

def is_even(k):
    return k & 1 == 0

def minmax(data):
    small, large = data[0], data[0]
    for item in data:
        if item < small:
            small = item
        elif item > large:
            large = item
        else:
            continue
    return small, large

def sumSquare(n):
    return sum(i*i for i in range(1, n))

def sumOddSquare(n):
    return sum(i*i for i in range(1, n) if not is_even(i))

def choice(data):
    import random
    return data[random.randrange(len(data))]


if __name__ == '__main__':
    import math
    x = 1
    for i in range(1, x):
        print(x, 'is a multiple of ', i, is_multiple(100, i))
        print(i, 'is even', is_even(i))
    data = [int(100*math.sin(j)) for j in range(10)]
    print(data)
    print(minmax(data))
    print(sumSquare(x))
    print(sumOddSquare(x))
    print(choice(data))