import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited_alpha = [False for _ in range(27)]
count = 0
alpha = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,
    "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
}
stack = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution():
    global count,stack
    stack.append(arr[0][0])
    dfs(1, 0, 0)

    print(count)


def dfs(countR, indexX, indexY):
    global count, visited_alpha, arr, alpha, dx, dy, stack


    if countR > count:
        count = countR

    if count == 26:
        return

    # for i in range(4):
    #     nx = indexX + dx[i]
    #     ny = indexY + dy[i]
    #     if 0 <= nx < C and 0 <= ny < R and not visited_alpha[alpha[arr[0][0]]]:
    #         visited_alpha[alpha[arr[ny][nx]]] = True
    #         dfs(countR + 1, nx, ny)
    #         visited_alpha[alpha[arr[ny][nx]]] = False
    for i in range(4):
        nx = indexX + dx[i]
        ny = indexY + dy[i]
        if 0 <= nx < C and 0 <= ny < R and arr[ny][nx] not in stack:
            stack.append(arr[ny][nx])
            dfs(countR + 1, nx, ny)
            stack.pop()
solution()
