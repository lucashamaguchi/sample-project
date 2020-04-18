# sample-api

## Main Dependencies and Requisites

- Python 3
- Flask

## Running Locally

Set the environment variables (following the env.example) or create a file named `.env` with them in the project root folder.


### Option 1 - With Docker

On the terminal:

```bash
docker-compose up
```

### Option 2 - Python virtual env

Instantiate a new virtual environment with your favorite tool.

Install everything you need:
```bash
pip install -r requirements.txt
```

Before running the project you'll need to add these environment variables:
```bash
export FLASK_RUN_PORT=5000
export FLASK_APP=sample_api.app
```

If you want to run the project on debug mode also add this environment variable:
```bash
export FLASK_ENV=development
```


On the virtual environment, Finally start the project with either:
```bash
flask run
```

or
```bash
python sample_api/app.py
```

or
```bash
sh entrypoint-dev.sh
```

## Tests

To run the tests simply run:
```bash
pytest
```
