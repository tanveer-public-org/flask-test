FROM python:3.8

RUN apt-get update &&\
    apt-get install -y -q sqlite3 &&\
    rm -rf /var/lib/apt/lists/*

ENV USE_ENV true
ENV WORKDIR /opt/test/python-flask-project
ENV HOME $WORKDIR

RUN groupadd app &&\
    useradd -g app -d $WORKDIR -s /sbin/nologin -c 'Docker image user for the app' app &&\
    mkdir -p $WORKDIR

ADD . $WORKDIR

RUN pip install -r $WORKDIR/requirements.txt

RUN chown -R app:app $WORKDIR

USER app

CMD cd $WORKDIR && python ./app.py

