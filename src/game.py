from filter import Filter


class Game:

    def __init__(self, suggestion_count=5):
        self._filter = Filter()
        self._suggestion_count = suggestion_count

    def run(self):
        self._print_menu()
        self._filter.print_initial_suggestions()
        while True:
            user_word = input('Enter a word: ')
            if user_word == 'reroll':
                print('Re-rolling suggested words')
                self._filter.print_remaining_suggestions()
                continue
            elif user_word == 'reset-':
                print('words reset')
                self._filter.reset()
                continue
            elif user_word == 'exit':
                break
            elif user_word == 'see all':
                print(f'{self._filter.potential_words}')
                continue
            elif len(user_word) != 5:
                print('Invalid length')
                continue
            user_colors = input('Enter a set of colors: ')
            if len(user_colors) != 5:
                print('Invalid length')
                continue
            elif user_colors == '22222':
                print('You win!')
                break
            print('Thinking...')
            self._filter.filter(user_word, user_colors)

    @staticmethod
    def _print_menu():
        print('=====================INFO======================')
        print('        Commands: ')
        print("'reroll    -> re roll the suggested words"  )
        print("'reset-'   -> reset the possible words list")
        print("'see all' -> see all of the possible words")
        print("'exit'    -> end the program")
        print('       Color Scheme:')
        print('Green     -> 2')
        print('Yellow    -> 1')
        print('Grey      -> 0')
        print('===============================================')
