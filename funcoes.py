import tkinter as tk
from tkinter import messagebox

# Lista compartilhada
lista = []

def adicionar_item(entrada_item, lista_itens):
    """Adiciona um ou mais itens à lista, separados por vírgula."""
    itens = entrada_item.get().split(",")  # Separar itens por vírgula
    if itens:
        for item in itens:
            item = item.strip()  # Remover espaços extras
            if item:  # Só adiciona itens não vazios
                lista.append(item)
        atualizar_lista(lista_itens)
        entrada_item.delete(0, tk.END)
        messagebox.showinfo("Sucesso", f"Itens adicionados à lista.")
    else:
        messagebox.showwarning("Aviso", "Digite um ou mais itens válidos.")

def remover_item(entrada_item, lista_itens):
    """Remove um ou mais itens da lista pelo índice."""
    indices = entrada_item.get().split(",")  # Separar os índices por vírgula
    try:
        # Converter os índices para inteiros e remover os itens
        indices = [int(indice.strip()) for indice in indices]
        indices.sort(reverse=True)  # Remover de trás para frente para evitar erros com índices alterados
        for indice in indices:
            if 1 <= indice <= len(lista):
                item = lista.pop(indice - 1)
                messagebox.showinfo("Sucesso", f"'{item}' removido da lista.")
            else:
                messagebox.showerror("Erro", f"Índice {indice} fora do intervalo.")
        atualizar_lista(lista_itens)
        entrada_item.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos como índices.")

def apagar_lista(lista_itens):
    """Apaga todos os itens da lista."""
    if lista:
        lista.clear()
        atualizar_lista(lista_itens)
        messagebox.showinfo("Sucesso", "Lista apagada.")
    else:
        messagebox.showwarning("Aviso", "A lista já está vazia.")

def atualizar_lista(lista_itens):
    """Atualiza a exibição da lista na interface."""
    lista_itens.delete(0, tk.END)
    for i, item in enumerate(lista, start=1):
        lista_itens.insert(tk.END, f"{i}. {item}")
