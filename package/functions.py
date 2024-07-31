import cv2 as cv
#Reconocimiento único de caracteres
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lalej\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def menu():
    try:
        camara_opcion = input("Seleccione el tipo de la cámara siendo 1 valor por defecto de tu computadora o 0 usando dirección IP. \n")
        if camara_opcion == '1': 
            video = cv.VideoCapture(0)
            print('video capture definido como por defecto')
            print("*******************")
            return video
        elif camara_opcion == '0':
            print('video capture definido por IP \n')
            print("para usar esta opciónes debes instalar la aplicación DROID CAM en tu teléfono \n") 
            print("ve a la google play y busca la Aplicación DROIDCAM: instalala y ejecutala, cuando la ejecutes encontraras 2 formas de acceso: \n")
            print(", a tra ves de WIFI IP y IP CAM ACCESS,usaremos IP CAMACCESS: su estructura de dirección es más o menos la  siguiente: http://192.168.1.12:4747/video \n")
            directorio = input("digite la dirección IP \n")
            droid_cam = f"http://{directorio}"
            video = cv.VideoCapture(droid_cam)
            print("-------------------")
            return video
        return video
    except KeyboardInterrupt:
        print('No eliges opción')


def video_recording(video):
    while True:
        try:
            # Lectura de la cámara
            ret, frame = video.read()
            if ret == False: break
            else:

                #Pasamos Imágen a escala de grises
                frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

                #Suavisamos el filtro ya que los pixeles cambian muy rápido
                frame_gray = cv.GaussianBlur(frame_gray,(1,1),0,0)

                _, frame_gray = cv.threshold(frame_gray,155,255,cv.THRESH_BINARY)

                contorno, _ = cv.findContours(frame_gray, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

                advertencia = "presiona 'c' para cerrar"
                frame = cv.putText(frame,advertencia,(10,450),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
            for c in contorno:
                #c es el numpy array de los puntos de todo el contorno
                area = cv.contourArea(c)
                (x,y,w,h) = cv.boundingRect(c)
                cuadrado = 0.09 * cv.arcLength(c, True)
                aproximado = cv.approxPolyDP(c, cuadrado, True)
                if len(aproximado)== 4 and area > 8000:
                    aspect_radio = float(300.6)/151.2
                    if aspect_radio > 1.8: 
                        frame = cv.drawContours(frame,[c],0,(0,255,0),3,cv.LINE_AA)
                        placa_figura = frame_gray[y:y + h, x:x + w]
                        texto = pytesseract.image_to_string(placa_figura,config='--psm 1')
                        if len(texto) >= 7 and len(texto) <= 10:
                            print("texto placa ",texto)
                            frame = cv.putText(frame,texto,(140,70),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,0),3)
                            exportar_doc(texto)        
            cv.imshow('imagen',frame)
            if cv.waitKey(1) & 0xFF == ord('c'):
                cerrar_video(video)
                break
        except KeyboardInterrupt:
            print("sales del programa por fuerza mayor, presionaste CTRL + C")
            break

def exportar_doc(texto):
    print('texto placa',texto)
    f = open('lector_placas.txt','a')
    f.write('\n' + texto)
    f.close()


def cerrar_video(video):
    cv.waitKey(1)
    video.release() #Cerramos video
    cv.destroyAllWindows()
    print("precione enter para cerrar el programa")
    input()