import tkinter as tk
import pyautogui
import time

"""
Nome do Programa: [Automatização Sefaz-PI]
Autor: [Wesley Fuchs]
Data de Criação: [30/10/2023]

Este programa foi criado para automatizar as solicitações de exportação de documentos no Sefaz PI

Instruções de Uso: Ao clicar começar, você tera 10s para clicar em 'Agendar Exportação',
assim a tela ficara no local correto para que o codigo funcione sem problemas
- 

Histórico de Versões:
- [Versão 1.0 (31/10/2023): Automatiza as solicitações de exportação de documentos de entrada (NFC-e)]
- [Versão 2.0 (03/11/2023): Automatiza as solicitações de exportação de documentos de entrada (NF-e)]
- [Versão 2.5 (28/01/2024): Adiciona arquivo datas.txt para adicionar datas]
- [Versão 3.0 (31/03/2024): Remove tempo de espera entre ações]

"""

def ler_datas_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            lines = file.readlines()
            date_sets = [tuple(line.strip().split(',')) for line in lines]
            return date_sets
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []
    

def automatizar_NFCe():  
    """Para cada set de datas em 'date_set' > Por meio de tabs ira chegar no campo de data 'Data Inicial' > digitar a data >
    tab para ir ao proximo campo 'Data Final' > digitar a data > tab para ir ao botão 'Agendar Exportação' > barra_de_espaço 
    para pressionar o botão > ira aguardar 3s para a proxima iteração do loop"""  

    # Tempo para o usuario clicar no lugar certo
    time.sleep(10)

    for data in date_sets:
        # time.sleep(3)

        # 11 tabs para checkbox 'Data inicial'
        for _ in range(11):
            pyautogui.press('tab')
    
        # Escrever a 'Data Inicial'
        pyautogui.write(data[0])
        # time.sleep(1)
        
        # Selecionar o campo 'Data Final'
        pyautogui.press('tab')
        # time.sleep(1)

        # Escrever a 'Data Final'
        pyautogui.write(data[1])
        # time.sleep(1)

        # Selecionar o botão 'Agendar Exportacao'
        pyautogui.press('tab')
        # time.sleep(1)

        # Pressionar o botão'
        pyautogui.press('space')
        time.sleep(3)

    status_label.config(text="Ação concluída!")


def automatizar_NFe():
    """Para cada set de datas em 'date_set' > Por meio de tabs e right_arrow 
    ira chegar na caixa 'Solicitar Emitente' > 
    tab e right_arrow para chegar na caixa 'Tipo de nota: Saida' > 
    tab para o campo 'Data Inicial' > tab para o campo 'Data Final' > 
    tab para ir ao botão 'Agendar Exportação' > barra_de_espaço 
    para pressionar o botão > ira aguardar para a proxima iteração do loop"""

    # Tempo para o usuario clicar no lugar certo
    time.sleep(10)

    for data in date_sets:
        # time.sleep(3)

        # 6 tabs para 'Tipos de Consulta'
        for _ in range(6):
            pyautogui.press('tab')
        # time.sleep(1)

        # Selecionar checkbox 'Contribuente como Emitente'
        pyautogui.press('right')
        # time.sleep(2)

        # 3 tabs para 'Tipo de nota:'
        for _ in range(3):
            pyautogui.press('tab')

        # Selecionar checkbox 'Saida'
        for _ in range(2):
            pyautogui.press('right')

        # 3 tabs para o campo de 'Data Inicial'
        for _ in range(3):
            pyautogui.press('tab')

        # Escrever a 'Data Inicial'
        pyautogui.write(data[0])
        
        # Selecionar o campo 'Data Final'
        pyautogui.press('tab')

        # Escrever a 'Data Final'
        pyautogui.write(data[1])
        # time.sleep(1)

        # Selecionar o botão 'Agendar Exportacao'
        pyautogui.press('tab')
        # time.sleep(1)

        # Pressionar o botão
        pyautogui.press('space')
        time.sleep(3)

    status_label.config(text="Ação concluída!")

# Configurações da janela do tkinter
window = tk.Tk()
window.title("Automatização Sefaz-PI")
window.geometry("300x150")

# Alteração para ler as datas do arquivo
date_sets = ler_datas_do_arquivo("assets/datas.txt")

nfce_button = tk.Button(window, text="Start NFC-e", command=automatizar_NFCe)
nfe_button = tk.Button(window, text="Start NF-e", command=automatizar_NFe)
status_label = tk.Label(window, text="")

nfce_button.pack(fill="both", pady=15, padx=40)
nfce_button.configure(border=2)
nfe_button.pack(fill="both", pady=15, padx=40)
nfe_button.configure(border=2)
status_label.pack()

window.mainloop()
