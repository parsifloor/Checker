from setuptools import setup

setup(
	name="Checker",
	version="1.0.0",
	author="Marat Guseynov",
	author_email="cooltable01@gmail.com",
	description="The cool script for check balance in console",
	packages=['src'],
	install_requires=[
		'requests',
		'bs4',
		'colorama',
	]
)
