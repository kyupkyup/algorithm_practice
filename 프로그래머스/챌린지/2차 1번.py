numbers = [2,7]
def solution(numbers):
    answer = []

    for num in numbers:
        bin_num = bin(num)
        count = 0
        print(len(bin_num))
        for i in range(len(bin_num) - 1, -1, -1):
            if bin_num[len(bin_num) - 1] == "0":
                count = 1
                break
            else:
                if bin_num[i] == "1":
                    count += 1
                else:
                    break
        answer.append(num+(2 ** (count - 1)))
    return answer
solution(numbers)