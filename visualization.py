"""
Simple visualization tool for the evolution of image from blurring to final detection
"""
import argparse
from PIL import Image, ImageOps
import cv2
import numpy as np

# Read image
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-i', '--image', required=False, help='Path')
args = vars(argument_parser.parse_args())
img_url = args['image'] or 'testimage.jpg'
img = cv2.imread(img_url)
top, bottom, left, right = [15]*4
img_for_plot=cv2.copyMakeBorder(img.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])

img_plot1 = img_for_plot.copy()
img_plot2 = None
img_plot3 = None
img_plot4 = None
img_plot5 = None
img_plot6 = None


class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):
        """
        :param c: a contour
        :return: name of the shape.
        """
        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        # if there are 3 vertices, the shape is a triangle
        if len(approx) == 3:
            shape = "triangle"

        # if there are 4 vertices, the shape is a square 
        elif len(approx) == 4: 
            shape = "square" 

        # otherwise, we assume the shape is a circle
        else:
            shape = "circle"

        # return the name of the shape
        return shape


def preprocess(image, median_size):
    median_size = min(median_size, 7)
    processed_img = cv2.medianBlur(img, median_size)
    return processed_img


def get_contours(img, median_size):
    global img_plot2, img_plot3, img_plot4, img_plot5
    color = [255,255,255] 
    top, bottom, left, right = [15]*4
    img_for_plot=cv2.copyMakeBorder(img.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])

    img_with_noise = img_for_plot.copy()
    img = preprocess(img, median_size)
    img_plot2 = cv2.copyMakeBorder(img.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])
    blurred = cv2.pyrMeanShiftFiltering(img, 31, 91)
    img_plot3 =cv2.copyMakeBorder(blurred.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])


    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    img_plot4 = cv2.copyMakeBorder(gray.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])

    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    top, bottom, left, right = [0,30,0,30]
    img_with_noise = cv2.copyMakeBorder(blurred.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])
    cv2.drawContours(img_with_noise, contours, -1, (0, 0, 255), 6)
    img_plot5 = img_with_noise.copy()
    return contours


def count_shapes(img, median_size):
    global img_plot6
    top, bottom, left, right = [15]*4
    img_for_plot=cv2.copyMakeBorder(img.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])

    shape_detector = ShapeDetector()
    contours = get_contours(img_for_plot, median_size)
    if contours[-1][0][0][0] == 0 and contours[-1][0][0][1] == 0 and contours[-1][-1][0][1] == 0:
        contours = contours[0:-1]
    for contour in contours:
        moments = cv2.moments(contour)
        if moments["m00"] <= 0.0:
            continue
        contourX = int((moments["m10"] / moments["m00"]))
        contourY = int((moments["m01"] / moments["m00"]))
        shape = shape_detector.detect(contour)
        cv2.drawContours(img_for_plot, [contour],
                         -1, (0, 255, 0), 2)
        cv2.putText(img, shape, (contourX, contourY),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 0), 2)
    top, bottom, left, right = [0,30,0,30]
    img_plot6 = cv2.copyMakeBorder(img.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0,0,0])


count_shapes(img, 7)
img_plot1 = cv2.resize(img_plot1, (0, 0), None, .4, .4)
img_plot2 = cv2.resize(img_plot2, (0, 0), None, .4, .4)
img_plot3 = cv2.resize(img_plot3, (0, 0), None, .4, .4)
img_plot4 = cv2.resize(img_plot4, (0, 0), None, .4, .4)
img_plot5 = cv2.resize(img_plot5, (0, 0), None, .4, .4)
img_plot6 = cv2.resize(img_plot6, (0, 0), None, .4, .4)
concat = np.concatenate((img_plot1, img_plot2, img_plot3, img_plot5, img_plot6), axis=1)
cv2.imshow('Different stages of image recognition (1):original image, (2): filtered image, (3): binary image, (4) image with detected contours, (5) image with classification', concat)
cv2.waitKey()