import json

import snowflake.connector
import modules.files as files


def connection(credentials_file_path: str):
    credentials = files.json_load(credentials_file_path)
    # with open(credentials_file_path, 'r') as file:
    #     credentials = json.load(file)

    connection = snowflake.connector.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute('select current_user(), current_database(), current_schema()')
    cursor.fetchall()

    return connection
