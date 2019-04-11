"""
    Main script for the Auto-complete Engine
    The Main file for the Auto-complete Engine
    This file is to be run first for the system to load database and create a Prefix-Tree

    :Author : Saad Iftikhar
    :Date   : 7-04-2019
    :Version    : 1

"""

import Trie_Struct as Tr
import Trie_gen as Tr1
import tqdm
import os


class Main:
    """
    """

    lang = input('Press Y/y to load default (English) database or N/n to provide database.txt file : ')

    if lang == 'y' or lang == 'Y':
        with open('words.txt') as f:
            words = f.readlines()
    else:
        user_input = input("Enter the path of your file : ")

        try:
            assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
            f = open(user_input, 'r')
            print(" \n The file was found ")
        except:
            print(" No such file in the directory. We are going to proceed with English Database    ")
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

    sug_count = input("kindly input required suggestion number  :   ")

    while 1:
        auto_comp=[]

        #auto_comp.append('')

        query = input("Enter the Word  :   ")
        root.add_word(query)
        f = open('words.txt', 'a')
        f.write(query + "\n")

        for word, _ in root.find_all(query):
            auto_comp.append(word)

        if len(auto_comp) < int(sug_count):
            counter = len(auto_comp)
        else:
            counter = int(sug_count)

        for i in range(0, counter):
            try:
                print("     Suggestion   : ", auto_comp[i])
            except:
                pass

