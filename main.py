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


#Sacamos una captura a la imagen en cada momento para poder leer el contorno, lo guardamos en la carpeta img
#imagen = f"img/imagen_{i+1}.jpg"

"""
PRIMER PASO: CAPTURAR OBJETO
"""


#Parámetros del triángulo
start_point = (130,150) #Cordenada inicial que representa la parte inferior izquierda del rectángulo
end_point = (500,300) #Coordenada final que representa la parte superior derecha del rectánculo
color = (255,0,0) #Color del borde
tamanio_linea = 1 #grosor de la linea, se mide en pixeles. Si es 1, significa que es 1px.


#Parámetros del texto
contenido = "texto" #Texto que desea ser visto - La usaremos para colocar la placa
org = (150,110) #Las coordenas que representan la zona superior izquierda en donde será visible el texto
fuente = cv.FONT_HERSHEY_COMPLEX #el tipo de fuente que vamos a usar
escala_fuente = 3 #Escala o tamaño de la fuente
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
                item = cv.rectangle(frame,start_point,end_point,color,1)
                
                #Agregamos texto
                texto_nuevo2 = cv.putText(item,contenido,org,fuente,escala_fuente,color,grosor)
                
                #Posicionamos el rectangulo en la posición requerida
                cv.rectangle(texto_nuevo2,(x1,y1),(x2,y2),(0,255,0),2)
                
                #Extraemos los pixeles que están en el rectángulo
                recorte = texto_nuevo2[y1:y2,x1:x2]
                
                #Extraemos los colores de la matriz roja, verde y azul 
                mb = np.matrix(recorte[:, :,0])
                mg = np.matrix(recorte[:, :,1])
                mr = np.matrix(recorte[:, :,2])
                
                #Extraemos el color amarillo = lo que hacemos aca es restar esos colores para que nos de amarillo = Resta entre matriz verde y azul
                Color = cv.absdiff(mg,mb)
                #
                ##Aplicamos umbral al color = HACEMOS QUE EL COLOR AMARILLO QUEDE EN BLANCO Y LOS OTROS COLORES EN NEGRO
                _ , umbral = cv.threshold(Color,40,255,cv.THRESH_BINARY)
                #
                ##Organizamos y detallamos los contornos
                contornos = cv.findContours(umbral,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
                #
                ##Ordenamos el contorno para dibujar el más grande primero
                #contornos = sorted(contornos, key=lambda x : cv.contourArea(x), reverse=True)
                

                cv.imshow("texto2",texto_nuevo2)
                cv.imshow("recorte",umbral)
                
                #Dibujamos contornos extraidos
                #for contorno in contornos:
                #area = cv.contour(contorno)
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