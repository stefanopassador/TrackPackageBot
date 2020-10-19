FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=tracker_db
ENV POSTGRES_DB=tracker_db
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql