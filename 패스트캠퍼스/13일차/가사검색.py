class Trie:
    def __init__(self):
        self.hash_table = dict()
        self.reversed_hash_table = dict()


    def add_word(self, word):
        pointer = 0
        while pointer < len(word) + 1 :
            if word[:pointer] not in self.hash_table:
                self.hash_table[word[:pointer]] = 1
            else:
                self.hash_table[word[:pointer]] += 1

            pointer += 1
        pointer = 0
        reversed = word[::-1]
        while pointer < len(word) + 1:
            if reversed[:pointer] not in self.reversed_hash_table:
                self.reversed_hash_table[reversed[:pointer]] = 1
            else:
                self.reversed_hash_table[reversed[:pointer]] += 1
            pointer += 1
    # 트라이 구조 만드는

    def find_word(self, word):
        count = 0
        if word in self.hash_table:
            count += self.hash_table[word]
        elif reversed in self.reversed_hash_table:
            count = self.reversed_hash_table[reversed]
        return count

def solution(words, queries):
    # Trie 구조 생성.
    answer= []
    length_dict = dict()

    for word in words:
        length = len(word)
        if length in length_dict:
            # 트라이로 들어가서 해당 글자에 대한 내용 추가
            length_dict[length].add_word(word)
        else:
            tree = Trie()
            length_dict[length] = tree
            tree.add_word(word)


    for query in queries:
        length = len(query)
        if length in length_dict:
            if query[0] != "?":
                # 접미사면 뒤집어서 찾아야함
                hash_word = length_dict[length]
                answer.append(hash_word.find_word(query[:query.index("?")]))
            else:
                #접두사면 그대로 넣어줌
                reversed = query[::-1]
                hash_word = length_dict[length]
                answer.append(hash_word.find_word(reversed[:reversed.index("?")]))
        else:
            answer.append(0)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]
print(solution(words, queries))


