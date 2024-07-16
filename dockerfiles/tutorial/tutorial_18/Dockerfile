FROM postgres:12

COPY ./setup-contrib.sql /docker-entrypoint-initdb.d/1-setup.sql
COPY ./contributors.sql /docker-entrypoint-initdb.d/2-data.sql
COPY ./setup-users.sql /docker-entrypoint-initdb.d/3-users.sql

RUN chown postgres:postgres /docker-entrypoint-initdb.d/*.sql
