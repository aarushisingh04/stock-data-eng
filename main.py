"""
Stock Data Engineering - Main Entry Point

This script transforms daily stock data into monthly summaries with 
technical indicators (SMA/EMA) and partitions output by ticker symbol.
"""
from pathlib import Path

from src.data_loader import load_stock_data
from src.aggregator import aggregate_to_monthly
from src.indicators import add_technical_indicators
from src.file_writer import write_output_files


def main():
    project_root = Path(__file__).parent
    input_file = project_root/"data"/"stock_data.csv"
    output_dir = project_root/"output"
    
    print("=" * 50)
    print("Stock Data Engineering Pipeline")
    print("=" * 50)
    
    print("\n[1/4] Loading stock data...")
    daily_data = load_stock_data(input_file)
    print(f"      Loaded {len(daily_data)} daily records for {daily_data['ticker'].nunique()} tickers")
    
    # this particular step is for the purpose of monthly OHLC aggregation
    print("\n[2/4] Aggregating to monthly OHLC : ")
    monthly_data = aggregate_to_monthly(daily_data)
    print(f"      Generated {len(monthly_data)} monthly records")
    
    # and this step is for the purpose of adding technical indicators
    print("\n[3/4] Calculating technical indicators (SMA/EMA) :")
    monthly_with_indicators = add_technical_indicators(monthly_data)
    print("      Added SMA_10, SMA_20, EMA_10, EMA_20")
    
    # finally we write the output files
    print("\n[4/4] Writing output files : ")
    write_output_files(monthly_with_indicators, output_dir)
    
    print("\n" + "=" * 50)
    print("Pipeline completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
