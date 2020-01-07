from prettytable import PrettyTable
from colorama import Fore, Back, Style, init
import os, threading, argparse, requests, time, json, random
from secmail.api import *

'''
BUG FIXES
BUG #1:
 - Can't open the email by id
 SOLVED: it was a <built_in_id> i should use another thanks to https://github.com/tashan022
'''

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
def goRead(login, domain, eid):
	theRes = mes(login, domain, eid)
	ClrScrn()
	if theRes == "Message not found":
		print(theRes)
		os.system('pause')
		tableTheInbox(login, domain)
	else:
		theRes = loads(theRes)
		table = PrettyTable()
		print(flwhite+theRes["textBody"]+"\n\n\n")
		table.field_names = [f"{fcyan}Attachments{fwhite}", f"{flyellow}Type{fwhite}", f"{flmagenta}Size (Bytes){fwhite}"]
		print("\n\n")
		try:
			for x in range(1000):
				table.add_row([fcyan+theRes["attachments"][x]["filename"], flyellow+theRes["attachments"][x]["contentType"], flmagenta+str(theRes["attachments"][x]["size"])])
			
		except IndexError:
			print(table)
			if len(theRes["attachments"]) > 0:
				try:
					fi = input(f'{fcyan}[+] Attachment to download (ctrl + c to cancel): ')
					attachment(login, domain, eid, fi)
				except KeyboardInterrupt:
					print(f'{flmagenta}\n[#] Cancelling...')
			
			os.system('pause')
			tableTheInbox(login, domain)
	

def tableTheInbox(login, domain):
	resInb = inbox(login, domain)
	ClrScrn()
	print(f"{fwhite}Email address: "+bcyan+login+freset+"@"+bgreen+domain+resetall)
	theJson = resInb
	table = PrettyTable()
	table.field_names = [f"{flcyan}id",f"{flgreen}From",f"{flmagenta}Subject",f"{flyellow}Date"]
	for x in range(len(theJson)):
		table.add_row([flcyan+str(theJson[x]['id']),flgreen+theJson[x]['from'],flmagenta+theJson[x]['subject'],flyellow+theJson[x]['date']+freset])
	print(table)
	print(f'{fyellow}r - Refresh the inbox\nn - Create new email.')
	try:
		inp = input(f"{fgreen}[+] Message id to read: ")
	except KeyboardInterrupt:
		print(f'{fred}\n[!] Exitting...')
		exit()
	
	print(f'{fcyan}[#] Loading message...{fwhite}')
	
	if inp == "r":
		tableTheInbox(login, domain)
	elif inp == "n":
		log = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+str(random.randint(1,10000))
		dom = random.choice(["1secmail.com","1secmail.net","1secmail.org"])
		
		
		tableTheInbox(log, dom)
	else:
		goRead(login, domain, str(inp))
def hlp():
	ClrScrn()
	table = PrettyTable()
	table.field_names = [f"{flred}Full Argument", f"{flgreen}Less Argument", f"{fwhite}Description"]
	table.add_row([f"{fred}--help", f"{fgreen}-h", f"{fwhite}Help. show this message"])
	table.add_row([f"{fred}--email", f"{fgreen}-e", f"{fwhite}A combination of login and domain like this, hanztest@1secmail.com\nPS: type it all for easy use including '@'"])
	table.add_row([f"{fred}--login", f"{fgreen}-l", f"{fwhite}username of email (ex. {bcyan}hanzo221{bmagenta}@{bgreen}1secmail.com{resetall} the cyan colored is 'login')"])
	table.add_row([f"{fred}--domain", f"{fgreen}-d", f"{fwhite}host of email (ex. {bcyan}hanzo221{bmagenta}@{bgreen}1secmail.com{resetall} the green colored is 'domain')"])
	print(table)

def initme():
	global arg_login
	global arg_domain
	global arg_email
	
	parser = argparse.ArgumentParser(description="Disposable Email Generator and Inbox", add_help=False)
	parser.add_argument("-h", "--help", help="Help Menu", action="store_true")
	
	parser.add_argument("-e", "--email", type=str)
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
	elif '@' in args.email:
		arg_email = args.email.split('@')
		
		tableTheInbox(arg_email[0], arg_email[1])
	else:
		log = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+str(random.randint(1,10000))
		dom = random.choice(["1secmail.com","1secmail.net","1secmail.org"])
		
		
		tableTheInbox(log, dom)
		

if __name__ == "__main__":
	initme()