
import Trie_Struct as Tr
import tqdm
import tkinter
from tkinter import filedialog
import sys
import os

class Main:
    """
    """

    lang = input('Do you want to load default (English) database or you have a database to load (Y/N) :')

    if lang == 'y' or lang == 'Y':
        with open('words.txt') as f:
            words = f.readlines()
    else:
        user_input = input("Enter the path of your file: ")

        assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
        f = open(user_input, 'r')
        print(" \n The file was found ")

        with open(user_input) as f:
            words = f.readlines()
        # stuff you do with the file goes here
        f.close()

    root1 = Tr.TrieNode()

    for word in tqdm.tqdm(words):
        root1.add_word(word.strip('\n'))

    del words

    for i in range(5):
        str = input('Enter you word :')
        root1.auto_complete_word(str)

