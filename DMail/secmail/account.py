import random, string
from requests import get
from json import loads

class Cache(object):
	def __init__(self):
		super().__init__()
		self.inbox = list()


class EmailAccount(object):
	def __init__(self, email=None, domain=None):
		super().__init__()

		if email is None:
			self.email = self.generate_email(domain)
		else:
			self.email = email

		self.cached = Cache()
		self.cache_inbox()

	def change_email(self, new_email):
		self.email = new_email
		self.cache_inbox()

	def generate_email(self, domain=None):
		azAZ09 = string.ascii_letters + string.digits
		domains = [
			'1secmail.com', '1secmail.org', '1secmail.net',
			'wwjmp.com', 'esiix.com', 'xojxe.com',
			'yoggm.com'
		]

		domain = domain if domain is not None else random.choice(domains)
		username = ''.join([random.choice(azAZ09) for i in range(10)])

		email = f'{username}@{domain}'
		return email

	def cache_inbox(self):
		# Clean ups
		self.cached.inbox = list()

		# Variables
		url = "https://www.1secmail.com/api/v1/"
		login, domain = self.parse_email()
		inbox = list()

		# Generate fake emails
		# for i in range(random.randint(10, 40)):
		# 	vercode = ''.join([chr(random.randint(65, 90)) for i in range(4)])
		# 	self.cached.inbox.append({
		# 		"No": i+1,
		# 		"Subject": f"Hello, your verification code is {vercode}. Happy learning!",
		# 		"From": f"bot{i}@verification.org",
		# 		"Body": f"Your verification code is {vercode}. Happy learning!\n" +
		# 				f"This mail has been brought to you by verification.org\n\n" +
		# 				f"Verify anything, anytime, costless."
		# 	})

		# Fetch from API
		data = loads(get(f"{url}?action=getMessages&login={login}&domain={domain}").text)

		# Restructure
		for i, mail in enumerate(data):
			_mail = dict()
			_mail['No'] = i + 1
			_mail['From'] = mail['from']
			_mail['Id'] = mail['id']
			_mail['Date'] = mail['date']
			_mail['Subject'] = mail['subject']

			inbox.append(_mail)

		# Cache
		self.cached.inbox = inbox

	def read_mail_content(self, index):
		# `id` param is the array index
		url = "https://www.1secmail.com/api/v1/"
		login, domain = self.parse_email()
		id = self.cached.inbox[index]['Id']

		if self.cached.inbox[index].get('Body', None) is None:
			data = loads(get(f"{url}?action=readMessage&login={login}&domain={domain}&id={id}").text)
			self.cached.inbox[index]['Body'] = data['body']
			return data['body']
		else:
			return self.cached.inbox[index]['Body']

	def parse_email(self):
		# Simply split things
		# Still dangerous
		return self.email.split('@')
