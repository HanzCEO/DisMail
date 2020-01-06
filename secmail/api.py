from requests import get
from json import loads
from webbrowser import open as shell

url = "https://www.1secmail.com/api/v1/"

def inbox(login, domain): #id, from, subject, date
	resjson = loads(get(f"http://1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}").text)
	
	return resjson

def mes(login, domain, id):
	return get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}").text

def attachment(login, domain, id, file):
	shell('http://1secmail.com/api/v1/?action=download&login='+login+'&domain='+domain+'&id='+id+'&file='+file)