import numpy as np  # thư viện tính toán toán học
import matplotlib.pyplot as plt  # visualize data sử dụng đồ thị
from scipy.spatial.distance import cdist  # Hỗ trợ tính khoảng cách

means = [
    [2, 2],
    [9, 2],
    [4, 9],
    [9, 9],
]

X = np.array([])

n_cluster = 3
num = 0


def init_data(k):
    global X
    cov = [[2, 0], [0, 2]]
    n_samples = 500
    for i in range(k):
        tmp_x = np.random.multivariate_normal(means[i], cov, n_samples)
        if len(X) == 0:
            X = tmp_x
        else:
            X = np.concatenate((
                X,
                tmp_x,
            ), axis=0)


def k_means_init_centers(X, n_cluster):
    # random k index beetween 0 and shape(X) without duplicate index.
    # Then return X[index] as cluster
    return X[np.random.choice(X.shape[0], n_cluster, replace=False)]


def k_means_predict_labels(X, centers):
    d = cdist(X, centers)
    print(d)
    # return index of the closest center
    idx = np.argmin(d, axis=1)
    print(idx)
    return idx


def k_means_update_centers(X, labels, n_cluster):
    centers = np.zeros((n_cluster, X.shape[1]))
    for k in range(n_cluster):
        # collect all points assigned to the k-th cluster
        Xk = X[labels == k, :]
        # take average
        centers[k, :] = np.mean(Xk, axis=0)
    return centers


def k_means_has_converged(centers, new_centers):
    # return True if two sets of centers are the same
    return (set([tuple(a) for a in centers]) ==
            set([tuple(a) for a in new_centers]))


# Hàm này dùng để vẽ dữ liệu lên đồ thị
# Random color chỉ làm việc với k <= 4
# Nếu bạn thay đổi k > 4, hãy sửa lại phần random color nhé
# Chỉ sử dụng trong bài toán này thôi nhé.
def k_means_visualize(X, centers, labels, n_cluster, title):
    global num
    plt.xlabel('x')  # label trục x
    plt.ylabel('y')  # label trục y
    plt.title(title)  # title của đồ thị
    plt_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']  # danh sách các màu hỗ trợ

    for i in range(n_cluster):
        data = X[labels == i]  # lấy dữ liệu của cụm i
        plt.plot(data[:, 0], data[:, 1], plt_colors[i] + '^', markersize=4,
                 label='Cụm ' + str(i + 1))  # Vẽ cụm i lên đồ thị
        plt.plot(centers[i][0], centers[i][1], plt_colors[i + 4] + 'o', markersize=10,
                 label='Tâm cụm ' + str(i + 1))  # Vẽ tâm cụm i lên đồ thị
    plt.legend()  # Hiện bảng chú thích
    img = plt.savefig('imgs/{}.png'.format(num))
    print(img)
    plt.show()


def k_means(init_centes, init_labels, X, n_cluster):
    global num
    centers = init_centes
    labels = init_labels
    times = 0
    while True:
        labels = k_means_predict_labels(X, centers)
        k_means_visualize(X, centers, labels, n_cluster, 'Gán nhãn cho dữ liệu tại thời điểm t = ' + str(times + 1))
        num += 1
        new_centers = k_means_update_centers(X, labels, n_cluster)
        if k_means_has_converged(centers, new_centers):
            break
        centers = new_centers
        k_means_visualize(X, centers, labels, n_cluster, 'Cập nhập vị trí trung tâm tại thời điểm t = ' + str(times + 1))
        times += 1
        num += 1
    return (centers, labels, times)


def test(k=3):
    global num, n_cluster
    n_cluster = k
    init_data(k)
    init_centers = k_means_init_centers(X, n_cluster)
    print(init_centers)  # In ra tọa độ khởi tạo ban đầu của các tâm cụm
    init_labels = np.zeros(X.shape[0])
    k_means_visualize(X, init_centers, init_labels, n_cluster,
                      'Khởi tao vị trí tâm cụm. Gán nhãn tất cả dữ liệu: cụm 0')
    num += 1
    centers, labels, times = k_means(init_centers, init_labels, X, n_cluster)
    print(centers)

    print('Done! Kmeans has converged after', times, 'times')

