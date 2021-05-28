FROM python:3.6.9
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pyhton test.py
EXPOSE 5000
COPY . .
CMD ["flask", "run"]