"""
This function allows to detect the contours of the image
"""
import cv2
from preprocessing import preprocess


def get_contours(img, median_size):
    """
    :param image: The original image, in which you wanna reduce the noise.
    :param median_size: the matrix dimensions of the median filter
    The code returns an numpy array with the contours and draw the original image with the contours detected
    """
    noisy_img = img
    img = preprocess(img, median_size)
    blurred = cv2.pyrMeanShiftFiltering(img, 20, 100) 
    #we first use a binary image to find the contours
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(noisy_img, contours, -1, (0, 0, 255), 6)
    cv2.namedWindow("Detection of contours", cv2.WINDOW_NORMAL)
    cv2.imshow("Detection of contours", noisy_img)
    cv2.waitKey()
    return contours
