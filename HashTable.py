class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Constructor method to initialise instances

    def _hash(self, key):  # Private method for hashing keys using the inbuilt hash function
        return hash(key) % self.size

    def insert(self, key, value):  # Method for inserting buckets into the hash table
        index = self._hash(key)  # hashing the key
        if self.table[index] is None:  # If the table is already empty we can just insert the tuple straight away.
            self.table[index] = [(key, value)]  # Note that buckets are essentially lists of tuples of the format (key,data)
        else:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:  # We iterate through the bucket to see if the key is present
                    self.table[index][i] = (key, value)  # Update value for existing key
                    break
            else:
                self.table[index].append((key, value))  # if the key isn't present, we append to the bucket

    def get(self, key):  # method for retrieving values from hash table
        index = self._hash(key)
        if self.table[index] is not None:  # if the table[hashed index] isn't empty
            for existing_key, existing_value in self.table[index]:
                if existing_key == key:
                    return existing_value  # we return the tables value
        raise KeyError(f"Key '{key}' not found in the hash table.")

    def delete(self, key):  # sometimes we might want to delete elements from the table because we're crazy
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]  # using the delete statement here
                    return
        raise KeyError(f"Key '{key}' not found in the hash table.")  # We can't exactly delete nothing can we
