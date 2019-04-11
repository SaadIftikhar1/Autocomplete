from flask import Flask, render_template, request
import tqdm
import os
import Trie_gen as Tr1

app = Flask(__name__)

"""with open('words.txt') as f:
    words = f.readlines()"""
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

f.close()

root = Tr1.TrieNode('')

for word in tqdm.tqdm(words):
   root.add_word(word.strip('\n'))

del words


@app.route('/output')
def output():
    return render_template("index.html", name="Joe")


@app.route('/autocomplete', methods=['POST', 'GET'])
def autocomplete():
    if request.method == 'POST':
        query = request.form["Enter Query"]
        sug_count = request.form["Suggestion count"]

        auto_comp = []

        root.add_word(query)
        f = open('words.txt', 'a')
        f.write(query + "\n")
        f.close()

        for word, _ in root.find_all(query):
            auto_comp.append(word)

        if len(auto_comp) < int(sug_count):
            counter = len(auto_comp)
        else:
            counter = int(sug_count)
        return render_template("index.html", suggestion=auto_comp[0:counter], numero=sug_count)
    else:
        query = request.args.get["Enter Query"]
        sug_count = request.args.get["Suggestion count"]
        auto_comp = []

        root.add_word(query)
        f = open('words.txt', 'a')
        f.write(query + "\n")
        f.close()

        for word, _ in root.find_all(query):
            auto_comp.append(word)
        return render_template("index.html", suggestion=auto_comp , numero= sug_count)


if __name__ == '__main__':
    app.run(debug=True)


