import cv2 as cv
import numpy as np
#Detectar caracteres en imágenes
import pytesseract 

directorio = "192.168.1.11:4747/video"
droid_cam = f"http://{directorio}"

video = cv.VideoCapture(droid_cam)

"""
Ver el siguiente link y tratar de comprenderlo
https://programarfacil.com/blog/vision-artificial/deteccion-de-movimiento-con-opencv-python/
"""

i = 0   

"""
PRIMER PASO: CAPTURAR OBJETO
"""

#Parámetros del rectángulo
start_point = (130,150) #Cordenada inicial que representa la parte inferior izquierda del rectángulo
end_point = (500,300) #Coordenada final que representa la parte superior derecha del rectánculo
color = (255,0,0) #Color del borde
tamanio_linea = 1 #grosor de la linea, se mide en pixeles. Si es 1, significa que es 1px.


#Parámetros del texto
contenido = "." #Texto que desea ser visto - La usaremos para colocar la placa
org = (150,110) #Las coordenas que representan la zona superior izquierda en donde será visible el texto
fuente = cv.FONT_HERSHEY_COMPLEX #el tipo de fuente que vamos a usar
escala_fuente = 1 #Escala o tamaño de la fuente
color_texto = (255,255,255) #Color del texto en BGR
grosor = 2 #grosor de la letra o en inglés conocido como = thickness, se mide en pixeles 2 = 2px

while True:
        try:
            # Lectura de la cámara
            ret, frame = video.read()
            #cv.imshow('CAMARA DROIDCAM', frame)
            
            if ret == False:
                break
            else:
                #Extraemos con librería numpy la altura, ancho
                alto, ancho, c = frame.shape
                
                #coordenadas X
                x1 = int(ancho / 3)
                x2 = int(x1 * 2)

                #coordenadas Y
                y1 = int (alto / 3)
                y2 = int(y1 * 2)
                
                #Ubicamos el rectánculo en la zona específica 
                
                #Agregamos texto
                frame = cv.putText(frame,contenido,org,fuente,escala_fuente,color,grosor)
                
                frame = cv.rectangle(frame,(x1,y1),(x2,y2),color,grosor)
                
                #Pasamos Imágen a escala de grises
                frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                
                #Suavisamos el filtro ya que los pixeles cambian muy rápido
                frame_gray = cv.GaussianBlur(frame_gray,(1,1),0,0)
                
                _, frame_gray = cv.threshold(frame_gray,127,255,cv.THRESH_BINARY)
                
                #buscamos los contornos con los parametros = De la función findcontours = devuelve 2 valores, hierarchy1 y el contorno
                """"
                img = la imagen o video que queremos que encuentre los contornos
                mode = es el modo de recuperación del contorno = usaremos para este ejemplo el de recuperar todos los contornos = cv.RETR_TREE
                method = método de aproximación de contorno, hay 2 formas = CHAIN_APPROX_SIMPLE y CHAIN_APPROX_NONE = usaremos el none que encuentra todos los puntos del contorno, CHAIN APROX_SIMPLE = Encuentra solo los elementos de las puntas
                """
                contorno, _ = cv.findContours(frame_gray, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
                
                #Parametros
                """
                frame = significa en donde queremos dibujar todo los contornos
                contorno = es el valor devuelto de los contornos encontrados
                -1 = con esto nos dibuja los contornos 
                (0,255,0) = es el color verde en forma bgr
                0 = grosor de la línea
                """
                frame = cv.drawContours(frame, contorno, -1, (0,255,0), 3)
                cv.imshow('imagen',frame)
                
                
                if cv.waitKey(1) & 0xFF == ord('c'):
                    print("Sales del programa")
                    #Guarda una captura de lo último que ve antes de salir del programa
                    ruta_imagen = f"img/imagen{i+1}.jpg"
                    break
        except KeyboardInterrupt:
            print("sales del programa por fuerza mayor, presionaste CTRL + C")
            ruta_imagen = f"img/imagen_{i+1}.jpg"
            imagen = cv.imwrite(ruta_imagen,frame)
            break

#Escribo la imágen luego de salir del programa
#imagen = cv.imwrite(ruta_imagen,frame)
#Leo la imagen 
#imagen = cv.imread(ruta_imagen,frame)

#imagen = cv.rectangle(imagen,start_point,end_point,color,tamanio_linea)


# Texto - este texto lo usaremos para mostrar en pantalla el texto que vamos a extraer # Los parámetros están arriba.
#Contenido[0:7] = colocamos esto porque como un string en python se lee como lista, queremos es que solo lea los caracteres de la placa, en tontal son solo 7
#texto = cv.putText(imagen,contenido[0:7],org,fuente,escala_fuente,color_texto,grosor)


# Asignar espacio importante de lectura
""""
En esta zona lo que haremos será a un cuarto de la pantalla le vamos a asignar un espacio importante que será en donde vaya a leer la información

1. Extraer alto y ancho de los fotogramas
"""




#Ubicamos el rectángulo dibujado en la zona en donde nos va a leer la placa
#texto_nuevo = cv.rectangle(texto,(x1,y1),(x2,y2),color_texto,2)

#recortar = texto_nuevo[y1:y2,x1:x2]

#Muestro el recorte con el rectángulo dibujado
#cv.imshow("imagen",texto_nuevo)
#cv.imshow("recorte",recortar)


cv.waitKey(1)
video.release() #Cerramos video
cv.destroyAllWindows()

"""
https://www.youtube.com/watch?v=0-tVTxBRgbY
"""