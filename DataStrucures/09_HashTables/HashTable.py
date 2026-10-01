class HashTable:
    def __init__ (self, size = 7):

        # Creating a list with 7 postions, all of them has None
        # each position is None at the start, later it becomes a list of [key, value]
        self.data_map: list[list | None] = [None] * size


    # Building the Hash function (method)
    def __hash(self, key):
        my_hash = 0
        for letter in key:
                                # ASCII of the letter
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash


    def set(self, key, value ):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []        
        self.data_map[index].append([key,value])  # pyright: ignore[reportOptionalMemberAccess]


    
    def get(self, key):
        index = self.__hash(key)
        
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):  # pyright: ignore[reportArgumentType]
                if self.data_map[index][i][0] == key:  # pyright: ignore[reportOptionalSubscript]
                    return self.data_map[index][i][1]  # pyright: ignore[reportOptionalSubscript]
        
        return None


    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):  # pyright: ignore[reportArgumentType]
                    all_keys.append(self.data_map[i][j][0])  # pyright: ignore[reportOptionalSubscript]

        return all_keys



    def print_table(self):
        for index, value in enumerate(self.data_map):
            print(index, ":", value)


my_hash_table = HashTable()

my_hash_table.set("bolts", 1400)
my_hash_table.set("washers", 50)
my_hash_table.set("lumber", 70)

#print(my_hash_table.get("bolts"))

print(my_hash_table.keys())


#my_hash_table.print_table()