import cv2


def detect_cat(image_path):
    # Load the pre-trained Haar Cascade classifier for cat detection
    cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

    # Read image
    image = cv2.imread(image_path)

    # Convert the image to grayscale for Haar Cascade
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cats in the image
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected cats
    for (x, y, w, h) in cats:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the image with detected cats
    cv2.imshow('Cat Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Replace 'path/to/your/cat/image.jpg' with the path to your cat image
image_path = 'path/to/your/cat/image.jpg'
detect_cat(image_path)
