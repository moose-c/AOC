import numpy as np


def pad_array(array, delimiter):
    padded_array = [delimiter + row + delimiter for row in array]
    padded_array.insert(0, delimiter * len(padded_array[0]))
    padded_array.append(delimiter * len(padded_array[0]))
    return padded_array
