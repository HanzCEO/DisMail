import requests

def format_url(action, **kwargs):
	queryString = '&'.join([f"{key}={kwargs[key]}" for key in kwargs])
	dest = f"https://1secmail.com/api/v1/?action={action}&{queryString}"

	return dest

def get_inbox(login, domain):
	res = requests.get(format_url("getMessages", login=login, domain=domain))
	# TODO: Check response

	data = res.json()
	return data
