arr = [0] * 102
n = 1
x = 0
y = 0
for n in range(1, 101):
    if n % 2 == 1:
        if x == 1:
            x = 1
            y = 0

        else:
            x = arr[n-1]
            y = arr[n-2]
    else:
        if n == 2:
            x= 1
            y = 0

        else:
            x = arr[n//2]
            y = arr[n//2 - 1]
    arr[n] = x + y
print(arr)