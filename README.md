# boilerplate-python-cleanarch
Boilerplate for Python using Clean Architecture 

## Requirements
- Python version 3.6+
- pip (package manager for Python), included since Python 3.4.
- virtualenv (tool to create isolated Python environments)

## Installing
Install virtualenv:
```
python3 -m pip install virtualenv
```

Create isolated Python environments using virtualenv:
```
virtualenv venv -p /usr/local/bin/python3 env
```

Activate virtual environment:
```
source venv/bin/activate
```

Install dependencies:
```
python3 -m pip install -r requirements.txt
```

Environment variables:
```
cp env.example .env
```

## Database Migiration
```
make migrate
```

## Run
```
make run
```
By default it will listen on `http://0.0.0.0:8001`

## Running Tests
Install requirement for test:
```
python3 -m pip install -r requirements/test.txt
```

Then run:
```
make test
```

### Coverage
```
make coverage
```

## Lint
```
make lint
```

## Module Generator
If you working on new module and too lazy to create the structure one by one, you can use generator:
```
python3 gawekno.py sales v1
```
