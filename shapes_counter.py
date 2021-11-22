
"""
The file is used to take an image and return the number of each object in a txt file.
1. Preprocessing to reduce the noise (lines and points)
2. Select the contours from the image.
3. Select the core approximate corners from each contour.
4. Determine the shape of the main contour; based on its number of vertices.
5. Draw the picture with its shapes tagged by their types.
6. Count the shapes occupancies and print the numbers, comma separated.
"""

import argparse

import cv2
from contours_detection import get_contours
from shape_detector import ShapeDetector


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-i', '--image', required=True, help='Path to the input image')
    args = vars(argument_parser.parse_args())
    image = cv2.imread(args['image'])
    count_shapes(image, 7)


def count_shapes(image, median_size):
    """
    @param image: The original image, in which you wanna reduce the noise.
    @param median_size: the matrix dimensions of the median filter
    This function returns an numpy array with the contours in this image
    We save the number of squares, circles and triangles in the image.
    """
    shapes = {
        "square": 0,
        "circle": 0,
        "triangle": 0
    }

    shape_detector = ShapeDetector()

    contours = get_contours(image, median_size)

    #delete the boarder
    if contours[-1][0][0][0] == 0 and contours[-1][0][0][1] == 0 and contours[-1][-1][0][1] == 0:
        contours = contours[0:-1]

    for contour in contours:
        # compute the center of the contour, then detect the name of the shape using only the contour

        moments = cv2.moments(contour)
        # If the shape is so small we delete it
        if moments["m00"] <= 0.0:
            continue

        contourX = int((moments["m10"] / moments["m00"]))
        contourY = int((moments["m01"] / moments["m00"]))

        shape = shape_detector.detect(contour)
        shapes[shape] += 1

        cv2.drawContours(image, [contour],
                         -1, (0, 255, 0), 2)
        cv2.putText(image, shape, (contourX, contourY),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 0), 2)

    print("%d,%d,%d" % (shapes["square"], shapes["circle"], shapes["triangle"]))
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return (shapes["square"], shapes["circle"], shapes["triangle"])

if __name__ == "__main__":
    main()
