install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

format:
	black *.py

test:
	python -m pytest -vv

train:
	source .venv/bin/activate &&\
		python training/train.py

predict:
	docker-compose up -d && sleep 5 && .  make_predict.sh