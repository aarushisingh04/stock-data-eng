import pandas as pd


def aggregate_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    monthly_data = []
    
    for ticker in df['ticker'].unique():
        ticker_df = df[df['ticker'] == ticker].copy()
        ticker_df = ticker_df.set_index('date')
        
        monthly_agg = ticker_df.resample('ME').agg({
            'open': 'first',    
            'high': 'max',      
            'low': 'min',       
            'close': 'last',    
            'volume': 'sum'     
        })
        
        monthly_agg['ticker'] = ticker
        monthly_agg = monthly_agg.reset_index()
        monthly_data.append(monthly_agg)
    
    result = pd.concat(monthly_data, ignore_index=True)
    return result
