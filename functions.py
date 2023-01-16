import pandas as pd
import re
from sklearn import metrics
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt 

def visualize(dbscan,labels,data,n_clusters_):
    clusters = {}

    unique_labels = set(labels)
    core_samples_mask = np.zeros_like(labels, dtype=bool)
    core_samples_mask[dbscan.core_sample_indices_] = True
    # core_samples_mask[dbscan.subcluster_centers_] = True
    # core_samples_mask[dbscan.ordering_] = True

    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
    # type: ignore
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = labels == k

        
        xy = data[class_member_mask & core_samples_mask]

        cluster = np.empty_like(xy)
        cluster = xy
        # print(xy.shape)
        # print(xy[:,0])
        plt.plot(
            xy[:, 0],
            xy[:, 1],
            "o",
            markerfacecolor=tuple(col),
            markeredgecolor="k",
            markersize=12,
        )

        xy = data[class_member_mask & ~core_samples_mask]

        # print(cluster)
        cluster = np.concatenate((cluster,xy),axis=0)
        # print(cluster)

        clusters[k] = cluster
        # print(xy.shape)
        plt.plot(
            xy[:, 0],
            xy[:, 1],
            "o",
            markerfacecolor=tuple(col),
            markeredgecolor="k",
            markersize=5,
        )

    plt.title(f"Estimated number of clusters: {n_clusters_}")
    plt.show()

    return clusters


# generate random integer values
from random import seed
from random import randint

def random_int(min_b,max_b):
# seed random number generator
    # seed(1)
    # generate some integers
    value = randint(min_b, max_b)

    return value

from yellowbrick.cluster import KElbowVisualizer

# Generate synthetic dataset with 8 random clusters
def elbow(model ,t_boundry,data,visual=False,metric='distortion'):
# Instantiate the clustering model and visualizer
    visualizer = KElbowVisualizer(model, k=t_boundry,metric=metric)
    visualizer.fit(data)        # Fit the data to the visualizer

    if visual:
        visualizer.show()   

    return visualizer.elbow_value_