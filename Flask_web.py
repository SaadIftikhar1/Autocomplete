from flask import Flask,render_template, redirect, request, url_for
import Trie_Struct as Tr
import tqdm
import sys
import os
app = Flask(__name__)

with open('words.txt') as f:
    words = f.readlines()

root1 = Tr.TrieNode()

#for word in tqdm.tqdm(words):
 #   root1.add_word(word.strip('\n'))

#del words

@app.route('/output')
def output():
    return render_template("index.html", name="Joe")

@app.route('/autocomplete', methods=['POST','GET'])
def autocomplete():
    if request.method == 'POST':
        string =request.form["Enter Query"]
        num_sug = request.form["Suggestion count"]
        return render_template("index.html", suggestion="saad /n iftikhar /n is it possible" , numero=num_sug )
    else:
        string = request.args.get["Enter Query"]
        num_sug = request.args.get["Suggestion count"]
        return render_template("index.html", suggestion="saad /n iftikhar /n is it possible" , numero=num_sug)


if __name__ == '__main__':
    app.run(debug=True)


