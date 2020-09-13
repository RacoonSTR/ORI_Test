FROM python:3

ADD src /src
ADD requirements.txt /

RUN pip install -r ./requirements.txt

WORKDIR ./src

CMD [ "python", "./main.py" ]