import sys, copy

input = sys.stdin.readline

N, M, H = map(int, input().split(' '))
rows = [list(map(int, input().split(' '))) for _ in range(M)]


def solution():
    def find():
        for x in range(1, N + 1):
            new_x = x
            for y in range(1, H + 1):
                for a, b in rows:
                    if new_x == b and y == a:
                        new_x += 1
                    elif new_x == b + 1 and y == a:
                        new_x -= 1
            if new_x != x:
                return False
        return True

    # find 가 False 라면 충족하지 않는 부분이 있으므로 추가해줘야 함.
    def plus_row1(num):
        count = 0
        visited = []
        new_arr = copy.deepcopy(rows)
        new_rows = []
        while count < num:
            for x in range(1, N + 1):
                for y in range(1, H + 1):
                    if [x,y] not in rows:
                        new_rows.append([x,y])
                        if new_rows not in visited and len(new_rows) == num:
                            visited.append(new_rows)
                            new_arr.append(new_rows)
                        count += 1
        if not find():
            plus_row1(num + 1)
        else:
            print(num)
        return
    plus_row1(1)
    print(-1)


    num = 1
    while num <= 3:
        if not find():
            plus_row1(num)
            num += 1
    print(-1)

solution()
