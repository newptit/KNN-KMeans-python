import csv
import numpy as np


def load(path):
    f = open(path, "r")
    data = csv.reader(f)
    data = np.array(list(data))
    data = np.delete(data, 0, 0)
    data = np.delete(data, 0, 1)
    np.random.shuffle(data)
    f.close()
    training_set = data[:100]
    testing_set = data[100:]
    return training_set, testing_set
