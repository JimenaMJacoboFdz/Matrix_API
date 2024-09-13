import cv2

# Read the image
image = cv2.imread('C:\\Users\\e_m_a\\Pictures\\Screenshots\\Captura de pantalla 2024-09-11 130143.png')

# Check if the image was successfully loaded
if image is None:
    print("Image not found or unable to open")
else:
    # Display the image
    cv2.imshow('Loaded Image', image)
    
    # Wait for a key press to close the window
    cv2.waitKey(0)
    
    # Close the window
    cv2.destroyAllWindows()
