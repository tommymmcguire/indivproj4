install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m unittest discover

format:	
	black *.py 

lint:
	# ruff check *.py
	# nbqa ruff *.ipynb
		
all: install test format 