from prettytable import PrettyTable
from colorama import Fore, Back, Style, init
import os, threading, argparse, time, json, random, re
from secmail.api import *
from requests import *
from requests.exceptions import *
from subprocess import call as cmd
'''
BUG FIXES
BUG #1:
 - Can't open the email by id
 SOLVED: it was a <built_in_id> i should use another. thanks to https://github.com/tashan022
'''

# clear screen
def ClrScrn():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("\n")

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
		tabled = PrettyTable()
		print(flwhite+theRes["textBody"]+"\n\n\n")
		tabled.field_names = [f"{fcyan}No{fwhite}", f"{flyellow}URL{fwhite}"]
		tabled.align = 'l'
		table.align = 'l'
		print("\n\n")
		regexed = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", theRes["body"])
		try:
			for x in range(1000000000):
				tabled.add_row([fcyan+str(x+1), flyellow+regexed[x]+fwhite])
		
		#except IndexError:
		#	pass
		#
		#try:
		#	regexed = re.findall(r"(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", theRes["body"])
		#	for x in range(1000000000):
		#		tabled.add_row([fcyan+str(x), flyellow+regexed[x]])
		#	
		except IndexError:
			print(tabled)
		table.field_names = [f"{fcyan}Attachments{fwhite}", f"{flyellow}Type{fwhite}", f"{flmagenta}Size (Bytes){fwhite}"]
		print("\nMessageID: {eid}\n".format(eid=eid))
		try:
			for x in range(1000):
				table.add_row([fcyan+theRes["attachments"][x]["filename"], flyellow+theRes["attachments"][x]["contentType"], flmagenta+str(theRes["attachments"][x]["size"])+fwhite])
			
		except IndexError:
			print(table)
			if len(theRes["attachments"]) > 0:
				try:
					fi = input(f'{fcyan}[+] Attachment to download (ctrl + c to cancel): ')
					attachment(login, domain, eid, fi, theRes["attachments"][x]["size"])
				except KeyboardInterrupt:
					print(f'{flmagenta}\n[#] Cancelling...')
			
			os.system('pause')
			tableTheInbox(login, domain)
	

def tableTheInbox(login, domain):
	print(f'{fcyan}[i] Loading...')
	try:
		resInb = inbox(login, domain)
		
		# v0.4.0: Now you can read mail easier
		# v0.4.0-t2: Change mails order, still starts with 0
		# v0.4.0-t3: Change mails order starts with 1
		mailIds = list()
		for __mail in resInb:
			mailIds.append(__mail['id'])
		mailIds.reverse()
		resInb.reverse()
		
		ClrScrn()
		#print(mailIds)
		print(f"{fwhite}Email address: "+bcyan+login+freset+"@"+bgreen+domain+resetall)
		theJson = resInb
		table = PrettyTable()
		table.field_names = [f"{flcyan}id",f"{flgreen}From",f"{flmagenta}Subject",f"{flyellow}Date"]
		for x in range(len(theJson)):
			table.add_row([flcyan+str(mailIds.index(theJson[x]['id'])+1),flgreen+theJson[x]['from'],flmagenta+theJson[x]['subject'],flyellow+theJson[x]['date']+freset])
		print(table)
		print(f'{fyellow}r - Refresh the inbox\nn - Create new email.')
		try:
			inp = input(f"{fgreen}[+] Message id to read: ")
		except KeyboardInterrupt:
			print(f'{fred}\n[!] Exitting...')
			exit()
		
		if 'r' in inp or 'n' in inp:
			''
		else:
			print(f'{fcyan}[#] Loading message...{fwhite}')
		
		if inp == "r":
			tableTheInbox(login, domain)
		elif inp == "n":
			log = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")+str(random.randint(1,100000))
			dom = random.choice(["1secmail.com","1secmail.net","1secmail.org"])
			
			
			tableTheInbox(log, dom)
		else:
			try:
				inp = mailIds[int(inp) - 1] # v0.4.0-t1, v0.4.0-t4: Now optimized
			except IndexError:
				print("[!] Index error, referring to the latest email...") # v0.4.0-t5: Added exception catch for smooth performance
				inp = mailIds[len(mailIds) - 1]
			goRead(login, domain, str(inp))
	except ConnectionError:
		print(f'{fred}[!] Connection error')
	except KeyboardInterrupt:
		print(f'{fred}[!] Cancelling...')
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
	if args.email:
		arg_email = args.email
		if '@' in arg_email:
			arg_email = args.email.split('@')
		
		tableTheInbox(arg_email[0], arg_email[1])
	else:
		log = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+str(random.randint(1,10000))
		dom = random.choice(["1secmail.com","1secmail.net","1secmail.org"])
		
		
		tableTheInbox(log, dom)
		

if __name__ == "__main__":
	cmd("title Disposable Email :: HanzHaxors", shell=True)
	ClrScrn()
	initme()