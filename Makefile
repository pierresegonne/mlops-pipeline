install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

format:
	black *.py

train:
	source .venv/bin/activate &&\
		python training/train.py