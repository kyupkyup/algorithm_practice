from _collections import deque
board = [[0,0,1,1],[1,1,1,1]]

def solution(board):
    height = len(board)
    width = len(board[0])
    ans = 0
    dq = deque([])

    for i in range(height):
        for j in range(width):
            cross = 1
            hori = 1

            if board[i][j] == 1:
                # 양쪽으로
                right = j
                down = i
                while True:
                    right = right + 1

                    if right < width:
                        if board[i][right] == 1:
                            cross += 1
                        else:
                            break
                    else:
                        break

                while True:
                    down = down + 1
                    if down < height:
                        if board[down][j] == 1:
                            hori += 1
                        else:
                            break
                    else:
                        break
                ans = max(ans , min(cross, hori) ** 2)

    print(ans)

solution(board)