import yaml
import sqlalchemy

class DatabaseConnector():
    
    @staticmethod
    def read_db_creds(filepath):
        with open(filepath, 'r') as file:
            db_cred = yaml.safe_load(file)
            return db_cred

    @staticmethod
    def init_db_engine(db_cred):
        return sqlalchemy.create_engine(f'postgresql+psycopg2://{db_cred["RDS_USER"]}:{db_cred["RDS_PASSWORD"]}@{db_cred["RDS_HOST"]}:{db_cred["RDS_PORT"]}/{db_cred["RDS_DATABASE"]}')

    @staticmethod
    def format_insert_statement(data, table_name):
        values_string = ""# //[for data]
        insert_string = ""
        return

    @staticmethod
    def upload_to_db(db, table_name, data,  if_exists="replace"):
        return_val = 0
        try:
            data.to_sql(table_name, db, index=False, if_exists=if_exists)
        except Exception as error:
            print("An error uploading has occured: ", error)
            return_val = 1
        return return_val