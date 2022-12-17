import time
import json
import random
from tqdm import tqdm


class Filter:
    def __init__(self):
        self.filename = 'words.txt'
        self.json_filename = 'words.json'
        self.words = list()
        self.words_dict = {}
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                if len(line.strip()) == 5:
                    self.words.append(line.strip().lower())

        with open(self.json_filename, 'r') as file:
            self.words_dict = json.load(file)

    def filter(self, guess_word: str, colors: str) -> list:
        """Filter the remaining words with a guess from the user.

        Args:
            guess_word (str): the word the user guessed list of letters that form the
            colors (str): the corresponding colors to the word that the user guessed (from wordle)

        return
            list: a whitelist of remaining possible words
        """
        start_time = time.time()
        # create the lists from the word
        guess_word_list = list()
        color_list = list()
        for i in range(0, 5):
            guess_word_list.append(guess_word[i])
            color_list.append(colors[i])

        # create the blacklist
        black_list = list()

        # eliminate the word that the user guessed
        black_list.append(guess_word)

        # eliminate words based on color outcomes from the guess word
        for i in range(0, 5):
            if color_list[i] == '2':
                # color is green
                # eliminate all words without that letter in that position
                for word in self.words:
                    if guess_word_list[i] != word[i]:
                        black_list.append(word)
            elif color_list[i] == '1':
                # color is yellow
                # eliminate all words with that letter in that position
                for word in self.words:
                    if guess_word_list[i] == word[i]:
                        black_list.append(word)
                    # word must have that letter in it somewhere
                    fault = True
                    for letter in word:
                        if guess_word_list[i] == letter:
                            fault = False
                    if fault:
                        black_list.append(word)
            else:
                # color is grey
                # eliminate all words with that letter anywhere
                for word in self.words:
                    fault = False
                    for letter in word:
                        if guess_word_list[i] == letter:
                            fault = True
                    if fault:
                        black_list.append(word)

        # create the whitelist
        white_list = list()
        # build the whitelist using the words and the blacklist
        for word in self.words:
            if word not in black_list:
                white_list.append(word)

        for word in black_list:
            if word in self.words_dict.keys():
                del self.words_dict[word]

        end_time = time.time()
        print(f'Eliminated : {len(black_list)} words')
        print(f'Remaining  : {len(white_list)} words')
        print(f'Rendered in {round(end_time - start_time,3)} seconds')

        self.print_suggestions()

        # set self.words to the whitelist
        self.words = white_list
        # return the whitelist
        return self.words

    def current_list(self):
        return self.words

    def print_suggestions(self):
        sort = sorted(self.words_dict.items(), key=lambda item: item[1])
        sort = sort[-100:]
        sort.reverse()
        suggestions = ''
        for _ in range(11):
            suggestions += f'{random.choice(sort)[0]} '
        print(f'Suggestions: {suggestions}')

    def random_word(self):
        if self.words:
            choice = random.choice(self.words)
            if "'" in choice or "." in choice or "-" in choice:
                return ' '
            return choice
        return ' '

    def reset(self):
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                if len(line.strip()) == 5:
                    self.words.append(line.strip().lower())
