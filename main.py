import cv2 as cv
import numpy as np

directorio = "192.168.1.11:4747/video"
droid_cam = f"http://{directorio}"

video = cv.VideoCapture(droid_cam)

"""
Ver el siguiente link y tratar de comprenderlo
https://programarfacil.com/blog/vision-artificial/deteccion-de-movimiento-con-opencv-python/
"""

i = 0   

#Sacamos una captura a la imagen en cada momento para poder leer el contorno, lo guardamos en la carpeta img
#imagen = f"img/imagen_{i+1}.jpg"

"""
PRIMER PASO: CAPTURAR OBJETO
"""

while True:
        try:
            ret, frame = video.read()
            cv.imshow('CAMARA DROIDCAM', frame)
            if ret == True:
                if cv.waitKey(0) & 0xFF == ord('c'):
                    print("Sales del programa")
                    break 
            else:
                print('Video no disponible')
                break
        except KeyboardInterrupt:
            print("sales del programa por fuerza mayor, presionaste CTRL + C")
            ruta_imagen = f"img/imagen_{i+1}.jpg"
            imagen = cv.imwrite(ruta_imagen,frame)
            break

ruta_imagen = f"img/imagen_{i+1}.jpg"
imagen = cv.imread(ruta_imagen,frame)
cv.imshow('Objeto Escala de gris', imagen)

# Leemos imágen para después recortarla
#img_recortada = imagen[160:300,230:380]
#cv.imwrite('imagen recortada',img_recortada)


#gris = cv.cvtColor(imagen,cv.COLOR_BGR2GRAY) # Pasamos la imágen a escala de grises
#cv.imshow('escala de gris',gris)
cv.waitKey(0)
video.release() #Cerramos video
cv.destroyAllWindows()


