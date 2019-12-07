from prettytable import PrettyTable
from colorama import Fore, Back, Style, init
import os, threading, argparse, requests, time, json, random
from secmail.api import inbox, message, attachment

# clear screen
def ClrScrn():
	os.system('cls' if os.name == 'nt' else 'clear')

############# COLORAMA ######################
init()

fblack = Fore.BLACK
fblue = Fore.BLUE
fcyan = Fore.CYAN
fgreen = Fore.GREEN
flblack = Fore.LIGHTBLACK_EX
flblue = Fore.LIGHTBLUE_EX
flcyan = Fore.LIGHTCYAN_EX
flgreen = Fore.LIGHTGREEN_EX
flmagenta = Fore.LIGHTMAGENTA_EX
flred = Fore.LIGHTRED_EX
flwhite = Fore.LIGHTWHITE_EX
flyellow = Fore.LIGHTYELLOW_EX
fmagenta = Fore.MAGENTA
fred = Fore.RED
freset = Fore.RESET
fwhite = Fore.WHITE
fyellow = Fore.YELLOW

bblack = Back.BLACK
bblue = Back.BLUE
bcyan = Back.CYAN
bgreen = Back.GREEN
blblack = Back.LIGHTBLACK_EX
blblue = Back.LIGHTBLUE_EX
blcyan = Back.LIGHTCYAN_EX
blgreen = Back.LIGHTGREEN_EX
blmagenta = Back.LIGHTMAGENTA_EX
blred = Back.LIGHTRED_EX
blwhite = Back.LIGHTWHITE_EX
blyellow = Back.LIGHTYELLOW_EX
bmagenta = Back.MAGENTA
bred = Back.RED
breset = Back.RESET
bwhite = Back.WHITE
byellow = Back.YELLOW

sbright = Style.BRIGHT
sdim = Style.DIM
snormal = Style.NORMAL
resetall = Style.RESET_ALL
#############################################

##################### MAIN FUNCTIONS ########
def goRead(id, login, domain):
	theRes = message(login, domain, id)
	ClrScrn()
	print(theRes)
	table = PrettyTable()
	table.field_names = [f"{flgreen}Body"]
	#table.add_row(f"{flwhite+str(theRes['body'])}")
	print(table)
	os.system('pause')
	tableTheInbox(login, domain)
	

def tableTheInbox(login, domain):
	resInb = inbox(login, domain)
	ClrScrn()
	print(f"{fwhite}Email address: "+bcyan+login+bgreen+"@"+domain+resetall)
	theJson = resInb
	table = PrettyTable()
	table.field_names = [f"{flcyan}id",f"{flgreen}From",f"{flmagenta}Subject",f"{flyellow}Date"]
	for x in range(len(theJson)):
		table.add_row([flcyan+str(theJson[x]['id']),flgreen+theJson[x]['from'],flmagenta+theJson[x]['subject'],flyellow+theJson[x]['date']+freset])
	print(table)
	inp = input(f"{fgreen}[+] Message id to read (r to refresh inbox): ")
	if inp == "r":
		tableTheInbox(login, domain)
	else:
		goRead(str(inp), login, domain)
def hlp():
	ClrScrn()
	table = PrettyTable()
	table.field_names = [f"{flred}Full Argument", f"{flgreen}Less Argument", f"{fwhite}Description"]
	table.add_row([f"{fred}--help", f"{fgreen}-h", f"{fwhite}Help. show this message"])
	table.add_row([f"{fred}--login", f"{fgreen}-l", f"{fwhite}username of email (ex. {bcyan}hanzo221{bgreen}@1secmail.com{resetall} the cyan colored is 'login')"])
	table.add_row([f"{fred}--domain", f"{fgreen}-d", f"{fwhite}host of email (ex. {bcyan}hanzo221{bgreen}@1secmail.com{resetall} the green colored is 'domain')"])
	print(table)

def initme():
	global arg_login
	global arg_domain
	
	parser = argparse.ArgumentParser(description="Disposable Email Generator and Inbox", add_help=False)
	parser.add_argument("-h", "--help", help="Help Menu", action="store_true")
	
	parser.add_argument("-l", "--login", type=str)
	parser.add_argument("-d", "--domain", type=str)
	
	args = parser.parse_args()
	
	if args.help:
		hlp()
		exit()
	
	if args.login and args.domain:
		arg_login = args.login
		arg_domain = args.domain
		
		tableTheInbox(arg_login, arg_domain)
	else:
		log = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+str(random.randint(1,10000))
		dom = random.choice(["1secmail.com","1secmail.net","1secmail.org"])
		
		
		tableTheInbox(log, dom)
		

if __name__ == "__main__":
	initme()