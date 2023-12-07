from time import time, ctime

conn = None

def run_data_quality_check(**options):
    print("*" * 50)
    print(ctime(time()))
    start_time = time()
    testname = options.pop("testname")
    test = options.pop("test")
    print(f"Starting test {testname}")
    status = test(**options)
    print(f"Finished Test {testname}")
    print(f"Test Passed {status}")
    end_time = time()
    options.pop("conn")
    print("Test Parameters")
    for key, value in options.items():
        print(f"{key} = {value}")
    print()
    print("Duration : ", str(end_time - start_time))
    print(ctime(time()))
    print("*" * 50)
    return testname,options.get('table'),options.get('column'),status

def check_for_nulls(column, table, conn = conn):
    SQL =f'SELECT COUNT(*) FROM "{table}" WHERE {column} IS NULL'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return bool(row_count)

def check_min_max(column, table, minimum, maximum, conn=conn):
    SQL = f'SELECT COUNT(*) FROM "{table}" WHERE {column} < {minimum} or {column} > {maximum}'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    cursor.close()
    return not bool(row_count[0])

def check_for_valid_values(column, table, valid_values = None, conn=conn):
    SQL=f'SELECT DISTINCT ({column}) FROM "{table}"'
    cursor = conn.cursor()
    cursor.execute(SQL)
    result = cursor.fetchall()
    actual_values = {x[0] for x in result}
    print(actual_values)
    status = [value in valid_values for value in actual_values]
    cursor.close()
    return all(status)

def check_for_duplicates(column, table, conn=conn):
    SQL = f'SELECT COUNT({column}) FROM "{table}" GROUP BY {column} HAVING COUNT({column}) > 1'
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_count = cursor.fetchone()
    return not bool(row_count)