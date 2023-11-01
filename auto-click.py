import tkinter as tk
import pyautogui
import time

# List of date sets to be typed
# date_sets = [("01/01/2023", "31/01/2023"), ("01;02;2023", "28;02;2023")]
# date_sets = [("01;01;2023", "31;01;2023")]
date_sets = [
    ("01/11/2023", "30/11/2023"),
    ("01/10/2023", "31/10/2023"),
    ("01/09/2023", "30/09/2023"),
    ("01/08/2023", "31/08/2023"),
    ("01/07/2023", "31/07/2023"),
    ("01/06/2023", "30/06/2023"),
    ("01/05/2023", "31/05/2023"),
    ("01/04/2023", "30/04/2023"),
    ("01/03/2023", "31/03/2023"),
    ("01/02/2023", "28/02/2023"),
    ("01/01/2023", "31/01/2023"),
    ("01/12/2022", "31/12/2022"),
    ("01/11/2022", "30/11/2022"),
    ("01/10/2022", "31/10/2022"),
    ("01/09/2022", "30/09/2022"),
    ("01/08/2022", "31/08/2022"),
    ("01/07/2022", "31/07/2022"),
    ("01/06/2022", "30/06/2022"),
    ("01/05/2022", "31/05/2022"),
    ("01/04/2022", "30/04/2022"),
    ("01/03/2022", "31/03/2022"),
    ("01/02/2022", "28/02/2022"),
    ("01/01/2022", "31/01/2022"),
    ("01/12/2021", "31/12/2021"),
    ("01/11/2021", "30/11/2021"),
    ("01/10/2021", "31/10/2021"),
    ("01/09/2021", "30/09/2021"),
    ("01/08/2021", "31/08/2021"),
    ("01/07/2021", "31/07/2021"),
    ("01/06/2021", "30/06/2021"),
    ("01/05/2021", "31/05/2021"),
    ("01/04/2021", "30/04/2021"),
    ("01/03/2021", "31/03/2021"),
    ("01/02/2021", "28/02/2021"),
    ("01/01/2021", "31/01/2021"),
    ("01/12/2020", "31/12/2020"),
    ("01/11/2020", "30/11/2020"),
    ("01/10/2020", "31/10/2020"),
    ("01/09/2020", "30/09/2020"),
    ("01/08/2020", "31/08/2020"),
    ("01/07/2020", "31/07/2020"),
    ("01/06/2020", "30/06/2020"),
    ("01/05/2020", "31/05/2020"),
    ("01/04/2020", "30/04/2020"),
    ("01/03/2020", "31/03/2020"),
    ("01/02/2020", "29/02/2020"),
    ("01/01/2020", "31/01/2020"),
    ("01/12/2019", "31/12/2019"),
    ("01/11/2019", "30/11/2019"),
    ("01/10/2019", "31/10/2019"),
    ("01/09/2019", "30/09/2019"),
    ("01/08/2019", "31/08/2019"),
    ("01/07/2019", "31/07/2019"),
    ("01/06/2019", "30/06/2019"),
    ("01/05/2019", "31/05/2019"),
    ("01/04/2019", "30/04/2019"),
    ("01/03/2019", "31/03/2019"),
    ("01/02/2019", "28/02/2019"),
    ("01/01/2019", "31/01/2019"),
    ("01/12/2018", "31/12/2018"),
    ("01/11/2018", "30/11/2018")
]
    

def move_click_and_type():    

    # Tempo para o usuario clicar no lugar certo
    time.sleep(10)

    for data in date_sets:
        time.sleep(3)

        # 11 tabs para checkbox 'Data inicial'
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
    
        # time.sleep(1)

        # Escrever a 'Data Inicial'
        pyautogui.typewrite(data[0], interval=0.1)
        # time.sleep(1)
        
        # Selecionar o campo 'Data Final'
        pyautogui.press('tab')
        # time.sleep(1)

        # Escrever a 'Data Final'
        pyautogui.typewrite(data[1], interval=0.1)
        # time.sleep(1)

        # Selecionar o botão 'Agendar Exportacao'
        pyautogui.press('tab')
        time.sleep(1)

        # Pressionar o botão'
        pyautogui.press('space')
        time.sleep(2)


    status_label.config(text="Ação concluída!")


window = tk.Tk()
window.title("Automatização de Cliques e Digitação")

start_button = tk.Button(window, text="Começar", command=move_click_and_type)
status_label = tk.Label(window, text="")

start_button.pack()
status_label.pack()

window.mainloop()
