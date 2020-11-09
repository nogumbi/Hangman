#TIP: use random.randint to get a random word from the list
import random

def read_file(file_name):
    f = open(file_name, 'r')
    files = f.readlines()
    return files


def select_random_word(words):
    wordlist = random.randint(0, len(words)-1)
    word = words[wordlist]
    blank = words[wordlist]
    print('Guess the word: ' + blank[:0]+'_'+blank[1+0:])
    return word


def get_user_input():
    return input('Guess the missing letter: ')
    
def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

