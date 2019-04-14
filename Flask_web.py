from flask import Flask, render_template, request
from operator import itemgetter
import tqdm
import os
import Trie_gen as Tr1

app = Flask(__name__)

"""with open('words.txt') as f:
    words = f.readlines()"""
lang = input('Press (Y/y) to load default (English) database or (N/n) to provide database.txt file : ')

if lang == 'y' or lang == 'Y':
    with open('words.txt') as f:
            words = f.readlines()
else:
    user_input = input("Enter the name of your file : ")

    try:
        assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
        f = open(user_input, 'r')
        print(" \n The file was found ")
    except:
        print(" No such file in the directory. We are going to proceed with English Database    ")
        user_input = 'words.txt'

    with open(user_input) as f:
        words = f.readlines()

f.close()

root = Tr1.TrieNode('')

for word in tqdm.tqdm(words):
   root.add_word(word.strip('\n'))

del words


@app.route('/autocomplete', methods=['POST', 'GET'])
def autocomplete():
    if request.method == 'POST':
        query = request.form["Enter Query"]
        root.add_word(query)
        f = open('words.txt', 'a')
        f.write(query + "\n")
        f.close()
        sug_count = request.form["Suggestion count"]

        split_query = query.split()
        last_word = split_query[-1]

        prefix = ' '.join(split_query[:-1])

        suggestions = root.find_all(last_word)

        full_sentence = []

        for suggestion in suggestions:
            full_sentence.append(('{}{}'.format((prefix + ' ') if prefix else ' ', suggestion[0]), suggestion[1],))

        sorted_suggestions = sorted(full_sentence, key=itemgetter(1), reverse=True, )

        auto_comp = list(map(itemgetter(0), sorted_suggestions))

        if len(auto_comp) < int(sug_count):
            counter = len(auto_comp)
        else:
            counter = int(sug_count)
        return render_template("index.html", suggestion=(',    '.join(auto_comp[0:counter])), numero=sug_count)
    else:
        query = request.args.get["Enter Query"]
        root.add_word(query)
        f = open('words.txt', 'a')
        f.write(query + "\n")
        f.close()
        sug_count = request.args.get["Suggestion count"]
        auto_comp = []

        split_query = query.split()
        last_word = split_query[-1]

        prefix = ' '.join(split_query[:-1])

        suggestions = root.find_all(last_word)

        full_sentence = []

        for suggestion in suggestions:
            full_sentence.append(('{}{}'.format((prefix + ' ') if prefix else ' ', suggestion[0]), suggestion[1],))

        sorted_suggestions = sorted(full_sentence, key=itemgetter(1), reverse=True, )

        auto_comp = list(map(itemgetter(0), sorted_suggestions))

        if len(auto_comp) < int(sug_count):
            counter = len(auto_comp)
        else:
            counter = int(sug_count)
        return render_template("index.html", suggestion=(',    '.join(auto_comp[0:counter])), numero=sug_count)


if __name__ == '__main__':
    app.run()


