from datetime import datetime

class Stash(object):
	def __init__(self, mailid, sender, subject, date):
		self.id = mailid
		self.sender = sender
		self.subject = subject
		self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
		self.position = 0

	def __str__(self):
		return f"[{self.id}] {self.sender}: {self.subject} | {self.date}"

	def __repr__(self):
		return self.__str__()

class Inbox(object):
	def __init__(self, stashes):
		self.stashes = stashes

	def __getitem__(self, index):
		return self.stashes[index]

	def get_by_id(self, mailid):
		for stash in self.stashes:
			if stash.id == mailid:
				return stash

	def filter_by_sender(self, sender):
		tmp = list()

		for stash in self.stashes:
			if stash.sender == sender:
				tmp.append(stash)

		return tmp

	def filter_by_subject(self, subject):
		tmp = list()

		for stash in self.stashes:
			if stash.subject == subject:
				tmp.append(stash)

		return tmp

	def filter_by_word_in_subject(self, word):
		tmp = list()

		for stash in self.stashes:
			if word in stash.subject:
				tmp.append(stash)

		return tmp

	def filter_by_date(self, start, end):
		# Normalize datetime
		if not isinstance(start, datetime):
			start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
		if not isinstance(end, datetime):
			end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

		tmp = list()

		for stash in self.stashes:
			if start >= stash.date or stash.date <= end:
				tmp.append(stash)

		return tmp
