# hibob-commands
HiBob commands including connection to HiBob API and data formating.

## In short
### Need
Display list of employees.
Display list of employees with name, surname, title, start date,
end date and type of contract.
Download list of employees.

### Action plan
Connection to HiBob api.
Get raw data.
Format data.

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
