"""
Debug script to check SquareQuant output format
"""

import squarequant as sq
import pandas as pd

# Create simple test data
dates = pd.date_range('2024-01-01', periods=100)
data = pd.DataFrame({
    'PETR4.SA_Close': [10 + i*0.1 for i in range(100)],
    'VALE3.SA_Close': [50 + i*0.2 for i in range(100)]
}, index=dates)

print("Input data columns:", list(data.columns))
print("\nInput data shape:", data.shape)
print("\nFirst 3 rows:")
print(data.head(3))

# Test Sharpe calculation
assets = ['PETR4.SA', 'VALE3.SA']
print(f"\nAssets: {assets}")

sharpe = sq.sharpe(data=data, assets=assets, use_returns=False, window=21)

print("\nSharpe output columns:", list(sharpe.columns))
print("\nSharpe shape:", sharpe.shape)
print("\nLast 5 Sharpe values:")
print(sharpe.tail())
print("\nNon-NaN count:")
print(sharpe.count())
