from sqlalchemy import create_engine
import yaml
import pandas as pd


def load_credentials(x):
    with open(x,'r') as file:
        return yaml.safe_load(file)
    
class RDSDatabaseConnector:
    
    
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = None


    def init_engine(self):
        if self.engine is None:
            conn_str = f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
            self.engine = create_engine(conn_str)
        return self.engine
    
    def extract_data(self, table_name="loan_payments"):
        
        if self.engine is None:
            self.init_engine()
        
        query = f"SELECT * FROM {table_name};"
        return pd.read_sql_query(query, self.engine)

    def save_df(self, df, filename):
       
        return df.to_csv(filename)