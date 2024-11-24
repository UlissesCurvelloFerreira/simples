import funcoes

def main():
    lista = []
    while True:
        funcoes.exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcoes.adicionar_item(lista)
        elif opcao == "2":
            funcoes.remover_item(lista)
        elif opcao == "3":
            funcoes.apagar_lista(lista)
        elif opcao == "4":
            funcoes.mostrar_lista(lista)
        elif opcao == "5":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
