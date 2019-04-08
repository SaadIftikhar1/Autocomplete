

class TrieNode:

    """
    The Trie Data Structure Node
    :word = The word in the language dictionary
    :letter = Letter in the Trie Nodes
    :Children_node = Child node
    :weight = weight assigned to each word depending upon the rate of use
    :index = index for iteration and search
    :ind_word = intermediate word... incomplete word during traversal
    

    """

    __slots__ = ('word','letter','children_node','weight','index','itd_word')

    def __init__(self):
        self.word = ''
        self.letter = ''
        self.children_node = {}
        self.weight=-1
        self.index = 0
        self.itd_word = ''



    def add_word(self, word, itd_word='', index = -1):
        self.word = word
        self.index = index

        if self.index >= 0:
            self.letter=self.word[self.index]



    def print_all(self):
        pass
    def auto_complete_word(self):
        pass


