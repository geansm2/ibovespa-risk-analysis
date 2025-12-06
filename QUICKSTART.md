# Ibovespa Risk Analysis - Quick Start Guide

## 🚀 Quick Start (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Analysis
```bash
python main.py
```

### 3. View Results
Check the `results/` folder for:
- CSV files with metrics
- PNG charts and visualizations

## 📊 What You'll Get

The analysis will generate:

1. **Risk Metrics Summary** (`risk_metrics_summary.csv`)
   - Sharpe Ratio
   - Sortino Ratio
   - Volatility
   - Maximum Drawdown
   - VaR & CVaR
   - And more...

2. **Portfolio Comparison** (`portfolio_comparison.csv`)
   - Equal Weight strategy
   - Conservative strategy
   - Aggressive strategy
   - Defensive strategy

3. **Visualizations**
   - Price history chart
   - Returns distribution
   - Risk metrics comparison
   - Heatmap
   - Sharpe vs Sortino scatter
   - Complete dashboard

## 🎯 Customization

### Analyze Different Stocks

Edit `main.py` and change the tickers:

```python
tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA']  # Your stocks here
```

### Change Time Period

```python
analyzer = IbovespaRiskAnalyzer(
    tickers=tickers,
    start_date='2020-01-01',
    end_date='2024-12-31'
)
```

### Custom Portfolio Weights

```python
from src.analysis.portfolio_analysis import PortfolioAnalyzer

weights = {
    'PETR4': 0.40,
    'VALE3': 0.30,
    'ITUB4': 0.30
}

portfolio = PortfolioAnalyzer(data, weights)
stats = portfolio.get_portfolio_statistics()
```

## 📓 Interactive Analysis

For interactive analysis, use the Jupyter notebook:

```bash
jupyter notebook notebooks/01_complete_analysis.ipynb
```

## 🆘 Troubleshooting

### Issue: Module not found
**Solution**: Make sure you're in the project directory and installed dependencies:
```bash
cd ibovespa-risk-analysis
pip install -r requirements.txt
```

### Issue: Data download fails
**Solution**: Check your internet connection. Yahoo Finance requires internet access.

### Issue: Charts not displaying
**Solution**: If running in a script, charts are saved to `results/`. If in Jupyter, add `%matplotlib inline`.

## 📚 Learn More

- Full documentation: [README.md](README.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)
- SquareQuant docs: https://github.com/SquareQuant/squarequant-package

## 💡 Tips

1. **First run takes longer** - Data needs to be downloaded
2. **Use virtual environment** - Keeps dependencies isolated
3. **Check results folder** - All outputs are saved there
4. **Explore notebooks** - Interactive analysis is more flexible

---

**Need help?** Open an issue on GitHub!
