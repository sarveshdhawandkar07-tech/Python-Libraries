Pandas has two main Data Structures Series and Dataframe :  
**Series** :  
- A series is a one-dimensional labeled array.  
labeled array --> normal arrays gives hidden indexes 0,1,2..
                  but labeled array can give indexes as per your choice.
for ex.,
```python
sales = pd.Series([150, 200, 350])
print(sales)
# Output
# 0  150
# 1  200
# 2  350
# dtype: int64
# The labels here are just 0, 1, 2.
```
```python
sales = pd.Series([150, 200, 350], index=['Store_A', 'Store_B', 'Store_C'])
print(sales)
# Output
# Store_A    150
# Store_B    200
# Store_C    350
# dtype: int64
# Now you can access the values and also modify the values by your labeled indexes.
```
- Pandas Series prefers to hold only one uniform data type for the entire column. This consistency allows Python to run mathematical
  operations incredibly fast.   
- If you mix different data types in a single Series (like a number and a word), Pandas will automatically default the entire Series to the
  object data type. This slows down performance and prevents math operations.
- Traditionally, if an integer Series has a missing value (NaN), Pandas automatically converts the whole Series into a float64 to accommodate
  the blank space.
- In series, if you have to add the two labelled arrays, basically in normal arrays the addition performed with corresponding elements
  first with first and second with second.
  But, in labeled arrays it automatically corresponds with the value of the same label even if they are in unordered form.

**DataFrames** :  
- A DataFrame is a two dimensional labelled data structure  
- It is a table made of rows and columns where both the rows and the columns have labels. 
Think of a DataFrame as a collection of multiple Series objects glued together, sharing the exact same row labels (index).  
         - Series (1D): A single column of data with row labels.  
         - DataFrame (2D): A grid of data with both Row Labels (Index) and Column Labels (Headers).
- Unlike series, a dataframe is a heterogeneous it can contain the columns of differenet data types  
  
COMMON DATAFRAME COMPONENTS :
1. df.values  
   What it does: Strips away all row and column labels, leaving only the raw data.  
   How to use it: Use it when you need to pass your data
   into machine learning libraries (like NumPy or Scikit-Learn) that don't use Pandas labels.  
   The Output: It returns a NumPy ndarray (a multi-dimensional array of pure data).  
3. df.index
4. df.columns  
HOW TO USE THEM AND WHAT TYPE OF OUTPUT THEY GIVE ??
```python
import pandas as pd
data = {'Price': [1.50, 2.99], 'Stock':[100,45]}
df = pd.DataFrame(data, index=['Apple', 'Banana'])
```
```python
print(df.index)
# Output: Index(['Apple', 'Banana'], dtype='object')
```
```python
print(df.columns)
# Output: Index(['Price', 'Stock'], dtype='object')
```
```python
print(df.values)
# Output: 
# [[  1.5  100.  ]
#  [  2.99  45.  ]]
# Note: Because NumPy arrays must hold one uniform type, 
# it automatically converted the integers to floats so they could sit next to each other!
```
