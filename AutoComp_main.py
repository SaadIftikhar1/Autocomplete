
import Trie_Struct as Tr
import tqdm

class Main:
    """


    """

    with open('words.txt') as f:
        words = f.readlines()



    root = Tr.TrieNode()

    for word in tqdm.tqdm(words):
        root.add_word(word.strip('\n'))

    del words

    for i in range(5):
        str = input('Enter you word :')
        root.auto_complete_word(str)

    