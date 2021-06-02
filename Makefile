.PHONY: update upload
DEFAULT: upload

update:
	python3 updater/updater.py

clean:
	mv dist/* archive

upload:
	@echo ---- BUILDING -------------------------------------
	sudo python3 setup.py sdist bdist_wheel
	@echo ---- CHECKING -------------------------------------
	twine check dist/*
	@echo ---- UPLOADING ------------------------------------
	twine upload dist/*
