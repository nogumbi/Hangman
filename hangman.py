import random

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    index = random.randint(0, len(word)-1)
    missing_letter = '_'*index+word[index]+'_'*(len(word)-index-1)
    return missing_letter


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if char in original_word and char not in answer_word:
        return True
    if char in original_word and char in answer_word:
        counter = 0
        counter1 = 0
        for i in original_word:
            if char == i:
                counter == 1
        for j in answer_word:
            if char == j:
                counter1 == 1
            else:
                return False
    else:
        return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    answer_word = list(answer_word)
    original_word = list(original_word)
    for i in range(0, len(original_word)):
        if original_word[i] == char:
            answer_word[i] = original_word[i]
    return ''.join(answer_word) 

def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):  
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)
    
# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    hangman = ['/----\n|\n|\n|\n|\n_______','/----\n|   0  \n|\n|\n|\n_______','/----\n|   0\n|  /|\\\n|\n|\n_______','/----\n|   0\n|  /|\\\n|   |\n|\n_______','/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______']
    if number_guesses == 4:
        print(hangman[0])
    if number_guesses == 3:
        print(hangman[1])
    if number_guesses == 2:
        print(hangman[2])
    if number_guesses == 1:
        print(hangman[3])
    if number_guesses == 0:
        print(hangman[4])

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    number_guesses = 5
    count = 0
    while answer != word and count != number_guesses:
        guess = get_user_input()
        #exit game if input is quit or exit
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        elif guess == "quit" or guess == "exit":
            print('Bye!')
            break
        else:
            number_guesses -= 1
            do_wrong_answer(answer, number_guesses)
            if number_guesses == 0:
                print('Sorry, you are out of guesses. The word was: ' + word)
            
# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

