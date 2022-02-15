from .classes import Inbox, Stash
from .inbox import get_inbox, read_mail

class SecmailAccount(object):
	def __init__(self, email):
		self.pagination = 0
		self.email = email
		self.login, self.domain = email.split('@')
		self.inbox = list()

	def refresh(self):
		inbox = get_inbox(self.login, self.domain)
		stashes = list()

		for i, mail in enumerate(inbox, start=1):
			newStash = Stash(
				mail["id"], mail["from"],
				mail["subject"], mail["date"]
			)
			newStash.position = i
			stashes.append(newStash)

		self.inbox = Inbox(stashes)

	def get_max_page(self, amount=5):
		retval = len(self.inbox.stashes) // amount

		if len(self.inbox.stashes) % amount != 0:
			retval += 1

		if retval == 0:
			retval = 1

		return retval

	def get_inbox(self, pagination=None, amount=5):
		if pagination is not None:
			self.pagination = pagination

		# Clamp value
		self.pagination = max(min(self.pagination, self.get_max_page()-1), 0)

		start = self.pagination * amount
		end = start + amount

		return self.inbox[start:end]

	def get_mail(self, index):
		index = abs(index)

		if index >= len(self.inbox.stashes):
			index = len(self.inbox.stashes) - 1

		return read_mail(self.login, self.domain, self.inbox[index].id)

	def test(self):
		from datetime import datetime

		print("Get By Id")
		print(self.inbox.get_by_id(self.inbox[0].id))
		print("Get by sender")
		print(self.inbox.filter_by_sender(self.inbox[0].sender))
		print("Get by subject")
		print(self.inbox.filter_by_subject(self.inbox[0].subject))
		print("Get by word in subject")
		print(self.inbox.filter_by_word_in_subject(self.inbox[0].subject.split(' ')[0]))

		start = self.inbox[0].date
		end = datetime.max
		print(self.inbox.filter_by_date(start, end))
