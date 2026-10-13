### Intuition
we have given one dataframe which contains a column salary which contains the duplicates and we have to find the second largest value in that if
dataframe is empty or their is no second largest value then we have to return None

### Approach
 **Brute Force :**
 - I used .drop_duplicates() function of pandas which removes the duplicates present in the series or the dataframe.
 - We only have to check second largest if len(df) >= 2 otherwise we have to return None
 - if len(df) >= 2 then i sorted the dataframe based on salaries column in descending order then i stored the second largest value by iloc[1].
 - and then created a dataframe to return  

 **Time Complexity :** O(nlogn) because we are sorting the entire dataframe and creating the copy of the new dataframe.  
 **Space Complexity :** O(n) 

 **Optimal Approach :**
 - 
 
