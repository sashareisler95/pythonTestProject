objects = [1, 2, 1, 2, 3]
mn = []
for obj in objects:
    if obj not in mn:
        mn.append(obj)


# print(len(mn))


# def closest_mod_5(x):
#     for i in range(10):
#         if x % 5 == 0:
#             return x
#         else:
#             x += 1

def closest_mod_5(x):
    return x if x % 5 == 0 else closest_mod_5(x + 1)


def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


# print(s(11, b=20))
# print('No')
# print(s(11, 10, b=10))
# print(s(21))
# print('No')
# print(s(5, 5, 5, 5, 1))
# print(s(11, 10))
# print(s(11, 10, 10))
# print(s(0, 0, 31))

# def c(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     else:
#         return c(n - 1, k) + c(n - 1, k - 1)
#
#
# n, k = map(int, input().split())
# print(c(n, k))
#
#
# x, y = 1, 2
#
#
# def foo():
#     global y
#     if y == 2:
#         x = 2
#         y = 1
#
#
# foo()
# print(x)
# if y == 1:
#     x = 3
# print(x)

namespaces = {}
variables = {}


def check_contains_namesp(arg, namesp):
    if variables.get(namesp) is None:
        return False
    else:
        return arg in variables[namesp]


def create(namesp, arg):
    namespaces[namesp] = arg


def get(namesp, arg):
    if namesp == 'global' and check_contains_namesp(arg, namesp) is False:
        return None
    return namesp if check_contains_namesp(arg, namesp) else get(namespaces[namesp], arg)


def add(namesp, arg):
    if variables.get(namesp) is None:
        variables[namesp] = set()
        variables[namesp].add(arg)
    else:
        variables[namesp].add(arg)


number = int(input())
for i in range(number):
    cmd, namesp, arg = input().split()
    if cmd == 'get':
        print(get(namesp, arg))
    elif cmd == 'add':
        add(namesp, arg)
    elif cmd == 'create':
        create(namesp, arg)
