import pandas as pd


def calculate_sma(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window).mean()


def calculate_ema(series: pd.Series, span: int) -> pd.Series:
    return series.ewm(span=span, adjust=False).mean()


def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    result_dfs = []
    
    for ticker in df['ticker'].unique():
        ticker_df = df[df['ticker'] == ticker].copy()
        ticker_df = ticker_df.sort_values('date')
        
        ticker_df['SMA_10'] = calculate_sma(ticker_df['close'], 10)
        ticker_df['SMA_20'] = calculate_sma(ticker_df['close'], 20)
        
        ticker_df['EMA_10'] = calculate_ema(ticker_df['close'], 10)
        ticker_df['EMA_20'] = calculate_ema(ticker_df['close'], 20)
        
        result_dfs.append(ticker_df)
    
    return pd.concat(result_dfs, ignore_index=True)
