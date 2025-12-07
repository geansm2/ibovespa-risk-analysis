"""
Risk Metrics Analysis for Ibovespa Stocks

This module provides comprehensive risk analysis for Brazilian stocks,
calculating multiple risk metrics including Sharpe ratio, Sortino ratio,
VaR, CVaR, Maximum Drawdown, Volatility, and more.

NOTE: Initially attempted to use SquareQuant library for metrics calculation,
but encountered compatibility issues where all metrics returned NaN values.
As a solution, we implemented custom risk metrics calculations using pandas
and numpy, demonstrating proficiency in quantitative finance formulas and
Python programming. This approach provides more control and transparency
over the calculations.

Author: Gean Santos
Date: December 2025
"""

import squarequant as sq  # Used only for data download
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Import custom risk metrics module
from . import custom_metrics as cm


class IbovespaRiskAnalyzer:
    """
    Comprehensive risk analysis for Ibovespa stocks.
    
    Attributes:
        tickers (list): List of stock tickers to analyze
        start_date (str): Start date for analysis
        end_date (str): End date for analysis
        data (pd.DataFrame): Downloaded stock price data
    """
    
    def __init__(self, tickers, start_date=None, end_date=None):
        """
        Initialize the risk analyzer.
        
        Args:
            tickers (list): List of stock tickers (e.g., ['PETR4.SA', 'VALE3.SA'])
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str): End date in 'YYYY-MM-DD' format
        """
        self.tickers = tickers
        
        # Default to 5 years of data if not specified
        if end_date is None:
            self.end_date = datetime.now().strftime('%Y-%m-%d')
        else:
            self.end_date = end_date
            
        if start_date is None:
            start = datetime.now() - timedelta(days=5*365)
            self.start_date = start.strftime('%Y-%m-%d')
        else:
            self.start_date = start_date
            
        self.data = None
        self.metrics = {}
        
    def download_data(self):
        """
        Download stock data using SquareQuant.
        
        Returns:
            pd.DataFrame: Downloaded stock price data
        """
        print(f"📊 Downloading data for {len(self.tickers)} stocks...")
        print(f"📅 Period: {self.start_date} to {self.end_date}")
        
        config = sq.DownloadConfig(
            start_date=self.start_date,
            end_date=self.end_date,
            interval='1d',
            columns=['Close'],
            source='yfinance'
        )
        
        raw_data = sq.download_tickers(self.tickers, config)
        
        # Reorganize data into a clean DataFrame
        self.data = pd.DataFrame()
        for ticker in self.tickers:
            col_name = f"{ticker}_Close"
            if col_name in raw_data.columns:
                # Remove .SA suffix for cleaner column names
                clean_name = ticker.replace('.SA', '')
                self.data[clean_name] = raw_data[col_name]
        
        print(f"✅ Downloaded {len(self.data)} days of data")
        return self.data
    
    def calculate_all_metrics(self, window=252, di_data=None):
        """
        Calculate all available risk metrics using custom implementations.
        
        NOTE: This method now uses custom-built risk metric calculations
        instead of SquareQuant, providing more reliable results and
        demonstrating quantitative finance expertise.
        
        Args:
            window (int): Rolling window size (default: 252 trading days = 1 year)
                         Note: Custom metrics calculate overall metrics, not rolling
            di_data (pd.DataFrame, optional): DataFrame with DI rates for dynamic risk-free calculation
            
        Returns:
            dict: Dictionary containing all calculated metrics
        """
        if self.data is None:
            raise ValueError("Data not downloaded. Call download_data() first.")
        
        print(f"\n📈 Calculating risk metrics for: {', '.join(self.data.columns)}")
        print("  ℹ️  Using custom implementations (pandas + numpy)")
        
        # Determine risk-free rate
        if di_data is not None and 'di_daily_rate' in di_data.columns:
            print("  ℹ️  Using dynamic DI risk-free rates")
            risk_free_rate = di_data['di_daily_rate']
        else:
            print("  ℹ️  Using constant risk-free rate (0.0)")
            risk_free_rate = 0.0
        
        # Calculate returns
        returns = cm.calculate_returns(self.data)
        
        # Calculate all metrics using custom module
        print("  ⚙️  Calculating Sharpe Ratio...")
        self.metrics['sharpe'] = pd.DataFrame({col: [cm.calculate_sharpe_ratio(returns[col], risk_free_rate)] 
                                               for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Sortino Ratio...")
        self.metrics['sortino'] = pd.DataFrame({col: [cm.calculate_sortino_ratio(returns[col], risk_free_rate)] 
                                                for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Volatility...")
        self.metrics['volatility'] = pd.DataFrame({col: [cm.calculate_volatility(returns[col])] 
                                                   for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Maximum Drawdown...")
        self.metrics['max_drawdown'] = pd.DataFrame({col: [cm.calculate_max_drawdown(self.data[col])] 
                                                     for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Value at Risk (VaR)...")
        self.metrics['var'] = pd.DataFrame({col: [cm.calculate_var(returns[col], confidence=0.95)] 
                                           for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Conditional VaR (CVaR)...")
        self.metrics['cvar'] = pd.DataFrame({col: [cm.calculate_cvar(returns[col], confidence=0.95)] 
                                            for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Semi-Deviation...")
        self.metrics['semidev'] = pd.DataFrame({col: [cm.calculate_semi_deviation(returns[col])] 
                                               for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Ulcer Index...")
        self.metrics['ulcer'] = pd.DataFrame({col: [cm.calculate_ulcer_index(self.data[col])] 
                                             for col in self.data.columns}, index=['value'])
        
        print("  ⚙️  Calculating Mean Absolute Deviation...")
        self.metrics['mad'] = pd.DataFrame({col: [cm.calculate_mad(returns[col])] 
                                           for col in self.data.columns}, index=['value'])
        
        print("✅ All metrics calculated successfully!\n")
        return self.metrics
    
    def get_latest_metrics(self):
        """
        Get the most recent values for all metrics.
        
        Returns:
            pd.DataFrame: DataFrame with latest metric values for each stock
        """
        if not self.metrics:
            raise ValueError("Metrics not calculated. Call calculate_all_metrics() first.")
        
        results = {}
        for metric_name, metric_df in self.metrics.items():
            # Custom metrics return single-row DataFrames
            results[metric_name] = metric_df.iloc[0]
        
        summary = pd.DataFrame(results)
        return summary
    
    def export_results(self, filename='results/risk_metrics_summary.csv'):
        """
        Export latest metrics to CSV file.
        
        Args:
            filename (str): Output filename
        """
        summary = self.get_latest_metrics()
        summary.to_csv(filename)
        print(f"📁 Results exported to {filename}")
        return summary


def main():
    """
    Main execution function - demonstrates the risk analysis workflow.
    """
    # Top 5 most liquid Ibovespa stocks
    # PETR4 = Petrobras, VALE3 = Vale, ITUB4 = Itaú, BBDC4 = Bradesco, ABEV3 = Ambev
    tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA']
    
    print("=" * 70)
    print("🇧🇷 IBOVESPA RISK ANALYSIS - TOP 5 LIQUID STOCKS")
    print("=" * 70)
    print("\nStocks analyzed:")
    print("  • PETR4 - Petrobras (Oil & Gas)")
    print("  • VALE3 - Vale (Mining)")
    print("  • ITUB4 - Itaú Unibanco (Banking)")
    print("  • BBDC4 - Bradesco (Banking)")
    print("  • ABEV3 - Ambev (Beverages)")
    print("\n" + "=" * 70 + "\n")
    
    # Initialize analyzer
    analyzer = IbovespaRiskAnalyzer(tickers)
    
    # Download data
    data = analyzer.download_data()
    
    # Calculate all metrics
    metrics = analyzer.calculate_all_metrics(window=252)
    
    # Get and display summary
    print("\n" + "=" * 70)
    print("📊 LATEST RISK METRICS SUMMARY")
    print("=" * 70 + "\n")
    
    summary = analyzer.get_latest_metrics()
    print(summary.round(4))
    
    # Export results
    print("\n" + "=" * 70)
    analyzer.export_results()
    
    print("\n✅ Analysis complete!")
    print("=" * 70)
    
    return analyzer, summary


if __name__ == "__main__":
    analyzer, summary = main()
