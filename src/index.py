import time
import cv2
from captura import iniciar_webcam, gravar_video
from reconhecimento import carregar_rosto_autorizado, verificar_rosto
from telegram import enviar_para_telegram
import os
from dotenv import load_dotenv

load_dotenv()

ROSTO_AUTORIZADO = os.getenv("ROSTO_AUTORIZADO")

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
            else:
                video_filename = gravar_video(video_capture)
                enviar_para_telegram(video_filename)
                time.sleep(120)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()
        print("Monitoramento encerrado")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
