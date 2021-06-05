
def solution(n):
    while n > 0:
        n /= 7
        if n == 1:
            return True
    return False
print(solution())