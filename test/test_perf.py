#!/usr/bin/env python

import numpy as np
from time import time
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from geometric_median import *


def total_distance(a, b):
    return cdist(a, b).sum()


def main():
    # create a bunch of point datasets for testing
    n_tests = 10
    n_points = 20
    n_dims = 10
    np.random.seed(0)
    test_data = np.random.uniform(size=(n_tests, n_points, n_dims))

    methods = [
        'minimize',
        'weiszfeld',
        'auto'
    ]

    test_results = []

    for points in test_data:
        results = []

        for method in methods:
            start_t = time()
            m = geometric_median(points, method=method)
            end_t = time()

            t = end_t - start_t
            d = total_distance([m], points)
            results.append((t, d))

        test_results.append(results)

    test_results = np.array(test_results)

    width = 0.90 / test_results.shape[1]
    bar_positions = np.arange(test_results.shape[0])
    colors = ['b', 'r', 'g']

    # Display computation time
    for method_i, method in enumerate(methods):
        method_times = test_results[:,method_i,0]

        plt.bar(
            bar_positions + (width * method_i),
            method_times,
            width,
            color=colors[method_i],
            label=method
        )

    plt.xticks(bar_positions)
    plt.ylabel("Computation time")
    plt.xlabel("Trials")
    plt.legend()
    plt.show()

    # Display result quality (closeness)
    '''
    for method_i, method in enumerate(methods):
        method_dists = test_results[:,method_i,1]

        plt.bar(
            bar_positions + (width * method_i),
            method_dists,
            width,
            color=colors[method_i],
            label=method
        )

    plt.xticks(bar_positions)
    plt.ylabel("Distance")
    plt.xlabel("Trials")
    plt.legend()
    plt.show()
    '''


if __name__ == '__main__':
    main()
