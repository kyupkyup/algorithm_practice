from collections import Counter

def find_top_N_recurring_words(seq, N):
    dcounter = Counter()
    for word in seq.split():
        dcounter[word] += 1 # dcounter 딕셔너리에 word에 대한 개수를 더해줌
    return dcounter.most_common(N) # 딕셔너리에서 N개 까지 가장 카운터가 높은 (key,value) 리스트를 리턴

def test_find():
    seq = "a a a a a a a a a b b b b b b c c c c c d d d d d d d"
    N = 3

    print(find_top_N_recurring_words(seq, N))

    return

if __name__ == "__main__":
    test_find()