import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2

# Load the MobileNetV2 model pre-trained on ImageNet data
base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')

# Freeze the pre-trained layers
for layer in base_model.layers:
    layer.trainable = False

# Build the cat recognition model on top of the pre-trained model
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Data preprocessing and augmentation
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
train_generator = train_datagen.flow_from_directory('path_to_training_data', target_size=(224, 224), batch_size=32, class_mode='binary')

# Train the model
model.fit(train_generator, epochs=10)

# Save the model for later use
model.save('cat_recognition_model.h5')

# Load the model
loaded_model = tf.keras.models.load_model('cat_recognition_model.h5')

# Make predictions on new images
def predict_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = loaded_model.predict(img_array)
    score = predictions[0][0]

    if score > 0.5:
        print(f"The image contains a cat with a confidence of {score*100:.2f}%.")
    else:
        print(f"The image does not contain a cat with a confidence of {(1-score)*100:.2f}%.")

# Example usage
predict_image('path_to_test_image.jpg')