
FROM ubuntu:16.04

#database config:
ARG dbName=Sociality.io
ARG dbUser=ekmek
ARG dbUserPw=veristronkpw
##########################

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

RUN apt install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update -y
RUN apt install -y python3.9
RUN apt-get install -y python3-pip
RUN pip3 install Flask

USER postgres
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER $dbUser WITH CREATEDB LOGIN SUPERUSER PASSWORD '${dbUserPw}';" &&\
    createdb  -O $dbUser $dbName
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

EXPOSE 5432
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 3333

#TODO: install en-GB locale for db
ENV LC_ALL=C.UTF-8 
ENV LANG=C.UTF-8
COPY . .
CMD (/usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c config_file=/etc/postgresql/9.3/main/postgresql.conf)&    python3 main.py