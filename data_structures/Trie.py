class Node:
    def __init__(self, data=None, level=None, size=27):
        # terminal $ at index 0
        self.link = [None] * size
        # data payload
        self.data = data
        # level of node
        self.level = level

class Trie:
    def __init__(self):
        self.root = Node(level=0)
    
    def insert(self, key, data=None):
        count_level = 1
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
                current.link[index] = Node(level=count_level)
                current = current.link[index]
            count_level = count_level + 1
        # go through the terminal $, index = 0
        index = 0
        if current.link[index] is not None:
            current = current.link[index]
        # if path doesn't exist
        else:
        # create new node
            current.link[index] = Node(level=count_level)
            current = current.link[index]
        # add in the payload
        current.data = data

    def insert_recur(self, key, data=None):
        current = self.root
        self.inser_recur_aux(current, key, data)
    
    def insert_recur_aux(self, current, key, data=None):
        # base
        if len(key) == 0:
            # what happen when i gone through all of my alpha in key
            return
        # recur
        else:
            # calculate index
            # $ = 0, a = 1, b = 2, c =3 ...
            index = ord(key[0]) - 97 + 1
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
            # if path doesn't exist
            else:
                # create new node
                current.link[index] = Node()
                current = current.link[index]
                self.insert_recur_aux(current, key[1:], data)

    def search(self, key):
        # begin from root
        current = self.root
        # go through the key 1 by 1
        for char in key:
            print(current.level)
            # calculate index
            # $ = 0, a = 1, b = 2, c =3 ...
            index = ord(char) - 97 + 1
            # if path exist
            if current.link[index] is not None:
                current = current.link[index]
            # if path doesn't exist
            else:
                raise Exception(str(key) + " Key doesn't exist")
        # go through the terminal $, index = 0
        index = 0
        print(current.level)
        if current.link[index] is not None:
            current = current.link[index]
        # if path doesn't exist
        else:
            raise Exception(str(key) + " Key doesn't exist")
        # now we are at the leaf
        print(current.level)
        return current.data

# Test Run for insert
bla = Trie()
bla.insert("lol", "123")
bla.insert("loa", "456")
bla.insert("lol", "789")
bla.insert("uwu", None)

# Test run for search
try:
    print(bla.search("lol"))
except Exception as e:
    print(e)
try:
    print(bla.search("loa"))
except Exception as e:
    print(e)
try:
    print(bla.search("los"))
except Exception as e:
    print(e)
try:
    print(bla.search("lo"))
except Exception as e:
    print(e)
try:
    print(bla.search("uwu"))
except Exception as e:
    print(e)