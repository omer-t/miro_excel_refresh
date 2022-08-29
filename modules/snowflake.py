import json

import pandas as pd
import snowflake.connector


def snowflake_connection(credentials_file_path: str) -> snowflake.connector.SnowflakeConnection:
    with open(credentials_file_path, 'r') as file:
        credentials = json.load(file)
    connection = snowflake.connector.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute('select current_user(), current_database(), current_schema()')
    cursor.fetchall()

    return connection


def sql_file_to_dataframe(sql_file_path: str, conn: snowflake.connector.SnowflakeConnection) -> pd.DataFrame:
    with open(sql_file_path, 'r') as file:
        sql = file.read()
    return pd.read_sql(sql, conn)
