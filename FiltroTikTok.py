import cv2 as cv

# Classificador en cascada
faceC = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv.imread("gorro.png", cv.IMREAD_UNCHANGED)

# obtener acceso a la webcam
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
anterior = 0
if not cap.isOpened():
    print('No se pudo acceder a la camara')
else:
    while True:
        # revisar si ya puedo leer imagenes de la camara
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)
        imagenGrises = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = faceC.detectMultiScale(
            imagenGrises,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        # por cada cara detectada pintar un cuadro

        filaDeseada = 100
        colDeseada = 200
        for (x, y, w, h) in faces:
            #cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 10)
        # Mostrar la deteccion
        # Redimensionar la imagen de entrada de acuerdo al ancho del
        # rostro detectado

            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    if (image[i, j][3] != 0):
                        frame[i + filaDeseada, j + colDeseada] = image[i, j]
        frame = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
        cv.imshow('Video', frame)
        cv.imwrite("combinacionPNG.png", frame)

        # se motraran las caras mientra no presionemos la tecla esc
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
            # liberar la camara
    cap.release()
    # cerrar todas las ventanas
    cv.destroyAllWindows()
