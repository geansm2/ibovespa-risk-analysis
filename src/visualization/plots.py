"""
Visualization utilities for Ibovespa risk analysis.

This module provides functions to create professional charts and plots
for visualizing risk metrics, stock performance, and comparative analysis.

Updated to work with single-value metrics from custom calculations.

Author: Gean Santos
Date: December 2025
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.gridspec import GridSpec

# Set style for professional-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10


def plot_price_history(data, title="Stock Price History", save_path=None):
    """
    Plot historical prices for all stocks.
    
    Args:
        data (pd.DataFrame): DataFrame with stock prices
        title (str): Plot title
        save_path (str): Path to save the figure (optional)
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    for column in data.columns:
        ax.plot(data.index, data[column], label=column, linewidth=2)
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Price (BRL)', fontsize=12)
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def plot_returns_distribution(data, save_path=None):
    """
    Plot distribution of returns for each stock.
    
    Args:
        data (pd.DataFrame): DataFrame with stock prices
        save_path (str): Path to save the figure (optional)
    """
    returns = data.pct_change().dropna()
    
    n_stocks = len(data.columns)
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    axes = axes.flatten()
    
    for i, column in enumerate(returns.columns):
        if i < len(axes):
            axes[i].hist(returns[column], bins=50, alpha=0.7, color='steelblue', edgecolor='black')
            axes[i].axvline(returns[column].mean(), color='red', linestyle='--', 
                          linewidth=2, label=f'Mean: {returns[column].mean():.4f}')
            axes[i].set_title(f'{column} Returns Distribution', fontweight='bold')
            axes[i].set_xlabel('Daily Returns')
            axes[i].set_ylabel('Frequency')
            axes[i].legend()
            axes[i].grid(True, alpha=0.3)
    
    # Hide unused subplots
    for i in range(n_stocks, len(axes)):
        axes[i].axis('off')
    
    plt.suptitle('Daily Returns Distribution', fontsize=16, fontweight='bold', y=1.00)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def plot_risk_metrics_comparison(metrics_dict, metric_names=None, save_path=None):
    """
    Create bar charts comparing risk metrics across stocks.
    
    Args:
        metrics_dict (dict): Dictionary of metric DataFrames from analyzer
        metric_names (list): List of metric names to plot (default: all)
        save_path (str): Path to save the figure (optional)
    """
    if metric_names is None:
        metric_names = ['sharpe', 'sortino', 'volatility', 'max_drawdown', 'var', 'cvar']
    
    # Filter available metrics and extract values
    available_metrics = {k: v.iloc[0] for k, v in metrics_dict.items() if k in metric_names}
    
    n_metrics = len(available_metrics)
    fig = plt.figure(figsize=(16, 4 * ((n_metrics + 1) // 2)))
    gs = GridSpec(((n_metrics + 1) // 2), 2, figure=fig, hspace=0.3, wspace=0.3)
    
    for idx, (metric_name, metric_values) in enumerate(available_metrics.items()):
        row = idx // 2
        col = idx % 2
        ax = fig.add_subplot(gs[row, col])
        
        # Create bar chart
        stocks = metric_values.index
        values = metric_values.values
        colors = plt.cm.viridis(np.linspace(0, 1, len(stocks)))
        
        bars = ax.bar(stocks, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}',
                   ha='center', va='bottom' if height >= 0 else 'top', fontsize=9)
        
        ax.set_title(f'{metric_name.upper().replace("_", " ")}', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Value', fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
        
        # Rotate x labels if needed
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.suptitle('Risk Metrics Comparison', fontsize=16, fontweight='bold', y=0.995)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def plot_metrics_heatmap(summary_df, save_path=None):
    """
    Create a heatmap of latest metric values.
    
    Args:
        summary_df (pd.DataFrame): DataFrame with latest metrics (from get_latest_metrics())
        save_path (str): Path to save the figure (optional)
    """
    # Normalize data for better visualization
    normalized = summary_df.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=1)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    sns.heatmap(normalized, annot=True, fmt='.3f', cmap='RdYlGn_r', 
                cbar_kws={'label': 'Normalized Value'}, ax=ax, linewidths=0.5)
    
    ax.set_title('Risk Metrics Heatmap (Normalized)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Stocks', fontsize=12)
    ax.set_ylabel('Risk Metrics', fontsize=12)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def plot_sharpe_sortino_comparison(metrics_dict, save_path=None):
    """
    Create a scatter plot comparing Sharpe and Sortino ratios.
    
    Args:
        metrics_dict (dict): Dictionary of metric DataFrames
        save_path (str): Path to save the figure (optional)
    """
    sharpe_latest = metrics_dict['sharpe'].iloc[0]
    sortino_latest = metrics_dict['sortino'].iloc[0]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    stocks = sharpe_latest.index
    colors = plt.cm.viridis(np.linspace(0, 1, len(stocks)))
    
    for i, stock in enumerate(stocks):
        ax.scatter(sharpe_latest[stock], sortino_latest[stock], 
                  s=200, c=[colors[i]], alpha=0.7, edgecolors='black', linewidth=2)
        ax.annotate(stock, (sharpe_latest[stock], sortino_latest[stock]), 
                   fontsize=11, fontweight='bold', ha='center', va='bottom')
    
    ax.set_xlabel('Sharpe Ratio', fontsize=12, fontweight='bold')
    ax.set_ylabel('Sortino Ratio', fontsize=12, fontweight='bold')
    ax.set_title('Risk-Adjusted Returns: Sharpe vs Sortino', 
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    ax.axvline(x=0, color='red', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def create_dashboard(data, metrics_dict, save_path=None):
    """
    Create a comprehensive dashboard with multiple visualizations.
    
    Args:
        data (pd.DataFrame): Stock price data
        metrics_dict (dict): Dictionary of metric DataFrames
        save_path (str): Path to save the figure (optional)
    """
    fig = plt.figure(figsize=(18, 12))
    gs = GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3)
    
    # 1. Price history (top row, full width)
    ax1 = fig.add_subplot(gs[0, :])
    for column in data.columns:
        ax1.plot(data.index, data[column], label=column, linewidth=2)
    ax1.set_title('Price History', fontsize=12, fontweight='bold')
    ax1.legend(loc='best', fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylabel('Price (BRL)')
    
    # Extract metric values (single row DataFrames)
    stocks = list(data.columns)
    colors = plt.cm.viridis(np.linspace(0, 1, len(stocks)))
    
    # 2. Sharpe Ratio
    ax2 = fig.add_subplot(gs[1, 0])
    sharpe_vals = metrics_dict['sharpe'].iloc[0]
    bars = ax2.bar(stocks, sharpe_vals, color=colors, alpha=0.7, edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}',
                ha='center', va='bottom', fontsize=8)
    ax2.set_title('Sharpe Ratio', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # 3. Sortino Ratio
    ax3 = fig.add_subplot(gs[1, 1])
    sortino_vals = metrics_dict['sortino'].iloc[0]
    bars = ax3.bar(stocks, sortino_vals, color=colors, alpha=0.7, edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}',
                ha='center', va='bottom', fontsize=8)
    ax3.set_title('Sortino Ratio', fontsize=11, fontweight='bold')
    ax3.grid(True, alpha=0.3, axis='y')
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # 4. Volatility
    ax4 = fig.add_subplot(gs[1, 2])
    vol_vals = metrics_dict['volatility'].iloc[0]
    bars = ax4.bar(stocks, vol_vals, color=colors, alpha=0.7, edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}',
                ha='center', va='bottom', fontsize=8)
    ax4.set_title('Volatility (Annualized)', fontsize=11, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='y')
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # 5. Maximum Drawdown
    ax5 = fig.add_subplot(gs[2, 0])
    mdd_vals = metrics_dict['max_drawdown'].iloc[0]
    bars = ax5.bar(stocks, mdd_vals, color=colors, alpha=0.7, edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height, f'{height:.2f}',
                ha='center', va='top', fontsize=8)
    ax5.set_title('Maximum Drawdown', fontsize=11, fontweight='bold')
    ax5.grid(True, alpha=0.3, axis='y')
    ax5.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    plt.setp(ax5.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # 6. VaR
    ax6 = fig.add_subplot(gs[2, 1])
    var_vals = metrics_dict['var'].iloc[0]
    bars = ax6.bar(stocks, var_vals, color=colors, alpha=0.7, edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height, f'{height:.3f}',
                ha='center', va='top', fontsize=8)
    ax6.set_title('Value at Risk (95%)', fontsize=11, fontweight='bold')
    ax6.grid(True, alpha=0.3, axis='y')
    ax6.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # 7. CVaR
    ax7 = fig.add_subplot(gs[2, 2])
    cvar_vals = metrics_dict['cvar'].iloc[0]
    bars = ax7.bar(stocks, cvar_vals, color=colors, alpha=0.7, edgecolor='black')
    for bar in bars:
        height = bar.get_height()
        ax7.text(bar.get_x() + bar.get_width()/2., height, f'{height:.3f}',
                ha='center', va='top', fontsize=8)
    ax7.set_title('Conditional VaR (95%)', fontsize=11, fontweight='bold')
    ax7.grid(True, alpha=0.3, axis='y')
    ax7.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    plt.setp(ax7.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.suptitle('Ibovespa Risk Analysis Dashboard', fontsize=16, fontweight='bold', y=0.995)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Dashboard saved to {save_path}")
    
    return fig


def plot_drawdown_waterfall(data, metrics_dict, save_path=None):
    """
    Create a waterfall chart showing maximum drawdown for each stock.
    
    Args:
        data (pd.DataFrame): Stock price data
        metrics_dict (dict): Dictionary of metric DataFrames
        save_path (str): Path to save the figure (optional)
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    
    mdd_values = metrics_dict['max_drawdown'].iloc[0]
    stocks = mdd_values.index
    values = mdd_values.values * 100  # Convert to percentage
    
    # Create waterfall effect
    colors = ['#d62728' if v < 0 else '#2ca02c' for v in values]
    bars = ax.bar(stocks, values, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, values)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.1f}%',
               ha='center', va='top' if height < 0 else 'bottom', 
               fontsize=11, fontweight='bold')
    
    ax.set_title('Maximum Drawdown Analysis', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Drawdown (%)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Stock', fontsize=12, fontweight='bold')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add reference lines
    ax.axhline(y=-20, color='orange', linestyle='--', alpha=0.5, label='Moderate Risk (-20%)')
    ax.axhline(y=-30, color='red', linestyle='--', alpha=0.5, label='High Risk (-30%)')
    ax.legend(loc='lower right')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def plot_var_cvar_violin(data, save_path=None):
    """
    Create violin plots showing VaR and CVaR distribution across stocks.
    
    Args:
        data (pd.DataFrame): Stock price data
        save_path (str): Path to save the figure (optional)
    """
    # Calculate returns
    returns = data.pct_change().dropna()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # Prepare data for violin plot
    returns_list = [returns[col].values for col in returns.columns]
    
    # VaR visualization (left plot)
    parts1 = ax1.violinplot(returns_list, positions=range(len(returns.columns)),
                            showmeans=True, showmedians=True)
    
    # Color the violins
    colors = plt.cm.viridis(np.linspace(0, 1, len(returns.columns)))
    for i, pc in enumerate(parts1['bodies']):
        pc.set_facecolor(colors[i])
        pc.set_alpha(0.7)
    
    # Add VaR lines
    for i, col in enumerate(returns.columns):
        var_95 = returns[col].quantile(0.05)
        ax1.hlines(var_95, i-0.4, i+0.4, colors='red', linestyles='--', linewidth=2)
    
    ax1.set_title('Returns Distribution with VaR (95%)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Daily Returns', fontsize=12)
    ax1.set_xticks(range(len(returns.columns)))
    ax1.set_xticklabels(returns.columns, rotation=45, ha='right')
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=1)
    
    # CVaR visualization (right plot) - Box plot style
    bp = ax2.boxplot(returns_list, labels=returns.columns, patch_artist=True,
                     showmeans=True, meanline=True)
    
    # Color the boxes
    for i, (patch, color) in enumerate(zip(bp['boxes'], colors)):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Highlight CVaR region
    for i, col in enumerate(returns.columns):
        var_95 = returns[col].quantile(0.05)
        cvar_95 = returns[col][returns[col] <= var_95].mean()
        ax2.plot(i+1, cvar_95, 'r*', markersize=15, label='CVaR' if i == 0 else '')
    
    ax2.set_title('Returns Box Plot with CVaR (95%)', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Daily Returns', fontsize=12)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax2.legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def plot_correlation_heatmap(data, save_path=None):
    """
    Create a correlation heatmap showing relationships between stocks.
    
    Args:
        data (pd.DataFrame): Stock price data
        save_path (str): Path to save the figure (optional)
    """
    # Calculate returns correlation
    returns = data.pct_change().dropna()
    correlation = returns.corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create mask for upper triangle
    mask = np.triu(np.ones_like(correlation, dtype=bool))
    
    # Create heatmap
    sns.heatmap(correlation, mask=mask, annot=True, fmt='.3f', 
                cmap='RdYlGn', center=0, square=True, linewidths=1,
                cbar_kws={"shrink": 0.8, "label": "Correlation"},
                ax=ax, vmin=-1, vmax=1)
    
    ax.set_title('Stock Returns Correlation Matrix', fontsize=16, fontweight='bold', pad=20)
    
    # Add interpretation guide
    textstr = 'Interpretation:\n> 0.7: Strong positive\n0.3-0.7: Moderate\n< 0.3: Weak'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(1.15, 0.5, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='center', bbox=props)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


def plot_risk_return_bubble(data, metrics_dict, save_path=None):
    """
    Create a bubble chart showing risk-return profile.
    
    Args:
        data (pd.DataFrame): Stock price data
        metrics_dict (dict): Dictionary of metric DataFrames
        save_path (str): Path to save the figure (optional)
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Calculate annualized returns
    returns = data.pct_change().dropna()
    annual_returns = returns.mean() * 252 * 100  # Annualized %
    
    # Get metrics
    volatility = metrics_dict['volatility'].iloc[0] * 100  # Convert to %
    sharpe = metrics_dict['sharpe'].iloc[0]
    
    # Create bubble chart
    stocks = list(data.columns)
    colors = plt.cm.viridis(np.linspace(0, 1, len(stocks)))
    
    for i, stock in enumerate(stocks):
        # Bubble size based on Sharpe ratio (scaled)
        size = max(100, abs(sharpe[stock]) * 500)
        
        scatter = ax.scatter(volatility[stock], annual_returns[stock], 
                           s=size, c=[colors[i]], alpha=0.6, 
                           edgecolors='black', linewidth=2)
        
        # Add stock label
        ax.annotate(stock, 
                   (volatility[stock], annual_returns[stock]),
                   fontsize=12, fontweight='bold', ha='center', va='center')
        
        # Add Sharpe value
        ax.annotate(f'Sharpe: {sharpe[stock]:.2f}',
                   (volatility[stock], annual_returns[stock]),
                   xytext=(0, -25), textcoords='offset points',
                   fontsize=9, ha='center', style='italic')
    
    ax.set_xlabel('Risk (Annualized Volatility %)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Return (Annualized %)', fontsize=13, fontweight='bold')
    ax.set_title('Risk-Return Profile\n(Bubble size = Sharpe Ratio)', 
                fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    
    # Add quadrant lines
    ax.axhline(y=annual_returns.mean(), color='gray', linestyle='--', alpha=0.5, label='Avg Return')
    ax.axvline(x=volatility.mean(), color='gray', linestyle='--', alpha=0.5, label='Avg Risk')
    
    # Add efficient frontier concept annotation
    textstr = 'Top-Right: High Return, High Risk\nTop-Left: High Return, Low Risk (Best!)\nBottom-Right: Low Return, High Risk (Worst!)'
    props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)
    
    ax.legend(loc='lower right')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Chart saved to {save_path}")
    
    return fig


if __name__ == "__main__":
    print("This module provides visualization utilities.")
    print("Import and use the functions in your analysis scripts.")

