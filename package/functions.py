def menu():
    while True:
        camara_opcion = input("Seleccione el tipo de la cámara siendo 1 valor por defecto de tu computadora o 0 usando dirección IP. \n")
        
        if camara_opcion == '1': 
        #video = cv.VideoCapture(0)
            video = 0
            print('video capture definido como por defecto')
            return video, camara_opcion
        elif camara_opcion == '0':
            print("-------------------")
            print('video capture definido por IP \n')
            print("para usar esta opciónes debes instalar la aplicación DROID CAM en tu teléfono \n") 
            print("ve a la google play y busca la Aplicación DROIDCAM: instalala y ejecutala, cuando la ejecutes encontraras 2  formas   de acceso: \n")
            print(", a tra ves de WIFI IP y IP CAM ACCESS,usaremos IP CAMACCESS: su estructura de dirección es más o menos la       siguiente: http://192.168.1.12:4747/video \n")
            directorio = input("digite la dirección IP \n")
            #directorio = "192.168.1.12:4747/video"
            droid_cam = f"http://{directorio}"
            video = droid_cam
            #video = cv.VideoCapture(droid_cam)
            print("-------------------")
            return video, camara_opcion
        break
    
    
def video(video):
    while True:
        try:
            # Lectura de la cámara
            ret, frame = video.read()
            if ret == False: break
            else:
                #Extraemos con librería numpy la altura, ancho
                alto, ancho, c = frame.shape
                #Sacar el tamaño del eje x
                x1 = int(ancho / 3)
                x2 = int(x1 * 2)
                
                #tamaño eje y
                y1 = int(alto / 4)
                y2 = int(y1 * 2)

                #Pasamos Imágen a escala de grises
                frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

                #Suavisamos el filtro ya que los pixeles cambian muy rápido
                frame_gray = cv.GaussianBlur(frame_gray,(1,1),0,0)

                _, frame_gray = cv.threshold(frame_gray,155,255,cv.THRESH_BINARY)
                #_, frame_gray = cv.threshold(frame_gray,200,255,cv.THRESH_BINARY_INV)

                #buscamos los contornos con los parametros = De la función findcontours = devuelve 2 valores, valoresHerados y el   contorno
                """"
                img = la imagen o video que queremos que encuentre los contornos
                mode = es el modo de recuperación del contorno = usaremos para este ejemplo el de recuperar todos los contornos =   cvRETR_TREE, nos muestra los contornos internos y externos
                method = método de aproximación de contorno, hay 2 formas = CHAIN_APPROX_SIMPLE y CHAIN_APPROX_NONE = usaremos el   none queencuentra todos los puntos del contorno, CHAIN APROX_SIMPLE = Encuentra solo los elementos de las puntas
                """
                ##Nos devuelve 2 cosas, el contorno y la jerarquía de los contornos
                contorno, _ = cv.findContours(frame_gray, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
            
            
                #Dibujamos un triángulo en el centro
                #frame_2 = cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
                #recorte = frame_2[y1:y2, x1:x2]
                for c in contorno:
                    #c es el numpy array de los puntos de todo el contorno
                    area = cv.contourArea(c)
                    (x,y,w,h) = cv.boundingRect(c)
                    #En este proceso tratamos de encontrar esclusivamente las figuras rectangulares y que no tengan curvas, el  argumento truedetermina si la forma es un contorno cerrado y no una curva
                    cuadrado = 0.09 * cv.arcLength(c, True)
                    aproximado = cv.approxPolyDP(c, cuadrado, True)
                    # Len aproximado == 4 significa si el area contiene 4 vertices
                    if len(aproximado)== 4 and area > 8000:
                        #Usarmos el aspect radio para determinar el contorno y saber que se trate de un rectángulo
                        aspect_radio = float(300.6)/151.2
                        #print("aspect radio=",aspect_radio)
                        if aspect_radio > 1.8: 
                            frame = cv.drawContours(frame,[c],0,(0,255,0),3,cv.LINE_AA)
                            # guardamos el area de la placa, para eso vamos a usar los contornos encontrados con boundingRect
                            placa_figura = frame_gray[y:y + h, x:x + w]
                            #Reconocer caracteres - usaremos pyteseract
                            """
                            Parámetros
                            placa figura = corresponde a lo que queremos leer
                            config = modo de segmentación de página, usaremos la forma --psm 11, podemos probar con otras pero el   resultadode conocimiento de caracteres puede cambiar
                            """
                            texto = pytesseract.image_to_string(placa_figura,config='--psm 1')
                        if len(texto) >= 7 and len(texto) <= 10:
                            print("texto placa ",texto)
                            #Colocamos texto en pantalla de lo que se lee
                            frame = cv.putText(frame,texto,(140,70),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,0),3)
                            #guardar placa en archivo de texto
                            f = open('lector_placas.txt','a')
                            f.write('\n' + texto)
                            f.close()
                cv.imshow('imagen',frame)
                if cv.waitKey(1) & 0xFF == ord('c'):
                    print("Sales del programa")
                    #Guarda una captura de lo último que ve antes de salir del programa
                    ruta_imagen = f"img/imagen{i+1}.jpg"
                    imagen = cv.imwrite(ruta_imagen,frame)
                    i = i + 1
                    break
        except KeyboardInterrupt:
            print("sales del programa por fuerza mayor, presionaste CTRL + C")
            ruta_imagen = f"img/imagen_{i+1}.jpg"
            imagen = cv.imwrite(ruta_imagen,frame)
            i = i + 1
        break

