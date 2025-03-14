import face_recognition
import os
import cv2

def carregar_rosto_autorizado(caminho_imagem):
    if not caminho_imagem or not os.path.exists(caminho_imagem):
        raise FileNotFoundError("Erro: Arquivo de rosto autorizado não encontrado.")

    imagem_conhecida = face_recognition.load_image_file(caminho_imagem)
    encodings = face_recognition.face_encodings(imagem_conhecida)

    if len(encodings) == 0:
        raise ValueError("Nenhum rosto encontrado na imagem autorizada.")

    return encodings[0]

def verificar_rosto(frame, encoding_autorizado):
    """Verifica se o rosto detectado é autorizado ou não."""
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    face_locations = face_recognition.face_locations(rgb_frame)
    
    if not face_locations:
        print("Nenhum rosto detectado.")
        return False

    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    if not face_encodings:
        print("Nenhuma codificação de rosto detectada.")
        return False

    for encoding in face_encodings:
        match = face_recognition.compare_faces([encoding_autorizado], encoding)
        if match[0]:
            return True 
    return False 
