def solution(N):
    col, diag1, diag2 = set(), set(), set()
    answer = 0
    def dfs(N, y, col, diag1, diag2):
        nonlocal answer
        if y == N:
            answer += 1
            return

        for x in range(N):
            if x in col or (x + y) in diag1 or (x - y) in diag2:
                continue
            col.add(x)
            diag1.add(x + y)
            diag2.add(x - y)
            dfs(N, y + 1, col, diag1, diag2)
            col.remove(x)
            diag1.remove(x + y)
            diag2.remove(x - y)
    dfs(N, 0, col, diag1, diag2)
    return answer

print(solution(12))