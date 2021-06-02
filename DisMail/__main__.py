import click, random, string, curses
from .secmail import *
from .interface import *

# Globals
account			= None
screen			= None

@click.command()
@click.argument('email', required=False, default=None)
def main(**kwargs):
	curses.wrapper(_main, **kwargs)

def _main(scr, **kwargs):
	global screen
	global account

	screen = scr
	email = kwargs['email']

	account = EmailAccount(email)
	i_menu(screen, account)

if __name__ == '__main__':
	main()
