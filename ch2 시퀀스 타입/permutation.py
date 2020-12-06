from itertools import permutations

def perm(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for cc in perm(s[:i] + s[i+1:]):
            res.append(c+cc)
    return res

def perm2(s):
    res = permutations(s)
    return ["".join(i) for i in res]

if __name__ == "__main__":
    val= "012"
    print(perm(val))
    print(perm2(val))