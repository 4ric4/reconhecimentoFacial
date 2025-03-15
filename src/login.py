import time
import cv2
import pyautogui
from reconhecimento import carregar_rosto_autorizado, verificar_rosto
import os
from dotenv import load_dotenv

load_dotenv()

ROSTO_AUTORIZADO = os.getenv("ROSTO_AUTORIZADO")
SENHA_WINDOWS = os.getenv("SENHA_WINDOWS")

def iniciar_webcam():
    """Inicia a captura da webcam."""
    return cv2.VideoCapture(0)

def realizar_login():
    """Simula o login no Windows após o reconhecimento do rosto, incluindo digitação da senha, se necessário."""
    print("Rosto autorizado detectado! Realizando o login...")

    # Caso o Windows esteja pedindo senha, você pode digitar a senha.
    if SENHA_WINDOWS:
        pyautogui.write(SENHA_WINDOWS)
        pyautogui.press("enter")
    else:
        # Se não houver necessidade de senha, apenas pressionar Enter
        pyautogui.press("enter")
    
    time.sleep(2)  # Aguarda para garantir que o login foi feito.
    print("Login realizado com sucesso.")

def main():
    try:
        encoding_autorizado = carregar_rosto_autorizado(ROSTO_AUTORIZADO)
        video_capture = iniciar_webcam()

        while True:
            ret, frame = video_capture.read()
            if not ret:
                print("Erro ao capturar frame.")
                break

            if verificar_rosto(frame, encoding_autorizado):
                print("Rosto autorizado detectado.")
                realizar_login()
                break  # Após o login, sai do loop.

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
        print("Monitoramento encerrado")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
