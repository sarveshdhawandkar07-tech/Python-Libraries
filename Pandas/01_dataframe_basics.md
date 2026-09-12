- Pandas makes it easy to read data from csv and excel files into a dataframe.


```python 
df = pd.read_csv('data.csv',index_col='Name')
``` 
- This will load a csv file and store it in a dataframe named df.
- We can make a single column as an index column by using parameter *index_col*(optional)  

```python
df = pd.read_excel('data.xlsx')
```
- This will load a excel file and store it in a dataframe named df.  
  
```python
df.head()
# returns the first n rows by which we can know the structure of the dataframe.
# default is 5.
# We can specify any value of rows it will return that much of rows.
# If value is negative it returns all rows except the last |n| rows.
# If value is larger than the total no. of rows then it will safely returns all available rows.
# Related methods --> 1. df.tail() --> gives last n rows
#                     2. df.sample() --> gives random n rows anywhere from the df. 
#                                       - It also has one frac parameter used as : df.sample(frac=0.25)
#                                       - It returns 25% of the total rows randomly.
```

```python
df.info()
# Prints a concise summary of a dataframe
# Including the index data type, column data types, non-null values, and memory usage
```

```python
df.shape
# It is an attribute 
# It returns a tuple of (rows,columns)
``` 

**Selecting Rows and Columns** :
```python
# Syntax : 
df.loc[row_label, column_label]
```
  
different variations of df.loc[]:
```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['NY', 'LA', 'SF', 'NY']
}, index=['a', 'b', 'c', 'd'])
```
  
```python
df.loc['a']                    # Row with index label 'a'
df.loc['a', 'name']            # Single value: 'Alice'
df.loc['a':'c']                # Rows a to c — INCLUSIVE of 'c'
df.loc[['a', 'c']]             # Specific rows by label list
df.loc[:, 'name']              # All rows, column 'name'
df.loc[:, ['name', 'age']]     # All rows, multiple columns
df.loc['a':'c', 'name':'age']  # Slice both rows and columns by label
df.loc[df['age'] > 28]         # Boolean condition
df.loc[df['age'] > 28, 'name'] # Condition + column selection
df.loc['e'] = ['Eve', 22, 'SF'] # Add a new row by label (works!)
df.loc['a', 'age'] = 26        # Set a value
df.loc[(df['age'] > 25) & (df['city'] == 'NY')]   # AND — use &
df.loc[(df['age'] > 25) | (df['city'] == 'NY')]   # OR — use |
```
  
Key point: when slicing with .loc, both endpoints are included ('a':'c' gives you a, b, c).  
  

```python
# Syntax :
df.iloc[row_position, column_position]
```

```python
df.iloc[0]                     # First row (position 0)
df.iloc[0, 0]                  # Value at row 0, col 0
df.iloc[0:3]                   # Rows 0,1,2 — EXCLUSIVE of 3
df.iloc[[0, 2]]                # Rows at positions 0 and 2
df.iloc[:, 0]                  # All rows, first column
df.iloc[:, 0:2]                # All rows, first two columns
df.iloc[0:2, 0:2]              # Slice both rows and columns by position
df.iloc[-1]                    # Last row
df.iloc[:, -1]                 # Last column
```
Key point: slicing with .iloc follows normal Python rules — the end index is excluded (0:3 gives you rows 0, 1, 2).  



when to use df[] and df.loc[] ??  

```python
df['col']                       # reading a column        → df[]
df[df['col'] > x]               # reading filtered rows    → df[] (read-only)
df.loc[cond, 'col'] = value     # writing/assigning         → df.loc[]
df.loc[row_label, col_label]    # row + column together     → df.loc[]
```
  
if you're just reading a column, use df[]. The moment you're filtering + selecting columns together, or assigning a value, switch to .loc[]  

  
```python
df.describe()
# It gives the quick statistical summary of the data
```
- By default it only summarizes numerical columns.  
1. count --> Number of all non-null values  
2. mean  --> Average     
3. std   --> Standard Deviation (spread of the data)  
4. min   --> Smallest Value  
5. 25%   --> 1st quartile (25th percentile)  
6. 50%   --> Median  
7. 75%   --> 3rd quartile (75th percentile)  
8. max   --> Largest Value  
  
- By this parameters we get the statistical overview of each column.  
  
To including non-numeric columns:  
```python
df.describe(include="all")
```
- Adds unique, top, freq for object/string columns (count of unique values, most frequent value, its frequency), and leaves numeric-only stats as NaN for string columns and vice versa.  
```python
df.describe(include='object')    # ONLY string/categorical columns
df.describe(include=[np.number]) # ONLY numeric columns (same as default)
df.describe(exclude=[np.number]) # everything EXCEPT numeric
```
  
- It works on Single series too  
```python
df["age"].describe()
```
  
- NaN values are excluded automatically from calculations (they don't count toward count).  
- It's usually the first thing you run after loading a new dataset — gives you a fast read on scale, spread, and whether something looks off (e.g., a max that's absurdly high signals a possible outlier or data error).  
- std being very large relative to mean signals high variability/spread in that column — worth investigating before modeling.  
- Doesn't tell you about missing values directly — pair it with df.isnull().sum() for that.  



