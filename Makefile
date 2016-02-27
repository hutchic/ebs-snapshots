.PHONY: snapshots
SHELL = /bin/bash

venv:
	test -d venv || virtualenv venv
	venv/bin/pip install -r requirements.txt

snapshots:
	venv/bin/ansible-playbook snapshots.yml
