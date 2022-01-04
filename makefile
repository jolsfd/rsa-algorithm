VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python

virtual_env:
	python -m venv venv

install:
	${PYTHON} -m pip install -r requirements.txt

run:
	${PYTHON} cli_rsa.py

test:
	${PYTHON} test_rsa.py

bench:
	${PYTHON} bench_rsa.py
