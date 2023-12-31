from sqlalchemy import create_engine
import os
import yaml
import psycopg2
import pandas as pd
import numpy as np

def load_credentials(data):
    """Function loads credentials from yaml file."""
    with open (data, "r") as x: return yaml.safe_load(x)
    
def load_dataframe(data): return pd.read_csv(data)
    
class RDSDatabaseConnector:
    """Class makes the connection for to the cloud in order to extract the data."""
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.engine = None
    """Initialising this class passes the given credentials as a parameter."""

    def engine_start(self):
        """Method initialises an SQLAlchemy engine so that the data can be extracted."""
        if self.engine is None: self.engine = create_engine(f"postgresql+psycopg2://{self.dictionary['RDS_USER']}:{self.dictionary['RDS_PASSWORD']}@{self.dictionary['RDS_HOST']}:{self.dictionary['RDS_PORT']}/{self.dictionary['RDS_DATABASE']}")
        return self.engine
    
    def extract(self, table = "loan_payments"):
        """Method returns the data of the given yaml file in a dataframe format. """
        if self.engine is None:
            self.engine_start()
        return pd.read_sql_query(f"SELECT * FROM {table};", self.engine)

    def save(self, dataframe, yaml_file):
        """Method saves the dataframe to a .csv file."""
        return dataframe.to_csv(yaml_file)

class DataTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        """Initialises the DataTransform in order to convert all tabular values to specific types of data."""
        
    def to_float (self, column):
        """Method turns vales of a specified column from string to float data."""
        self.dataframe[column] = self.dataframe[column].to_string().str.extract('(\d+)')
        self.dataframe[column] = self.dataframe[column].astype('float')
        
    def to_date_time(self, column):
        """Method turns values of a specified column to datetime format."""
        for i in column:
            self.dataframe[i] = pd.to_datetime(self.dataframe[i], format="%b-%Y")
        
    def to_categorical(self, column):
        """Method assigns the values of a specified column to categorical data."""
        self.dataframe[column] = self.dataframe[column].astype('category')

    def drop(self, column):
        """Method removes specific columns."""
        for i in column:
            self.dataframe.drop(i, axis=1, inplace=True)
    

class DataFrameInfo:
    def __init__(self, dataframe):
        """Initialises class meant to help with extracting information about the data."""
        self.dataframe=dataframe

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
        count = self.dataframe.isna().sum()
        percent = (self.dataframe.isna().sum() / len(self.dataframe)) * 100
        return pd.DataFrame({'count_nan': count, 'percent_nan': percent})

class DataFrameTransform:
    def __init__(self, dataframe):
        """Initiates class meant to aid in filling the missing values in the """
        self.dataframe = dataframe;

    def impute_zeros(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(0)

    def impute_median(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median(), inplace=True)

file1 = "loan_payments.csv"
file2 = "modified_loan_payments.csv"
if __name__ == "__main__":
    #loading the credentials and Generating the raw data file
    credentials = load_credentials('credentials.yaml')
    Generator = RDSDatabaseConnector (credentials )
    data = Generator.extract()
    Generator.save(data, file1)
    dataframe = load_dataframe(file1)

    #familiarizing with data
    Stats = DataFrameInfo(dataframe)
    print(Stats.data_type())
    print(Stats.describe(['loan_amount']))
    print(Stats.distinct_values(['grade']))
    print(Stats.shape())
    print(Stats.null_values())

#transforming the data
    modified_dataframe = dataframe
    categorical_columns = ['grade', 'sub_grade', 'home_ownership', 'verification_status',
                           'loan_status', 'payment_plan', 'purpose','earliest_credit_line', 'application_type']
    datetime_columns = ['issue_date', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']
    
    float_columns = ['term', 'employment_length']
    TransformedData = DataTransform(modified_dataframe)
    TransformedData.to_categorical(categorical_columns)
    TransformedData.to_date_time(datetime_columns)
    TransformedData.to_float(float_columns)
    modified_dataframe = TransformedData.dataframe
    modified_dataframe.to_csv(file2)

    Stats = DataFrameInfo(modified_dataframe)
    print(Stats.data_type())
# funded_amount, term, int_rate, employment_length,last_payment_date and last_credit_pull_date columns 
# have less than 10% of null data therefore values will be imputed; 
# mths_since_last_delinq, mths_since_last_record, mths_since_last_major_derog, next_payment_date  and
# all have a very high percentage of null values and would be safer to drop entirely.

    dropped_columns=['mths_since_last_delinq', 'mths_since_last_record', 'mths_since_last_major_derog', 
                     'next_payment_date']
    TransformedData.drop(dropped_columns)
    modified_dataframe = TransformedData.dataframe
    modified_dataframe.to_csv(file2)
    Stats = DataFrameInfo(modified_dataframe)
    print(Stats.null_values())

#'funded_amount', 'int_rate', 'term' 'employment_length', 'last_payment_date' and 'collections_12_mths_ex_med' all have under 
#10% of data missing and will therefore either be discarded or imputed as follows

    TransformedDataFrame = DataFrameTransform(modified_dataframe)
    TransformedDataFrame.impute_zeros('employment_length') 
    #'employment_length' missing values are probably refering to people being unemployed therefore will be imputed as zeros
    TransformedDataFrame.impute_median(['funded_amount', 'term', 'int_rate'])
    modified_dataframe.dropna(subset=['last_payment_date'], inplace=True)
    Stats = DataFrameInfo(modified_dataframe)
    print(Stats.null_values())

#fix to_float method then finalize inputting nan 