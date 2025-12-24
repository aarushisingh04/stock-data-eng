# FamApp (YC19) - Stock Data Engineering

I shall be showcasing the approach/results for the problem statement I worked on which was presented by Fam. Please reach out to me at aarushisingh04@gmail.com for any questions or clarifications regarding the same!

### Provided Problem Statement

Dataset: A 2-year historical dataset containing daily stock prices for 10 unique symbols (ticker) in a single CSV file. The dataset is located at **data/stock_data.csv**.

Tasks: 
- **Task 1**: Resample the data from daily to monthly frequency.
- **Task 2**: Calculate specific Aggregates and Technical Indicators (Simple and Exponential Moving Averages SMA 10, SMA 20 and EMA 10 & EMA 20). 
- **Task 3**: Partition the results into individual files per stock symbol.

## Project Structure

```
├── main.py              # Pipeline entry point
├── src/
│   ├── data_loader.py   # CSV loading and parsing
│   ├── aggregator.py    # Monthly OHLC aggregation
│   ├── indicators.py    # SMA/EMA calculations
│   └── file_writer.py   # Output file generation
├── data/
│   └── stock_data.csv   # Input (Dataset with 2 years of daily stock data)
└── output/
    └── result_*.csv     # Output (10 monthly summary files for each ticker)
```

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

For each of the 10 tickers, the output files will be generated in `output/result_{SYMBOL}.csv`.

## Features

- **Monthly OHLC Aggregation**: Converts daily data to monthly Open, High, Low, Close
- **Technical Indicators**: Calculates SMA_10, SMA_20, EMA_10, EMA_20 on monthly close prices
- **Partitioned Output**: Generates 10 separate CSV files (one per ticker)

## Assumptions

Below, I shall be mentioning the practical assumptions I have made while solving the problem:

1. **Date Range**: Dataset covers exactly 24 months (June 2018 - May 2020)
2. **Open Price**: First trading day's opening price of each month
3. **Close Price**: Last trading day's closing price of each month
4. **EMA Initialization**: First EMA value is seeded with SMA (standard approach)
5. **NaN Values**: First 9 rows lack SMA_10, first 19 rows lack SMA_20 (insufficient data)
6. **Month-End Frequency**: Using pandas `'ME'` for month-end resampling
7. **Vectorized Operations**: All calculations use pandas built-in functions (no external TA libraries)

## Output Schema

Each `result_{SYMBOL}.csv` contains 24 rows with columns in the below mentioned order:
- `date`: Month-end date
- `open`: First trading day's open price
- `high`: Maximum high during the month
- `low`: Minimum low during the month
- `close`: Last trading day's close price
- `volume`: Total monthly volume
- `SMA_10`: 10-period Simple Moving Average
- `SMA_20`: 20-period Simple Moving Average
- `EMA_10`: 10-period Exponential Moving Average
- `EMA_20`: 20-period Exponential Moving Average

## Formulas Used for Calculation

**SMA Formula**: `Sum of closing prices (over 'N' periods)/Number of periods (N).`

**EMA Formula**: 
- Multiplier = `2/(Number of Periods + 1)`
- EMA = `(Current Price - Previous Day's EMA) * Multiplier + Previous Day's EMA`
        (For the first EMA, you often use the SMA as the "Previous Day's EMA")
