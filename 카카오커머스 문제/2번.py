
m = 4
v =	[3,2,3,1]
arr = [[] for i in range(len(v))]

def solution():
    #1층부터 블록을 쌓되 그 다음 수가 합이 m을 넘어가면 2층, 층별로 배열을 만들어 각 배열이 안되면 윗배열로 들어가
    floor = 0
    for i in v:
        for floor in arr:
            if sum(floor) + i <= m:
                floor.append(i)
                break
            else:
                continue

    count = 0
    for i in arr:
        if len(i) > 0:
            count +=1
    print(count)

solution()