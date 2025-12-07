
import pandas as pd
import numpy as np
from datetime import datetime

def load_di_data(filepath='data/DI_PRE_OVER_5y.xls'):
    """
    Load DI PRE OVER data from the specific tab-delimited file.
    
    The file has a specific format:
    - 38 lines of metadata header to skip
    - Tab delimited
    - Decimal separator is comma
    - Date format is DD/MM/YYYY
    - Relevant columns: 'Data' and 'Fator Diário'
    
    Args:
        filepath (str): Path to the xls/txt file
        
    Returns:
        pd.DataFrame: DataFrame with 'date' index and 'di_daily_rate', 'di_annual_rate' columns
    """
    try:
        # Read data skipping metadata rows
        # The file is actually tab-delimited text despite .xls extension
        df = pd.read_csv(
            filepath, 
            sep='\t', 
            skiprows=38, 
            encoding='latin1', # Usually latin1 for Brazilian financial files
            decimal=','        # Handle comma as decimal separator
        )
        
        # Rename columns for clarity (handling potential encoding issues in column names)
        # We look for columns that contain specific substrings
        col_map = {}
        for col in df.columns:
            if 'Data' in col:
                col_map[col] = 'date'
            elif 'Fator' in col and 'Di' in col:
                col_map[col] = 'daily_factor'
            elif 'Taxa' in col and 'SELIC' in col:
                col_map[col] = 'selic_annual'
                
        df = df.rename(columns=col_map)
        
        # Keep only relevant columns and drop rows with missing date/data
        cols_to_keep = ['date', 'daily_factor', 'selic_annual']
        # Filter only existing columns
        cols_to_keep = [c for c in cols_to_keep if c in df.columns]
        df = df[cols_to_keep].dropna()
        
        # Convert date column
        # Try/except block to handle different date formats if necessary
        try:
            df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        except ValueError:
             df['date'] = pd.to_datetime(df['date'])
             
        df = df.set_index('date').sort_index()
        
        # Convert daily factor to daily rate (percentage)
        # Factor is usually 1.00045... -> Rate = Factor - 1
        if 'daily_factor' in df.columns:
            # Ensure it is numeric
            if df['daily_factor'].dtype == object:
                 # If read_csv decimal param didn't catch it because of thousands separator or other issues
                 df['daily_factor'] = df['daily_factor'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)
            
            df['di_daily_rate'] = df['daily_factor'] - 1.0
            
            # Calculate annualized DI rate from daily factor for check
            # (1 + daily)^252 - 1
            df['di_annualized'] = (df['daily_factor'] ** 252) - 1.0
            
        return df
        
    except Exception as e:
        print(f"Error loading DI data: {e}")
        return None

if __name__ == "__main__":
    # Simple test
    df = load_di_data()
    if df is not None:
        print("DI Data Loaded Successfully:")
        print(df.head())
        print(f"\nShape: {df.shape}")
        print(f"Date Range: {df.index.min()} to {df.index.max()}")
        print(f"Average Annualized DI: {df['di_annualized'].mean():.4%}")
