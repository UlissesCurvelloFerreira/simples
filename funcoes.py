import tkinter as tk
from tkinter import messagebox

# Lista compartilhada
lista = []

def adicionar_item(entrada_item, lista_itens):
    """Adiciona um item à lista."""
    item = entrada_item.get()
    if item:
        lista.append(item)
        atualizar_lista(lista_itens)
        entrada_item.delete(0, tk.END)
        messagebox.showinfo("Sucesso", f"'{item}' adicionado à lista.")
    else:
        messagebox.showwarning("Aviso", "Digite um item válido.")

def remover_item(entrada_item, lista_itens):
    """Remove um item da lista pelo índice."""
    indice = entrada_item.get()
    try:
        indice = int(indice)
        if 1 <= indice <= len(lista):
            item = lista.pop(indice - 1)
            atualizar_lista(lista_itens)
            entrada_item.delete(0, tk.END)
            messagebox.showinfo("Sucesso", f"'{item}' removido da lista.")
        else:
            messagebox.showerror("Erro", "Índice fora do intervalo.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido como índice.")

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
