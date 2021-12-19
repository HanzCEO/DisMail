import re, random
import click

from mailutils import generate_email

@click.command()
@click.argument("email", required=False)
def main(email):
	emailRegEx = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

	if email is None or re.match(emailRegEx, email) is None:
		email = generate_email(random.randint(4, 8))

	print(f"Logged in as: {email}")

if __name__ == "__main__":
	main()
