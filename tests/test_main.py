import os
import pytest
from src.main import adicionar_medicamento, listar_medicamentos, remover_medicamento, DATA_FILE

@pytest.fixture(autouse=True)
def setup_teardown():
    # Limpar o arquivo de dados antes de cada teste
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    yield
    # Limpar após o teste
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_adicionar_medicamento_sucesso():
    med = adicionar_medicamento("Aspirina", "1 comprimido", "08:00")
    assert med["nome"] == "Aspirina"
    assert med["dosagem"] == "1 comprimido"
    assert med["horario"] == "08:00"
    
    dados = listar_medicamentos()
    assert len(dados) == 1
    assert dados[0]["nome"] == "Aspirina"

def test_adicionar_medicamento_horario_invalido():
    with pytest.raises(ValueError, match="Horário inválido"):
        adicionar_medicamento("Aspirina", "1 comprimido", "25:00")

def test_adicionar_medicamento_campos_vazios():
    with pytest.raises(ValueError, match="Todos os campos são obrigatórios"):
        adicionar_medicamento("", "1 comprimido", "08:00")

def test_remover_medicamento_sucesso():
    med = adicionar_medicamento("Aspirina", "1 comprimido", "08:00")
    assert len(listar_medicamentos()) == 1
    
    remover_medicamento(med["id"])
    assert len(listar_medicamentos()) == 0

def test_remover_medicamento_inexistente():
    with pytest.raises(ValueError, match="Medicamento não encontrado"):
        remover_medicamento(999)
