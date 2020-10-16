FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
COPY private_config.py private_config.py
CMD ["python", "-u", "app.py"]