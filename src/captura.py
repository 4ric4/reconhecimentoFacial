import cv2
import time
import os


def iniciar_webcam():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise Exception("Erro ao acessar a webcam.")
    return video_capture

def gravar_video(video_capture, video_filename="alerta.mp4", duracao=3):
    print("Rosto não autorizado detectado Gravando vídeo...")

    video_filename = os.path.join('videos', video_filename)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_filename, fourcc, 20.0, (640, 480))

    start_time = time.time()
    while time.time() - start_time < duracao:
        ret, frame = video_capture.read()
        if not ret:
            print("Erro ao capturar vídeo.")
            break
        out.write(frame)

    out.release()
    print("Vídeo salvo")
    return video_filename
