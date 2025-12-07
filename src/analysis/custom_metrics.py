"""
Custom Risk Metrics Calculation Module

This module implements risk metrics manually using pandas and numpy,
as an alternative to SquareQuant which was experiencing compatibility issues.

Author: Gean Santos
Date: December 2025
"""

import pandas as pd
import numpy as np
from scipy import stats


def calculate_returns(prices):
    """Calculate simple returns from prices."""
    return prices.pct_change().dropna()


def calculate_sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=252):
    """
    Calculate Sharpe Ratio.
    
    Args:
        returns (pd.Series or pd.DataFrame): Asset returns
        risk_free_rate (float or pd.Series): Risk-free rate. 
                                           If float, assumed to be annualized.
                                           If pd.Series, assumed to be daily rates aligned with returns.
        periods_per_year (int): Number of periods per year (252 for daily)
    
    Returns:
        float or pd.Series: Sharpe ratio(s)
    """
    # Calculate excess returns
    if isinstance(risk_free_rate, pd.Series):
        # Dynamic daily risk-free rate
        # Align indexes
        common_idx = returns.index.intersection(risk_free_rate.index)
        if len(common_idx) < len(returns):
             # minimal warning or handling if alignment loses data
             pass
        
        aligned_returns = returns.loc[common_idx]
        aligned_rf = risk_free_rate.loc[common_idx]
        
        # If returns is DataFrame, subtract rf from each column
        if isinstance(returns, pd.DataFrame):
            excess_returns = aligned_returns.sub(aligned_rf, axis=0)
        else:
            excess_returns = aligned_returns - aligned_rf
            
        # For dynamic rf, we calculate stats on the excess returns series directly
        return np.sqrt(periods_per_year) * excess_returns.mean() / excess_returns.std()
        
    else:
        # Constant annualized risk-free rate
        rf_daily = risk_free_rate / periods_per_year
        excess_returns = returns - rf_daily
        return np.sqrt(periods_per_year) * excess_returns.mean() / returns.std()


def calculate_sortino_ratio(returns, risk_free_rate=0.0, periods_per_year=252):
    """
    Calculate Sortino Ratio (uses downside deviation instead of total volatility).
    
    Args:
        returns (pd.Series or pd.DataFrame): Asset returns
        risk_free_rate (float or pd.Series): Risk-free rate.
        periods_per_year (int): Number of periods per year
    
    Returns:
        float or pd.Series: Sortino ratio(s)
    """
    # Calculate excess returns
    if isinstance(risk_free_rate, pd.Series):
        # Dynamic calculation
        common_idx = returns.index.intersection(risk_free_rate.index)
        aligned_returns = returns.loc[common_idx]
        aligned_rf = risk_free_rate.loc[common_idx]
        
        if isinstance(returns, pd.DataFrame):
            excess_returns = aligned_returns.sub(aligned_rf, axis=0)
        else:
            excess_returns = aligned_returns - aligned_rf
            
        # Use aligned returns for downside calculation
        returns_to_use = aligned_returns
        
    else:
        # Constant calculation
        rf_daily = risk_free_rate / periods_per_year
        excess_returns = returns - rf_daily
        returns_to_use = returns

    # Calculate Downside deviation
    if isinstance(returns, pd.DataFrame):
        result = {}
        for col in returns.columns:
            col_excess = excess_returns[col]
            # Downside is defined typically as returns below a target (MAR). 
            # Often target = 0 or target = risk_free. 
            # Standard Sortino uses target = 0 for downside filter, but numer is excess return.
            # Some definitions use target = risk_free for downside filter.
            # We'll stick to: downside = returns < 0 (absolute loss) for consistency with common libraries,
            # or we could strictly use returns < target. Let's use returns < 0 for "bad days".
            
            # Note: A stricter financial definition might use (R - Rf) < 0. 
            # Let's check the previous implementation: it used `returns[returns < 0]`.
            # We will maintain that logic for consistency.
            
            # Only consider the aligned portion if dynamic
            col_returns = returns_to_use[col]
            downside = col_returns[col_returns < 0]
            downside_std = downside.std()
            
            if downside_std > 0:
                result[col] = np.sqrt(periods_per_year) * col_excess.mean() / downside_std
            else:
                result[col] = np.nan
        return pd.Series(result)
    else:
        downside = returns_to_use[returns_to_use < 0]
        downside_std = downside.std()
        
        if downside_std > 0:
            return np.sqrt(periods_per_year) * excess_returns.mean() / downside_std
        return np.nan


def calculate_volatility(returns, periods_per_year=252):
    """
    Calculate annualized volatility.
    
    Args:
        returns (pd.Series or pd.DataFrame): Asset returns
        periods_per_year (int): Number of periods per year
    
    Returns:
        float or pd.Series: Annualized volatility
    """
    return returns.std() * np.sqrt(periods_per_year)


