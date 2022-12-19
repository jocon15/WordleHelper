[TOC]


# WordleHelper
Never lose a Wordle again!

## What is it?
Have you ever played wordle? Have you ever been on the last wordle guess and gotten stuck? No need to fear, the WordleHelper is here!

Wordle helper is a console application designed to help you with wordle. Use it as you do the daily wordle.

## Under the Hood
There are about 30,825 5-letter words in the english language. That means you have a 1 in 30,825 chance of guessing the word on the first try. Not very good odds. Let's see if we can use a CPU to help.

This program works by using brute force process of eliminations. We begin with a list the 22950 possible words. Wordle provies us ways to eliminate letters. As you play wordle and enter in the results, the program removes possible words from the list based on the results.

## Example
Let's play a game of wordle! The word is  "RIVAL".

Loading up the program looks like:

![Menu](https://github.com/jocon15/WordleHelper/blob/master/images/menu.png)

You can see it gives us some random word suggestions.
But I don't think any of those words sound good... So I'm going to guess "CHOKE".

![guess1](https://github.com/jocon15/WordleHelper/blob/master/images/guess1.png)

Now we enter that into the program...

![input1](https://github.com/jocon15/WordleHelper/blob/master/images/input1.png)

WOW, that guess elimiated 25,548 words from our original 30,825.

Again, I don't like the suggestions so I'm going to guess "TRAPS".

![guess2](https://github.com/jocon15/WordleHelper/blob/master/images/guess2.png)

Enter that in...

![input2](https://github.com/jocon15/WordleHelper/blob/master/images/input2.png)

Cool, we eliminated 10,757 with that word.

Let's guess the word "RABID"...

![guess3](https://github.com/jocon15/WordleHelper/blob/master/images/guess3.png)

Once again, enter it in...

![input3](https://github.com/jocon15/WordleHelper/blob/master/images/input3.png)

Looky here, only 7 words left. You can look through these words yourself. Which one of them seems like it might be a word that wordle would select? (Which word sounds familiar) Ah yes, "RIVAL"!

Let's try that...

![guess5](https://github.com/jocon15/WordleHelper/blob/master/images/guess5.png)

Ding! Ding! Ding!

## WordleHelper Results
Yes, WordleHelper was born yesterday. I have not added any logic to suggest certain words over others - that's still to come. However, I have played about 50 mock-wordle games with it and with moderate human selection, it usually deduces the word by guess 4 or 5.

## Suggestion Model
As previously mentioned, Wordle selects words that are commonly used in the English dictionary. You can't just manually sort 30K words one-by-one that would take way too long. My original thought was to use the Google Trends API to map a usage score to each word. Unfortunately, with the rate limit of the free version of the API, it would take 25 years to map all 5-letter words with a single usage score.

So I thought of another way...

I asked myself: what contains a lot of frequently used words?. . .Books! I found a website that houses royalty free text files of common books. I downloaded 20 books. I then built book_parse.py to build counters for all 5-letter words and count how many times they were used. You can see the results in words.json.

Now, when you enter in a guess and narrow down the possible words, some randomly selected words from the most common of the remaining possible words are present to you. In the older version, you would see suggested words you've never heard of. Now, you see words that are familiar to you.

There's still ways I can make this better, see The Future section for more.

## The Future

20 books is not exactly the best sample size for word frequency analytics. I specifically remember trying to avoid older books as they have older (less-used) words. But I included some 1800's language books to try to taper the counts in a way that rejects words that are Shakespeare-esque language. Of course, the sample size is limited and there are words that are not accurately represented based on the luck of small sample sizes.

Another potentially useful suggestion mechanism is to favor words with a unique letter for each letter-spot. For example, let's say it's your first guess. You could guess something like "THERE". Notice that the letter "E" is repeated. When it comes time to filter, we only have 4 letters to filter with. Consider the word "CHORE". In this word, there's a unique letter in every spot. "CHORE" is a better first guess becuase it allows us to filter with 5 unique letters instead of 4.

#### Additions Wishlist
- [x] Suggestions based on current word usage analytics
- [ ] Remove 5-letter words that are names from the database
- [ ] Remove 5-character words that have characters like ' and  -
- [ ] Suggestions with unique letters


