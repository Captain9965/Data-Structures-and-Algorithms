""" Implementation of a hash table in python: """


class HashTable:
    htable = [[],] * 10
    def __int__(self):
        self.htable = [[],] * 10
    def checkPrime(self, n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n//2):  #floor division..
            if n % i == 0:
                return False
        return True

    def getPrime(self, n):
        #add one to the number if even number...
        if n % 2 == 0:
            n += 1
        while not self.checkPrime(n):
            n +=2
        return n
    def hashFunction(self, key):
        capacity = self.getPrime(10)
        return key % capacity
    def insertData(self, key, data):
        index = self.hashFunction(key)
        self.htable[index] = [key, data]
        return
    def removeData(self, key):
        index = self.hashFunction(key)
        self.htable[index] = []


if __name__ == "__main__":
    hashtable = HashTable()
    print(hashtable.htable)
    hashtable.insertData(123, "Lenny")
    hashtable.insertData(432, "Jacqueline")
    hashtable.insertData(556, "Cephas")

    print(hashtable.htable)

    hashtable.removeData(556)
    print(hashtable.htable)