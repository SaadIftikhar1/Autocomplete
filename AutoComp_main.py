
import Trie_Struct as Tr
import Trie_gen as Tr1
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

        try:
            assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
            f = open(user_input, 'r')
            print(" \n The file was found ")
        except:
            print(" No such file in the directory. We are going to proceed with English Database")
            user_input = 'words.txt'

        with open(user_input) as f:
            words = f.readlines()
            # stuff you do with the file goes here
    f.close()

    # root1 = Tr.TrieNode()
    root = Tr1.TrieNode("")

    for word in tqdm.tqdm(words):
        root.add_word(word.strip('\n'))

    del words

    # Set the suggestion count

    sug_count = input("kindly input required suggestion number  :")

    auto_comp=[]

    auto_comp.append('')

    query = input(" Enter the Word")

    for word, _ in root.find_all(query):
        auto_comp.append(word)

    if  len(auto_comp) < int(sug_count):
        suggestion_count= len(auto_comp) - 1

    for i in range(0, int(sug_count) + 1):
        print(auto_comp[i])


