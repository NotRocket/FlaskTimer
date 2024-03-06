# Use an official Python runtime as an image
FROM python:3.9

WORKDIR /usr/src/app
COPY . .

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 5000
#CMD gunicorn -b 127.0.0.1:5000 app:app --timeout 600
CMD ["python", "app.py"]


