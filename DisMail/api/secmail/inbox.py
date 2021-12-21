import requests

from .classes import Mail

def format_url(action, **kwargs):
	queryString = '&'.join([f"{key}={kwargs[key]}" for key in kwargs])
	dest = f"https://1secmail.com/api/v1/?action={action}&{queryString}"

	return dest

def get_inbox(login, domain):
	res = requests.get(format_url("getMessages", login=login, domain=domain))
	# TODO: Check response

	data = res.json()
	return data

def read_mail(login, domain, mailid):
	res = requests.get(format_url("readMessage", login=login, domain=domain, id=mailid))
	# TODO: Check response

	data = res.json()
	return Mail(mailid=data["id"], sender=data["from"], **data)

def download_attachment(login, domain, mailid, filename):
	pass
