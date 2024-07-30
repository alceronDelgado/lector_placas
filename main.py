#import cv2 as cv
import numpy as np
#Reconocimiento único de caracteres
import pytesseract
#TODO: Hacer archivo ejecutable
from setuptools import setup
from package.functions import menu
from package.functions import video_recording

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lalej\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def ejecutar():
    video_recording(menu())


ejecutar()

#while True:
#    try:
#        # Lectura de la cámara
#        ret, frame = video.read()
#        if ret == False: break
#        else:
#
#            #Pasamos Imágen a escala de grises
#            frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#
#            #Suavisamos el filtro ya que los pixeles cambian muy rápido
#            frame_gray = cv.GaussianBlur(frame_gray,(1,1),0,0)
#
#            _, frame_gray = cv.threshold(frame_gray,155,255,cv.THRESH_BINARY)
#            
#            contorno, _ = cv.findContours(frame_gray, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#            
#            advertencia = "presiona 'c' para cerrar"
#            frame = cv.putText(frame,advertencia,(10,450),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
#            for c in contorno:
#                #c es el numpy array de los puntos de todo el contorno
#                area = cv.contourArea(c)
#                (x,y,w,h) = cv.boundingRect(c)
#                cuadrado = 0.09 * cv.arcLength(c, True)
#                aproximado = cv.approxPolyDP(c, cuadrado, True)
#                if len(aproximado)== 4 and area > 8000:
#                    aspect_radio = float(300.6)/151.2
#                    if aspect_radio > 1.8: 
#                        frame = cv.drawContours(frame,[c],0,(0,255,0),3,cv.LINE_AA)
#                        placa_figura = frame_gray[y:y + h, x:x + w]
#                        texto = pytesseract.image_to_string(placa_figura,config='--psm 1')
#                        if len(texto) >= 7 and len(texto) <= 10:
#                            print("texto placa ",texto)
#                            frame = cv.putText(frame,texto,(140,70),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,0),3)
#                            f = open('lector_placas.txt','a')
#                            f.write('\n' + texto)
#                            f.close()
#            cv.imshow('imagen',frame)
#            if cv.waitKey(1) & 0xFF == ord('c'):
#                print("Sales del programa")
#                break
#    except KeyboardInterrupt:
#        print("sales del programa por fuerza mayor, presionaste CTRL + C")
#        break

#cv.waitKey(1)
#video.release() #Cerramos video
#cv.destroyAllWindows()
#print("precione enter para cerrar el programa")
#input()
#f.open = ('lector_placas.txt','r')
#f.close()


#if __name__ == '__main__':
#    main()