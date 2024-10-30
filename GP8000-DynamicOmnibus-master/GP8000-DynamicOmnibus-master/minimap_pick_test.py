import cv2
import numpy as np

img = cv2.imread("NTU_minimap.png")
# cv2.imshow("Minimap", img)

# Resize the image to fit the screen (e.g., 50% of the original size)
scale_percent = 50  # Percentage of original size, adjust as needed
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Make a copy of the resized image to reset annotations
img_copy = resized_img.copy()


# Function to display coordinates on click
def show_coordinates(event, x, y, flags, param):
    global resized_img
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        # Reset to original resized image (removes previous coordinates)
        resized_img = img_copy.copy()

        # Display new coordinates on the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f'({x}, {y})'
        cv2.putText(resized_img, text, (x, y), font, 0.5, (255, 0, 0), 2)  # Blue color text
        cv2.imshow("Image", resized_img)


# Create a named window and set the mouse callback function
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", show_coordinates)

# Display the resized image
while True:
    cv2.imshow("Image", resized_img)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Close all windows
cv2.destroyAllWindows()