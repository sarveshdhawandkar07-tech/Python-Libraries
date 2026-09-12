- Filtering allows us to get the specific rows which statisfies the given condition.  
- by using df[] we can filter out the rows by applying the conditions on the columns.  

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 22],
    'city': ['NY', 'LA', 'SF', 'NY', 'LA'],
    'salary': [50000, 60000, 75000, 90000, 45000]
})
```
  
**Normal Filtering** :  
```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 22],
    'city': ['NY', 'LA', 'SF', 'NY', 'LA'],
    'salary': [50000, 60000, 75000, 90000, 45000]
})
```
- Under the hood: df['age'] > 28 produces a boolean Series, and df[]/.loc[] uses that mask to keep only True rows.  
  
**Filtering with multiple conditions** :  
```python
df[(df['age'] > 25) & (df['city'] == 'NY')]     # AND
df[(df['age'] > 25) | (df['salary'] > 80000)]    # OR
df[~(df['city'] == 'NY')]                          # NOT
```
  
**.isin()** :
- Match against a list of values  
```python
df[df['city'].isin(['NY', 'SF'])]        # rows where city is NY or SF
df[~df['city'].isin(['NY', 'SF'])]        # rows where city is NOT NY or SF
```
  
**between** :  
- Range Filtering  
```python
df[df['age'].between(25, 35)]     # inclusive on both ends by default
df[df['age'].between(25, 35, inclusive='left')]   # 25 <= age < 35
```
  
**.query()** :  
- SQL like string syntax  
```python
df.query('age > 28')
df.query('age > 25 and city == "NY"')
df.query('city in ["NY", "SF"]')

x = 30
df.query('age > @x')     # reference external variables with @
```
- Here we don't have to use brackets for each condition we write the query like a sentence in quotes.  
  
**String Based Filtering** :  
```python
df[df['name'].str.contains('a', case=False)]     # names containing 'a'
df[df['name'].str.startswith('A')]
df[df['name'].str.endswith('e')]
df[df['name'].str.len() > 4]
```
  
**Filtering out missing values** :  
```python
df[df['age'].notna()]      # keep rows where age is NOT null
df[df['age'].isna()]        # keep rows where age IS null
df.dropna(subset=['age'])   # same effect as notna(), drops those rows
```
  
**Filtering columns** :  
```python
df.filter(items=['name', 'age'])              # keep specific columns
df.filter(like='a')                            # columns containing 'a' in name
df.filter(regex='^c')                          # columns matching regex
```
  
**Sorting :**  

**.sort_values()** :  
```python
df.sort_values('age')                     # ascending by default
df.sort_values('age', ascending=False)     # descending
df.sort_values(['city', 'age'])            # sort by city first, then age within each city
df.sort_values(['city', 'age'], ascending=[True, False])   # different order per column
# Sort by column 1 first → whenever column 1 has ties (same value), break the tie using column 2 → if column 2 also ties, use column 3, and so on.
```
- Writing "by=" is optional positionally.  

**sort_index()** :  
```python
df.sort_index()                # sort rows by index label
df.sort_index(ascending=False)  # descending index
df.sort_index(axis=1)           # sort COLUMNS alphabetically
```
  
**Handling missing values while sorting** :  
```python
df.sort_values('age', na_position='first')   # NaNs at top
df.sort_values('age', na_position='last')     # NaNs at bottom (default)
```
  
**nlargest() / nsmallest() — top-N shortcuts** :  
```python
df.nlargest(3, 'salary')      # top 3 rows by salary — faster than sort_values().head(3)
df.nsmallest(2, 'age')          # bottom 2 rows by age
```
  
**In-place sorting** :  
```python 
df = df.sort_values('age')
```

**Filtering + Sorting together** :  
```python
(df[df['age'] > 25]
   .sort_values('salary', ascending=False)
   .head(3))
```


**.value_counts() :**  
- Counts how many times each unique value appears in a Series (or column), sorted by frequency (highest first, by default).  
- Returns a Series: the unique values become the index, and the counts become the values — already sorted descending by count.  
```python
s.value_counts(
    normalize=False,
    sort=True,
    ascending=False,
    bins=None,
    dropna=True
)
```
normalize --> Gives proportions instead of raw counts  
sort --> if we did False it gives the order as per as the dataframe.  
ascending --> here default is descending  
dropna --> drops the missing values(by default)  

```python
df['city'].unique()        # array(['NY', 'LA', 'SF'], dtype=object)
df['city'].nunique()         # 3
df['city'].value_counts()    # NY:3, LA:2, SF:1
```

**Getting just the top value** :  
```python
df['city'].value_counts().index[0]     # most frequent value
df['city'].value_counts().idxmax()      # same result, more idiomatic
```
  
