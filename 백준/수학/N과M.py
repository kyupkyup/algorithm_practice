from itertools import permutations
a, b = map(int, input().split(" "))
a = [i for i in range(1, a+1)]

permute = list(permutations(a,b))
for i in permute:
    for j in range(b):
        print(i[j], end=" ")
    print()

