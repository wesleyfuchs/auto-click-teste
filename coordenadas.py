import pyautogui
import pyperclip

def main():
    print("Clique na tela para obter as coordenadas (Pressione Ctrl+C para sair).")
    
    try:
        while True:
            x, y = pyautogui.position()
            coordinates = f"Coordenadas (x, y): {x}, {y}"
            pyperclip.copy(coordinates)
            print(coordinates)
            pyautogui.sleep(1)  # Atualiza a cada 1 segundo
    except KeyboardInterrupt:
        print("Programa encerrado.")

if __name__ == "__main__":
    main()
