FROM tensorflow/tensorflow:2.3.0

WORKDIR /home/app

COPY ./rest/ .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py"]

