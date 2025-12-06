# 📓 Guia Rápido - Jupyter Notebook

## ✅ Problema Resolvido!

O notebook foi atualizado com uma célula de instalação automática de dependências.

## 🚀 Como Usar o Notebook

### Opção 1: Via Jupyter Notebook (Recomendado)

1. **Abra o terminal na pasta do projeto:**
   ```bash
   cd C:\Users\geans\.gemini\antigravity\scratch\ibovespa-risk-analysis
   ```

2. **Inicie o Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

3. **No navegador que abrir:**
   - Navegue até `notebooks/`
   - Clique em `01_complete_analysis.ipynb`

4. **Execute as células em ordem:**
   - **Célula 0 (IMPORTANTE)**: Execute primeiro para instalar dependências
   - Depois execute as demais células sequencialmente
   - Use `Shift + Enter` para executar cada célula

### Opção 2: Via VS Code

1. **Abra o arquivo:**
   - `notebooks/01_complete_analysis.ipynb`

2. **Selecione o kernel Python:**
   - Clique em "Select Kernel" no canto superior direito
   - Escolha o Python que tem o Anaconda instalado

3. **Execute a primeira célula:**
   - Clique em "Run Cell" na célula 0 (Setup)
   - Aguarde a instalação das dependências

4. **Continue executando as demais células**

## 📝 O que foi corrigido

### Mudanças no Notebook:

1. ✅ **Nova Célula 0 - Setup**
   - Instala automaticamente todas as dependências
   - Verifica se os pacotes já estão instalados
   - Evita reinstalações desnecessárias

2. ✅ **Adicionado `%matplotlib inline`**
   - Garante que os gráficos apareçam no notebook

3. ✅ **Melhor tratamento de imports**
   - Mensagens claras de sucesso/erro

## 🎯 Estrutura do Notebook

O notebook está organizado em 10 seções:

0. **Setup** - Instalação de dependências (EXECUTE PRIMEIRO!)
1. **Importações** - Carrega bibliotecas
2. **Download de Dados** - Baixa dados do Ibovespa
3. **Visualização de Preços** - Gráfico de histórico
4. **Distribuição de Retornos** - Análise estatística
5. **Cálculo de Métricas** - 9 métricas de risco
6. **Resumo das Métricas** - Tabela consolidada
7. **Visualização de Métricas** - Heatmaps e gráficos
8. **Análise de Portfólio** - Comparação de estratégias
9. **Dashboard Completo** - Visão geral
10. **Insights e Conclusões** - Análise final

## ⚠️ Dicas Importantes

1. **Execute a Célula 0 primeiro** - Ela instala as dependências
2. **Execute as células em ordem** - Cada célula depende das anteriores
3. **Aguarde cada célula terminar** - Algumas podem demorar (download de dados)
4. **Se der erro de módulo** - Execute a Célula 0 novamente

## 🔧 Troubleshooting

### Erro: "No module named 'squarequant'"
**Solução**: Execute a Célula 0 (Setup) primeiro

### Erro: Kernel não encontrado
**Solução**: 
```bash
python -m ipykernel install --user
```

### Gráficos não aparecem
**Solução**: Certifique-se que a célula com `%matplotlib inline` foi executada

## 📊 Tempo Estimado

- **Primeira execução**: ~3-5 minutos (inclui download de dados)
- **Execuções seguintes**: ~1-2 minutos (dados em cache)

## ✅ Teste Agora!

1. Feche e reabra o notebook no Jupyter/VS Code
2. Execute a Célula 0 (Setup)
3. Execute as demais células em sequência
4. Aproveite a análise interativa!

---

**Qualquer dúvida, consulte o README.md ou QUICKSTART.md**
