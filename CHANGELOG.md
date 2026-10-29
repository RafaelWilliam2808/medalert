# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.1.0] - 2026-10-29

### Alterado
- Validação de horário reescrita sem `datetime`, aceitando apenas `HH:MM` entre 00:00 e 23:59.
- Dependências de desenvolvimento (pytest e Ruff) movidas para o grupo opcional `dev`.
- Regras do Ruff definidas no `pyproject.toml`, com formatação verificada no CI.
- CI atualizado para `actions/checkout@v4` e `actions/setup-python@v5`, rodando em Python 3.10, 3.11 e 3.12.
- README reorganizado, com exemplo de uso e próximos passos.

### Adicionado
- Testes parametrizados para horários inválidos (10 testes no total).

## [1.0.0] - 2025-04-12

### Adicionado
- Interface CLI com menu interativo.
- Funcionalidade de adicionar medicamentos com nome, dosagem e horário.
- Funcionalidade de listar todos os medicamentos cadastrados.
- Funcionalidade de remover medicamentos pelo ID.
- Armazenamento persistente em arquivo JSON local.
- Validação de formato de horário (HH:MM).
- Validação de campos obrigatórios.
- Testes automatizados com pytest (5 casos de teste).
- Linting configurado com ruff.
- Pipeline de CI com GitHub Actions.
- README.md completo com instruções de instalação e uso.
