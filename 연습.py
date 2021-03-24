import array

arr = array.array('l', [0] * 5)
print(id(arr))
brr = arr
brr[0] = 1
print(id(brr))

