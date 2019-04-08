
import Trie_Struct as Tr
class main:
    """

    """
    words =['den','dear','do','disco']
    root= Tr.TrieNode()

    for words in words:
        root.add_word(word)

    root.print_all()

    print('de :')
    root.auto_complete_word('de')
