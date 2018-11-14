#!/usr/bin/python3

from unicurses import *

def welcome(stdscr):
	stdscr.addstr(1,1,"Hello, bro")
	stdscr.addstr(2,1,"this would be tic tac toe")
	stdscr.addstr(5,5,"Press any key to continue.")
	stdscr.getch()

def clear(stdscr):
	stdscr.clear()
	stdscr.border()
	stdscr.refresh()

def table(stdscr, pos):
	centx = getmaxyx(stdscr)[1]//2
	centy = getmaxyx(stdscr)[0]//2


	stdscr.addstr(centy-2,centx-2, "|")
	stdscr.addstr(centy-2,centx+1, "|")
	stdscr.addstr(centy-1,centx-4, "--------")
	stdscr.addstr(centy,centx-2, "|")
	stdscr.addstr(centy,centx+1, "|")
	stdscr.addstr(centy+1,centx-4, "--------")
	stdscr.addstr(centy+2,centx-2, "|")
	stdscr.addstr(centy+2,centx+1, "|")

	stdscr.move(centy,centx)

	return pos

def mov(y,x):
	input = getkey()

	if input == "w":
		y = y-1
	elif input == "s":
		y = y+1
	elif input == "d":
		x = x+1
	elif input == "a":
		x = x-1
	elif input == "q":
		quit()
	move(y,x)
	mov(y,x)

def main():
	stdscr = initscr()
	centx = getmaxyx(stdscr)[1]//2
	centy = getmaxyx(stdscr)[0]//2

	stdscr.clear()
	stdscr.border()

	welcome(stdscr)
	clear(stdscr)
	stdscr.refresh()

	pos = [['O','X','O'],[' ',' ',' '],[' ',' ',' ']]
	table(stdscr,pos)

	while True:
		mov(centy,centx)

main()
