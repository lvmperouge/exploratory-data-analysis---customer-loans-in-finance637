import pandas as pd
import numpy as np

class DataTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        """Initialises the DataTransform in order to convert all tabular values to specific types of data."""
        
    def to_float (self, column):
        """Method turns values of a specified column from string to float data."""
        for i in column:
        # Ensure the column is of type string
            if self.dataframe[i].dtype == 'object':
                self.dataframe[i] = self.dataframe[i].str.extract('(\d+)').astype(float)
            else:
                # If it's already numeric, convert it directly
                self.dataframe[i] = self.dataframe[i].astype(float)

    def to_date_time(self, column):
        """Method turns values of a specified column to datetime format."""
        self.dataframe[column] = pd.to_datetime(self.dataframe[column], format="%b-%Y")
        
    def to_categorical(self, column):
        """Method assigns the values of a specified column to categorical data."""
        self.dataframe[column] = self.dataframe[column].astype('category')

    def drop_column(self, column):
        """Method removes specific columns."""
        for i in column:
            self.dataframe.drop(i, axis=1, inplace=True)