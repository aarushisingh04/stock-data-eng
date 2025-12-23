import pandas as pd
from pathlib import Path


def write_output_files(df: pd.DataFrame, output_dir: str) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    output_columns = [
        'date', 'open', 'high', 'low', 'close', 
        'volume', 'SMA_10', 'SMA_20', 'EMA_10', 'EMA_20'
    ]
    
    for ticker in df['ticker'].unique():
        ticker_df = df[df['ticker'] == ticker].copy()
        ticker_df = ticker_df.sort_values('date')
        
        output_df = ticker_df[output_columns].copy()
        output_df['date'] = output_df['date'].dt.strftime('%Y-%m-%d')
        filename = output_path / f"result_{ticker}.csv"
        output_df.to_csv(filename, index=False)
        
        print(f"Written {len(output_df)} rows to {filename}")
