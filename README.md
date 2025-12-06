# 🇧🇷 Análise de Risco do Ibovespa | Ibovespa Risk Analysis 📊

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![SquareQuant](https://img.shields.io/badge/SquareQuant-Latest-green)](https://github.com/SquareQuant/squarequant-package)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Read this in other languages: [English](#english) | [Português](#português)*

---

## Português

### 📖 Sobre o Projeto

Este projeto apresenta uma análise quantitativa abrangente das **5 ações mais líquidas do Ibovespa**, utilizando a biblioteca open-source [SquareQuant](https://github.com/SquareQuant/squarequant-package). O objetivo é demonstrar técnicas modernas de análise de risco financeiro aplicadas ao mercado brasileiro.

**Ações Analisadas:**
- 🛢️ **PETR4** - Petrobras (Petróleo & Gás)
- ⛏️ **VALE3** - Vale (Mineração)
- 🏦 **ITUB4** - Itaú Unibanco (Bancário)
- 🏦 **BBDC4** - Bradesco (Bancário)
- 🍺 **ABEV3** - Ambev (Bebidas)

### ✨ Funcionalidades

- **Download Automático de Dados**: Coleta dados históricos via Yahoo Finance
- **Métricas de Risco Completas**: Calcula 9 métricas diferentes
  - Sharpe Ratio
  - Sortino Ratio
  - Volatilidade
  - Maximum Drawdown (MDD)
  - Value at Risk (VaR)
  - Conditional VaR (CVaR)
  - Semi-Desvio
  - Ulcer Index
  - Mean Absolute Deviation (MAD)
- **Análise de Portfólio**: Compara diferentes estratégias de alocação
- **Visualizações Profissionais**: Gráficos e dashboards interativos
- **Exportação de Resultados**: Dados em CSV para análises adicionais

### 🚀 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/ibovespa-risk-analysis.git
cd ibovespa-risk-analysis
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### 💻 Uso

#### Execução Rápida

Execute a análise completa com um único comando:

```bash
python main.py
```

Este script irá:
1. Baixar dados históricos (últimos 5 anos)
2. Calcular todas as métricas de risco
3. Gerar visualizações
4. Exportar resultados para a pasta `results/`

#### Uso Avançado

**Análise Customizada:**

```python
from src.analysis.risk_metrics import IbovespaRiskAnalyzer

# Defina suas próprias ações e período
tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA']
analyzer = IbovespaRiskAnalyzer(
    tickers=tickers,
    start_date='2020-01-01',
    end_date='2024-12-31'
)

# Baixe dados e calcule métricas
data = analyzer.download_data()
metrics = analyzer.calculate_all_metrics(window=252)
summary = analyzer.get_latest_metrics()
```

**Análise de Portfólio:**

```python
from src.analysis.portfolio_analysis import PortfolioAnalyzer

# Defina pesos personalizados
weights = {
    'PETR4': 0.30,
    'VALE3': 0.30,
    'ITUB4': 0.20,
    'BBDC4': 0.10,
    'ABEV3': 0.10
}

portfolio = PortfolioAnalyzer(data, weights)
stats = portfolio.get_portfolio_statistics()
```

**Visualizações:**

```python
from src.visualization.plots import (
    plot_price_history,
    plot_risk_metrics_comparison,
    create_dashboard
)

# Gere gráficos individuais
plot_price_history(data, save_path='my_chart.png')
plot_risk_metrics_comparison(metrics, save_path='metrics.png')

# Ou crie um dashboard completo
create_dashboard(data, metrics, save_path='dashboard.png')
```

### 📊 Resultados

Após executar `main.py`, você encontrará na pasta `results/`:

- **CSV Files:**
  - `risk_metrics_summary.csv` - Resumo de todas as métricas
  - `portfolio_comparison.csv` - Comparação de estratégias

- **Visualizações:**
  - `01_price_history.png` - Histórico de preços
  - `02_returns_distribution.png` - Distribuição de retornos
  - `03_risk_metrics_comparison.png` - Comparação de métricas
  - `04_metrics_heatmap.png` - Heatmap de métricas
  - `05_sharpe_sortino_comparison.png` - Sharpe vs Sortino
  - `06_complete_dashboard.png` - Dashboard completo

### 📁 Estrutura do Projeto

```
ibovespa-risk-analysis/
├── src/
│   ├── analysis/
│   │   ├── risk_metrics.py       # Cálculo de métricas de risco
│   │   └── portfolio_analysis.py # Análise de portfólio
│   └── visualization/
│       └── plots.py               # Funções de visualização
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_risk_analysis.ipynb
│   └── 03_portfolio_optimization.ipynb
├── results/                       # Resultados gerados
├── data/                          # Cache de dados (gitignored)
├── main.py                        # Script principal
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

### 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre:
- Como reportar bugs
- Como sugerir melhorias
- Processo de Pull Request
- Padrões de código

### 📚 Recursos Adicionais

- [Documentação SquareQuant](https://github.com/SquareQuant/squarequant-package)
- [Notebooks Jupyter](notebooks/) - Análises interativas
- [Artigos sobre Análise de Risco](https://www.investopedia.com/terms/r/risk-analysis.asp)

### 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

### 👤 Autor

**Gean Paulo Soares Machado**
- GitHub: [@seu-usuario](https://github.com/geansm2)
- LinkedIn: [Seu Nome](https://linkedin.com/in/gean-machado)

### 🙏 Agradecimentos

- [SquareQuant](https://github.com/SquareQuant/squarequant-package) - Biblioteca de análise quantitativa
- Comunidade Python de finanças quantitativas

---

## English

### 📖 About The Project

This project presents a comprehensive quantitative analysis of the **top 5 most liquid stocks in the Ibovespa index**, using the open-source [SquareQuant](https://github.com/SquareQuant/squarequant-package) library. The goal is to demonstrate modern financial risk analysis techniques applied to the Brazilian market.

**Analyzed Stocks:**
- 🛢️ **PETR4** - Petrobras (Oil & Gas)
- ⛏️ **VALE3** - Vale (Mining)
- 🏦 **ITUB4** - Itaú Unibanco (Banking)
- 🏦 **BBDC4** - Bradesco (Banking)
- 🍺 **ABEV3** - Ambev (Beverages)

### ✨ Features

- **Automatic Data Download**: Fetches historical data via Yahoo Finance
- **Comprehensive Risk Metrics**: Calculates 9 different metrics
  - Sharpe Ratio
  - Sortino Ratio
  - Volatility
  - Maximum Drawdown (MDD)
  - Value at Risk (VaR)
  - Conditional VaR (CVaR)
  - Semi-Deviation
  - Ulcer Index
  - Mean Absolute Deviation (MAD)
- **Portfolio Analysis**: Compares different allocation strategies
- **Professional Visualizations**: Charts and interactive dashboards
- **Results Export**: CSV data for additional analysis

### 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/ibovespa-risk-analysis.git
cd ibovespa-risk-analysis
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### 💻 Usage

#### Quick Start

Run the complete analysis with a single command:

```bash
python main.py
```

This script will:
1. Download historical data (last 5 years)
2. Calculate all risk metrics
3. Generate visualizations
4. Export results to `results/` folder

#### Advanced Usage

**Custom Analysis:**

```python
from src.analysis.risk_metrics import IbovespaRiskAnalyzer

# Define your own stocks and period
tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA']
analyzer = IbovespaRiskAnalyzer(
    tickers=tickers,
    start_date='2020-01-01',
    end_date='2024-12-31'
)

# Download data and calculate metrics
data = analyzer.download_data()
metrics = analyzer.calculate_all_metrics(window=252)
summary = analyzer.get_latest_metrics()
```

**Portfolio Analysis:**

```python
from src.analysis.portfolio_analysis import PortfolioAnalyzer

# Define custom weights
weights = {
    'PETR4': 0.30,
    'VALE3': 0.30,
    'ITUB4': 0.20,
    'BBDC4': 0.10,
    'ABEV3': 0.10
}

portfolio = PortfolioAnalyzer(data, weights)
stats = portfolio.get_portfolio_statistics()
```

**Visualizations:**

```python
from src.visualization.plots import (
    plot_price_history,
    plot_risk_metrics_comparison,
    create_dashboard
)

# Generate individual charts
plot_price_history(data, save_path='my_chart.png')
plot_risk_metrics_comparison(metrics, save_path='metrics.png')

# Or create a complete dashboard
create_dashboard(data, metrics, save_path='dashboard.png')
```

### 📊 Results

After running `main.py`, you'll find in the `results/` folder:

- **CSV Files:**
  - `risk_metrics_summary.csv` - Summary of all metrics
  - `portfolio_comparison.csv` - Strategy comparison

- **Visualizations:**
  - `01_price_history.png` - Price history
  - `02_returns_distribution.png` - Returns distribution
  - `03_risk_metrics_comparison.png` - Metrics comparison
  - `04_metrics_heatmap.png` - Metrics heatmap
  - `05_sharpe_sortino_comparison.png` - Sharpe vs Sortino
  - `06_complete_dashboard.png` - Complete dashboard

### 📁 Project Structure

```
ibovespa-risk-analysis/
├── src/
│   ├── analysis/
│   │   ├── risk_metrics.py       # Risk metrics calculation
│   │   └── portfolio_analysis.py # Portfolio analysis
│   └── visualization/
│       └── plots.py               # Visualization functions
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_risk_analysis.ipynb
│   └── 03_portfolio_optimization.ipynb
├── results/                       # Generated results
├── data/                          # Data cache (gitignored)
├── main.py                        # Main script
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

### 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details on:
- How to report bugs
- How to suggest improvements
- Pull Request process
- Code standards

### 📚 Additional Resources

- [SquareQuant Documentation](https://github.com/SquareQuant/squarequant-package)
- [Jupyter Notebooks](notebooks/) - Interactive analyses
- [Risk Analysis Articles](https://www.investopedia.com/terms/r/risk-analysis.asp)

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 👤 Author

**Gean Paulo Soares Machado**
- GitHub: [@seu-usuario](https://github.com/geansm2)
- LinkedIn: [Seu Nome](https://linkedin.com/in/gean-machado)

### 🙏 Acknowledgments

- [SquareQuant](https://github.com/SquareQuant/squarequant-package) - Quantitative analysis library
- Python quantitative finance community

---

**⭐ If you found this project useful, please consider giving it a star!**
