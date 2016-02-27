.PHONY: clean install snapshots
SHELL = /bin/bash

clean:
	rm -rf venv

install:
	test -d venv || virtualenv venv
	venv/bin/pip install -r requirements.txt

snapshots: install
	venv/bin/ansible-playbook snapshots.yml
