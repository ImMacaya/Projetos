# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.

O formato é inspirado em *Keep a Changelog* e o versionamento segue *Semantic Versioning*.

---

## [0.1.0] - 2026-04-04
### Added
- Estrutura de projeto com `src/` layout e empacotamento via `pyproject.toml`
- CLI com **Typer + Rich** (help, prompts, tabelas e painéis)
- Persistência em **SQLite** com inicialização automática via `schema.sql`
- Camadas do projeto: `domain`, `security`, `repository`, `service`, `presentation`
- Hash de senha com **PBKDF2 + salt** e verificação segura
- Comandos do CLI:
  - `create`, `list`, `show`, `update`, `activate`, `deactivate`, `login` (MVP)
- Testes com **Pytest** (validações e segurança)
- Qualidade de código com **Ruff** (lint e format)
- CI com **GitHub Actions** (ruff + pytest) em Python 3.10/3.11/3.12
- Documentação inicial no README com instruções e screenshots

### Changed
- Padronização do fluxo de instalação para `pip install -e ".[dev]"` (desenvolvimento)

### Fixed
- Correções de importação relacionadas ao `src/` layout
- Correções de tipagem/contratos e ajustes para atender ao Ruff
