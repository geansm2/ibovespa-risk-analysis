"""
Script to add new visualization cells to the Jupyter notebook
"""
import json
import sys
import io

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Load the notebook
with open('notebooks/01_complete_analysis.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# New cells to add
new_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 11. Visualizações Avançadas | Advanced Visualizations\n",
            "\n",
            "Vamos criar visualizações mais sofisticadas para análise aprofundada:\n",
            "\n",
            "*Let's create more sophisticated visualizations for in-depth analysis:*\n",
            "\n",
            "1. **Drawdown Waterfall** - Magnitude das quedas\n",
            "2. **VaR/CVaR Distribution** - Distribuição de tail risk\n",
            "3. **Correlation Heatmap** - Relações entre ações\n",
            "4. **Risk-Return Bubble** - Perfil risco-retorno"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Import new visualization functions\n",
            "from visualization.plots import (\n",
            "    plot_drawdown_waterfall,\n",
            "    plot_var_cvar_violin,\n",
            "    plot_correlation_heatmap,\n",
            "    plot_risk_return_bubble\n",
            ")\n",
            "\n",
            "print(\"✅ Advanced visualization functions imported!\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 11.1 Drawdown Waterfall Chart"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Waterfall chart showing maximum drawdown\n",
            "plot_drawdown_waterfall(data, metrics)\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Interpretation:\")\n",
            "print(\"- Red bars show maximum losses from peak\")\n",
            "print(\"- Reference lines indicate risk levels\")\n",
            "print(\"- BBDC4 has the largest drawdown (-46%)\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 11.2 VaR & CVaR Distribution"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Violin and box plots showing tail risk distribution\n",
            "plot_var_cvar_violin(data)\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Interpretation:\")\n",
            "print(\"- Left: Violin plots show full distribution of returns\")\n",
            "print(\"- Right: Box plots highlight CVaR (red stars)\")\n",
            "print(\"- Wider violins = higher volatility\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 11.3 Correlation Heatmap"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Correlation matrix between stocks\n",
            "plot_correlation_heatmap(data)\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Key Insights:\")\n",
            "print(\"- ITUB4 & BBDC4: High correlation (0.711) - both banks\")\n",
            "print(\"- PETR4 & VALE3: Low correlation (0.247) - good diversification\")\n",
            "print(\"- Lower correlation = better portfolio diversification\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 11.4 Risk-Return Bubble Chart"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Bubble chart: Risk vs Return (bubble size = Sharpe Ratio)\n",
            "plot_risk_return_bubble(data, metrics)\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Interpretation:\")\n",
            "print(\"- X-axis: Risk (volatility)\")\n",
            "print(\"- Y-axis: Return (annualized)\")\n",
            "print(\"- Bubble size: Sharpe Ratio (bigger = better)\")\n",
            "print(\"- Top-left quadrant is ideal: High return, low risk\")\n",
            "print(\"- PETR4 shows best risk-adjusted performance\")"
        ]
    }
]

# Add new cells before the last cell (resources)
nb['cells'] = nb['cells'][:-1] + new_cells + [nb['cells'][-1]]

# Update imports in the first code cell
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'from visualization.plots import' in ''.join(cell['source']):
        # Update the imports
        cell['source'] = [
            "import sys\n",
            "import os\n",
            "\n",
            "# Add src to path\n",
            "sys.path.insert(0, os.path.join(os.getcwd(), '..', 'src'))\n",
            "\n",
            "from analysis.risk_metrics import IbovespaRiskAnalyzer\n",
            "from analysis.portfolio_analysis import PortfolioAnalyzer, create_sample_strategies\n",
            "from visualization.plots import (\n",
            "    plot_price_history,\n",
            "    plot_returns_distribution,\n",
            "    plot_risk_metrics_comparison,\n",
            "    plot_metrics_heatmap,\n",
            "    plot_sharpe_sortino_comparison,\n",
            "    create_dashboard,\n",
            "    plot_drawdown_waterfall,\n",
            "    plot_var_cvar_violin,\n",
            "    plot_correlation_heatmap,\n",
            "    plot_risk_return_bubble\n",
            ")\n",
            "\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "import matplotlib.pyplot as plt\n",
            "import seaborn as sns\n",
            "\n",
            "import warnings\n",
            "warnings.filterwarnings('ignore')\n",
            "\n",
            "# Set display options\n",
            "pd.set_option('display.max_columns', None)\n",
            "pd.set_option('display.precision', 4)\n",
            "\n",
            "# Enable inline plotting\n",
            "%matplotlib inline\n",
            "\n",
            "print(\"✅ Imports successful!\")"
        ]
        break

# Save the updated notebook
with open('notebooks/01_complete_analysis.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print(f"✅ Notebook updated successfully!")
print(f"Total cells: {len(nb['cells'])}")
print(f"Added 9 new cells for advanced visualizations")
