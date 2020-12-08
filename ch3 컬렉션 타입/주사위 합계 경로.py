from collections import Counter, defaultdict

# 주사위 두개를 던져서 S라는 합이 만들어질 수 있는 경우의 수 모두를 찾아야 함
def find_dice_probabilities(n_faces, S):

    if S > 2 * n_faces or S < 2:
        return None

    cdict = Counter() # 각 합에 대해 몇개의 경우가 나오는지 계산하는 딕셔너리
    ddict = defaultdict(list) # 그 경우의 수가 어떤 것들인지

    for dice1 in range(1, n_faces):
        for dice2 in range(1, n_faces):
            t = [dice1, dice2] # 현재 주사위 조합
            cdict[dice1+dice2] += 1 #
            ddict[dice1+dice2].append(t)

    return [cdict[S], ddict[S]] # S에 해당하는 경우의 수와 경우 전부

def test_find_dice_probabilities():
    n_faces = 10
    S = 8
    result = find_dice_probabilities(n_faces, S)
    print(result)

    return

if __name__ == "__main__":
    test_find_dice_probabilities()