FROM python:3.11.4

ENV PYTHONBUFFER=1

WORKDIR /code

COPY requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

#RUN pip3 install Brlapi==0.8.4

COPY . .

EXPOSE 8000

CMD ["python3","manage.py","runserver"]