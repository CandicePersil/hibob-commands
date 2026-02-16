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
Activate virtual env
```
-- pipenv shell
```

## Run command
### Dependances
* data folder in src containing a .env file
* .env must contain service user authentication tokens
```
SERVICE_ID=...
SERVICE_PASSWORD=...
```

No need to activate the virtual env to run the commands.
```
cd ./src
pipenv run python main.py
```
It should generate a result file in a results folder.
File format `employees_{YYYYMMDD}.csv` where `{YYYYMMDD}` is the date of the file generation.

## Run tests
```
cd ./src
pipenv run pytest ./test/integration
```
No need to activate the virtual env to run the tests.