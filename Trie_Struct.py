"""
Module for Trie Data Structure
"""

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
            self.letter = self.word[self.index]
            self.itd_word = itd_word + self.word[self.index]
        if self.index + 1 < len(self.word):
            if self.word[self.index + 1] not in self.children_node:
                self.children_node[self.word[self.index + 1]] = TrieNode()
                self.children_node[self.word[self.index + 1]].add_word(self.word,
                                                                   self.itd_word,
                                                                   self.index +1)
            else:
                self.children_node[self.word[self.index + 1]].add_word(self.word,
                                                                       self.itd_word,
                                                                       self.index + 1)

    def print_all(self):
        if self:
            if len(self.children_node) == 0:
                print(self.itd_word)
            else:
                for i in self.children_node:
                    self.children_node[i].print_all()

    def auto_complete_word(self, prefix : str):
        if len(prefix) > 0 and prefix[0] in self.children_node:
            self.children_node[prefix[0]].auto_complete_word(prefix[1:])
        if len(prefix) == 0:
            print("autoComplete :")
            self.print_all()




