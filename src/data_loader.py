import pandas as pd
from pathlib import Path


def load_stock_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)   
    df['date'] = pd.to_datetime(df['date'])
    
    # this is sorted by ticker and date for ordered time series processing
    df = df.sort_values(['ticker', 'date']).reset_index(drop=True)  
    return df
