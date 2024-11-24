import pandas as pd

def max_common(df_a, df_b): 
    common_columns = df_a.columns.intersection(df_b.columns)
    
    if not common_columns.size: 
        return df_a.copy()

    result_df = df_a.copy() 

    for col in common_columns:
        result_df[col] = df_a[col].combine(df_b[col], max) 

    return result_df