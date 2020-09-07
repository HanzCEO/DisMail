.PHONY: test update
DEFAULT: test
test:
	python3 emailgenerator.py
	python3 emailinbox.py

update:
	python3 updater/updater.py