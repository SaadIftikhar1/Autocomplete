# Autocomplete
Basic Autocomplete Engine in Python

# Introduction
This is a simple python implementation of an Autocomplete Engine using a Prefix Tree (Trie). Github Repository provides
two front end implementations of our Engine (using HTTP and Websockets)

# Structure

The main structure which encapsulates the database of English words in itself is a Prefix tree (Trie). 
The program allows the user to load the database at the start. The file needs to be in the form of a .txt file 
with each word of the language present in a separate line.
In the repository words.txt file taken from https://github.com/dwyl/english-words/ contains rough 4.6k English 
Language words.  The program has been tested using this database.

# Files in the Repository

: **AutoComp_main.py** is the main file which imports the necessary data structure and files to run the console 
    implementation fo the Autocomplete Engine
: **Tire_Struct.py**   is first implementation of the Prefix tree data structure in Python, which was later improved in
    Trie_gen file
: **Trie_gen.py**   Python implementation fo Trie data structure. The implementation uses iterator and generators for 
    efficient implementation
: **words.txt**     This txt file contains English Language word's database.
: **Flask_web.py**     Flask implementation of web based front end for our Autocomplete Engine
: **socket_test.py**    Websockets implementation in python using socket.io for our second front end of the Engine
: **templates**     template folder contains HTML files for tht front end of our Engine

# How to Build, run and test the Code

*   First download the github repository on your computer
*   You can test the code by running AutoComp_main.py. The program will first ask you to load the databased.
    The database has to be in the form of a .txt file with each new word in the new line of the file. The program also
    provides you with the option of selecting number of suggestions required for each word/ sentence.
*   The program can also be tested using the two front end web implementations present in the templates folder.
    : **index.html** is an Http based front end for our engine. To test our program we first need to run **Flask.web.py** 
    application to set up the web server. After setting up the server we can test the program by running index.html
    : **socket_index.html** is a websocket based front end for our engine. To test our program we first need to run 
    **scoket_test.py** application to set up the web server. After setting up the server we can test the program by 
    running index.html
    
# Advantages & Limitations:

*   The weight of each word is currently equal. Hence the suggestions are currently based on alphabetical order rather 
    than the frequency of search. Weighted trie implementation is currently in progress.
*   The Trie structure had more time efficiency compared to SQL based database implementation, hence, it was slected for 
        