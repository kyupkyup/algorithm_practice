
next_student = [6, 10, 8, 5, 8, 10, 5, 1, 6, 7]
visited = []
ans = 0
max_count = 0
def solution():
    global ans, visited, max_count
    next_student.insert(0,0)
    for i in range(1, len(next_student)):
        if i in visited:
            continue
        else:
            visited.append(i)
            temp = dfs(next_student[i], 1)

            if temp > max_count:
                ans = i
                max_count = temp
            elif temp == max_count:
                ans = i
            visited = []
    print(ans)

def dfs(num, count):
    global visited

    if num in visited:
        return count
    if next_student[num] == 0:
        return count

    else:
        visited.append(num)
        return dfs(next_student[num], count+1)

solution()
