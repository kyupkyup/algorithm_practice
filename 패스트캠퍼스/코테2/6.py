
def solution(s, n):
    arr = [[0 for _ in range(n * 2 -1)] for _ in range(n)]
    p1 = 0
    x, y = 0, n-1
    while True:
        arr[y][x] = s[p1]
        if y == n-1 and x == 2 * n - 2:
            break

        if x == 0:
            if y == 0:
                x += 1
                y += 1
            else:
                y -= 1

        elif 0< x < n-1:
            x += 1
            y += 1

        elif 2 * n - 2 > x >= n-1:
            x += 1
            y -= 1
        elif x == 2 * n - 2:
            y += 1

        p1 += 1
        if p1 == len(s):
            p1 = 0

    print(arr)
    answer = ""
    for j in range(n):
        for i in range(2 * n - 1):
            if arr[j][i] != 0:
                answer += arr[j][i]

    return answer
solution("정갈아나정갈정것신같신것신같나아나", 5)