
import cv2
import numpy as np

def compare_images(img1_path, img2_path):
    # Load images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Compute Structural Similarity Index (SSIM)
    ssim = cv2.compare_ssim(gray1, gray2)
    
    # Define a threshold for SSIM to determine if images are similar
    threshold = 0.95
    
    # Compare SSIM with threshold
    if ssim > threshold:
        return "Images are similar"
    else:
        return "Images are different"

# Example usage
img1_path = '/dataset/Screenshot (915).png'
img2_path = '/dataset/Screenshot (915).png'
result = compare_images(img1_path, img2_path)
print(result)