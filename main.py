import cv2
import numpy as np
import sys

original = cv2.imread(f"./data/cube{x[1] if len(x:=sys.argv) > 1 else 0}.jpg")

img = original.copy()


class Colour:
    ranges = {
        "blue": [166, 280],
        "green": [71, 165],
        "orange": [6, 20],
        "red": [281, 5],
        "yellow": [21, 70],
        "white": [-1, -1],
    }

    value = 5

    def __init__(self, value):
        self.value = value

    def display_name():
        return list(self.ranges.keys())[self.value]

    @staticmethod
    def determine_colour(hue) -> int:  # returns the index of colour
        for i, c in enumerate(ranges):
            if ranges[c][0] <= hue <= ranges[c][1]:
                return c


def find_colour_at(pos: tuple[int, int], img) -> Colour:
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(img_hsv[pos[0], pos[1]])

    # Colour.determine_colour()
