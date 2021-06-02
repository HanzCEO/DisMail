.PHONY: update upload
DEFAULT: upload

update:
	python3 updater/updater.py

clean:
	mv dist/* archive

upload:
	python3 setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*
