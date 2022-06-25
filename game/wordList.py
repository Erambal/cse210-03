import random
from game.terminal_service import TerminalService 
class Word_list:
    """A person who directs the game. 
    """
    def __init__(self, terminal_service):
        self.terminal_service = terminal_service
        self._list_of_words = ['computer', 'laptop', 'python', 'mouse', 'keyboard']
        self.current_secret = self._get_secret_word()

    """ This will draw out the blanks for the words"""
    def draw_state(self, list_of_guesses):
        output = ""
        for letter in self.current_secret:
            if letter.lower() in list_of_guesses:
                output = output + letter + " "
            else:
                output = output + "_ "
        self.terminal_service.write_text(output)

    """This gets the word"""
    def get_current_secret(self):
        return self.current_secret

    """This allows for lowercase input from user"""
    def is_letter_in_secret(self, letter):
        return letter.lower() in self.current_secret.lower()

    """This verifies if the letter is part of the word"""
    def is_guessed(self, letters):
        result = True
        for letter in self.current_secret:
            if not letter.lower() in letters:
                result = False
        return result

    """This keeps track of the amount of bad guesses"""
    def too_many_guesses(self, letters):
        badGuesses = 0
        for guess in letters:
            if not guess in self.current_secret.lower():
                badGuesses += 1
        return badGuesses > 4

    def _get_secret_word(self):
        """Gets a secret word for the puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: A secret word
            ]        """
        index = random.randrange(0, len(self._list_of_words))
        secretWord = self._list_of_words[index].upper()
        return secretWord
