import pyautogui
import time

# Função para esperar até que um elemento esteja visível na tela ou até que um tempo limite seja atingido
def wait_until_visible(image, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if pyautogui.locateOnScreen(image) is not None:
            return True
        time.sleep(0.5)  # Espera um curto período antes de verificar novamente
    return False

# Função para esperar até que um elemento não esteja mais visível na tela ou até que um tempo limite seja atingido
def wait_until_not_visible(image, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if pyautogui.locateOnScreen(image) is None:
            return True
        time.sleep(0.5)  # Espera um curto período antes de verificar novamente
    return False

# Exemplo de uso
if wait_until_visible('elemento.png', timeout=10):
    # Faz algo quando o elemento está visível
    print("Elemento encontrado!")
else:
    # Lida com o caso em que o elemento não é encontrado dentro do tempo limite
    print("Elemento não encontrado dentro do tempo limite.")

# Você pode ajustar o tempo limite de acordo com suas necessidades e o tempo de espera será adaptativo
