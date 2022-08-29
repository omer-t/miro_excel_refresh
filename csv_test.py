import json

import pandas as pd
import snowflake.connector


def snowflake_connection(credentials_file_path: str):
    with open(credentials_file_path, 'r') as file:
        credentials = json.load(file)
    connection = snowflake.connector.connect(**credentials)
    cursor = connection.cursor()
    cursor.execute('select current_user(), current_database(), current_schema()')
    cursor.fetchall()

    return connection


conn = snowflake_connection('credentials/snowflake.json')
sql_file_path = f'sql/example.sql'
with open(sql_file_path, 'r') as file:
    sql = file.read()
df = pd.read_sql(sql, conn)
df.to_csv(f'output/csv_test.csv', index=False)
# df.to_excel(f'output/csv_test.xlsx', engine='xlsxwriter', index=False)
print('done!')
df.SPEND.sum()
