from graphviz import Digraph

WORD_FILE = "./parole_validate_treccani.txt"

class TrieNode:
    counter = 0

    def __init__(self, letter):
        self.id = f"{TrieNode.counter}"
        self.letter = letter
        TrieNode.counter += 1

        self.children = {}


    def dfs(self):
        graph.node(self.id, label=self.letter, shape='circle')
        
        for char, child_node in self.children.items():
            child_node.dfs()
            graph.edge(self.id, child_node.id)

class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]

    def get_node(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
        

# Esempio di utilizzo della classe Trie


if __name__ == "__main__":

    trie = Trie()

    graph = Digraph(comment='Prefix Tree')

    with open(WORD_FILE, 'r') as f:
        words = f.readlines()
        words = words[:5000]

    # created trie thanks to the class Trie
    for word in words:
        trie.insert(word.strip())
    trie.root.dfs()
    print("Trie created")
    print("Start rendering...")
    graph.render('test.pdf', view=True, cleanup=True)
    