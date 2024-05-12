import cv2
from PIL import Image
import io
import numpy as np

def is_digit_aspect_ratio(w, h):
    aspect_ratio = float(w) / h
    return aspect_ratio >= 0.3 and aspect_ratio <= 1.5

def extract_digits_and_symbols(image):
    # Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
    # cv2.imshow("Gray Image", gray)
    # cv2.waitKey(0)
    
    # Aplicar umbral para obtener una imagen binaria
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
  
    # cv2.imshow("Thresh Image", thresh)
    # cv2.waitKey(0)
        
    # Encontrar contornos externos
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Ordenar los contornos de izquierda a derecha
    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])

    # Lista para almacenar digitos
    digits = []

    # Iterar sobre los contornos
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # Filtrar contornos por tamaño
        if w >= 40 and h >= 70 and is_digit_aspect_ratio(w, h):
            roi = image[y:y + h, x:x + w]
            digits.append(roi)

    return digits


def extract_digits_img(image_data):
    # Leer imagen
    image = Image.open(io.BytesIO(image_data))

    # Convertir a formato OpenCV
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# 
    original_image = image.copy()
  
    # cv2.imshow("Original Image", original_image)
    # cv2.waitKey(0)

    # Definir ROI (Region of Interest) %
    roi_top_left_x = 0.65 
    roi_top_left_y = 0.2  
    roi_width = 0.2  
    roi_height = 0.2  

    # Extraer ROI
    roi = image[int(roi_top_left_y * image.shape[0]):int((roi_top_left_y + roi_height) * image.shape[0]), 
            int(roi_top_left_x * image.shape[1]):int((roi_top_left_x + roi_width) * image.shape[1])]

    # cv2.imshow("ROI", roi)
    # cv2.waitKey(0)
    
    # # Extract digitos
    digits = extract_digits_and_symbols(roi)
    

    # Display each digit and symbol
    # for i, roi in enumerate(digits):
    #     # cv2.imwrite(f"digit_{i+1}.jpg", roi)
    #     cv2.imshow(f"Digit {i+1}", roi)
    #     cv2.waitKey(0)  # Reduce wait time for faster display

    # cv2.destroyAllWindows()


    return digits

