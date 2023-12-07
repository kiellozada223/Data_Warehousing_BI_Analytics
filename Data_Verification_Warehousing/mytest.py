from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_for_duplicates

test1 = {
    "testname":"Check for nulls",
    "test":check_for_nulls,
    "column":"billedamount",
    "table":"FactBilling"
}

test2 = {
    "testname":"Check for duplicates",
    "test": check_for_duplicates,
    "column":"billid",
    "table":"FactBilling"
}

test3 = {
    "testname": "Check for valid values",
    "test": check_for_valid_values,
    "column": "quarter",
    "table": "DimMonth",
    "valid_values": {1,2,3,4}
}