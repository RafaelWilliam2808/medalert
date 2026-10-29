# 💊 MedAlert

[![CI](https://github.com/RafaelWilliam2808/medalert/actions/workflows/ci.yml/badge.svg)](https://github.com/RafaelWilliam2808/medalert/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-3776AB?logo=python&logoColor=white)
![Ruff](https://img.shields.io/badge/lint-Ruff-D7FF64?logo=ruff&logoColor=black)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)

Aplicação de linha de comando para **idosos e cuidadores** registrarem e consultarem os medicamentos do dia: nome, dosagem e horário.

## 🎯 O problema

Esquecer um remédio ou tomar a dose errada pode causar internações evitáveis e perda de qualidade de vida. Para quem toma vários medicamentos por dia, ou cuida de alguém que toma, manter tudo organizado não é simples.

## 💡 A solução

O MedAlert oferece um menu simples para:

- **Adicionar** um medicamento com nome, dosagem e horário (`HH:MM`, validado)
- **Listar** todos os medicamentos cadastrados
- **Remover** um medicamento concluído ou suspenso

Os dados ficam salvos em um arquivo JSON local e não se perdem ao fechar o programa.

## 🖥️ Exemplo de uso

```text
=== MedAlert: Controle de Medicamentos para Idosos ===
1. Adicionar Medicamento
2. Listar Medicamentos
3. Remover Medicamento
4. Sair
======================================================
Escolha uma opção: 2

--- Lista de Medicamentos ---
[1] Losartana - 1 comprimido (50 mg) às 08:00
[2] Metformina - 1 comprimido (500 mg) às 20:00
-----------------------------
```

## 🛠️ Tecnologias e práticas

| Área | Ferramenta |
|---|---|
| Linguagem | Python 3.10+ |
| Persistência | Arquivo JSON local |
| Testes | pytest (10 testes, incluindo casos de erro) |
| Lint e formatação | Ruff |
| Integração contínua | GitHub Actions, rodando em Python 3.10, 3.11 e 3.12 a cada push |
| Versionamento | Versionamento semântico (veja o [CHANGELOG](CHANGELOG.md)) |

## 📁 Estrutura

```text
medalert/
├── src/
│   └── main.py          # Regras de negócio e menu interativo
├── tests/
│   └── test_main.py     # Testes automatizados
├── .github/workflows/
│   └── ci.yml           # Pipeline de lint e testes
└── pyproject.toml       # Dependências e configuração do Ruff e do pytest
```

## 🚀 Como rodar

```bash
git clone https://github.com/RafaelWilliam2808/medalert.git
cd medalert

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -e ".[dev]"
python src/main.py
```

## 🧪 Testes e lint

```bash
pytest -v                        # testes
ruff check src/ tests/           # lint
ruff format --check src/ tests/  # formatação
```

## 🗺️ Próximos passos

- [ ] API REST para os medicamentos
- [ ] Interface web responsiva, pensada para uso por idosos
- [ ] Banco de dados no lugar do arquivo JSON
- [ ] Lembretes no horário de cada medicamento

## 👤 Autor

**Rafael William Dantas Quintiliano**, estudante de Engenharia de Software no CEUB

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-william-5190b33a8/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/RafaelWilliam2808)

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE).
