data = ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4",
        "8 BROWN-CONY 4"]
word = "SALLY"


class Node:
    def __init__(self, id, name, parent_id):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.if_leaf = True
        self.count_index = []
        self.search_count = 10000000

    # def __repr__(self):
    #     return repr((self.search_count))


def solution(data, word):
    answer = []
    node_arr = []
    for i in range(len(data)):
        data1 = data[i].split(" ")
        node_arr.append(Node(data1[0], data1[1], data1[2]))
        for node in node_arr:
            if data1[2] == node.id:
                node.if_leaf = False
    print(node_arr)

    for node in node_arr:
        if node.if_leaf:
            if node.name == word:
                answer.append(node)
                continue
                # 같으면
            else:
                if node.name.count(word) >= 1:
                    node.search_count = node.name.count(word)
                    index = -1
                    while True:
                        index = node.name.find(word, index + 1)
                        if index == -1:
                            break
                        node.count_index.append(index)
    sort_node_arr = sorted(node_arr, key=lambda x: (x.search_count, x.count_index))
    real_ans = []
    for node in sort_node_arr:
        if node.search_count >= 1 and node.search_count != 10000000 :
            real_ans.append(node)

    if not answer:
        return ["Your search for (" + word + ") didn't return any results"]

    return answer


solution(data, word)
