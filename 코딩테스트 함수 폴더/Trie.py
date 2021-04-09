class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return len(words)

def solution(words, queries):
    answer= []
    length_dict = dict()

    for word in words:
        length = len(word)
        if length in length_dict:
            # 트라이로 들어가서 해당 글자에 대한 내용 추가
            length_dict[length].insert(word)
            length_dict[length].insert(word[::-1])
        else:
            tree = Trie()
            length_dict[length] = tree
            tree.insert(word)
            tree.insert(word[::-1])


    for query in queries:
        length = len(query)
        if length in length_dict:
            if query[0] != "?":
                # 접미사면 뒤집어서 찾아야함
                hash_word = length_dict[length]
                answer.append(hash_word.starts_with(query[:query.index("?")]))
            else:
                #접두사면 그대로 넣어줌
                reversed = query[::-1]
                hash_word = length_dict[length]
                answer.append(hash_word.starts_with(reversed[:reversed.index("?")]))
        else:
            answer.append(0)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]
print(solution(words, queries))