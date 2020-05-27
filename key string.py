class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hashValue=self.calculate_hash_value(string)
        
        if hashValue != -1:
            if self.table[hashValue] != None:
                self.table[hashValue].append(string)
            else:
                self.table[hashValue] = [string]

        """Input a string that's stored in 
        the table."""
        

    def lookup(self, string):
        hashValue=self.calculate_hash_value(string)
        
        if hashValue!=-1:
            if self.table[hashValue]!=None:
                if string in self.table[hashValue]:
                    return hashValue
        return -1
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hashValue=ord(string[0])*100+ord(string[1])
        return hashValue
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
