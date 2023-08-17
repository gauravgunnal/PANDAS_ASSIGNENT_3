'''Q1'''
import pandas as pd

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]
df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})
print(df)
# Print the data in the second row
second_row = df.iloc[1]
print(second_row)

'''Q2'''
'''In Pandas, the `loc` and `iloc` functions are used for indexing and selecting data from a DataFrame, and they differ in how they handle indexing methods:

1. **`loc`**:
   - `loc` is label-based indexing, meaning you use labels (row and column names) to select data.
   - You provide row labels and column labels to extract data from the DataFrame.
   - Labels can be strings, integers, or slices.
   - Slicing using `loc` includes the last element of the slice.
   - Example: `df.loc[2:4, 'duration']` selects rows with labels 2, 3, and 4, from the 'duration' column.

2. **`iloc`**:
   - `iloc` is integer-based indexing, meaning you use integer indices to select data.
   - You provide integer row indices and column indices to extract data from the DataFrame.
   - Indices are zero-based, similar to Python indexing.
   - Slicing using `iloc` excludes the last element of the slice, following standard Python behavior.
   - Example: `df.iloc[2:4, 1]` selects rows at positions 2 and 3 (exclusive), from the second column ('duration').

Here's a summary of the differences between `loc` and `iloc` for Pandas DataFrames:

- `loc` uses labels (strings or integers) for both rows and columns.
- `iloc` uses integer indices for both rows and columns.
- `loc` is inclusive of the end point when using slicing.
- `iloc` is exclusive of the end point when using slicing.

In your provided example, if you want to access the second row using `loc`, you would do:

```python
df.loc[1]
```

And using `iloc`, you would do:

```python
df.iloc[1]
```

Both of these will retrieve the data in the second row of the DataFrame.'''

'''Q3'''

#Sure, let's address your questions step by step:

#Reindexing and Accessing DataFrame Elements:

python
Copy code
import pandas as pd
course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]
df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})
reindex = [3, 0, 1, 2]
new_df = df.reindex(reindex)
#Now, let's find the output for both new_df.loc[2] and new_df.iloc[2]:

#python
print(new_df.loc[2])
print(new_df.iloc[2])
'''Q4'''
import pandas as pd

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]
df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})

# (i) Mean of each and every column
mean_values = df.mean()
print("Mean of each column:\n", mean_values)

# (ii) Standard deviation of column 'duration'
std_deviation_column_2 = df['duration'].std()
print("Standard deviation of column 'duration':", std_deviation_column_2)
'''Q5'''
import pandas as pd

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]
df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})

# Replace the data in the second row of 'duration' column with a string
df.loc[1, 'duration'] = 'String Data'

# Calculate the mean of the 'duration' column (Note: This will raise an error)
try:
    mean_duration = df['duration'].mean()
    print("Mean of 'duration' column:", mean_duration)
except Exception as e:
    print("Error:", e)

'''Q6'''
'''In Pandas, a "window function" (also known as "rolling" or "moving" function) is a type of operation that is applied to a moving window of data points within a specified range. It is often used for time series data or any data that has an ordered sequence. Window functions are useful for calculating rolling statistics, such as moving averages, rolling sums, and other aggregations, to gain insights into trends and patterns in the data.

The general syntax for applying a window function is:

```python
result = df['column'].rolling(window=window_size).function()
```

Here, `window_size` specifies the size of the window, and `function()` is the specific window function you want to apply.

Here are some commonly used window functions in Pandas:

1. **`rolling().mean()`**: Calculates the rolling mean (moving average) of a column.

2. **`rolling().sum()`**: Calculates the rolling sum of a column.

3. **`rolling().min()`**: Calculates the rolling minimum of a column.

4. **`rolling().max()`**: Calculates the rolling maximum of a column.

5. **`rolling().std()`**: Calculates the rolling standard deviation of a column.

6. **`rolling().var()`**: Calculates the rolling variance of a column.

7. **`rolling().apply()`**: Applies a custom function to the rolling window.

8. **`rolling().corr()`**: Calculates the rolling correlation between two columns.

9. **`expanding().sum()`**: Calculates the expanding sum of a column (cumulative sum).

10. **`expanding().mean()`**: Calculates the expanding mean of a column (cumulative mean).

11. **`expanding().min()`**: Calculates the expanding minimum of a column (cumulative minimum).

12. **`expanding().max()`**: Calculates the expanding maximum of a column (cumulative maximum).

13. **`expanding().std()`**: Calculates the expanding standard deviation of a column (cumulative standard deviation).

14. **`expanding().var()`**: Calculates the expanding variance of a column (cumulative variance).

These window functions allow you to compute aggregated statistics within a moving or expanding window of data points. They are particularly useful for time-based data analysis and feature engineering.'''

'''Q7'''
import pandas as pd

# Get the current date and time
current_datetime = pd.Timestamp.now()

# Extract the current month and year
current_month = current_datetime.month
current_year = current_datetime.year

print("Current Month:", current_month)
print("Current Year:", current_year)

'''Q8'''
import pandas as pd

# Input dates from the user
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert input strings to Pandas Timestamp objects
try:
    timestamp1 = pd.Timestamp(date1)
    timestamp2 = pd.Timestamp(date2)
except ValueError:
    print("Invalid date format. Please use the format YYYY-MM-DD.")
    exit()

# Calculate the time difference
time_difference = timestamp2 - timestamp1

# Extract days, hours, and minutes from the time difference
days = time_difference.days
hours, remainder = divmod(time_difference.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Display the result
print(f"Difference between {date1} and {date2}:")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")


'''Q9'''
import pandas as pd

# Prompt the user to enter the file path of the CSV file
file_path = input("Enter the file path of the CSV file: ")

# Read the CSV file into a Pandas DataFrame
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    exit()

# Prompt the user to enter the column name to convert
column_name = input("Enter the name of the column to convert to categorical: ")

# Prompt the user to enter the desired category order
category_order = input("Enter the desired category order (comma-separated): ")
categories = [cat.strip() for cat in category_order.split(',')]

# Convert the specified column to a categorical data type with the specified category order
df[column_name] = pd.Categorical(df[column_name], categories=categories, ordered=True)

# Sort the DataFrame by the categorical column
sorted_df = df.sort_values(by=[column_name])

# Display the sorted data
print(sorted_df)

'''Q10'''
import pandas as pd
import matplotlib.pyplot as plt

# Input file path from the user
file_path = input("Enter the CSV file path: ")

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    exit()

# Group the data by product category and time period
grouped = df.groupby(['Category', 'Date']).sum()

# Pivot the data for stacked bar chart
pivot_df = grouped.reset_index().pivot(index='Date', columns='Category', values='Sales')

# Create a stacked bar chart
ax = pivot_df.plot(kind='bar', stacked=True, figsize=(10, 6))
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title('Stacked Bar Chart of Product Sales by Category over Time')
plt.xticks(rotation=45)
plt.legend(title='Category')

# Display the chart
plt.tight_layout()
plt.show()

'''Q11'''
import pandas as pd
from scipy import stats

# Prompt the user to enter the file path of the CSV file
file_path = input("Enter the file path of the CSV file containing student data: ")

# Read the CSV file into a Pandas DataFrame
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    exit()

# Calculate mean, median, and mode of test scores
mean_score = df['Test Score'].mean()
median_score = df['Test Score'].median()
mode_scores = stats.mode(df['Test Score'])[0]

# Display the results in a table
results = pd.DataFrame({
    'Statistic': ['Mean', 'Median', 'Mode'],
    'Value': [mean_score, median_score, ', '.join(map(str, mode_scores))]
})

print(results)
