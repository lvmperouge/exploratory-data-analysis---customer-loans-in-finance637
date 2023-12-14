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

class DataFrameInfo:
    def __init__(self, dataframe):
        """Initialises class meant to help with extracting information about the data."""
        self.dataframe = dataframe

    def data_type(self):
        """Method returns the type of data for each column."""
        return self.dataframe.dtypes
    
    def describe(self, column):
        """Method returns statistics for a specific column."""
        return self.dataframe.describe()

    def distinct_values(self, column):
        """Method returns distinct values in a column."""
        return self.dataframe[column].value_counts

    def shape(self):
        """Method returns the shape of the data."""
        return self.dataframe.shape

    def null_values(self):
        """Method returns a DataFrame with 2 columns, one for the total NULL values and one for the percentage."""
        count= self.dataframe.isna().sum()
        percent= (self.dataframe.isna().sum() / len(self.dataframe)) * 100
        return pd.DataFrame({'count_nan': count, 'percent_nan': percent})
    
    def drop(self, column):
        """Method removes specific columns."""
        for i in column:
            self.dataframe.drop(i, axis=1, inplace=True)


if __name__ == '__main__':
    dataframe = load_data("loan_payments.csv")
    Stats = DataFrameInfo(dataframe)

    print(Stats.data_type())
    print(Stats.describe(['loan_amount']))
    print(Stats.distinct_values(['grade']))
    print(Stats.shape())
    print(Stats.null_values())
    # funded_amount, term, int_rate, employment_length,last_payment_date and last_credit_pull_date columns 
    # have less than 10% of null data therefore values will be imputed; 
    # mths_since_last_delinq, mths_since_last_record, mths_since_last_major_derog, next_payment_date  and
    # and mths_since_last_major_derog all have a very high percentage of null values and would be safer to
    # drop entirely.
    