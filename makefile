default: main

deps:
	pip install gspread
	pip install oauth2client

main:
	python main.py
