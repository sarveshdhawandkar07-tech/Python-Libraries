### Intuition 
- we have to rank the scores. Same scores should have same ranking and return score and rank columns.

### Approach

**Brute Approach :**  
- first sort the list
- create a rank column with default value 1
- intialize a count variable with 1
- start from 1'st index
- check is the current value at index i equals to the previous value at index i-1 using .iloc we can access the values
- if above condition is True change the rank of that score equals to current count value
- if condition fails increment count and assign the count at that position
- at last return the score and rank table of the scores dataframe.
**Time Complexity :** O(nlogn)  
**Space Complexity :** O(n)   

**Optimal Approach :**
- Using .rank() built-in function we don't need the for loop it automatically ranks the scores
**.rank() :**
  ```python
  s.rank(
    axis=0,
    method='average',
    numeric_only=False,
    na_option='keep',
    ascending=True,
    pct=False)
  ```

- method :
    1. Average : Tied values get the average of the ranks
       for ex., if you have 3 tied values at position 4,5 and 6 then each value gets the (4+5+6)/3 rank
    2. min : If values tied rank will be equal to the lowest position and the next values will skip.
        for ex., Two people occupy 2nd place, so the next person is 4th, because three people finished ahead of or tied with the 2nd-place
       group before them. This is the same as an Olympic result: two silver medals, and the next athlete gets the bronze-position number
       4th, not 3rd.
    3. max : tied values all take the worst (largest-numbered) place in their group, so there’s no gap after the tie, and the group’s
        rank is the highest position it occupies.
    4. first : gets unique rank for each value
    5. dense : gets the same value for duplicates without skipping any number.
- numeric_only :(False by default) 
   1. Your DataFrame has a mix of text and number columns and you only care about ranking the numbers you have to use **numeric_only = True**
   2. You want to avoid accidental alphabetical ranking of text columns like names or cities
  ```python
  numeric_only = True
  ```
- na_option :
    default (keep): keep NaN as it is  
    top : NaNs get the smallest ranks  
    bottom : NaNs get the largest ranks
- pct : pct=True converts each rank into a fraction between 0 and 1 (rank ÷ number of values), so instead of “3rd place” you get “0.6”,
        meaning that value is at or above about 60% of the data.
we get the rank in float values to convert it in integer we have to use *.astype()* function.
**Time Complexity :** O(nlogn)  
**Space Complexity :** O(n)  
