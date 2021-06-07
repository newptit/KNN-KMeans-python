from k_nn.calc_distance import calc_euclid_distance
from k_nn.load_data import load


# Get k nearest neighbors
def k_nearest_neighbors(training_set, point, k):
    distances = []
    for item in training_set:
        distances.append({
            "label": item[-1],
            "value": calc_euclid_distance(item, point)
        })
    # Sap xep theo khoang cach tu be toi lon
    distances.sort(key=lambda x: x["value"])
    labels = [item["label"] for item in distances]
    # Lay k phan tu co khoang cach nho nhat
    return labels[:k]


def find_most_occur(arr):
    labels = set(arr)
    ans = ""
    max_occur = 0
    for label in labels:
        num = arr.count(label)
        if num > max_occur:
            max_occur = num
            ans = label
    return ans


def test(file_path, k=5):
    print({k})
    rows = []
    training_set, testing_set = load(file_path)
    num_of_right_answer = 0
    for item in testing_set:
        knn = k_nearest_neighbors(training_set, item, k)
        answer = find_most_occur(knn)
        num_of_right_answer += item[-1] == answer
        rows.append("Nhãn: {} -> Dự đoán: {} ({})"
            .format(item[-1], answer, item[-1] == answer))
        print("label: {} -> predicted: {}".format(item[-1], answer))

    ratio = num_of_right_answer/len(testing_set)
    print("Accuracy", num_of_right_answer/len(testing_set))
    return ratio, rows


if __name__ == '__main__':
    test()
