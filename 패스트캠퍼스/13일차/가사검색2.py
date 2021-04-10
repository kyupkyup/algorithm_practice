class Node(object):
    def __init__(self, data=""):
        self.data = data
        self.num_children = 0
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        current_node = self.head
        temp_string = ""
        for char in string:
            temp_string += char
            if char not in current_node.children:
                current_node.children[char] = Node(temp_string)
            current_node.num_children += 1
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        if string == current_node.data:
            return current_node.num_children
        if string[0] not in current_node.children:
            if string[0] == "?":
                return current_node.num_children
            else:
                return 0

        temp_ans = 0
        for char in string:
            if char == "?":
                return temp_ans
            if char not in current_node.children:
                return 0

            current_node = current_node.children[char]
            temp_ans = current_node.num_children

        return 0

def solution(words, queries):
    length_dict = dict()
    length_reverse_dict = dict()
    answer = []
    for word in words:
        length = len(word)
        if length not in length_reverse_dict:
            length_reverse_dict[length] = Trie()
        length_reverse_dict[length].insert(word[::-1])
        if length not in length_dict:
            length_dict[length] = Trie()
        length_dict[length].insert(word)

    for query in queries:
        length = len(query)
        if length not in length_dict and length not in length_reverse_dict:
            answer.append(0)
        else:
            if length == query.count("?"):
                answer.append(length_dict[length].head.num_children)
            elif query[0] == "?":
                reversed_query = query[::-1]
                answer.append(length_reverse_dict[length].search(reversed_query))
            else:
                answer.append(length_dict[length].search(query))
    return answer

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "?????", "???????"]
solution(words, queries)
