from sqlalchemy import create_engine
import os
import yaml
import psycopg2
import pandas as pd
import numpy as np

def load_credentials(data):
    """Function loads credentials from yaml file."""
    with open (data, "r") as x: return yaml.safe_load(x)
    
def load_data(data): return pd.read_csv(data)


class DataFrameTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe;

    def impute_zeros(self, column):
        for i in column:
            self.dataframe[i] = self.dataframe[i].fillna(0)

    def impute_median(self, column):
        for i in column:
            self.dataframe[i] = self.dataframe[i].fillna(self.dataframe[i].median())

