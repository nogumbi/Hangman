# Problems - Hangman
Iteration 1: The player has one chance to guess the entire word that is chosen randomly from a predefined list.
Notice how we are simplifying the rules of the game. We don’t worry about guessing letters, and the player either survives or dies after just one guess. Importantly, we focus on choosing a random word from a list, and checking if the guessed word matches the chosen word.

Iteration 2: The player can also load different word lists and gets hints for their guesses.

Iteration 3: The player makes guesses one letter at a time until they win or die. We also draw the hangman with each guess so that the player knows how many chances are left.



### To Run

* `python3 hangman.py`
* follow the input prompts to play the game

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific step's unittest, e.g step *1*: `python3 -m unittest tests.test_main.MyTestCase.test_step1`
* _Note_: at the minimum, these (*unedited*) tests must succeed before you may submit the solution for review.
