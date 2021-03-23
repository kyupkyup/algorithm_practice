import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0] * capacity)

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    def check_capacity(self):
        if self.length + 1 > self.capacity:
            self.capacity *= 2
            temp_array = array.array('l', [0] * self.capacity)
            for i in range(self.length):
                temp_array[i] = self.array[i]
            self.array = temp_array


    def prepend(self, value):
        # capacity 확인 후 추가했을 때 length 가 capacity를 초과하지 않을 경우 추가
        self.check_capacity()
        if self.length == 0:
            self.array[0] = value

        else:
            for i in range(self.length, 0, -1):
                self.array[i] = self.array[i - 1]
            self.array[0] = value
        self.length += 1

    def append(self, value):
        self.check_capacity()
        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        self.length -= index
        temp_array = array.array('l', [0] * self.capacity)
        for j in range(self.length):
            temp_array[j] = self.array[index+j]
        self.array = temp_array

    def access(self, index):
        if index >= self.length or index < 0:
            return "index out of range."
        return self.array[index]


    def insert(self, index, value):
        if index >= self.length or index < 0:
            return "index out of range."

        self.check_capacity()
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = value
        self.length += 1


    def remove(self, index):
        if index >= self.length or index < 0:
            return "index out of range."
        for i in range(index, self.length):
            self.array[i] = self.array[i+1]
        self.length -= 1


    def print(self):
        for i in range(self.length):
            print(self.array[i], end=" ")
        print()

arrayList = ArrayList(2)
arrayList.prepend(10)
arrayList.prepend(20)
arrayList.prepend(30)
arrayList.prepend(40)
arrayList.prepend(50)
arrayList.prepend(60)
arrayList.prepend(70)
arrayList.append(80)
arrayList.print()
arrayList.set_head(2)
arrayList.print()
arrayList.insert(2,120)
print(arrayList.access(3))
arrayList.print()
arrayList.remove(4)
arrayList.print()

print(arrayList.is_empty())
