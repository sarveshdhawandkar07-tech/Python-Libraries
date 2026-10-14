# Brute Force
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores.sort_values('score',ascending=False)
    sorted_scores['rank'] = 1
    count = 1
    for i in range(1,len(sorted_scores['score'])):
        if sorted_scores['score'].iloc[i-1] == sorted_scores['score'].iloc[i]:
            sorted_scores['rank'].iloc[i] = count
        else:
            count += 1
            sorted_scores['rank'].iloc[i] = count
    
    return sorted_scores[['score','rank']]

# Optimal 
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_scores = scores.sort_values('score',ascending=False)
    
    sorted_scores['rank'] = sorted_scores['score'].rank(method='dense',ascending=False).astype(int)

    return sorted_scores[['score','rank']]

    
