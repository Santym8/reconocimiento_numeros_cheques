import numpy as np
from PIL import Image
import io
from .model_loader import model

def get_number_from_image(image_data):
    image = Image.open(io.BytesIO(image_data))
    
    if image.mode != 'RGB':
        image = image.convert('RGB')

    image_array = np.array(image)
    
    if image_array.shape[0] != 28 or image_array.shape[1] != 28:
        image = image.resize((28, 28), Image.LANCZOS)
        image_array = np.array(image)

    gray = np.dot(image_array[..., :3], [0.299, 0.587, 0.114])

    gray = gray.reshape(1, 28, 28, 1) / 255

    prediction = model.predict(gray)
    return np.argmax(prediction)
