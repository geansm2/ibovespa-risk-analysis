"""
Test script to verify project functionality and display results
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
from analysis.portfolio_analysis import PortfolioAnalyzer
import pandas as pd

print("=" * 80)
print("🧪 TESTING IBOVESPA RISK ANALYSIS PROJECT")
print("=" * 80)

# Test 1: Data Download
print("\n📊 Test 1: Data Download")
print("-" * 80)
tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA']
analyzer = IbovespaRiskAnalyzer(tickers)
data = analyzer.download_data()

print(f"\n✅ Data shape: {data.shape}")
print(f"✅ Columns: {list(data.columns)}")
print(f"\n📈 First 3 rows:")
print(data.head(3))
print(f"\n📈 Last 3 rows:")
print(data.tail(3))

# Test 2: Basic Statistics
print("\n\n📊 Test 2: Basic Statistics")
print("-" * 80)
returns = data.pct_change().dropna()
print("\n📈 Daily Returns Statistics:")
print(returns.describe())

print("\n📈 Correlation Matrix:")
print(returns.corr().round(3))

# Test 3: Risk Metrics (with smaller window for testing)
print("\n\n📊 Test 3: Risk Metrics Calculation")
print("-" * 80)
print("Using 21-day window for faster calculation...")

metrics = analyzer.calculate_all_metrics(window=21)

# Get last 5 values for each metric
print("\n📈 Last 5 Sharpe Ratio values:")
print(metrics['sharpe'].tail())

print("\n📈 Last 5 Volatility values:")
print(metrics['volatility'].tail())

# Test 4: Portfolio Analysis
print("\n\n📊 Test 4: Portfolio Analysis")
print("-" * 80)

weights = {
    'PETR4': 0.30,
    'VALE3': 0.30,
    'ITUB4': 0.20,
    'BBDC4': 0.10,
    'ABEV3': 0.10
}

portfolio = PortfolioAnalyzer(data, weights)
stats = portfolio.get_portfolio_statistics()

print("\n📈 Portfolio Statistics:")
for key, value in stats.items():
    print(f"  {key:.<30} {value:.4f}")

# Test 5: File Generation
print("\n\n📊 Test 5: Generated Files")
print("-" * 80)

results_dir = 'results'
if os.path.exists(results_dir):
    files = os.listdir(results_dir)
    print(f"\n✅ Found {len(files)} files in results/:")
    for f in sorted(files):
        size = os.path.getsize(os.path.join(results_dir, f))
        size_kb = size / 1024
        print(f"  • {f:<40} {size_kb:>8.1f} KB")
else:
    print("❌ Results directory not found")

# Test 6: Open visualizations
print("\n\n📊 Test 6: Opening Visualizations")
print("-" * 80)
print("\nOpening dashboard in default image viewer...")

dashboard_path = os.path.join(results_dir, '06_complete_dashboard.png')
if os.path.exists(dashboard_path):
    os.startfile(dashboard_path)
    print(f"✅ Opened: {dashboard_path}")
else:
    print("❌ Dashboard not found")

print("\n" + "=" * 80)
print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 80)
print("\n💡 Next steps:")
print("  1. Review the opened dashboard image")
print("  2. Check other PNG files in results/ folder")
print("  3. Review CSV files for data export")
print("  4. Try the Jupyter notebook: jupyter notebook notebooks/01_complete_analysis.ipynb")
print("\n" + "=" * 80)
