import random
import game.terminal_service

class Jumper:
    """The person falling from the sky 
    
    The responsibility of the jumper is to track the state of the parachute and how many wrong guesses have been made.
    
    """

    def __init__(self, terminal_service):
        """Constructs a new Jumper.
        """
        self.terminal = terminal_service
        self._guess = []
        self.bad_guess_count = 0
        self._parachute = [
            "  _____  ",
            " /_____\ ",
            " \     / ",
            "  \   /  ",
            "    O    ",
            "  / | \  ",
            "   / \   ",
            "         ",
            "^^^^^^^^^"
            ]


    """ This will track the amount of bad guesses """
    def made_bad_guess(self):
        if self.bad_guess_count >= 5:
            return
        self.bad_guess_count += 1
        self._parachute.pop(0)


    """ This will draw out the parachute and on bad guess 5 it will replace the O with an X """
    def draw(self):
        if self.bad_guess_count >= 5:
            self.terminal.write_text("    X    ")
        for line in self._parachute:
            self.terminal.write_text(line)


