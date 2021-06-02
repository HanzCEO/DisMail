import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
	name="dmail",
	version="1.0.0-rc1",
	description="CLI to help you read your disposable emails straight from your console",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/HanzCEO/DMail",
	author="HanzHaxors",
	author_email="hanzhaxors@gmail.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
	],
	packages=["DMail"],
	include_package_data=True,
	install_requires=["requests", "click"],
	entry_points={
		"console_scripts": [
		    "dmail=DMail.__main__:main",
		]
	},
)
