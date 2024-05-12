import numpy as np
from PIL import Image
from .model_loader import model
import cv2

def get_number_from_image(image):
    if(len(image.shape) == 3):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #     Invertir imagen
    image = cv2.bitwise_not(image)
    # Cambiar tamaño a 28x28
    image = cv2.resize(image, (28, 28))

    # Smooth the image
    image = cv2.GaussianBlur(image, (1, 1), 0)

    image[image < 110] = 0
    image[image >= 110] = 255


    # Normalizar imagen
    image = image / 255.0
    image = image.reshape(1, 28, 28, 1)


    # Predecir el número
    prediction = model.predict([image])

    # Obtener el número con mayor probabilidad
    number = np.argmax(prediction)
    return number
    

