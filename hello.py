
genres = ["classic", "pop", "classic", "classic", "pop"]
plays=[500, 600, 150, 800, 2500]

def solution():
    genres_play = {}
    each_play = {}
    ans = []
    for i in range(len(genres)):
        if genres[i] not in genres_play:
            genres_play[genres[i]] = plays[i]
            each_play[genres[i]] = [[plays[i], i], [-1, -1]]
        else:
            genres_play[genres[i]] += plays[i]
            if plays[i] > each_play[genres[i]][0][0]:
                each_play[genres[i]][1] = each_play[genres[i]][0]
                each_play[genres[i]][0] = [plays[i],i]
            elif plays[i] > each_play[genres[i]][1][0]:
                each_play[genres[i]][1][0] = plays[i]
                each_play[genres[i]][1][1] = i
            else:
                continue

    temp = sorted(genres_play.items(), key=lambda x: -x[1])

    for k, v in temp:
        if each_play[k][1][0] == -1 and each_play[k][1][0] == -1:
            ans.append(each_play[k][0][1])
        elif len(each_play[k]) == 2:
            ans.append(each_play[k][0][1])
            ans.append(each_play[k][1][1])

    return ans



solution()