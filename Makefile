hello:
	echo "This is my first make command"
install:
	echo "Placeholder for install command"
lint:
	pylint --disable=R,C,E1120,W0613 hello.py

all: hello install