"""
Main execution script for Ibovespa Risk Analysis

This script runs the complete analysis pipeline:
1. Downloads stock data
2. Calculates risk metrics
3. Generates visualizations
4. Exports results

Author: Gean Paulo Soares Machado
Date: December 2025
"""

import sys
import os
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from analysis.risk_metrics import IbovespaRiskAnalyzer
from analysis.portfolio_analysis import PortfolioAnalyzer, create_sample_strategies
from visualization.plots import (
    plot_price_history,
    plot_returns_distribution,
    plot_risk_metrics_comparison,
    plot_metrics_heatmap,
    plot_sharpe_sortino_comparison,
    create_dashboard,
    plot_drawdown_waterfall,
    plot_var_cvar_violin,
    plot_correlation_heatmap,
    plot_risk_return_bubble
)

import warnings
warnings.filterwarnings('ignore')


def main():
    """
    Execute complete Ibovespa risk analysis pipeline.
    """
    print("\n" + "=" * 80)
    print(" " * 20 + "🇧🇷 IBOVESPA RISK ANALYSIS 🇧🇷")
    print(" " * 15 + "Powered by SquareQuant Library")
    print("=" * 80 + "\n")
    
    # ========== STEP 1: DATA DOWNLOAD ==========
    print("STEP 1: DATA DOWNLOAD")
    print("-" * 80)
    
    # Top 5 most liquid Ibovespa stocks
    tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA']
    
    print("Selected stocks:")
    print("  🛢️  PETR4 - Petrobras (Oil & Gas)")
    print("  ⛏️  VALE3 - Vale (Mining)")
    print("  🏦 ITUB4 - Itaú Unibanco (Banking)")
    print("  🏦 BBDC4 - Bradesco (Banking)")
    print("  🍺 ABEV3 - Ambev (Beverages)\n")
    
    analyzer = IbovespaRiskAnalyzer(tickers)
    data = analyzer.download_data()
    
    # ========== STEP 2: RISK METRICS CALCULATION ==========
    print("\n" + "=" * 80)
    print("STEP 2: RISK METRICS CALCULATION")
    print("-" * 80)
    
    metrics = analyzer.calculate_all_metrics(window=252)
    
    # ========== STEP 3: RESULTS SUMMARY ==========
    print("\n" + "=" * 80)
    print("STEP 3: LATEST RISK METRICS SUMMARY")
    print("-" * 80 + "\n")
    
    summary = analyzer.get_latest_metrics()
    print(summary.round(4))
    
    # Export to CSV
    print("\n")
    analyzer.export_results('results/risk_metrics_summary.csv')
    
    # ========== STEP 4: PORTFOLIO ANALYSIS ==========
    print("\n" + "=" * 80)
    print("STEP 4: PORTFOLIO ANALYSIS")
    print("-" * 80 + "\n")
    
    # Create sample strategies
    stock_names = list(data.columns)
    strategies = create_sample_strategies(stock_names)
    
    print("Comparing 4 portfolio strategies:")
    for strategy_name, weights in strategies.items():
        print(f"\n  📊 {strategy_name}:")
        for stock, weight in weights.items():
            print(f"      {stock}: {weight*100:.1f}%")
    
    # Compare strategies
    portfolio_analyzer = PortfolioAnalyzer(data)
    comparison = portfolio_analyzer.compare_strategies(strategies)
    
    print("\n" + "-" * 80)
    print("Portfolio Performance Comparison:\n")
    print(comparison.round(4))
    
    # Export portfolio results
    comparison.to_csv('results/portfolio_comparison.csv')
    print("\n📁 Portfolio comparison exported to results/portfolio_comparison.csv")
    
    # ========== STEP 5: VISUALIZATIONS ==========
    print("\n" + "=" * 80)
    print("STEP 5: GENERATING VISUALIZATIONS")
    print("-" * 80 + "\n")
    
    # Create results directory if it doesn't exist
    os.makedirs('results', exist_ok=True)
    
    print("Creating charts...")
    
    # 1. Price history
    plot_price_history(data, 
                      title="Ibovespa Top 5 Stocks - Price History (5 Years)",
                      save_path='results/01_price_history.png')
    
    # 2. Returns distribution
    plot_returns_distribution(data, save_path='results/02_returns_distribution.png')
    
    # 3. Risk metrics comparison
    plot_risk_metrics_comparison(metrics, save_path='results/03_risk_metrics_comparison.png')
    
    # 4. Metrics heatmap
    plot_metrics_heatmap(summary, save_path='results/04_metrics_heatmap.png')
    
    # 5. Sharpe vs Sortino
    plot_sharpe_sortino_comparison(metrics, save_path='results/05_sharpe_sortino_comparison.png')
    
    # 6. Complete dashboard
    create_dashboard(data, metrics, save_path='results/06_complete_dashboard.png')
    
    # 7. Drawdown waterfall chart (NEW!)
    plot_drawdown_waterfall(data, metrics, save_path='results/07_drawdown_waterfall.png')
    
    # 8. VaR/CVaR violin plots (NEW!)
    plot_var_cvar_violin(data, save_path='results/08_var_cvar_distribution.png')
    
    # 9. Correlation heatmap (NEW!)
    plot_correlation_heatmap(data, save_path='results/09_correlation_heatmap.png')
    
    # 10. Risk-return bubble chart (NEW!)
    plot_risk_return_bubble(data, metrics, save_path='results/10_risk_return_bubble.png')
    
    # ========== COMPLETION ==========
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE!")
    print("=" * 80)
    print("\nGenerated files:")
    print("   results/risk_metrics_summary.csv")
    print("   results/portfolio_comparison.csv")
    print("   results/01_price_history.png")
    print("   results/02_returns_distribution.png")
    print("   results/03_risk_metrics_comparison.png")
    print("   results/04_metrics_heatmap.png")
    print("   results/05_sharpe_sortino_comparison.png")
    print("   results/06_complete_dashboard.png")
    print("   results/07_drawdown_waterfall.png (NEW!)")
    print("   results/08_var_cvar_distribution.png (NEW!)")
    print("   results/09_correlation_heatmap.png (NEW!)")
    print("   results/10_risk_return_bubble.png (NEW!)")
    print("\n" + "=" * 80 + "\n")
    
    return analyzer, metrics, summary, comparison


if __name__ == "__main__":
    analyzer, metrics, summary, comparison = main()
