from filter import Filter


class Game:

    def __init__(self, suggestion_count=5):
        self._filterAPI = Filter()
        self._suggestion_count = suggestion_count

    def run(self):
        self._print_menu()
        self._filterAPI.print_initial_suggestions()
        while True:
            user_word = input('Enter a word: ')
            if user_word == 'reroll':
                print('Re-rolling suggested words')
                self._filterAPI.print_initial_suggestions()
                continue
            elif user_word == 'reset-':
                print('words reset')
                self._filterAPI.reset()
                continue
            elif user_word == 'exit':
                break
            elif user_word == 'see all':
                print(f'{self._filterAPI.current_list()}')
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
            suggested_words = self._filterAPI.filter(user_word, user_colors)
            # print(f'\n{suggested_words[:10]}\n')

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

    def _print_random_words(self):
        output = 'Random words: '
        for _ in range(0, self._suggestion_count):
            output += f'{self._filterAPI.random_word()} '
        print(output)
