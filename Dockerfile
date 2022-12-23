FROM python:3.10.8

ENV FLASK_APP=app
ENV FLAK_DEBUG=$FLAK_DEBUG
ENV JWT_SECRET_KEY='113865193623474475555296534400970127735'

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY . /opt

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT