
# for a hash table we should always have a prime number of addresses
#The reason is because a prime number increases the amount of randomness
# for how the key value pair are going to be distributed to the hash table
#In that case we will reduce the collisions

class HashTable:
    def __init__(self, size=7):
        #this is our address space
        self.data_map = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            #ord(letters) will get the ASCII value (ord(char)) key for each character
            # or Return the Unicode number of a character
            my_hash = (my_hash + ord(letter) *23) % len(self.data_map)
        return my_hash
    
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
            
    def set_item(self, key, value):    
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
            
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys
    
    
def item_in_common(list1, list2):
    count = {}
    for i in list1:
        count[i] = count.get(i, 0) + 1
    
    for j in list2:
        if count.get(j, 0) >= 1:
            return True
    return False


my_hash_table = HashTable()
my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 700)
# print(my_hash_table.get_item("bolts"))
# print(my_hash_table.get_item("lumber"))
print(my_hash_table.keys())
my_hash_table.print_table()

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))