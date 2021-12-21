class Mail:
	def __init__(self, mailid, sender, **kwargs):
		self.id = mailid
		self.sender = sender
		self.subject = kwargs["subject"]
		self.date = kwargs["date"]
		self.attachments = kwargs["attachments"]
		self.body = kwargs["body"]
		self.textbody = kwargs["textBody"]
		self.htmlbody = kwargs["htmlBody"]
