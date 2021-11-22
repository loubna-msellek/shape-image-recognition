"""
Evaluate on new unlabeled images 
Set the image and label paths in the variable below
1. Do image preprocessing and reduce noise
2. Select contours from image
3. Select core approximate corners from each contour
4. Determine the shape of the contours based on its number of vertices
5. Draw the picture with its shapes tagged by their types
6. Count the shapes and print it 
"""
import argparse
import cv2
from contours_detection import get_contours
from shape_detector import ShapeDetector

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-i', '--image', required=True, help='Path')

    args = vars(argument_parser.parse_args())
    image = cv2.imread(args['image'])
    cv2.imshow("Original Image", image)
    count_shapes(image,7)

def count_shapes(image, median_size):
    shapes = {
        "square": 0,
        "circle": 0,
        "triangle": 0,
    }

    shape_detector = ShapeDetector()

    contours = get_contours(image, median_size)

    if contours[-1][0][0][0] == 0 and contours[-1][0][0][1] == 0 and contours[-1][-1][0][1] == 0:
        contours = contours[0:-1]

    for contour in contours:
 
        moments = cv2.moments(contour)
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

   
    print("The number of squares predicted is: %d" % (shapes["square"]))
    print("The number of circles predicted is: %d" % (shapes["circle"]))
    print("The number of triangles predicted is: %d" % (shapes["triangle"]))

    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return (shapes["square"], shapes["circle"], shapes["triangle"])

if __name__ == "__main__":
    main()