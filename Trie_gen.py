"""
Prefix Trie Data Structure
Code based on the original code at : https://gist.github.com/tizz98/fbad67ac008b21e53c292543a32dfbac
Author of original code : Elijah Wilson
"""
class TrieNode:
    __slots__ = ('value', 'end_of_word', 'children', 'weight')

    def __init__(self, value: str, end_of_word=False):
        self.value = value
        self.end_of_word = end_of_word
        self.children = {}
        self.weight = -1

    def add_word(self, word_part: str, *, weight: int=-1) -> None:
        if len(word_part) == 0:
            self.end_of_word = True
            self.weight = weight
            return

        first_char = word_part[0]
        node = self.children.setdefault(first_char, TrieNode(first_char))
        node.add_word(word_part[1:], weight=weight)

    def find_all(self, word_part: str, path: str= ""):
        if self.end_of_word:
            yield path + self.value, self.weight

        if len(word_part) > 0:
            char = word_part[0]
            node = self.children.get(char)

            if node is not None:
                yield from node.find_all(word_part[1:], path + self.value)
        else:
            for node in self.children.values():
                yield from node.find_all("", path + self.value)







