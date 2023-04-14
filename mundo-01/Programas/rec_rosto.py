import cv2
import mediapipe as mp
webCam=cv2.VideoCapture(0)
solucao_reconhecimento_rosto= mp.solutions.face_detection
reconhecedor_rostos=solucao_reconhecimento_rosto.FaceDetection()
desenho=mp.solutions.drawing_utils

while True:
    verificador,frame=webCam.read()
    if not verificador:
        break

    listas_rostos = reconhecedor_rostos.process(frame)
    if listas_rostos.detections:
        for rosto in listas_rostos.detections:
            desenho.draw_detection(frame,rosto)
    cv2.imshow("App web",frame)
    if cv2.waitKey(5)==ord('d'):
        break
webCam.release()
cv2.destroyAllWindows()