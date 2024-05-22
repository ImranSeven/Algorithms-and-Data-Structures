class Node:
    def __init__(self, start=None, end=None, size=27):
        # links to child nodes
        self.link = [None] * size
        # suffix link (used in advanced suffix tree implementations like Ukkonen's)
        self.suffix_link = None
        # starting index of the substring represented by the edge leading to this node
        self.start = start
        # ending index of the substring represented by the edge leading to this node
        self.end = end if end is not None else float('inf')
        # children of the node
        self.children = {}

class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = Node()
        self.build_suffix_tree()

    def build_suffix_tree(self):
        """
        Build the suffix tree for the input text.
        """
        size = len(self.text)
        for i in range(size):
            self.insert_suffix(self.text[i:], i)
        
    def insert_suffix(self, suffix, start_index):
        """
        Insert a suffix into the suffix tree.
        """
        current = self.root
        j = 0
        while j < len(suffix):
            index = ord(suffix[j]) - 97 + 1
            if current.link[index] is not None:
                current = current.link[index]
                j += 1
            else:
                new_node = Node(start=start_index + j, end=start_index + len(suffix))
                current.link[index] = new_node
                current = new_node
                j += 1

    def print_tree(self, node=None, indent=0):
        """
        Utility function to print the suffix tree.
        """
        if node is None:
            node = self.root
        if node.start is not None:
            print(' ' * indent + self.text[node.start:node.end])
        for child in node.link:
            if child is not None:
                self.print_tree(child, indent + 2)

# Define Node and SuffixTree classes here as provided previously

# Test Case 1
print("Test Case 1: Single Character String")
text = "a"
suffix_tree = SuffixTree(text)
suffix_tree.print_tree()

# Test Case 2
print("\nTest Case 2: Simple String with Repeated Characters")
text = "aa"
suffix_tree = SuffixTree(text)
suffix_tree.print_tree()

# Test Case 3
print("\nTest Case 3: Simple String with Different Characters")
text = "abc"
suffix_tree = SuffixTree(text)
suffix_tree.print_tree()

# Test Case 4
print("\nTest Case 4: String with Repeated Substrings")
text = "banana"
suffix_tree = SuffixTree(text)
suffix_tree.print_tree()

# Test Case 5
print("\nTest Case 5: Palindromic String")
text = "racecar"
suffix_tree = SuffixTree(text)
suffix_tree.print_tree()
