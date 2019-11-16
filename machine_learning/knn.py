from collections import Counter
from itertools import cycle
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

class KNn:

    def __init__(self, data, k):
        self.x_ = [d[0] for d in data]
        self.y_ = [d[1] for d in data]
        self.k = k

    @staticmethod
    def distance(x1, x2):
        return cdist([x1], [x2], 'cityblock')

    def classify(self, new_x):
        distances = []
        for x, y in zip(self.x_, self.y_):
            distances.append((float(self.distance(x, new_x)), y))

        print(distances)
        classes = sorted(distances, key=lambda t:t[0])
        print(classes)
        classes = [tuple[1] for tuple in classes[:self.k]]
        print(classes)
        return Counter(classes).most_common()[0][0]

def main():
    data = [
       [[2.2, 4.5], 1],
       [[2.3, 4], 1],
       [[2.1, 3.5], 1],
       [[1.8, 4], 1],
       [[1.9, 3], 1],
       [[2.5, 1.5], 0],
       [[2.7, 1], 0],
       [[2.9, 1.5], 0],
       [[3.1, 1], 0],
       [[4.5, 2.5], 0],
    ]
    new1 = [2.6, 2.5]
    new2 = [2.0, 4]

    knn = KNn(data, 3)
    new_y1 = knn.classify(new1)
    new_y2 = knn.classify(new2)
    print([new_y1, new_y2])

    classes = list(set([d[1] for d in data]))
    cy_colors = cycle('bgrcmy')
    plt.figure()

    plt.scatter([new1[0]], [new1[1]], color='k')
    plt.scatter([new2[0]], [new2[1]], color='k')

    for c in classes:
        plt.scatter([d[0][0] for d in data if d[1] == c],
                    [d[0][1] for d in data if d[1] == c],
                    color=next(cy_colors)
                    )

    plt.show()

if __name__ == '__main__':
    main()
