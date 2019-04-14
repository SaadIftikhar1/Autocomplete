"""
    Main script for the Auto-complete Engine
    The Main file for the Auto-complete Engine
    This file is to be run first for the system to load database and create a Prefix-Tree

    :Author : Saad Iftikhar
    :Date   : 7-04-2019
    :Version    : 1

"""

import Trie_Struct as Tr
from operator import itemgetter
import Trie_gen as Tr1
import tqdm
import os


def auto_complete(query):  # the basic code structure provided in https://gist.github.com/tizz98/fbad67ac008b21e53c292543a32dfbac
    split_query = query.split()
    last_word = split_query[-1]

    prefix = ' '.join(split_query[:-1])

    suggestions = root.find_all(last_word)

    full_sentence = []

    for suggestion in suggestions:
        full_sentence.append(('{}{}'.format((prefix + ' ') if prefix else ' ', suggestion[0]), suggestion[1],))

    sorted_suggestions = sorted(full_sentence, key = itemgetter(1), reverse=True, )

    return list(map(itemgetter(0), sorted_suggestions))


lang = input('Press Y/y to load default (English) database or N/n to provide database.txt file : ') # load the word database

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

sug_count = input("kindly input required suggestion number  :   ")   # Number of suggestions required

while 1:

    query = input("Enter the Word  :   ")
    root.add_word(query)
    f = open('words.txt', 'a')
    f.write(query + "\n")
    f.close()

    suggestion = auto_complete(query)
    if len(suggestion) < int(sug_count):
        counter = len(suggestion)
    else:
        counter = int(sug_count)
    print((',    '.join(suggestion[0:counter])))




