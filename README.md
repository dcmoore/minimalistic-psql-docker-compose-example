# Minimalistic psql docker-compose Example

A simple proof of concept that shows how to build an application that depends on a locally running postgres db without needing to "install" postgres on your local computer. This sort of setup is helpful for applications that want to have an integration testing layer that requires an ephemeral database. You simply edit db/seed.sql with whatever you want, then you can test your application with that seed data already loaded and ready to go.

## Setup

Create the following files in your **db directory** and fill them with whatever values you want:

- postgres_db.txt
- postgres_password.txt
- postgres_user.txt

## Build & Run

To start app, run: `docker-compose up --build`
