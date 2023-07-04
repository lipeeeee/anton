#
#	ANTON MAKEFILE
#

run:
	python main.py

compile:
	pyinstaller.exe -F main.py --collect-all customtkinter --icon=anton.ico -n 'anton'	
