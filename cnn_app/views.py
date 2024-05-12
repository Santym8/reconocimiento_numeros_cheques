import base64
from django.shortcuts import render
from .forms import ImageForm
from .cnn_proces import get_number_from_image
from .digit_divider import extract_digits_img
import matplotlib.pyplot as plt

def index(request):
    image_data_url = None
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            image_data = image.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            image_data_url = f"data:image/{image.content_type.split('/')[-1]};base64,{encoded_image}"

            numbers_img = extract_digits_img(image_data)
            number_result = ""
            for number_img in numbers_img:
                number = get_number_from_image(number_img)
                number_result += str(number)

            # # Plot each digit in the same figure

            # fig, ax = plt.subplots(1, len(numbers_img), figsize=(12, 12))
            # for i, image in enumerate(numbers_img):
            #     ax[i].imshow(image)
            #     ax[i].axis("off")
            #     # Using model predict
            #     number = get_number_from_image(image)
            #     ax[i].set_title(f"Digit {number}")

            # plt.tight_layout()
            # plt.savefig("results.png")
            # plt.close()


            return render(request, 'index.html', {'form': form, 'image_data_url': image_data_url, 'number_result': number_result})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form, 'image_data_url': image_data_url})
