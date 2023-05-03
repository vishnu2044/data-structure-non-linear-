class Trie:
    head = {}
    def add_wrd(self, word):
        crnt = self.head
        for char in word:
            if char not in crnt:
                crnt[char] = {}
            crnt = crnt[char]
        crnt["*"] = {}

    def search(self, word):
        crnt = self.head
        for char in word:
            if char not in crnt:
                return print("The word is not in the trie!!")
            crnt = crnt[char]

        if "*" in crnt:
            print("The word is present in the Trie!!")
        else:
            print("the word is nor present in the trie!!")

mytrie = Trie()
mytrie.add_wrd("ASD")
mytrie.add_wrd("ASZXC")
mytrie.add_wrd("ASDFGH")
mytrie.add_wrd("AQWER")
mytrie.search("ASDFGT")