def calculate_max_drawdown(prices):
    """
    Calculate maximum drawdown.
    
    Args:
        prices (pd.Series or pd.DataFrame): Asset prices
    
    Returns:
        float or pd.Series: Maximum drawdown (negative value)
    """
    if isinstance(prices, pd.DataFrame):
        return prices.apply(lambda x: calculate_max_drawdown(x))
    
    cumulative = (1 + prices.pct_change()).cumprod()
    running_max = cumulative.expanding().max()
    drawdown = (cumulative - running_max) / running_max
    return drawdown.min()


def calculate_var(returns, confidence=0.95):
    """
    Calculate Value at Risk (VaR) using historical method.
    
    Args:
        returns (pd.Series or pd.DataFrame): Asset returns
        confidence (float): Confidence level (e.g., 0.95 for 95%)
    
    Returns:
        float or pd.Series: VaR (negative value representing potential loss)
    """
    if isinstance(returns, pd.DataFrame):
        return returns.quantile(1 - confidence)
    return returns.quantile(1 - confidence)


def calculate_cvar(returns, confidence=0.95):
    """
    Calculate Conditional Value at Risk (CVaR) / Expected Shortfall.
    
    Args:
        returns (pd.Series or pd.DataFrame): Asset returns
        confidence (float): Confidence level
    
    Returns:
        float or pd.Series: CVaR (average loss beyond VaR)
    """
    if isinstance(returns, pd.DataFrame):
        result = {}
        for col in returns.columns:
            var = calculate_var(returns[col], confidence)
            result[col] = returns[col][returns[col] <= var].mean()
        return pd.Series(result)
    
    var = calculate_var(returns, confidence)
    return returns[returns <= var].mean()


def calculate_semi_deviation(returns, periods_per_year=252):
    """
    Calculate semi-deviation (downside volatility).
    
    Args:
        returns (pd.Series or pd.DataFrame): Asset returns
        periods_per_year (int): Number of periods per year
    
    Returns:
        float or pd.Series: Annualized semi-deviation
    """
    if isinstance(returns, pd.DataFrame):
        result = {}
        for col in returns.columns:
            downside = returns[col][returns[col] < 0]
            result[col] = downside.std() * np.sqrt(periods_per_year)
        return pd.Series(result)
    
    downside = returns[returns < 0]
    return downside.std() * np.sqrt(periods_per_year)


def calculate_ulcer_index(prices):
    """
    Calculate Ulcer Index (measure of downside risk).
    
    Args:
        prices (pd.Series or pd.DataFrame): Asset prices
    
    Returns:
        float or pd.Series: Ulcer Index
    """
    if isinstance(prices, pd.DataFrame):
        return prices.apply(lambda x: calculate_ulcer_index(x))
    
    cumulative = (1 + prices.pct_change()).cumprod()
    running_max = cumulative.expanding().max()
    drawdown = (cumulative - running_max) / running_max
    return np.sqrt((drawdown ** 2).mean())


def calculate_mad(returns):
    """
    Calculate Mean Absolute Deviation.
    
    Args:
        returns (pd.Series or pd.DataFrame): Asset returns
    
    Returns:
        float or pd.Series: MAD
    """
    return (returns - returns.mean()).abs().mean()


def calculate_all_metrics(prices, returns=None):
    """
    Calculate all risk metrics for given price data.
    
    Args:
        prices (pd.DataFrame): Price data
        returns (pd.DataFrame): Returns data (optional, will be calculated if not provided)
    
    Returns:
        dict: Dictionary with all metrics
    """
    if returns is None:
        returns = calculate_returns(prices)
    
    metrics = {
        'sharpe': calculate_sharpe_ratio(returns),
        'sortino': calculate_sortino_ratio(returns),
        'volatility': calculate_volatility(returns),
        'max_drawdown': calculate_max_drawdown(prices),
        'var': calculate_var(returns, confidence=0.95),
        'cvar': calculate_cvar(returns, confidence=0.95),
        'semidev': calculate_semi_deviation(returns),
        'ulcer': calculate_ulcer_index(prices),
        'mad': calculate_mad(returns)
    }
    
    return pd.DataFrame(metrics).T


if __name__ == "__main__":
    # Test with sample data
    dates = pd.date_range('2020-01-01', periods=1000)
    test_prices = pd.DataFrame({
        'Stock_A': 100 * (1 + np.random.randn(1000) * 0.02).cumprod(),
        'Stock_B': 100 * (1 + np.random.randn(1000) * 0.015).cumprod()
    }, index=dates)
    
    print("Testing custom risk metrics...")
    metrics = calculate_all_metrics(test_prices)
    print("\nCalculated Metrics:")
    print(metrics.round(4))
    print("\n✅ All metrics calculated successfully!")
