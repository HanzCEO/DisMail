from __future__ import ( division, absolute_import, print_function, unicode_literals )

import sys, os, tempfile, logging, zipfile, shutil, re
from distutils.dir_util import copy_tree

if sys.version_info >= (3,):
	import urllib.request as urllib2
	import urllib.parse as urlparse
else:
	import urllib2
	import urlparse

from requests import get
from json import loads
#from webbrowser import open as shell # Deprecated in v0.4.0


url = "https://www.1secmail.com/api/v1/"

def inbox(login, domain): #id, from, subject, date
	resjson = loads(get(f"{url}?action=getMessages&login={login}&domain={domain}").text)
	
	return resjson

def mes(login, domain, id):
	return get(f"{url}?action=readMessage&login={login}&domain={domain}&id={id}").text

def attachment(login, domain, id, file, size):
	url = f'{url}?action=download&login={login}&domain={domain}&id={id}&file={file}'
	nf = str(input("[#] Rename attachment to (leave blank to make it as is): "))
	dest = file if nf != '' else nf
	u = urllib2.urlopen(url)

	scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
	filename = os.path.basename(path)
	if dest:
		filename = os.path.join(dest)
	
	try:
		with open(filename, 'wb') as f:
			meta = u.info()
			meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
			meta_length = meta_func("Content-Length")
			file_size = None
			if meta_length:
				file_size = int(meta_length[0])
				file_size =  size if file_size is None else file_size
			print(f"Downloading: {file} Bytes: {file_size}")

			file_size_dl = 0
			block_sz = 8192
			while True:
				buffer = u.read(block_sz)
				if not buffer:
					break

				file_size_dl += len(buffer)
				f.write(buffer)

				status = f"{file_size_dl}"
				if file_size:
					status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
				status += chr(13)
				print(status, end="\r")
			print()
	except FileNotFoundError:
		print("[!] File not found")