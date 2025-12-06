# Script para remover arquivos pessoais do Git
# Mantém os arquivos localmente, mas remove do repositório

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Removendo Arquivos Pessoais do Git" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Lista de arquivos para remover do Git
$arquivos = @(
    "LINKEDIN_ARTICLE.md",
    "GIT_DESKTOP_GUIDE.md",
    "GITHUB_GUIDE.md",
    "NOTEBOOK_GUIDE.md",
    "PROJECT_SUMMARY.md",
    "QUICKSTART.md",
    "update_notebook.py"
)

Write-Host "Os seguintes arquivos serão removidos do Git:" -ForegroundColor Yellow
Write-Host "(mas permanecerão no seu computador)" -ForegroundColor Green
Write-Host ""

foreach ($arquivo in $arquivos) {
    Write-Host "  - $arquivo" -ForegroundColor White
}

Write-Host ""
$confirmacao = Read-Host "Deseja continuar? (S/N)"

if ($confirmacao -ne "S" -and $confirmacao -ne "s") {
    Write-Host ""
    Write-Host "Operação cancelada pelo usuário." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "Removendo arquivos do Git..." -ForegroundColor Cyan
Write-Host ""

$removidos = 0
$naoEncontrados = 0

foreach ($arquivo in $arquivos) {
    if (Test-Path $arquivo) {
        try {
            # Remove do Git mas mantém no disco
            git rm --cached $arquivo 2>$null
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "[OK] $arquivo removido do Git" -ForegroundColor Green
                $removidos++
            } else {
                Write-Host "[INFO] $arquivo não estava no Git" -ForegroundColor Yellow
                $naoEncontrados++
            }
        }
        catch {
            Write-Host "[ERRO] Falha ao remover $arquivo" -ForegroundColor Red
        }
    } else {
        Write-Host "[INFO] $arquivo não existe localmente" -ForegroundColor Yellow
        $naoEncontrados++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Resumo:" -ForegroundColor Cyan
Write-Host "  Removidos: $removidos" -ForegroundColor Green
Write-Host "  Não encontrados: $naoEncontrados" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if ($removidos -gt 0) {
    Write-Host "Próximos passos:" -ForegroundColor Cyan
    Write-Host "1. Faça commit das alterações:" -ForegroundColor White
    Write-Host '   git commit -m "remove: arquivos pessoais do repositório"' -ForegroundColor Gray
    Write-Host ""
    Write-Host "2. Envie para o GitHub:" -ForegroundColor White
    Write-Host "   git push" -ForegroundColor Gray
    Write-Host ""
    
    $autoCommit = Read-Host "Deseja fazer o commit automaticamente? (S/N)"
    
    if ($autoCommit -eq "S" -or $autoCommit -eq "s") {
        Write-Host ""
        Write-Host "Fazendo commit..." -ForegroundColor Cyan
        git commit -m "remove: arquivos pessoais do repositório"
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] Commit realizado com sucesso!" -ForegroundColor Green
            Write-Host ""
            
            $autoPush = Read-Host "Deseja fazer push para o GitHub agora? (S/N)"
            
            if ($autoPush -eq "S" -or $autoPush -eq "s") {
                Write-Host ""
                Write-Host "Enviando para o GitHub..." -ForegroundColor Cyan
                git push
                
                if ($LASTEXITCODE -eq 0) {
                    Write-Host ""
                    Write-Host "[OK] Push realizado com sucesso!" -ForegroundColor Green
                    Write-Host "Seus arquivos pessoais foram removidos do GitHub!" -ForegroundColor Green
                } else {
                    Write-Host ""
                    Write-Host "[ERRO] Falha ao fazer push. Execute manualmente:" -ForegroundColor Red
                    Write-Host "git push" -ForegroundColor Gray
                }
            }
        } else {
            Write-Host "[ERRO] Falha ao fazer commit" -ForegroundColor Red
        }
    }
} else {
    Write-Host "Nenhum arquivo foi removido. Nada a fazer." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Script finalizado!" -ForegroundColor Green
Write-Host ""
