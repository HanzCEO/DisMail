import curses

def Table(scr, y, x, headers, rows):
	limits = {}
	suffixes = {}

	for i, header in enumerate(headers):
		limits[header] = len(header)
		for row in rows:
			chrlen = len(str(row[header]))
			if chrlen > limits.get(header, 0):
				limits[header] = chrlen+2
			if limits[header] > 40:
				limits[header] = 40
				suffixes[header] = "..."

	for i_h, header in enumerate(headers):
		x_padding = x+sum(list(limits.values())[:i_h])+(i_h*2)

		scr.addstr(y, x_padding, str(header), curses.A_BOLD)
		for i, row in enumerate(rows):
			scr.addstr(
				y+i+1,
				x_padding,
				str(row[header])[:limits[header]-len(suffixes.get(header, ''))] + suffixes.get(header, '')
			)

	scr.refresh()
