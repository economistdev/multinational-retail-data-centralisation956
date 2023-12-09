#!/usr/bin/env python3

from database_utils import DatabaseConnector
from data_extraction import DataExtractor


db_connector = DatabaseConnector()

db_creds = db_connector.read_db_creds("db_creds.yaml")
db = db_connector.init_db_engine(db_creds)


extractor = DataExtractor()
table_names = extractor.list_db_tables(db)

query1 = f"SELECT * FROM {table_names[0]}"
table = extractor.read_rds_table(db, query1)
print(table)


