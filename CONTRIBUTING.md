# Contributing to Ibovespa Risk Analysis

*Leia em português: [Português](#português) | Read in English: [English](#english)*

---

## Português

Obrigado por considerar contribuir para este projeto!

### Reportando Bugs

Se você encontrou um bug, por favor abra uma [issue](../../issues) incluindo:

1. **Descrição clara do problema**
2. **Passos para reproduzir**
   ```
   1. Execute '...'
   2. Veja o erro em '...'
   ```
3. **Comportamento esperado**
4. **Comportamento atual**
5. **Ambiente**
   - Python version
   - Sistema operacional
   - Versão das bibliotecas (`pip list`)
6. **Screenshots** (se aplicável)

### Sugerindo Melhorias

Adoraríamos ouvir suas ideias! Para sugerir melhorias:

1. Verifique se já não existe uma [issue](../../issues) similar
2. Abra uma nova issue com a tag `enhancement`
3. Descreva:
   - O problema que a melhoria resolve
   - A solução proposta
   - Alternativas consideradas
   - Impacto esperado

### Contribuindo com Código

#### Preparando o Ambiente

1. **Fork o repositório**

2. **Clone seu fork**
   ```bash
   git clone https://github.com/seu-usuario/ibovespa-risk-analysis.git
   cd ibovespa-risk-analysis
   ```

3. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/nome-da-feature
   ```

#### Convenções de Branch

- `feature/` - Novas funcionalidades
- `fix/` - Correções de bugs
- `docs/` - Mudanças na documentação
- `refactor/` - Refatoração de código
- `test/` - Adição ou correção de testes

Exemplos:
- `feature/add-new-risk-metric`
- `fix/volatility-calculation`
- `docs/update-readme`

#### Padrões de Código

- **PEP 8**: Siga as convenções de estilo Python
- **Docstrings**: Use docstrings para funções e classes
  ```python
  def calculate_metric(data, window=252):
      """
      Calculate risk metric.
      
      Args:
          data (pd.DataFrame): Stock price data
          window (int): Rolling window size
          
      Returns:
          pd.DataFrame: Calculated metric
      """
      pass
  ```
- **Type Hints**: Use quando possível
  ```python
  def process_data(data: pd.DataFrame) -> pd.DataFrame:
      pass
  ```
- **Comentários**: Explique o "porquê", não o "o quê"

#### Processo de Pull Request

1. **Atualize seu fork**
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

2. **Teste suas mudanças**
   ```bash
   python main.py
   # Verifique se tudo funciona corretamente
   ```

3. **Commit suas mudanças**
   ```bash
   git add .
   git commit -m "feat: adiciona nova métrica de risco"
   ```

   **Convenção de Commits:**
   - `feat:` - Nova funcionalidade
   - `fix:` - Correção de bug
   - `docs:` - Mudanças na documentação
   - `style:` - Formatação, ponto e vírgula, etc
   - `refactor:` - Refatoração de código
   - `test:` - Adição de testes
   - `chore:` - Atualização de tarefas, etc

4. **Push para seu fork**
   ```bash
   git push origin feature/nome-da-feature
   ```

5. **Abra um Pull Request**
   - Descreva suas mudanças claramente
   - Referencie issues relacionadas
   - Adicione screenshots se aplicável

### Melhorando a Documentação

Documentação é crucial! Você pode ajudar:

- Corrigindo erros de digitação
- Melhorando explicações
- Adicionando exemplos
- Traduzindo conteúdo
- Criando tutoriais

### Checklist do Pull Request

Antes de submeter, verifique:

- [ ] O código segue os padrões do projeto
- [ ] Adicionei docstrings para novas funções
- [ ] Atualizei a documentação se necessário
- [ ] Testei as mudanças localmente
- [ ] O commit segue a convenção de commits
- [ ] A branch está atualizada com main

### Dúvidas?

Não hesite em abrir uma issue com a tag `question` ou entrar em contato!

---

## English

Thank you for considering contributing to this project!

### Reporting Bugs

If you found a bug, please open an [issue](../../issues) including:

1. **Clear description of the problem**
2. **Steps to reproduce**
   ```
   1. Run '...'
   2. See error at '...'
   ```
3. **Expected behavior**
4. **Actual behavior**
5. **Environment**
   - Python version
   - Operating system
   - Library versions (`pip list`)
6. **Screenshots** (if applicable)

### Suggesting Enhancements

We'd love to hear your ideas! To suggest improvements:

1. Check if a similar [issue](../../issues) doesn't already exist
2. Open a new issue with the `enhancement` tag
3. Describe:
   - The problem the enhancement solves
   - Proposed solution
   - Alternatives considered
   - Expected impact

### Contributing Code

#### Setting Up the Environment

1. **Fork the repository**

2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/ibovespa-risk-analysis.git
   cd ibovespa-risk-analysis
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a branch for your feature**
   ```bash
   git checkout -b feature/feature-name
   ```

#### Branch Conventions

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding or fixing tests

Examples:
- `feature/add-new-risk-metric`
- `fix/volatility-calculation`
- `docs/update-readme`

#### Code Standards

- **PEP 8**: Follow Python style conventions
- **Docstrings**: Use docstrings for functions and classes
  ```python
  def calculate_metric(data, window=252):
      """
      Calculate risk metric.
      
      Args:
          data (pd.DataFrame): Stock price data
          window (int): Rolling window size
          
      Returns:
          pd.DataFrame: Calculated metric
      """
      pass
  ```
- **Type Hints**: Use when possible
  ```python
  def process_data(data: pd.DataFrame) -> pd.DataFrame:
      pass
  ```
- **Comments**: Explain the "why", not the "what"

#### Pull Request Process

1. **Update your fork**
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

2. **Test your changes**
   ```bash
   python main.py
   # Verify everything works correctly
   ```

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add new risk metric"
   ```

   **Commit Convention:**
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `style:` - Formatting, semicolons, etc
   - `refactor:` - Code refactoring
   - `test:` - Adding tests
   - `chore:` - Task updates, etc

4. **Push to your fork**
   ```bash
   git push origin feature/feature-name
   ```

5. **Open a Pull Request**
   - Describe your changes clearly
   - Reference related issues
   - Add screenshots if applicable

### Improving Documentation

Documentation is crucial! You can help by:

- Fixing typos
- Improving explanations
- Adding examples
- Translating content
- Creating tutorials

### Pull Request Checklist

Before submitting, verify:

- [ ] Code follows project standards
- [ ] Added docstrings for new functions
- [ ] Updated documentation if necessary
- [ ] Tested changes locally
- [ ] Commit follows commit convention
- [ ] Branch is up to date with main

### Questions?

Don't hesitate to open an issue with the `question` tag or reach out!

---

**Thank you for your contribution!**