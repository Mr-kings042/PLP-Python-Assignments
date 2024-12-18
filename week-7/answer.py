import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

print(df.head())
print(df.info())
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
print(df.describe())
grouped = df.groupby('species').mean()
print(grouped)
print(df.columns)

# line chart
# plt.figure(figsize=(10, 6))
# sns.lineplot(data=df, x=['year'], y=['title'])
# plt.title('Trends Over Time')
# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal length (cm)'], bins=10, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

try:
    df = pd.read_csv('./book.csv')
except FileNotFoundError:
    print("The specified file was not found.")
except pd.errors.EmptyDataError:
    print("No data found in the file.")
except pd.errors.ParserError:
    print("Error parsing the file.")