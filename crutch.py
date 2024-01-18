import seaborn as sns
import matplotlib.pyplot as plt

class Plotter:
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

# Example usage:
# Instantiate the DataFramePlotter class
df_plotter = Plotter()

# Example DataFrame
import pandas as pd

data = {
    'Category': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'],
    'Value': [10, 15, 7, 12, 8, 11, 14, 9]
}

df = pd.DataFrame(data)

# Plot bar chart
df_plotter.plot_bar(df=df, x='Category', y='Value', title='Bar Chart Example')

# Plot scatter plot
df_plotter.plot_scatter(df=df, x='Category', y='Value', title='Scatter Plot Example')

# Plot box plot
df_plotter.plot_box(df=df, x='Category', y='Value', title='Box Plot Example')
