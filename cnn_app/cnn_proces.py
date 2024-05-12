import numpy as np
from PIL import Image
from .model_loader import model
import cv2

def get_number_from_image(image_array):
    image = Image.fromarray(image_array)
    
    if image.mode != 'RGB':
        image = image.convert('RGB')


    image_array = np.array(image)
    
    if image_array.shape[0] != 28 or image_array.shape[1] != 28:
        image = image.resize((28, 28), Image.LANCZOS)
        image_array = np.array(image)

    gray = np.dot(image_array[..., :3], [0.299, 0.587, 0.114])

    gray = gray.reshape(1, 28, 28, 1) / 255

    # binarize image
    gray[gray < 0.5] = 0
    gray[gray >= 0.5] = 1

    # Save image
    cv2.imwrite("digit.jpg", gray[0] * 255)

    prediction = model.predict(gray)

    return np.argmax(prediction)
