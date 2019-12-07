from requests import get
from json import loads
from webbrowser import open as shell

url = "https://www.1secmail.com/api/v1/"

def inbox(login, domain): #id, from, subject, date
	resjson = loads(get('https://www.1secmail.com/api/v1/?action=getMessages&login='+login+'&domain='+domain).text)
	
	return resjson

def message(login, domain, id):
	resjson = loads(get('https://www.1secmail.com/api/v1/?action=readMessages&login='+login+'&domain='+domain+'&id='+id).text)
	
	return resjson

def attachment(login, domain, id, file):
	shell('https://www.1secmail.com/api/v1/?action=download&login='+login+'&domain='+domain+'&id='+id+'&file='+file)