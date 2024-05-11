from keras.models import load_model

print("Cargando modelo")
model = load_model("cnn_app/data/model_Mnist_LeNet_v2.h5")
# model = load_model("cnn_app/data/model_Mnist.h5")


