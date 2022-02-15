import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
	name="DisMail",
	version="1.0.1",
	description="CLI to help you read your disposable emails straight from your console",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/HanzCEO/DisMail",
	author="Haxors",
	author_email="hanzhaxors@gmail.com",
	license="UNLICENSED",
	classifiers=[
		"License :: OSI Approved :: The Unlicense (Unlicense)",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
	],
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
		"requests==2.26.0", "click==8.0.3"
	],
	entry_points={
		"console_scripts": [
		    "dismail=DisMail.__main__:main"
		]
	},
)
