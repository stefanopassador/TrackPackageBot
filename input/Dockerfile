FROM python:latest
WORKDIR /code
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY private_config.py private_config.py
RUN pip install -r requirements.txt
CMD ["python", "-u", "app.py"]