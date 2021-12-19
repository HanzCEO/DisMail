from .inbox import get_inbox

class SecmailAccount(object):
	def __init__(self, email):
		self.login, self.domain = email.split('@')

	def refresh(self):
		self.inbox = get_inbox(self.login, self.domain)

	def get_inbox(self, pagination=0, amount=5):
		start = pagination * amount
		end = start + amount

		return self.inbox[start:end]
