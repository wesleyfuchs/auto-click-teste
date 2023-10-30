import tkinter as tk
import pyautogui
import time

# List of date sets to be typed
date_sets = [("01/01/2023", "31/01/2023"), ("01/02/2023", "28/02/2023"), ("01/03/2023", "31/03/2023")]

def move_click_and_type():
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())

        for date_set in date_sets:
            # Move the mouse and click at the first set of coordinates
            pyautogui.moveTo(x1, y1)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            # Move the mouse and click at the second set of coordinates
            pyautogui.moveTo(x2, y2)
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)

            # Type the first date
            pyautogui.typewrite(date_set[0], interval=0.1)

            # Simulate a Tab key press to move to the second field
            pyautogui.press('tab')
            time.sleep(1)

            # Type the second date
            pyautogui.typewrite(date_set[1], interval=0.1)

        status_label.config(text="Ação concluída!")
    except ValueError:
        status_label.config(text="Coordenadas inválidas. Use números inteiros.")

window = tk.Tk()
window.title("Automatização de Cliques e Digitação")

x1_label = tk.Label(window, text="Coordenada X 1:")
entry_x1 = tk.Entry(window)
y1_label = tk.Label(window, text="Coordenada Y 1:")
entry_y1 = tk.Entry(window)

x2_label = tk.Label(window, text="Coordenada X 2:")
entry_x2 = tk.Entry(window)
y2_label = tk.Label(window, text="Coordenada Y 2:")
entry_y2 = tk.Entry(window)

start_button = tk.Button(window, text="Começar", command=move_click_and_type)
status_label = tk.Label(window, text="")

x1_label.pack()
entry_x1.pack()
y1_label.pack()
entry_y1.pack()
x2_label.pack()
entry_x2.pack()
y2_label.pack()
entry_y2.pack()
start_button.pack()
status_label.pack()

window.mainloop()
