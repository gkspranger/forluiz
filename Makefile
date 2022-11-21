help:
	@echo "make r			remove venv"
	@echo "make i			create venv and install dependencies"
	@echo "make f			run code formatter"
	@echo "make l			run code linter"
	@echo "make n			run code"

r:
	@rm -fr venv

i:
	@python3 -m venv venv
	@./venv/bin/pip3 install -r requirements.txt

f:
	@./venv/bin/black *.py

l:
	@./venv/bin/pylint *.py

n:
	@./venv/bin/python3 worldcup.py
