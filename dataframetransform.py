import pandas as pd
import numpy as np

class DataFrameTransform:
    def __init__(self, dataframe):
        """Initiates class meant to aid in filling the missing values in the """
        self.dataframe = dataframe;

    def impute_zeros(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(0)

    def impute_median(self, column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median(), inplace=True)
    def drop(self, column):
        """Method removes specific columns."""
        for i in column:
            self.dataframe.drop(i, axis=1, inplace=True)