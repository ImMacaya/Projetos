# User Registry (Python) — SQLite + Typer + Rich

[![CI](https://github.com/ImMacaya/User-Registry-Py/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ImMacaya/User-Registry-Py/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Ruff](https://img.shields.io/badge/Ruff-lint%20%26%20format-261230)
![SQLite](https://img.shields.io/badge/SQLite-embedded-003B57)
![CLI](https://img.shields.io/badge/CLI-Typer%20%2B%20Rich-8A2BE2)

Sistema de cadastro de usuários via terminal, com persistência em SQLite, arquitetura em camadas e segurança básica de senha.

> Projeto estruturado com `src/` layout e instalação em modo editável para facilitar desenvolvimento e testes.

---

## ✨ Features
- CRUD de usuários (create, list, show, update, activate/deactivate)
- Login (MVP): valida e retorna OK/erro
- Senha com hash + salt (PBKDF2)
- CLI bonito com Rich (tabelas e painéis)
- Testes com Pytest
- Arquitetura replicável em C++

---

## 🧱 Estrutura do projeto

```text
src/user_registry/     # código fonte do pacote
tests/                # testes
.data/                # banco SQLite local (ignorado pelo git)
pyproject.toml        # config do projeto + dependências

---

## 🚀 Instalação (modo desenvolvimento)

```bash
python -m venv .venv
# ative o ambiente...
python -m pip install -e ".[dev]"

---

```md
## 🧪 Testes
```bash
pytest