- Pandas has three main tools for combining Dataframes :
    - .merge() --> SQL-style-joins
    - .join() --> index-based-joins
    - .concat() --> stacking
  
```python
import pandas as pd

students = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Amit', 'Riya', 'Sara', 'John']
})

marks = pd.DataFrame({
    'id': [2, 3, 5, 6],
    'score': [88, 92, 75, 60]
})
```

**.merge() Syntax :**  
  
```python
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, suffixes=('_x', '_y'),
         indicator=False, validate=None)
```
  
- how --> Type of join : inner, left, right, outer, cross
    - inner (default) : Keeps only rows whose key exists in both DataFrames.  
         for ex.,
         ```python
         pd.merge(students, marks, on='id', how='inner')
         ```
         ```
            id  name  score
         0   2  Riya     88
         1   3  Sara     92
         ```
    - Left join : Keeps all rows from the left DataFrame. Unmatched right-side values become NaN.  
         for ex.,
         ```python
         pd.merge(students, marks, on='id', how='left')
         ```
         ```
            id  name  score
         0   1  Amit    NaN
         1   2  Riya   88.0
         2   3  Sara   92.0
         3   4  John    NaN
         ```
    - Right join : Keeps all rows from the right DataFrame. Unmatched left-side values become NaN.  
         for ex.,
         ```python
         pd.merge(students, marks, on='id', how='right')
         ```
         ```
            id  name  score
         0   2  Riya     88
         1   3  Sara     92
         2   5   NaN     75
         3   6   NaN     60
         ```
    - Outer (full) join : Keeps all rows from both DataFrames, filling NaN where there’s no match.  
        for ex.,
        ```python
        pd.merge(students, marks, on='id', how='outer')
        ```
        ```
           id  name  score
        0   1  Amit    NaN
        1   2  Riya   88.0
        2   3  Sara   92.0
        3   4  John    NaN
        4   5   NaN   75.0
        5   6   NaN   60.0
        ```
  - Cross join : Every row of the left is paired with every row of the right (Cartesian product). No key is needed.
        for ex.,
      ```python
      pd.merge(students, marks, how='cross')   # 4 x 4 = 16 rows
      ```
       Overlapping column names get the _x and _y suffixes. for ex., col_name_x and col_name_y  
       these are default suffixes we can change it by using parameter suffixes=('','')  
- If you have to join two dataframes based on two different column names like left dataframe have different column name and right dataframe have
  different column name then you have to use parameters left_on and right_on,
  
  ```python
  pd.merge(students, marks, left_on='id', right_on='student_id')
  ```
  
- If we have to join based on multiple keys

```python
pd.merge(df1, df2, on=['dept', 'year'], how='inner')
```

- Joining based on index in pandas
  **Sample Data**
  ```python
  import pandas as pd

  students = pd.DataFrame({
    'name': ['Amit', 'Riya', 'Sara', 'John']
    }, index=[1, 2, 3, 4])
  students.index.name = 'id'

    marks = pd.DataFrame({
    'score': [88, 92, 75]
    }, index=[2, 3, 5])
  marks.index.name = 'id'
    ```
```
    students           marks
         name               score
    id                  id
    1    Amit           2      88
    2    Riya           3      92
    3    Sara           5      75
    4    John
```
Both indexes are the keys    
```python
pd.merge(students, marks, left_index=True, right_index=True)
```

```
    name  score
id              
2   Riya     88
3   Sara     92
```
left_index=True means use the left DataFrame’s index as the key.  
right_index=True means use the right DataFrame’s index as the key.  
The default is how='inner', so only labels present in both indexes survive.  
The result keeps the index.  
we can change join type using how parameter.    
    
**We can also do df1.merge(df2, all_other_parametres) instead of pd.merge(df1,df2)**     
  
**.concat() method :**  
```python
pd.concat([df1, df2], axis=0)                  # stack rows (union)
pd.concat([df1, df2], axis=1)                  # side by side, aligned on index
pd.concat([df1, df2], axis=1, join='inner')    # only matching index labels
pd.concat([df1, df2], ignore_index=True)       # reset the index
```
  


    
        
