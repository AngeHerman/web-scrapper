
.PHONY: all run clean

all: run

run:
	python3 main.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
