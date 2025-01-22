from time import perf_counter
import json
import random


class TileColors:
    GREY = '0'
    YELLOW = '1'
    GREEN = '2'


class Filter:
    def __init__(self):
        self.filename = 'words.txt'
        self.json_filename = 'words.json'
        self.potential_words = []
        self.words_dict = {}
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                if len(line.strip()) == 5:
                    self.potential_words.append(line.strip().lower())

        with open(self.json_filename, 'r') as file:
            self.words_dict = json.load(file)

    def filter(self, guess_word: str, guess_word_colors: str) -> list:
        """Filter the remaining words with a guess from the user.

        Args:
            guess_word (str): the word the user guessed list of letters that form the
            guess_word_colors (str): the corresponding colors to the word that the user guessed (from wordle)

        return
            list: a whitelist of remaining possible words
        """
        start_time = perf_counter()

        # transform the strings into lists
        guess_word_letters = [guess_word[i] for i in range(0, 5)]
        guess_word_tile_colors = [guess_word_colors[i] for i in range(0, 5)]

        # create the blacklist - eliminating the word that the user guessed
        black_list_words = [guess_word]

        green_letters = []
        # eliminate words based on color outcomes from the guess word
        for i in range(0, 5):
            tile_color = guess_word_tile_colors[i]

            if tile_color == TileColors.GREEN:
                self.__filter_with_green_tile(i, guess_word_letters, guess_word_tile_colors, green_letters,
                                              black_list_words)
            elif tile_color == TileColors.YELLOW:
                self.__filter_with_yellow_tile(i, guess_word_letters, black_list_words)
            else:
                self.__filter_with_grey_title(i, guess_word_letters, green_letters, black_list_words)

        white_list_words = []
        for word in self.potential_words:
            if word not in black_list_words:
                white_list_words.append(word)

        for word in black_list_words:
            if word in self.words_dict.keys():
                del self.words_dict[word]

        end_time = perf_counter()
        print(f'Eliminated : {len(black_list_words)} words')
        print(f'Remaining  : {len(white_list_words)} words')
        print(f'Rendered in {round(end_time - start_time, 3)} seconds')

        self.print_suggestions()

        # set self.words to the whitelist
        self.potential_words = white_list_words
        # return the whitelist
        return self.potential_words

    def current_list(self):
        return self.potential_words

    def print_suggestions(self):
        sort = sorted(self.words_dict.items(), key=lambda item: item[1])
        sort = sort[-100:]
        sort.reverse()
        suggestions = ''
        for _ in range(11):
            suggestions += f'{random.choice(sort)[0]} '
        print(f'Suggestions: {suggestions}')

    def random_word(self):
        if self.potential_words:
            choice = random.choice(self.potential_words)
            if "'" in choice or "." in choice or "-" in choice:
                return ' '
            return choice
        return ' '

    def reset(self):
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                if len(line.strip()) == 5:
                    self.potential_words.append(line.strip().lower())

    def __filter_with_green_tile(self, letter_index: int, guess_word_letters: list[str],
                                 guess_word_tile_colors: list[str], green_letters: list[str],
                                 black_list_words: list[str]):
        tile_letter = guess_word_letters[letter_index]
        tile_color = guess_word_tile_colors[letter_index]

        if tile_color == TileColors.GREEN:
            # store the green letters to help decide grey letters
            if tile_letter not in green_letters:
                green_letters.append(tile_letter)
            # eliminate all words without that letter in that position
            for word in self.potential_words:
                if tile_letter != word[letter_index]:
                    black_list_words.append(word)

    def __filter_with_yellow_tile(self, letter_index: int, guess_word_letters: list[str], black_list_words: list[str]):
        tile_letter = guess_word_letters[letter_index]

        # eliminate all words with that letter in that position
        for word in self.potential_words:
            if tile_letter == word[letter_index]:
                black_list_words.append(word)
            else:
                # eliminate words that do not have that letter in it somewhere else
                letter_found_elsewhere = False
                for j in range(0, 5):
                    if j == letter_index:
                        continue
                    if tile_letter == word[j]:
                        letter_found_elsewhere = True
                        break
                if not letter_found_elsewhere:
                    black_list_words.append(word)

    def __filter_with_grey_title(self, letter_index: int, guess_word_letters: list[str], green_letters: list[str],
                                 black_list_words: list[str]):
        tile_letter = guess_word_letters[letter_index]

        # checks the case where a letter is green in one spot, but if elsewhere in guessed word, appears grey
        # be sure we do not eliminate words prematurely
        if tile_letter not in green_letters:
            # eliminate all words with that letter anywhere
            for word in self.potential_words:
                for letter in word:
                    if tile_letter == letter:
                        black_list_words.append(word)
                        break
