"""
Portfolio Analysis for Ibovespa Stocks

This module provides portfolio-level risk analysis, comparing different
allocation strategies and calculating portfolio risk metrics.

Author: Gean Santos
Date: December 2025
"""

import squarequant as sq
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


class PortfolioAnalyzer:
    """
    Portfolio-level risk analysis for Ibovespa stocks.
    """
    
    def __init__(self, data, weights=None):
        """
        Initialize portfolio analyzer.
        
        Args:
            data (pd.DataFrame): Stock price data
            weights (dict): Portfolio weights {ticker: weight}
        """
        self.data = data
        
        # Equal weights if not specified
        if weights is None:
            n_stocks = len(data.columns)
            self.weights = {col: 1.0/n_stocks for col in data.columns}
        else:
            self.weights = weights
            
        # Validate weights sum to 1
        total_weight = sum(self.weights.values())
        if not np.isclose(total_weight, 1.0):
            print(f"⚠️  Warning: Weights sum to {total_weight:.4f}, normalizing...")
            self.weights = {k: v/total_weight for k, v in self.weights.items()}
    
    def calculate_portfolio_returns(self):
        """
        Calculate portfolio returns based on weights.
        
        Returns:
            pd.Series: Portfolio returns
        """
        returns = self.data.pct_change().dropna()
        
        portfolio_returns = pd.Series(0, index=returns.index)
        for stock, weight in self.weights.items():
            if stock in returns.columns:
                portfolio_returns += returns[stock] * weight
        
        return portfolio_returns
    
    def calculate_portfolio_value(self, initial_value=100000):
        """
        Calculate portfolio value over time.
        
        Args:
            initial_value (float): Initial portfolio value in BRL
            
        Returns:
            pd.Series: Portfolio value over time
        """
        returns = self.calculate_portfolio_returns()
        portfolio_value = initial_value * (1 + returns).cumprod()
        return portfolio_value
    
    def get_portfolio_statistics(self):
        """
        Calculate comprehensive portfolio statistics.
        
        Returns:
            dict: Portfolio statistics
        """
        returns = self.calculate_portfolio_returns()
        
        stats = {
            'Total Return': (1 + returns).prod() - 1,
            'Annualized Return': returns.mean() * 252,
            'Annualized Volatility': returns.std() * np.sqrt(252),
            'Sharpe Ratio': (returns.mean() * 252) / (returns.std() * np.sqrt(252)),
            'Max Drawdown': self._calculate_max_drawdown(returns),
            'Skewness': returns.skew(),
            'Kurtosis': returns.kurtosis(),
            'VaR (95%)': returns.quantile(0.05),
            'CVaR (95%)': returns[returns <= returns.quantile(0.05)].mean(),
        }
        
        return stats
    
    def _calculate_max_drawdown(self, returns):
        """Calculate maximum drawdown from returns."""
        cumulative = (1 + returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        return drawdown.min()
    
    def compare_strategies(self, strategies):
        """
        Compare multiple portfolio strategies.
        
        Args:
            strategies (dict): Dictionary of {strategy_name: weights_dict}
            
        Returns:
            pd.DataFrame: Comparison of strategies
        """
        results = {}
        
        for strategy_name, weights in strategies.items():
            temp_analyzer = PortfolioAnalyzer(self.data, weights)
            stats = temp_analyzer.get_portfolio_statistics()
            results[strategy_name] = stats
        
        comparison = pd.DataFrame(results).T
        return comparison


def create_sample_strategies(stocks):
    """
    Create sample portfolio strategies for comparison.
    
    Args:
        stocks (list): List of stock tickers
        
    Returns:
        dict: Dictionary of strategies
    """
    n_stocks = len(stocks)
    
    strategies = {
        'Equal Weight': {stock: 1.0/n_stocks for stock in stocks},
        'Conservative': {
            stocks[0]: 0.15,  # PETR4
            stocks[1]: 0.15,  # VALE3
            stocks[2]: 0.30,  # ITUB4
            stocks[3]: 0.30,  # BBDC4
            stocks[4]: 0.10,  # ABEV3
        },
        'Aggressive': {
            stocks[0]: 0.35,  # PETR4
            stocks[1]: 0.35,  # VALE3
            stocks[2]: 0.10,  # ITUB4
            stocks[3]: 0.10,  # BBDC4
            stocks[4]: 0.10,  # ABEV3
        },
        'Defensive': {
            stocks[0]: 0.10,  # PETR4
            stocks[1]: 0.10,  # VALE3
            stocks[2]: 0.25,  # ITUB4
            stocks[3]: 0.25,  # BBDC4
            stocks[4]: 0.30,  # ABEV3
        },
    }
    
    return strategies


def main():
    """
    Demonstrate portfolio analysis.
    """
    print("=" * 70)
    print("📊 PORTFOLIO ANALYSIS - IBOVESPA STOCKS")
    print("=" * 70)
    
    # This would typically use data from risk_metrics.py
    # For demonstration, we'll show the structure
    
    print("\nThis module provides portfolio-level analysis.")
    print("Use it in conjunction with risk_metrics.py for complete analysis.")
    print("\nExample usage:")
    print("  from src.analysis.portfolio_analysis import PortfolioAnalyzer")
    print("  analyzer = PortfolioAnalyzer(data, weights)")
    print("  stats = analyzer.get_portfolio_statistics()")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
