# Contribuindo

Obrigado por considerar contribuir com este projeto! 🙌

## Pré-requisitos
- Python 3.10+
- Git
- Ambiente virtual (recomendado)

## Setup do ambiente (dev)
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat

python -m pip install -e ".[dev]"
```

## Padrão de commits (Conventional Commits)
Use mensagens no formato:
- `feat: ...` (nova funcionalidade)
- `fix: ...` (correção)
- `docs: ...` (documentação)
- `test: ...` (testes)
- `chore: ...` (tarefas internas)
- `ci: ...` (pipeline)

Exemplo:
```bash
git commit -m "feat: add command to reset password"
```

## Fluxo de contribuição
1. Faça um fork do repositório
2. Crie uma branch para sua alteração:
   ```bash
   git checkout -b feat/minha-melhoria
   ```
3. Faça suas mudanças e rode os checks
4. Faça commit e push:
    ```bash
    git commit -m "feat: minha melhoria"
    git push origin feat/minha-melhoria
    ```
5. Abra um Pull Request descrevendo:
    - O que foi alterado
    - Como testar
    - Prints/logs (se aplicável)

## Estilo de código
- Formatação e lint: **Ruff**
- Linha máxima: **88** caracteres
- Prefira código simples, com nomes claros e funções pequenas
- Use tipagem (`typing`) quando ajudar na leitura/manutenção
- Mantenha regras de negócio no `service/` e validações no `domain/`
- Evite acessar SQLite diretamente fora do `repository/`

## Reportando bugs / sugestões
Abra uma issue com:
- Passo a passo para reproduzir
- Resultado esperado vs. obtido
- Ambiente (SO, versão do Python)
- Logs/prints relevantes