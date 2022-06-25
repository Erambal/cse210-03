# from game.wordList import Word_list
# from game.terminal_service import TerminalServicez
# wordlist = Word_list(TerminalService())
# wordlist.draw_state(["A","C", "O"])

from game.director import Director

director = Director()
director.start_game()