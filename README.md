[![GitHub version](https://badge.fury.io/gh/HanzHaxors%2FDisposableEmailCLI.svg?style=flat-square)](https://github.com/HanzHaxors/DisposableEmailCLI) <br/>
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://lbesson.mit-license.org/) [![Github all releases](https://img.shields.io/github/downloads/HanzHaxors/DisposableEmailCLI/total.svg?style=flat-square)](https://GitHub.com/HanzHaxors/DisposableEmailCLI/releases/)<br/>[![HitCount](http://hits.dwyl.io/HanzHaxors/DisposableEmailCLI.svg)](#)


# DisposableEmailCLI
Python 3.7.4 based app for disposable email service

# Tested On
* Python 3.7.x
* Python 3.8.x

# WARNING!!
**The author of this repository does not responsible for any illegal actions**

# How to use
### 1. From source
```
git clone https://github.com/HanzHaxors/DisposableEmailCLI
cd DisposableEmailCLI
python3 emailinbox.py
```

# Programs
Name | Filename | Description
---- | -------- | -----------
Email Inbox | emailinbox.py | Main script that shows disposable email panel and generates email randomly or set by user
Email Generator | emailgenerator.py | Python script for generating bulk disposable email
Script Updater | update.py | Python script that allows you to update this tool

### 2. .exe File
Run `dismail.exe` normally

# Flags/Arguments
Short Flag | Long Flag | Description
---------- | --------- | -----------
-h | --help | Shows help message (and exit)
-e | --email | A combination of login and domain like this, hanztest@1secmail.com PS: type it all for easy use including '@'
-l | --login | Username of email
-d | --domain | Domain of email (without '@')

**All of the flags/arguments is optional**

# What is 'username' and 'domain'?
username is a word before '@' <br>
domain is a word after '@' (like gmail.com, yahoo.com, etc.)

**Function: for retrieve inbox from specific email 'username'@'domain'**
