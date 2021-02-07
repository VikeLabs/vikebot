FROM python:3.9
ENV BOT_TOKEN=""
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /app/
WORKDIR /app
CMD ["python", "main.py"]
