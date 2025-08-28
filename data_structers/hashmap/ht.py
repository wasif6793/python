class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize list of buckets

    def _hash(self, key):
        # Simple hash function: built-in hash and modulo size
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        # Check if key exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # If key not found, append new key-value pair
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False  # Key not found

    def __str__(self):
        return str(self.table)


# Example usage
ht = HashTable()

ht.set("apple", 10)
ht.set("banana", 20)
ht.set("orange", 30)

print(ht.get("apple"))  # Output: 10
print(ht.get("banana"))  # Output: 20
print(ht.get("grape"))  # Output: None

ht.delete("banana")
print(ht.get("banana"))  # Output: None

print(ht)

