import curses
from curses.textpad import rectangle

# Create option form
def Options(scr, y, x, options, label='', initial_value=0, pointer='>', inactive=''):
	if len(pointer) != len(inactive):
		inactive = inactive + ' ' * (len(pointer) - len(inactive))
	previously_selected = initial_value
	selected = initial_value
	nlines = len(options)
	ncols = max([len(option['label']) for option in options])
	editwin = curses.newwin(nlines, ncols + 3, y+1, x+1)

	rectangle(scr, y, x, y+nlines+1, x+ncols+len(label)+len(pointer)+3)
	scr.addstr(y, x+2, label)
	scr.refresh()

	for i, option in enumerate(options):
		if len(option['label']) == 0:
			scr.addstr(y+i+1, x+1, len(inactive) * ' ' + option['label'])
		else:
			scr.addstr(y+i+1, x+1, inactive + ' ' + option['label'])

	while True:
		scr.addstr(y+previously_selected+1, x+1, inactive + ' ' * (len(pointer) - len(inactive)))
		scr.addstr(y+selected+1, x+1, pointer)
		# scr.move(y+selected+1, x+1)
		c = scr.getch()

		previously_selected = selected
		if c == 10:
			break
		elif c == curses.KEY_UP:
			selected = (selected - 1) if (selected - 1) >= 0 else nlines - 1
			if len(options[selected]['label']) == 0:
				selected = (selected - 1) if (selected - 1) >= 0 else nlines - 1
		elif c == curses.KEY_DOWN:
			selected = (selected + 1) if (selected + 1) < nlines else 0
			if len(options[selected]['label']) == 0:
				selected = (selected + 1) if (selected + 1) < nlines else nlines + 1

	return selected
