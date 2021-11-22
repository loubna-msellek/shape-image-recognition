"""
This function is used for preprocessing includig noise reducig usig median blur in the image (points+lines)
"""
import cv2

# Median filter
def preprocess(image, median_size):
    """
    @param image: original image 
    @param median_size: the matrix dimensions of the median filter used
    This function returns the filtered image
    """
    #the maximum size is 7
    median_size = min(median_size, 7)
    processed_image = cv2.medianBlur(image, median_size)
    return processed_image
