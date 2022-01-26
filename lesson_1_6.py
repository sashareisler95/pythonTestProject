inheritance = {}


def add(a, b):
    if a not in inheritance:
        inheritance[a] = b
    else:
        for i in b:
            if i not in inheritance[a]:
                inheritance[a].append(i)


def get(c, d):
    if c == d and ((get_key(inheritance, c) is not None) or (inheritance.get(c) is not None)):
        return True
    elif c == d and ((get_key(inheritance, c) is None) and (inheritance.get(c) is None)):
        return False
    else:
        if inheritance.get(d) is None:
            return False
        else:
            if c in inheritance[d]:
                return True
            else:
                for value in inheritance[d]:
                    res = get(c, value)
                    if res:
                        return True
                return False


def get_key(d, value):
    for k in d.keys():
        if value in d[k]:
            return k


n = int(input())
for i in range(n):
    a, *b = input().replace(":", " ").split()
    add(a, b)

q = int(input())
for i in range(q):
    c, d = input().split()
    if get(c, d):
        print('Yes')
    else:
        print('No')
