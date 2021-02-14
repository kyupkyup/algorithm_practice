from collections import deque

T = int(input())

def solution():
    for _ in range(T):
        dq = deque([])
        check = False
        conv = int(input())
        conv_arr = []
        dq.append(list(map(int, input().split(" "))))
        for _ in range(conv):
            conv_arr.append(list(map(int, input().split(" "))))
        endX, endY = map(int, input().split(" "))

        while dq:
            convX, convY = dq.popleft()
            if abs(endX - convX) + abs(endY - convY) <= 1000:
                check = True
                print("happy")
                break
            for i in conv_arr[:]:
                if abs(i[0] - convX) + abs(i[1] - convY) <= 1000:
                    dq.append([i[0], i[1]])
                    conv_arr.remove(i)
        if not check:
            print("sad")


solution()