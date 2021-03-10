N = int(input())

arr = [0, 9]
arr1 = [0, 1]
for i in range(1, N):
    arr1.append(arr1[i]+i)
    arr.append(arr[i] * 2 - arr1[i])

print(arr[-1] % 1000000000)