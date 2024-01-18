import pandas as pd 
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