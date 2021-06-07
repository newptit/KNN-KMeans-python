import math


def calc_euclid_distance(point_a, point_b, num_of_feature=4):
    tmp = 0
    for i in range(num_of_feature):
        tmp += (float(point_a[i]) - float(point_b[i])) ** 2
    return math.sqrt(tmp)
