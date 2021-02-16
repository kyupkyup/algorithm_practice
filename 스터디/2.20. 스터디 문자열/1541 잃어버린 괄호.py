S = input()

def solution():
    ans = ""
    arr = ""
    temp_arr = ""

    temp = 0

    for i in range(len(S)):
        if S[i] == "-":
            temp_arr = S[temp: i]
            temp = i + 1
            temp_arr_temp = 0
            for j in range(len(temp_arr)):
                if temp_arr[j] == "+":
                    arr += str(int(temp_arr[temp_arr_temp: j]))
                    arr += "+"
                    temp_arr_temp = j + 1
            arr += str(int(temp_arr[temp_arr_temp:]))
            ans += str(eval(arr))
            arr = ""
            ans += "-"

    temp_arr_temp = 0
    temp_arr = S[temp:]
    for j in range(len(temp_arr)):
        if temp_arr[j] == "+":
            arr += str(int(temp_arr[temp_arr_temp: j]))
            arr += "+"
            temp_arr_temp = j + 1
    arr += str(int(temp_arr[temp_arr_temp:]))
    ans += str(eval(arr))


    print(eval(ans))

solution()
