import cv2
import numpy as np
import sys


DEBUG = True


class Colour:
    ranges = {
        "blue": [166, 280],
        "green": [71, 165],
        "orange": [6, 42],
        "red": [281, 5],
        "yellow": [43, 70],
        "white": [-1, -1],
    }

    value = 5

    def __init__(self, value):
        self.value = value

    def display_name():
        return list(self.ranges.keys())[self.value]

    @staticmethod
    def determine_colour(hue) -> int:  # returns the index of colour
        for i, c in enumerate(Colour.ranges):
            if Colour.ranges[c][0] <= hue <= Colour.ranges[c][1]:
                return c


def find_colour_at(pos: tuple[int, int], img) -> Colour:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    x = hsv[pos[1], pos[0]]
    hue = x[0] * 2  # see https://answers.opencv.org/question/203501/cv2color_rgb2hsv-is-not-giving-correct-hsv-values/

    colour = Colour.determine_colour(hue)

    if DEBUG:
        print(x)
        print(hue)
        print(colour)

        img = cv2.circle(img, pos, 4, (255, 255, 255), 4)
        cv2.imshow("plotted", img)


find_colour_at((1365, 1045), img)  # orange
find_colour_at((1555, 1165), img)  # green
find_colour_at((1729, 871), img)  # blue


# INFO: keep windows
cv2.waitKey(0)
cv2.destroyAllWindows()
