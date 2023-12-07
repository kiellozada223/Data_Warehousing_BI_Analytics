import os
import psycopg2
import pandas as pd
from tabulate import tabulate

import mytest

from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_duplicates
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_min_max
from dataqualitychecks import run_data_quality_check

pgpassword = os.environ.get("POSTGRES_PASSWORD")
conn = psycopg2.connect(
    user = 'postgres',
    password = pgpassword,
    host = 'localhost',
    port = '5432',
    database = 'billing_dw')

print("Connected to data warehouse")

results = []
tests = {key:value for key,value in mytest.__dict__.items() if key.startswith('test')}
for testname,test in tests.items():
    test['conn'] = conn
    results.append(run_data_quality_check(**test))

df = pd.DataFrame(results)
df.index+=1
df.columns = ['Test Name', 'Table', 'Column', 'Test Passed']
print(tabulate(df, headers='keys', tablefmt='psql'))
conn.close()
print("Disconnected from the data warehouse")
