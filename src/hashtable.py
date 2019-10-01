# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if self.count >= self.capacity:
        #     self.resize()

        # Make the key a valid integer index
        hashed_key = self._hash_mod(key)
        
        # Store it
        if self.storage[hashed_key] is not None:
            # print("This key already exists in storage, adding it to chain at index: ", hashed_key)
            current = self.storage[hashed_key]
            while True:
                if current.next is None:
                    current.next = LinkedPair(key, value)
                    self.count += 1
                    break
                elif current.next is not None:
                    current = current.next
                else:
                    print('Warning: Error inserting value.')

        else:
            self.storage[hashed_key] = LinkedPair(key, value)
            self.count += 1
        


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] is None:
            print("Warning: key not found.")
            return
        else: 
            self.storage[hashed_key] = None



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] is None:
            return self.storage[hashed_key]
        
        else:
            current = self.storage[hashed_key]
            while current is not None:
                if current.key is key:
                    return current.value
                else:
                    current = current.next



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Double capacity, fill it with None
        # self.capacity *= 2
        # new_storage = [None] * self.capacity

        # # Rehash keys for placement in our working storage
        # for item in self.storage:
        #     if item is not None:
        #         new_hashed_key = self._hash_mod(item.key)
        #         new_storage[new_hashed_key] = item

        # # Set our class storage equal to our working storage once we are done
        # self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print('First retrievals ----------------')
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print('Second retrievals ------------------')
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
