def solution(genres, plays):
    gen_dict = dict()
    for genre_index in range(len(genres)):
        if gen_dict.get(genres[genre_index]):
            gen_dict[genres[genre_index]] += plays[genre_index]
        else:
            gen_dict[genres[genre_index]] = plays[genre_index]
    play_dict = dict()
    for play_index in range(len(plays)):
        play_dict[plays[play_index]] = genres[play_index]

    index_dict = dict()
    for play_index in range(len(plays)):
        index_dict[plays[play_index]] = play_index

    sorted_gen_dict = sorted(gen_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_play_dict = sorted(play_dict.items(), key=lambda x: x[0], reverse=True)

    answer = []
    for gen in sorted_gen_dict:
        count = 0
        i = 0
        while i < len(sorted_play_dict):
            if gen[0] == sorted_play_dict[i][1]:
                answer.append(index_dict[sorted_play_dict[i][0]])
                count += 1
            if count >= 2:
                break
            i += 1


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
