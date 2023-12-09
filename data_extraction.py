from sqlalchemy import inspect, text
import pandas as pd


class DataExtractor():
    
    @staticmethod
    def list_db_tables(db_engine):
        table_names = inspect(db_engine).get_table_names()
        print("Tables: \n", table_names)
        return table_names

    @staticmethod
    def execute_sql(db_engine, raw_sql="", set_write=False):
        with db_engine.connect() as conn:
            if set_write:
                if set_write:
                    write = "ON"
                else:
                    write = "OFF"
                return print(conn.execute(text(f"SET default_transaction_read_only = {write}")))
            result = conn.execute(text(raw_sql))
            return pd.DataFrame(result.fetchall())
