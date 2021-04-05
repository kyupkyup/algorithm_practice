class HashTable:
    def __init__(self, hash_func = None, bucket_size=15):
        self.hash_func = hash_func
        self.bucket_size = bucket_size
        self.hashTable = [[i, None, None, None] for i in range(bucket_size)]

    def set(self, key, value):
        hash_result = self.hash_func(key)
        object = self.hashTable[hash_result % self.bucket_size]
        if object[1] is None:
            object[1] = key
            object[2] = value
        else:
            if object[1] == key:
                print("already key")
                return False
            else:
                new_node = [hash_result % self.bucket_size, key, value, None]
                while object[3] is not None:
                    object = object[3]
                object[3] = new_node

    def get(self, key):
        hash_result = self.hash_func(key)
        object = self.hashTable[hash_result % self.bucket_size]
        if object[1] == key:
            return object[2]
        else:
            if object[3] is not None:
                while object[3] is not None:
                    object = object[3]
                    if object[3] is None:
                        print("no key")
                        return False
                    elif object[1] == key:
                        return object[2]
            else:
                print("no key")
                return False

HT = HashTable(hash, 5)

for i in range(20):
    HT.set(i, i*2)
for i in range(60):
    print(HT.get(i))
print(HT)

