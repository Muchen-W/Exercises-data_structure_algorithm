# p1-29

def permutation1(chars):
    if len(chars) <= 1:
        return chars
    else:
        result = list()
        perms = permutation1(chars[1:])
        for perm in perms:
            for i in range(len(chars)):
                result.append(perm[:i]+chars[0]+perm[i:])
        return result


def permutation2(chars, start, end):
    if start == end:
        print(chars)
    else:
        for i in range(start, end+1):
            chars[start], chars[i] = chars[i], chars[start]
            permutation2(chars, start+1, end)
            chars[start], chars[i] = chars[i], chars[start]


# p1-30
def logarithm1(num, cnt=0):
    if num >= 2:
        cnt = logarithm1(num/2, cnt)
        cnt += 1
    return cnt


def logarithm2(num, cnt=0):
    if num < 2:
        return cnt
    else:
        cnt += 1
        return logarithm2(num/2, cnt)


def logarithm3(num):
    cnt = 0
    while num >= 2:
        num /= 2
        cnt += 1
    return cnt


def logarithm4(num):
    import math
    return math.floor(math.log2(num))


def test1():
    lst = ['c', 'a', 't', 'd', 'o', 'g']
    print(permutation1(lst))
    permutation2(lst, 0, len(lst)-1)


def test2():
    number = 15
    print(logarithm1(number))
    print(logarithm2(number))
    print(logarithm3(number))
    print(logarithm4(number))


if __name__ == '__main__':
    test2()

