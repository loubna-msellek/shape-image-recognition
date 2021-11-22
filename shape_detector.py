import cv2

class ShapeDetector:
    """
    This class works as a shape classifier, based on the number of vertices
    extracted from the approximation of the contours.
    """
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
