import curses
from curses.textpad import Textbox, rectangle

# Create input boxes
def Input(scr, y, x, label='', placeholder=None, nlines=1, ncols=25):
	editwin = curses.newwin(nlines, ncols, y+1, x+1)

	rectangle(scr, y, x, y+nlines+1, x+ncols+1)
	scr.addstr(y, x+2, label)
	scr.refresh()

	box = Textbox(editwin)

	if placeholder is not None:
		editwin.addstr(placeholder, curses.A_DIM)
		editwin.getch()
		editwin.clear()

	return box
