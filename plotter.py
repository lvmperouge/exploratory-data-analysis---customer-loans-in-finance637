import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

def Plotter(self, dataframe):
    def __init__(self):
        # Set Seaborn style and color palette
        sns.set(style="whitegrid")
        self.palette = sns.color_palette("Set2").as_hex()

    def plot_bar(self, df, x, y, title=None):
        # Plot a bar chart using Seaborn
        plt.figure(figsize=(8, 6))
        sns.barplot(x=x, y=y, data=df, palette=self.palette)
        plt.title(title)
        plt.show()

    def plot_scatter(self, df, x, y, title=None):
        # Plot a scatter plot using Seaborn
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=x, y=y, data=df, palette=self.palette)
        plt.title(title)
        plt.show()

    def plot_box(self, df, x, y, title=None):
        # Plot a box plot using Seaborn
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=x, y=y, data=df, palette=self.palette)
        plt.title(title)
        plt.show()