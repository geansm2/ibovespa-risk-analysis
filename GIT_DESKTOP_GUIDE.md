# Guia Rápido: Git Desktop e .gitignore

## O que é o .gitignore?

O arquivo `.gitignore` diz ao Git quais arquivos **NÃO** devem ser enviados para o GitHub. Isso é importante para:

- ✅ **Evitar arquivos grandes** desnecessários
- ✅ **Proteger informações sensíveis** (senhas, tokens)
- ✅ **Manter o repositório limpo** (sem cache, compilações)
- ✅ **Facilitar colaboração** (cada desenvolvedor tem suas próprias configurações)

## Arquivos que NÃO vão para o GitHub (já configurado)

### 🐍 Python
- `__pycache__/` - Cache de compilação Python
- `*.pyc`, `*.pyo` - Arquivos compilados
- `.pytest_cache/` - Cache de testes
- `*.egg-info/` - Informações de pacotes

### 📊 Dados e Resultados
- `data/` - Dados baixados (podem ser grandes)
- `*.csv`, `*.xlsx` - Planilhas de dados
- `results/` - Resultados de análises
- `*.png`, `*.jpg`, `*.pdf` - Gráficos gerados
- `*.log` - Arquivos de log

### 💻 IDEs e Editores
- `.vscode/` - Configurações do VS Code
- `.idea/` - Configurações do PyCharm
- `*.swp` - Arquivos temporários do Vim

### 🌍 Ambientes Virtuais
- `venv/`, `env/` - Ambientes virtuais Python
- `.env` - Variáveis de ambiente (senhas, chaves API)

### 🖥️ Sistema Operacional
- `.DS_Store` - Arquivos do macOS
- `Thumbs.db` - Miniaturas do Windows

## Como usar com Git Desktop

### 1️⃣ Primeira vez - Publicar no GitHub

1. **Abra o Git Desktop**
2. **File → Add Local Repository** (ou Ctrl+O)
3. Selecione a pasta: `c:\Users\geans\.gemini\antigravity\scratch\ibovespa-risk-analysis`
4. **Verifique os arquivos** na aba "Changes"
   - ✅ Arquivos `.py`, `.md`, `.txt` devem aparecer
   - ❌ Arquivos em `data/`, `__pycache__/`, `*.pyc` **NÃO** devem aparecer
5. **Escreva uma mensagem** de commit (ex: "Initial commit")
6. Clique em **"Commit to main"**
7. Clique em **"Publish repository"**
8. Escolha:
   - Nome do repositório
   - Descrição (opcional)
   - ☑️ **Keep this code private** (se quiser privado)
9. Clique em **"Publish repository"**

### 2️⃣ Atualizações futuras

1. **Faça suas alterações** nos arquivos
2. **Abra o Git Desktop**
3. Veja os arquivos modificados em "Changes"
4. **Escreva uma mensagem** descrevendo as mudanças
5. Clique em **"Commit to main"**
6. Clique em **"Push origin"** para enviar ao GitHub

### 3️⃣ Se arquivos indesejados aparecerem

Se você ver arquivos que **não deveria** enviar (ex: `__pycache__`, `.pyc`):

#### Opção A: Adicionar ao .gitignore (antes do commit)
1. Abra o arquivo `.gitignore`
2. Adicione o padrão do arquivo (ex: `*.pyc` ou `pasta/`)
3. Salve o arquivo
4. No Git Desktop, os arquivos desaparecerão da lista

#### Opção B: Remover arquivos já commitados
Se você **já enviou** arquivos por engano:

```bash
# Remover arquivo específico do Git (mas manter no seu computador)
git rm --cached nome_do_arquivo.csv

# Remover pasta inteira
git rm -r --cached data/

# Depois, faça commit e push
```

## Dicas Importantes

### ✅ Boas Práticas

1. **Sempre revise** os arquivos antes de fazer commit
2. **Mensagens claras** de commit (ex: "Adiciona análise de risco", não "update")
3. **Commits pequenos e frequentes** são melhores que commits gigantes
4. **Nunca commite**:
   - Senhas ou tokens
   - Dados sensíveis
   - Arquivos muito grandes (>100MB)

### 📝 Mensagens de Commit Sugeridas

- `feat: Adiciona nova funcionalidade X`
- `fix: Corrige bug no cálculo Y`
- `docs: Atualiza documentação`
- `refactor: Melhora código da função Z`
- `style: Formata código`
- `test: Adiciona testes`

### 🔍 Verificar o que será enviado

No Git Desktop:
- **Changes** = Arquivos que serão commitados
- **History** = Histórico de commits
- **Repository → Repository Settings** = Configurações

## Estrutura Recomendada para GitHub

```
ibovespa-risk-analysis/
├── .gitignore          ✅ Vai para o GitHub
├── README.md           ✅ Vai para o GitHub
├── requirements.txt    ✅ Vai para o GitHub
├── main.py             ✅ Vai para o GitHub
├── src/                ✅ Vai para o GitHub
│   └── *.py
├── notebooks/          ✅ Vai para o GitHub
│   └── *.ipynb
├── data/               ❌ NÃO vai (muito grande)
│   └── *.csv
├── results/            ❌ NÃO vai (gerado automaticamente)
│   └── *.png
├── __pycache__/        ❌ NÃO vai (cache)
└── venv/               ❌ NÃO vai (ambiente virtual)
```

## Solução de Problemas

### Problema: "Muitos arquivos para commitar"
**Solução**: Verifique se o `.gitignore` está correto e se você não está na pasta errada

### Problema: "Arquivo muito grande"
**Solução**: Adicione o arquivo ao `.gitignore` e use Git LFS se realmente precisar versionar

### Problema: "Já commitei arquivo errado"
**Solução**: Use `git rm --cached` para remover do Git sem deletar do computador

## Recursos Adicionais

- [Git Desktop Documentation](https://docs.github.com/en/desktop)
- [Gitignore Templates](https://github.com/github/gitignore)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

**Dúvidas?** Abra uma issue no GitHub ou consulte a documentação oficial!
