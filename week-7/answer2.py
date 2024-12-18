import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the book dataset
try:
    df_books = pd.read_csv('./book.csv')  # Adjust path if necessary
    print(df_books.head())
    
    # Ensure the 'rank' column is treated as a categorical variable
    df_books['rank'] = df_books['rank'].astype('category')

    # Line chart: Trends in the number of nominees/winners by year
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_books, x='year', hue='rank')
    plt.title('Number of Nominees/Winners Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend(title='Rank')
    plt.xticks(rotation=45)
    plt.show()

    # Bar chart: Count of books by subcategory and rank
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df_books, x='subcategory', hue='rank')
    plt.title('Count of Books by Subcategory and Rank')
    plt.xlabel('Subcategory')
    plt.ylabel('Count')
    plt.legend(title='Rank')
    plt.xticks(rotation=45)
    plt.show()

    # Histogram: Distribution of ranks
    plt.figure(figsize=(10, 6))
    sns.histplot(df_books['rank'], discrete=True, kde=False)
    plt.title('Distribution of Ranks')
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter Plot: Number of books per subcategory over the years
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df_books, x='year', y='subcategory', hue='rank', style='rank', s=100)
    plt.title('Number of Books per Subcategory Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Subcategory')
    plt.xticks(rotation=45)
    plt.legend(title='Rank')
    plt.show()

except FileNotFoundError:
    print("The specified file was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("No data found in the file.")
except pd.errors.ParserError:
    print("Error parsing the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")