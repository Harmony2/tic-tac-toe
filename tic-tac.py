#!/usr/bin/python3

from unicurses import *

def welcome(stdscr):
	stdscr.addstr(1,1,"Hello, bro")
	stdscr.addstr(2,1,"this would be tic tac toe")


def main():
	stdscr = initscr()

	stdscr.clear()
	stdscr.border()

	welcome(stdscr)
	stdscr.refresh()

	while True:
		if stdscr.getkey() == "q":
			endwin()
			quit()
main()
