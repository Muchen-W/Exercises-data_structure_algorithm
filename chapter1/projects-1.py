# p1-29

def permutation1(chars):
    if len(chars) <= 1:
        return chars
    else:
        result = list()
        perms = permutation1(chars[1:])
        print(perms)
        for perm in perms:
            for i in range(len(chars)):
                print(perm[:i])
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


if __name__ == '__main__':
    lst = ['c', 'a', 't', 'd', 'o', 'g']
    print(permutation1(lst))
    permutation2(lst, 0, len(lst)-1)
