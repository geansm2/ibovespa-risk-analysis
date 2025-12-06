"""
Debug script to check why metrics are returning NaN
"""

import sys
import os
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from analysis.risk_metrics import IbovespaRiskAnalyzer
import pandas as pd

print("=" * 80)
print("DEBUGGING METRICS")
print("=" * 80)

# Download data
tickers = ['PETR4.SA', 'VALE3.SA']
analyzer = IbovespaRiskAnalyzer(tickers)
data = analyzer.download_data()

print(f"\nData shape: {data.shape}")
print(f"Data columns: {list(data.columns)}")

# Calculate metrics with smaller window
print("\n\nTesting with window=21 (3 weeks)...")
metrics = analyzer.calculate_all_metrics(window=21)

print("\nSharpe Ratio shape:", metrics['sharpe'].shape)
print("\nFirst 5 Sharpe values:")
print(metrics['sharpe'].head())

print("\nLast 5 Sharpe values:")
print(metrics['sharpe'].tail())

print("\nCount of non-NaN values per column:")
print(metrics['sharpe'].count())

# Try to get latest
summary = analyzer.get_latest_metrics()
print("\nLatest metrics summary:")
print(summary)

print("\n" + "=" * 80)