import json
import pyodbc

with open('config.json', 'r') as file:
    config = json.load(file)


class Connection:
    def __init__(self):
        db_config = config['database']
        server = db_config['server']
        database = db_config['name']
        username = db_config['username']
        password = db_config['password']
        driver = db_config['driver']

        try:
            print('Connecting to database...')
            self.connection = pyodbc.connect(f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
        except Exception as error:
            print(error)
        finally:
            print('Connection finished')