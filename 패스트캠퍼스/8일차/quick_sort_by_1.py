
def quick_sort(x, start, end):
    
    if len(x) == 0:
        return x
    
    pivot = (start + end) // 2
    while True:
        while start <= end:
            while x[start] >= x[pivot]:
                start += 1
                if start == end:
                    break
            while x[end] < x[pivot]:
                end -= 1
                if start == end:
                    break

            if start <= end:
                x[start], x[end] = x[end], x[start]
                start += 1
                end -= 1
        pivot = start
        start = 0
        end = len(x)-1


x = [4,1,9,3,2,7,8,0]
quick_sort(x, 0, len(x)-1)