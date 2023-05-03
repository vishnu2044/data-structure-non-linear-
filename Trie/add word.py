class Trie:

    head = {}
    def add_wrd(self, word):
        crnt = self.head
        for char in word:
            if char not in crnt:
                crnt[char] = {}
            crnt = crnt[char]
        crnt["*"] = {}


mytrie = Trie()
mytrie.add_wrd("vishn5")
mytrie.add_wrd("vishnav")
print(mytrie.head)

