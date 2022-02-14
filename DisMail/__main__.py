import re, random
import click

from .mailutils import generate_email
from .api.secmail import SecmailAccount, download_attachment

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

def size_convert(file_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if file_size < 1024 or unit == 'TB':
            break
        file_size /= 1024.0
    return f'{file_size:.2f} {unit}'

def display_mail(account, mail):
	print("=" * 20)
	print(f"{mail.subject}")
	print(f"From: {mail.sender}")
	print(f"Date: {mail.date}\n")

	print(mail.textbody)

	if len(mail.attachments) > 0:
		print()
		print("Attachments")
		print("=" * 20)

		for i, atch in enumerate(mail.attachments, start=1):
			print(f"[{i}] {atch['filename']} ({size_convert(atch['size'])})")

		inp = input("Download attachment? (Y/N) ")
		if inp.upper() == "Y":
			print("Type attachment number to start downloading (leave blank to abort)")
			inp = input(">> ")

			if inp.isnumeric():
				attachment = mail.attachments[int(inp)-1]
				filename = attachment["filename"]
				filesize = attachment["size"]

				# Start downloading
				stream = download_attachment(
					account.login, account.domain, mail.id,
					filename
				)

				for progress in stream:
					print(f"{filename} ({size_convert(progress)} of {size_convert(filesize)})", end="\r")
				print("\nFile downloaded")

	input("Press Enter/Return to continue to menu")

def menu(account):
	print(
		f"{account.email}\n" +
		"=" * 20 + "\n"
	)

	for mail in account.get_inbox():
		print(f"[{mail.position}] {mail.sender}: {mail.subject[:50]} | {mail.date}")

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
			display_mail(account, mail)

if __name__ == "__main__":
	main()
