# Brute Force
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(df) >= 2:
        return pd.DataFrame([df.iloc[1]],columns=['SecondHighestSalary'])
    return pd.DataFrame([None],columns=['SecondHighestSalary'])

# Optimal

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    if len(unique_salaries) >= 2:
        second_largest = unique_salaries.nlargest(2).iloc[1]
        return pd.DataFrame([second_largest],columns=['SecondHighestSalary'])
    return pd.DataFrame([None],columns=['SecondHighestSalary'])

    
