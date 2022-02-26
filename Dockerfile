# syntax=docker/dockerfile:1
FROM python:3.8.12-slim-bullseye
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
# Lint
CMD [ "python3", "-m", "pylint", "--disable=R,C", "app.py"]
# Test
CMD ["python3", "-m", "pytest", "-vv"]
CMD ["flask", "run"]