import json
import os

DATA_FILE = "medicamentos.json"


def carregar_dados():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_dados(dados):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def validar_horario(horario):
    """Valida um horário no formato HH:MM (00:00 a 23:59)."""
    partes = horario.split(":")
    formato_ok = len(partes) == 2 and all(p.isdigit() and len(p) == 2 for p in partes)
    if not formato_ok or not (0 <= int(partes[0]) <= 23 and 0 <= int(partes[1]) <= 59):
        raise ValueError("Horário inválido. Use o formato HH:MM.")


def adicionar_medicamento(nome, dosagem, horario):
    if not nome or not dosagem or not horario:
        raise ValueError("Todos os campos são obrigatórios.")

    validar_horario(horario)

    dados = carregar_dados()
    novo_id = 1 if not dados else max(m["id"] for m in dados) + 1

    novo_medicamento = {
        "id": novo_id,
        "nome": nome,
        "dosagem": dosagem,
        "horario": horario,
    }

    dados.append(novo_medicamento)
    salvar_dados(dados)
    return novo_medicamento


def listar_medicamentos():
    return carregar_dados()


def remover_medicamento(id_medicamento):
    dados = carregar_dados()
    dados_filtrados = [m for m in dados if m["id"] != id_medicamento]

    if len(dados) == len(dados_filtrados):
        raise ValueError("Medicamento não encontrado.")

    salvar_dados(dados_filtrados)
    return True


def exibir_menu():
    print("\n=== MedAlert: Controle de Medicamentos para Idosos ===")
    print("1. Adicionar Medicamento")
    print("2. Listar Medicamentos")
    print("3. Remover Medicamento")
    print("4. Sair")
    print("======================================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do medicamento: ")
            dosagem = input("Dosagem (ex: 1 comprimido): ")
            horario = input("Horário (HH:MM): ")
            try:
                adicionar_medicamento(nome, dosagem, horario)
                print("✅ Medicamento adicionado com sucesso!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif opcao == "2":
            medicamentos = listar_medicamentos()
            if not medicamentos:
                print("📭 Nenhum medicamento cadastrado.")
            else:
                print("\n--- Lista de Medicamentos ---")
                for m in medicamentos:
                    print(f"[{m['id']}] {m['nome']} - {m['dosagem']} às {m['horario']}")
                print("-----------------------------")

        elif opcao == "3":
            try:
                id_med = int(input("ID do medicamento a remover: "))
                remover_medicamento(id_med)
                print("✅ Medicamento removido com sucesso!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif opcao == "4":
            print("Saindo do MedAlert. Lembre-se de tomar seus remédios!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
