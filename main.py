import tkinter as tk
from funcoes import adicionar_item, remover_item, apagar_lista

# Inicializando a janela principal
janela = tk.Tk()
janela.title("Gerenciador Simples de Lista")
janela.geometry("400x450")
janela.config(bg="lightblue")  # Definir a cor de fundo da janela

# Layout da interface

# Adicionando um Canvas para a barra horizontal
canvas = tk.Canvas(janela, width=400, height=30, bg="green", highlightthickness=0)
canvas.pack()


titulo = tk.Label(janela, text="Gerenciador Simples de Lista", font=("Helvetica", 16), bg="lightblue")
titulo.place(relx=0.5, y=15, anchor="center")  # Centraliza o texto na janela

frame = tk.Frame(janela, bg="lightblue")
frame.pack(pady=10)

lbl_item = tk.Label(frame, text="Item/Índice:", bg="lightblue")
lbl_item.grid(row=0, column=0, padx=5, pady=5)

entrada_item = tk.Entry(frame, width=20)
entrada_item.grid(row=0, column=1, padx=5, pady=5)

# Botões principais
frame_botoes = tk.Frame(janela, bg="lightblue")
frame_botoes.pack(pady=10)

btn_adicionar = tk.Button(frame_botoes, text="Adicionar", width=12, command=lambda: adicionar_item(entrada_item, lista_itens))
btn_adicionar.grid(row=0, column=0, padx=5, pady=5)

btn_remover = tk.Button(frame_botoes, text="Remover por Índice", width=18, command=lambda: remover_item(entrada_item, lista_itens))
btn_remover.grid(row=0, column=1, padx=5, pady=5)

btn_apagar = tk.Button(frame_botoes, text="Apagar Lista", width=12, command=lambda: apagar_lista(lista_itens))
btn_apagar.grid(row=0, column=2, padx=5, pady=5)

# Exibição da lista
lbl_lista = tk.Label(janela, text="Itens na Lista:", bg="lightblue")
lbl_lista.pack(pady=5)

lista_itens = tk.Listbox(janela, width=50, height=15)
lista_itens.pack(pady=10)

btn_sair = tk.Button(janela, text="Sair", width=10, command=janela.quit)
btn_sair.pack(pady=10)

# Definindo atalhos de teclado
janela.bind('<Control-a>', lambda event: adicionar_item(entrada_item, lista_itens))  # Ctrl + A para adicionar
janela.bind('<Control-x>', lambda event: remover_item(entrada_item, lista_itens))  # Ctrl + X para remover

# Iniciando o loop da interface
janela.mainloop()
