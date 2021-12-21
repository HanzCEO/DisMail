import re, random
import click

from mailutils import generate_email
from api.secmail import SecmailAccount

@click.command()
@click.argument("email", required=False)
def main(email):
	emailRegEx = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

	if email is None or re.match(emailRegEx, email) is None:
		email = generate_email(random.randint(4, 8))

	print(f"Logged in as: {email}")
	account = SecmailAccount(email)

	account.refresh()
	#print(account.test())

	input_loop(account)

def display_mail(mail):
	print("=" * 20)
	print(f"{mail.subject}")
	print(f"From: {mail.sender}")
	print(f"Date: {mail.date}\n")

	print(mail.textbody)
	input("Press Enter/Return to continue")

def menu(account):
	print(
		f"{account.email}\n" +
		"=" * 20 + "\n"
	)

	for mail in account.get_inbox():
		print(f"[{mail.position}] {mail.sender}: {mail.subject[:20]} | {mail.date}")

	print()
	print(f"Page {account.pagination+1} of {account.get_max_page()}")
	print("r - Refresh inbox")
	print("q - Quit")
	print("b - Previous page")
	print("n - Next page")
	print("Type the email number to read them")

def input_loop(account):
	while True:
		print("\n" * 50)
		menu(account)
		inp = input(">> ")

		if inp == "r":
			account.refresh()
		elif inp == "q":
			break

		elif inp == "b":
			account.pagination -= 1
		elif inp == "n":
			account.pagination += 1

		elif inp.isnumeric():
			index = int(inp) - 1
			mail = account.get_mail(index)
			# Display email
			display_mail(mail)

if __name__ == "__main__":
	main()
