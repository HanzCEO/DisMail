import random, string

def generate_email(username_length):
	username = ""
	domain = ""

	for i in range(username_length):
		username += random.choice(string.ascii_lowercase + string.digits)

	domain = get_domain()

	return f"{username}@{domain}"

def get_domain():
	providers = ["1secmail.com", "1secmail.org", "1secmail.net"]
	return random.choice(providers)
