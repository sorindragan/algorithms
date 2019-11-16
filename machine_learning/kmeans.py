from itertools import cycle
import matplotlib.pyplot as plt
from random import shuffle
from scipy.spatial.distance import cdist
import time

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = -1
        self.id = -1

    def assign_cluster(self, cluster_id):
        self.cluster = cluster_id

    def new_coordinates(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class KMeans:

    def __init__(self, k, iterations, points):
        self.k = k
        self.iterations = iterations
        self.points = [Point(p[0], p[1]) for p in points]

    def closest_centroid(self, centroids, point):
        distances = [(self.distance(point, c), c) for c in centroids]
        return min(distances, key = lambda tuple: tuple[0])[1]

    def recalculate_centroids(self, centroids, points):
        for c in centroids:
            x_values = [p.x for p in points if p.cluster.id == c.id]
            y_values = [p.y for p in points if p.cluster.id == c.id]
            c.new_coordinates(sum(x_values) / len(x_values),
                              sum(y_values) / len(y_values)
                              )

    def init_random_centroids(self, k, points):
        centroids = []
        shuffle_points = points
        shuffle(shuffle_points)
        for idx, centroid in enumerate(shuffle_points[:k]):
            c = Point(centroid.x, centroid.y)
            c.id = idx
            centroids.append(c)

        return centroids

    @staticmethod
    def distance(p1, p2):
        return cdist([[p1.x, p1.y]], [[p2.x, p2.y]], 'euclidean')

    def k_means(self):
        centroids = self.init_random_centroids(self.k, self.points)
        cycol = cycle('bgrcmy')

        for _ in range(self.iterations):
            for p in self.points:
                p.cluster = self.closest_centroid(centroids, p)
            self.recalculate_centroids(centroids, self.points)

        plt.figure()
        plt.scatter([c.x for c in centroids], [c.y for c in centroids], color='k')
        for c in centroids:
            plt.scatter([p.x for p in self.points if p.cluster.id == c.id],
                        [p.y for p in self.points if p.cluster.id == c.id],
                        color=next(cycol)
                        )
        plt.show()

def main():
    k = KMeans(3, 10, [[0, 0], [1, 1], [1, 2], [5, 6], [6, 6], [6, 7], [7, 8],
                       [0, 8], [0, 9], [1, 8], [1, 9]]
                       )
    k.k_means()

if __name__ == '__main__':
    main()
