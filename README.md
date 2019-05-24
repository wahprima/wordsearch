# wordsearch
searching and counting word from a grid with a mixed of random letters.

This script is inspired and a modification from :
https://github.com/mashingan/word-search-solver


## How to use the script :
1. Open command prompt/terminal
2. Go to the folder where the input file and the script located
3. Once you inside the folder, type :
```
>python pw_wordsearch.py input.in.example.txt
```
4. The above command will give a result : 
```
Case 1: 4

Case 2: 8

Case 3: 4
```
5. To save the result in a text file, simply write this command : 
```
>python pw_wordsearch.py fileinput.txt > nameoftheoutput.txt
```


## Problem

There is a well-known puzzle called Word Search that involves looking for words
in a grid of letters. The words are given in a list and can appear in the grid
horizontally, vertically, or diagonally on any direction. In this task, you should
implement a solver for word search. You will be given grids and a word to search for,
and you have to find how many times taht word comes out in the grid. Words that are
spelled the same backwards and forwards, also known as palindromes,
will not be given, so you don't need to worry about words that match in the exact
same spot in two different directions.

**Input : **

The first line is the number of test cases T. Each test case will have two numbers
N and M, each of their own line given in that order. Following that is N lines of
M lowercase letters each representing the grid of letters, a word W is given that
you must look for.

**Output : **

For each test case, output one line of the form "Case C: X" (without the quotes),
where C is the case number (starting from 1), and X is how many times the word W
appeared in the grid.

**Constraints : **

**1 <= T <= 100**

**1 <= N <= 100**

**1 <= M <= 100**

**1 <= length(W) <= 100

**Sample Input : **
```
3
3
4
catt
aata
tatc
cat
5
5
gogog
ooooo
godog
ooooo
gogog
dog
2
8
bananana
kalibrrr
nana
```
