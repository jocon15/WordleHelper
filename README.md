# WordleHelper
Never lose a Wordle again!

## What is it?
Have you ever played wordle? Have you ever been on the last wordle guess and gotten stuck? No need to fear, the wordle helper is here!

Wordle helper is a console application designed to help you with wordle. Use it as you do the daily wordle.

## Under the Hood
there are about 30,825 5-letter words in the english language. That means you have a 1 in 30,825 chance of guessing the word on the first try. Not very good odds. Let's see if we can use a CPU to help.

This program works by using brute force process of eliminations. We begin with a list the 22950 possible words. Wordle provies us ways to eliminate letters. As you play wordle and enter in the results, the program removes possible words from the list based on the results.

## Example
Let's play a game of wordle! The word is  "RIVAL".

Loading up the program looks like:
![Menu](https://github.com/jocon15/WordleHelper/blob/master/images/menu.png)

You can see it gives us some random word suggestions.
But I don't think any of those words sound good... So I'm going to guess "CHOKE".
![guess1](https://github.com/jocon15/WordleHelper/blob/master/images/guess2.png)

Now we enter that into the program...
![input1](https://github.com/jocon15/WordleHelper/blob/master/images/input1.png)

WOW, that guess elimiated 25,548 words from our original 30,825.

Again, I don't like the suggestions so I'm going to guess "TRAPS".
![guess2](https://github.com/jocon15/WordleHelper/blob/master/images/guess2.png)

Enter that in...
![input2](https://github.com/jocon15/WordleHelper/blob/master/images/input2.png)
Cool, we eliminated 10,757 with that word.



## WordleHelper Results
Yes, WordleHelper was born yesterday. I have not added any logic to suggest certain words over others - thats still to come. However, I have played about 50 mock-wordle games with it and with moderate human selection, it usually deduces the word by guess 4 or 5.

## The Future
If you've played wordle, you get the sense that the words that it selects are commonly used words in the English language. In our set of words, we have some words that are valid words, but are rarely (if ever) used in today's English. An interesting area of research could be to look at something like Google Trends (https://trends.google.com/trends/?geo=US) for each of the remaining possible words, then select the more frequently used words as suggestions for the user.

#### Additions Wishlist
- [ ] Remove 5-letter words that are names from the database
- [ ] Remove 5-character words that have characters like ' and  -
- [ ] Suggestions based on current word usage analytics


