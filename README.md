This is a Flask API for managing guest appearances on Late Show episodes.

## Features
- View all episodes and guests
- View detailed episode with guest appearances
- Add new guest appearances with validations

## Routes
- `GET /episodes`
- `GET /episodes/:id`
- `GET /guests`
- `POST /appearances`

## Setup
```bash
cd server
pipenv install
export FLASK_APP=app
flask db init
flask db migrate -m "init"
flask db upgrade
python seed.py
flask run
```
