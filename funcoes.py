def exibir_menu():
    """Exibe o menu principal."""
    print("\n==== Gerenciador Simples ====")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Apagar lista")
    print("4. Mostrar lista")
    print("5. Sair")
    print("===================================")

def adicionar_item(lista):
    """Adiciona um item à lista."""
    item = input("Digite o item para adicionar: ")
    lista.append(item)
    print(f"'{item}' adicionado à lista.")


