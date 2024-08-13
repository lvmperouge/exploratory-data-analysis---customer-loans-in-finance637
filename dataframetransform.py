import pandas as pd
import numpy as np

class DataFrameTransform:
    def __init__(self, dataframe):
        """Initiates class meant to aid in filling the missing values in the dataframe."""
        self.dataframe = dataframe;

    def input_zeros(self, column):
        """Method inputs zeros in spaces with missing values."""
        self.dataframe[column] = self.dataframe[column].fillna(0)

    def input_median(self, column):
        """Method inputs median values in spaces with missing values."""
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median(), inplace=True)
        
    def drop(self, column):
        """Method removes specific columns."""
        for i in column:
            self.dataframe.drop(i, axis=1, inplace=True)