
def func(x, left, right, value):
    if left >= right:
        return False

    if right > len(x) or left < 0:
        return False

    mid = (left + right) // 2

    if value == x[mid]:
        return mid
    elif value > x[mid]:
        left = mid + 1
    elif value < x[mid]:
        right = mid - 1
    return func(x, left, right, value)

print(func([0,1,2,3,4,5,6,7,8,9,10], 0, 10, 6))

def func1(x):

    return ord(x) % 26

print(func1("a"))
print(func1("b"))
print(func1("c"))
print(func1("d"))
print(func1("e"))
print(func1("f"))
print(func1("g"))
print(func1("h"))
print(func1("i"))
print(func1("j"))
print(func1("k"))
print(func1("l"))
print(func1("m"))
print(func1("n"))
print(func1("o"))
print(func1("p"))
print(func1("q"))
print(func1("r"))
print(func1("s"))
print(func1("t"))
print(func1("u"))
print(func1("v"))
print(func1("w"))
print(func1("x"))
print(func1("y"))
print(func1("z"))


