from collections import Counter


def is_anagram(word1, word2):
    counter = Counter()  # 카운터 딕셔너리
    for word in word1:  # word1 을 다 까서 글자 하나하나가 몇개인지
        counter[word] += 1  # 해당 글자가 있으면 플러스
    for word in word2:
        counter[word] -= 1 # 해당 글자가 두번째에 있으면 마이너스

    for i in counter.values(): # 모든 values 는 0이되어야함 애너그램이라면
        if i:
            return False # 0이 아니라면 False
    return True #


def test_is_anagram():
    word1 = "asdf"
    word2 = "asfsd"
    print(is_anagram(word1, word2))


if __name__ == "__main__":
    test_is_anagram()
