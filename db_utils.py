from sqlalchemy import create_engine
import yaml
import pandas as pd


with open('credentials.yaml') as file:
    prime_service = yaml.safe_load(file)

class RDSDatabaseConnector:
    
    
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = None


    def init_engine(self):
        if self.engine is None:
            conn_str = f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
            self.engine = create_engine(conn_str)
        return self.engine