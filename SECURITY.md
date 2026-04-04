# Security Policy

Obrigado por ajudar a manter este projeto seguro.

## Supported Versions

Este projeto está em desenvolvimento. A versão mais recente no branch `main` é a única considerada para correções de segurança.

## Reporting a Vulnerability

Se você encontrar uma vulnerabilidade (ex.: exposição de dados, bypass de autenticação, execução indevida), por favor:

1. **Não** abra uma issue pública com detalhes sensíveis.
2. Envie um reporte privado com:
   - Passo a passo para reproduzir
   - Impacto (o que pode acontecer)
   - Ambiente (SO, versão do Python)
   - Evidências (logs/prints, se possível)
3. Contato:
   - GitHub: abra uma **Discussion** com título “Security Report” (sem detalhes sensíveis) e solicite contato privado
   - Alternativa: abra uma issue pública **sem detalhes**, apenas informando que há uma falha e pedindo canal privado

## Disclosure

- Você receberá um retorno assim que possível.
- Após correção, podemos publicar uma nota no `CHANGELOG.md` descrevendo a correção de forma segura (sem exploração detalhada).

## Scope

Coberto por esta política:
- Armazenamento e verificação de senhas (PBKDF2 + salt)
- Persistência local (SQLite)
- CLI e validações de input

Fora de escopo:
- Vulnerabilidades de dependências externas já reportadas oficialmente (mas você pode sinalizar se quiser).