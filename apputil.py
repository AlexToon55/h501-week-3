import seaborn as sns
import pandas as pd


# update/add code below ...


#exercise 1
# A simple function to compute the nth Fibonacci number
def fibonacci(n):
    "Return the nth Fibonacci number."
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b


#exercise 2
# A function to convert a positive integer to its binary representation
def to_binary(n):
    "Convert an integer to its binary representation as a string."
    if n < 0:
        return "Input should be a non-negative integer."
    elif n == 0:
        return "0"
    bits = []
    # Convert to binary
    while n:
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))
# Example usage
num = 18  # Example input





#exercise 3

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
Raw_columns = df_bellevue.columns.tolist() #store the raw column names


def task_1(): 
    #Return a list of all column names, *sorted* such that the first column has the *least* missing values, and the last column has the *most* missing values (use the raw column names)
    # *Note: there is an issue with the `gender` column you'll need to remedy first ...*


#clean the g and h rows from the gender column
    df_bellevue['gender'] = (
        df_bellevue['gender']
        astype('string')
        .str.lower()
        .str.strip()
        .replace
        ({'h': pd.NA, 'g': pd.NA, 'm': 'm', 'f': 'f', '?': pd.NA})
    )
    missing_counts = df_bellevue[Raw_columns].isnull().sum() #use the raw column names to count missing values
    sorted_columns = missing_counts.sort_values().index.tolist()
    return sorted_columns


def task_2(): 
    #Return a **data frame** with two columns:
   #- the year (for each year in the data), `year`
   #- the total number of entries (immigrant admissions) for each year, `total_admissions`
    df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in']).dt.year
    admissions_per_year = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
    
    return admissions_per_year


def task_3(): 
    #Return a **series** with:
    # - Index: gender (for each gender in the data)
    # - Values: the average age for the indexed gender.
    
    pandas_series = df_bellevue.groupby('gender')['age'].mean()
    return pandas_series




def task_4(): 
    #Return a list of the 5 most common professions *in order of prevalence* (so, the most common is first).
    top_5_profession = df_bellevue['profession'].value_counts().head(5).index.tolist()
    return top_5_profession




