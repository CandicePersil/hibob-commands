# Employees manager
Employees manager including connection to HiBob API, data formating and other functionalities.

## In short
### Need
Display list of employees.
Display list of employees with name, surname, email, title, start date and type of contract.
Download list of employees.
Format the list according to the specifications of the platform ingesting the data.
Compare the platform's existing data with the new provided data.

## Environment setp up
Use pipenv

Intall pipenv
```
-- pipx install pipenv
-- pipenv install
```
Activate env
```
-- pipenv shell
```
Install dependences
```
-- pip install dotenv
-- pip install pydantic
-- pip install pytest
-- pip install requests
```

## Run command
### Dependances
* data folder in src containing a .env file
* .env must contain service user authentication tokens
```
SERVICE_ID=...
SERVICE_PASSWORD=...
```

```
cd ./src
python main.py
```
It should generate 

## Run tests
```
cd ./src
pytest ./test/integration/
```
