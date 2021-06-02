import curses, random, math, re
from curses.textpad import Textbox, rectangle
from .options import Options
from .input import Input
from .table import Table

page: int = 0
menu_x, menu_y = (10, 5)

# Main menu interface
# aka inbox
def i_menu(scr, account):
	global page
	global menu_x
	global menu_y

	last_cursor_option = 0

	if account.email is None:
		i_login(scr)

	while True:
		opts = [
			{
				"value": 0,
				"label": "Read email"
			},
			{
				"value": 1,
				"label": "Prev page"
			},
			{
				"value": 2,
				"label": "Next page"
			},
			{
				"value": 3,
				"label": "Refresh inbox"
			},
			{
				"value": 4,
				"label": ""
			},
			{
				"value": 5,
				"label": "Generate new email"
			},
			{
				"value": 6,
				"label": "Exit"
			}
		]
		headers = ['No', 'Subject', 'From']
		rows = account.cached.inbox
		reserved = len(opts) * 2 + 3

		# Display stuffs
		scr.clear()
		scr.addstr(menu_y, menu_x, f"Email: {account.email}", curses.A_BOLD)

		# Create table
		Table(
			scr,
			menu_y+2,
			menu_x,
			headers,
			rows[10 * page:(10 * page) + 10]
		)

		# Ask user input
		result = Options(
			scr,
			menu_y+reserved+2,
			menu_x,
			opts,
			label=f"Main Menu [Page {page}]",
			pointer=" █",
			# inactive=" #",
			initial_value=last_cursor_option
		)

		# Clean up
		scr.addstr(menu_y+reserved, menu_x, "Loading, please wait...")
		scr.refresh()

		# Do actions
		if result == 0:
			i_read(scr, account)
		elif result == 1:
			page = (page - 1) if (page - 1) >= 0 else math.ceil(len(rows) / 10) - 1
		elif result == 2:
			page = (page + 1) if (page + 1) < math.ceil(len(rows) / 10) else 0
		elif result == 3:
			account.cache_inbox()
		elif result == 4 or result == 5:
			print("NEW EMAIL ADDRESS")
			i_login(scr, account)
		elif result == 6:
			exit()
		else:
			pass

		last_cursor_option = result

# Login interface
def i_login(scr, account):
	scr.clear()

	scr.addstr(8, 10, "Put nothing to generate random email")
	box = Input(scr, 10, 10, label="LOGIN", placeholder="test@example.com")
	box.edit()

	message = box.gather().strip()
	scr.addstr(13, 11, f"Logging in as {message}")

	if message == '':
		account.change_email(account.generate_email())
	else:
		account.change_email(message)

	scr.refresh()

	return message

# Reading email interface
def i_read(scr, account):
	scr.clear()

	scr.addstr(8, 10, "Put the email number to read them")
	message = 1
	box = Input(scr, 10, 10, label="READ EMAIL", placeholder="1")
	box.edit()

	try:
		message = re.findall(r"\d+", box.gather().strip())[0]
		message = int(message)
	except Exception as e:
		message = 1

	scr.refresh()

	i_display_mail(scr, account, message - 1)

# Display reading interface
def i_display_mail(scr, account, id):
	global menu_x
	global menu_y

	scr.clear()

	mail = account.cached.inbox[id]
	mail_body = account.read_mail_content(id)

	scr.addstr(menu_y, menu_x, f"Subject\t: {mail['Subject']}", curses.A_BOLD)
	scr.addstr(menu_y + 1, menu_x, f"From\t\t: {mail['From']}", curses.A_BOLD)
	scr.addstr(menu_y + 2, menu_x, f"Date\t\t: {mail['Date']}", curses.A_BOLD)


	for i, line in enumerate(mail_body.split('\n')):
		scr.addstr(menu_y + 4 + i, menu_x, line)

	scr.addstr(menu_y + 4 + len(mail_body.split('\n')), menu_x, "Press anything to continue", curses.A_DIM)
	scr.getch()

if __name__ == '__main__':

	curses.wrapper(i_menu)
