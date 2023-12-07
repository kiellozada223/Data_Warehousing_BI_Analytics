echo "Creating the database"

createdb -h localhost -U postgres -p 5432 billing_dw

echo "Extracting Files"
tar -xvzf billing-datawarehouse.tgz

echo "Creating Schema"

psql -h localhost -U postgres -p 5432 billing_dw < star-schema.sql

echo "Loading the data"

psql -h localhost -U postgres -p 5432 billing_dw < DimCustomer.sql
psql -h localhost -U postgres -p 5432 billing_dw < DimMonth.sql
psql -h localhost -U postgres -p 5432 billing_dw < FactBilling.sql

echo "Finished loading data"

psql -h localhost -U postgres -p 5432 billing_dw < verify.sql