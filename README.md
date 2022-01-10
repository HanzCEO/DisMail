# DisMail
Python 3 based app for disposable email service

[![Downloads](https://static.pepy.tech/personalized-badge/dismail?period=total&units=none&left_color=grey&right_color=yellowgreen&left_text=Downloads)](https://pepy.tech/project/dismail)

## How to use
### 1. From source
```sh
$ git clone git@github.com:HanzCEO/DisMail.git
$ cd DisMail
$ python3 DisMail/__main__.py [EMAIL ADDRESS]
```
### 2. From PyPi
```sh
$ sudo pip3 install DisMail
$ dismail [EMAIL ADDRESS]
```

## Usage
```
Usage: dismail [OPTIONS] [EMAIL]

Options:
  --help  Show this message and exit.
Arguments:
  email   username@domain pair used for login, defaults to random email
```

## Known issues
 - **SecMail API** limit attachment size to around 40000 bytes
