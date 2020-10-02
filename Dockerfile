FROM python:3

ADD src /src
ADD requirements.txt /
ADD data/markup /data/markup

RUN pip install -r ./requirements.txt

WORKDIR ./src

CMD [ "python", "./main.py" ]