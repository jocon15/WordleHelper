import os
import json
from tqdm import tqdm


def special_strip(string):
    string = string.replace('.', '')
    string = string.replace(',', '')
    string = string.replace('!', '')
    string = string.replace('?', '')
    string = string.replace('\\', '')
    string = string.replace(';', '')
    string = string.replace(':', '')
    string = string.replace('_', '')
    string = string.replace('=', '')
    string = string.replace('&', '')
    string = string.replace('$', '')
    string = string.replace(')', '')
    string = string.replace('(', '')
    string = string.replace('"', '')
    string = string.replace("'", '')

    string = string.replace('0', '')
    string = string.replace('1', '')
    string = string.replace('2', '')
    string = string.replace('3', '')
    string = string.replace('4', '')
    string = string.replace('5', '')
    string = string.replace('6', '')
    string = string.replace('7', '')
    string = string.replace('8', '')
    string = string.replace('9', '')

    return string


def main():
    lines = list()
    for filename in os.listdir('books'):
        with open(f'books\\{filename}', encoding='utf-8-sig') as file:
            lines += file.readlines()

    # build the popularity dict
    words = {}
    for line in tqdm(lines):
        for word in line.split(' '):
            word = word.strip()
            word = word.lower()
            word = special_strip(word)
            if len(word) == 5:
                if word in words.keys():
                    words[word] = words[word] + 1
                else:
                    words[word] = 1

    # build the all words dict
    all_words = {}
    with open('words.txt', 'r') as file:
        for word in tqdm(file.readlines()):
            word = word.strip()
            word = word.lower()
            if len(word) == 5:
                all_words[word] = 0

    # match the numbers to the words
    for word in tqdm(all_words.keys()):
        if word in words.keys():
            all_words[word] = words[word]

    # write the words to a json file
    with open('words.json', 'w+') as file:
        json.dump(all_words, file)


if __name__ == '__main__':
    main()
