class MyHashMap:

    def __init__(self):
        self.data = []
        for _ in range(1009):
            self.data.append([])


    def __hash(self, key):
        return key % 1009


    def put(self, key: int, value: int) -> None:
        hashed_key = self.__hash(key)

        bucket = self.data[hashed_key]
        for chave_valor in bucket:
            if chave_valor[0] == key:
                chave_valor[1] = value
                return
        bucket.append([key, value])
        


    def get(self, key: int) -> int:
        hashed_key = self.__hash(key)

        bucket = self.data[hashed_key]
        for chave_valor in bucket:
            if chave_valor[0] == key:
                return chave_valor[1]
        return -1



    def remove(self, key: int) -> None:
        hashed_key = self.__hash(key)

        bucket = self.data[hashed_key]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
#obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


obj.put(9, 4)
obj.put(7, 8)
obj.put(1018, 7)
#print(obj.data[9])   # esperado: [[9, 8], [1018, 7]]

obj.remove(1018)


print(obj.data[9])