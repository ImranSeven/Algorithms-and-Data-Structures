class Node:
    def __init__(self, data=None, size=27):
        # terminal $ at index 0
        self.link = [None] * size
        # data payload
        self.data = data

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, key, data=None):
        # begin from root
        current = self.root
        # go through the key 1 by 1
        for char in key:
            # calculate index
            # $ = 0, a = 1, b = 2, c =3 ...
            index = ord(char) - 97 + 1
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
            # if path doesn't exist
            else:
                # create new node
                current.link[index] = Node()
                current = current.link[index]
        # go through the terminal $, index = 0
        index = 0
        if current.link[index] is not None:
            current = current.link[index]
        # if path doesn't exist
        else:
        # create new node
            current.link[index] = Node()
            current = current.link[index]
        # add in the payload
        current.data = data

# Test Run
bla = Trie()
bla.insert("lol", "123")
bla.insert("loa", "456")
bla.insert("lol", "789")
