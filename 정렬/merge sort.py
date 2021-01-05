

def merge_sort(list1):
    if len(list1) < 2:
        return list1
    # 배열을 양쪽으로 나눈다
    left_list = list1[0:len(list1)//2]
    right_list = list1[len(list1)//2: len(list1)]
    # return 값이 없을 때 까지 재귀함수로 분할

    # 합치면서 정렬을 하는데...
    # merge
    left_list = merge_sort(left_list) # 왼쪽
    right_list= merge_sort(right_list) # 오른쪽
    return merge(left_list, right_list)

def merge(list1, list2):
    # left~mid 와 mid ~ right while 문 돌면서 비교 해서 sorted에 넣어줌

    result= []
    while list1 and list2:
        if list1[-1] >= list2[-1]:
            result.append(list1.pop())
        else:
            result.append(list2.pop())
    result.reverse()
    return (list1 or list2) + result


def solution():
    unsorted_list = [3,5,2,6,8,1,0,3,5,6,2]

    # 미드 값 지정,
    return merge_sort(unsorted_list)

print(solution())
