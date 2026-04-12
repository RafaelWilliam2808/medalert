# MedAlert - Controle de Medicamentos para Idosos

![Build Status](https://github.com/RafaelWilliam2808/medalert/actions/workflows/ci.yml/badge.svg)

## 🎯 O Problema
Muitos idosos e seus cuidadores enfrentam dificuldades em organizar e lembrar os horários corretos para a administração de medicamentos. O esquecimento ou a dosagem incorreta pode levar a sérios problemas de saúde, internações evitáveis e perda de qualidade de vida.

## 💡 A Solução
O **MedAlert** é uma aplicação de Interface de Linha de Comando (CLI) simples e direta, desenvolvida para ajudar idosos e cuidadores a registrar e consultar os medicamentos que precisam ser tomados ao longo do dia. A aplicação permite cadastrar o nome do remédio, a dosagem e o horário, além de listar e remover medicamentos já concluídos ou suspensos.

## 👥 Público-Alvo
- Idosos que gerenciam sua própria medicação e têm familiaridade básica com computadores.
- Cuidadores familiares ou profissionais que precisam de um registro rápido e confiável.

## ✨ Funcionalidades Principais
- **Adicionar Medicamento**: Registra nome, dosagem e horário (formato HH:MM).
- **Listar Medicamentos**: Exibe todos os medicamentos cadastrados de forma clara.
- **Remover Medicamento**: Permite excluir um medicamento pelo seu ID.

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.8+
- **Armazenamento**: Arquivo local JSON (`medicamentos.json`)
- **Testes**: `pytest`
- **Linting/Análise Estática**: `ruff`
- **CI/CD**: GitHub Actions

## 🚀 Instruções de Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/RafaelWilliam2808/medalert.git
   cd medalert
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -e .
   ```

## 💻 Instruções de Execução

Para iniciar a aplicação, execute o arquivo principal:
```bash
python src/main.py
```

Siga as instruções no menu interativo na tela.

## 🧪 Instruções para Rodar os Testes

A aplicação possui testes automatizados para garantir o funcionamento correto das regras de negócio. Para executá-los:
```bash
pytest tests/
```

## 🧹 Instruções para Rodar o Lint

Para verificar a qualidade e padronização do código usando o Ruff:
```bash
ruff check src/ tests/
```

## 📦 Versão Atual
**1.0.0** (Versionamento Semântico MAJOR.MINOR.PATCH)

## ✍️ Autor
**Rafael William Dantas Quintiliano**

## 🔗 Link do Repositório Público
[https://github.com/RafaelWilliam2808/medalert](https://github.com/RafaelWilliam2808/medalert)
