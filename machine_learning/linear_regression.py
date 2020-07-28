import matplotlib.pyplot as plt
import numpy as np

def least_squares_regression(data_points):
    no_points = len(data_points)
    x_sum = sum([p[0] for p in data_points])
    y_sum = sum([p[1] for p in data_points])
    x_sq_sum = sum([p[0]**2 for p in data_points])
    x_y_sum = sum([p[0] * p[1] for p in data_points])
    
    # calculate slope
    m = (no_points * x_y_sum - x_sum * y_sum) / (no_points * x_sq_sum - x_sum ** 2)

    # calculate intercept
    b = (y_sum - m * x_sum) / no_points

    return m, b

def main():
    data_points = [(2, 4), (3, 5), (4, 7), (7, 10), (9, 15), (10, 15)]
    x = np.array([p[0] for p in data_points])
    y = np.array([p[1] for p in data_points])
    m, b = least_squares_regression(data_points)
    plt.plot(x, y, 'bo')
    plt.axis([0, max(data_points, key=lambda p: p[0])[0] + 2,
              0, max(data_points, key=lambda a:a[1])[1] + 2
              ])
    y_ = m * x + b
    plt.plot(x, y_, '-k')
    plt.show()

if __name__ == '__main__':
    main()
