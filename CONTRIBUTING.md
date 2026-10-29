# Como Contribuir

Obrigado por seu interesse em contribuir com o MedAlert!

## Fluxo de Trabalho

1. Faça um *fork* do repositório.
2. Crie uma *branch* para sua funcionalidade: `git checkout -b feature/minha-funcionalidade`.
3. Implemente as alterações e adicione testes quando necessário.
4. Certifique-se de que o lint e os testes passam: `ruff check src/ tests/`, `ruff format --check src/ tests/` e `pytest`.
5. Faça o *commit* das suas alterações: `git commit -m "feat: descrição da funcionalidade"`.
6. Envie para o seu *fork*: `git push origin feature/minha-funcionalidade`.
7. Abra um *Pull Request* para a branch `main` deste repositório.

## Padrões de Código

Este projeto usa o `ruff` para linting. Certifique-se de que não há erros antes de enviar seu PR.
