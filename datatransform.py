import pandas as pd
import numpy as np

class DataTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        """Initialises the DataTransform in order to convert all tabular values to specific types of data."""
        
    def to_float (self, column):
        """Method turns vales of a specified column from string to float data."""
        self.dataframe[column] = self.dataframe[column].to_string().str.extract('(\d+)').astype(float)
                
    def to_date_time(self, column):
        """Method turns values of a specified column to datetime format."""
        self.dataframe[column] = pd.to_datetime(self.dataframe[column]) 
        
    def to_categorical(self, column):
        """Method assigns the values of a specified column to categorical data."""
        self.dataframe[column] = self.dataframe[column].astype('category')

    def drop(self, column):
        """Method removes specific columns."""
        for i in column:
            self.dataframe.drop(i, axis=1, inplace=True)