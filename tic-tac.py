#!/usr/bin/python3
from curses import *


def mov(window,atty,attx):
	if window.getkey() == "a":
		attx = attx-1
	elif window.getkey() == "d":
		attx = attx+1

	window.move(atty,attx)
	#window.redrawwin()
	window.refresh()
	mov(window,atty,attx)

def main():
	window = initscr()
	window.addstr(1,1,"teste")

	centy = window.getmaxyx()[0]//2
	centx = window.getmaxyx()[1]//2

	window.addstr(2,1,str(centx))
	window.addstr(3,1,str(centy))
	window.getch()

	window.clear()
	window.refresh()
	window.border()

	mov(window,centy,centx)

main()
