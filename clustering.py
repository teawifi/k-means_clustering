import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn import preprocessing
from settings import DATASET_DIR_PATH

np.random.seed(42)
no_clusters = 5

data = pd.read_csv(DATASET_DIR_PATH + '/' + '3d_dataset_clustering.csv')

normalizer = preprocessing.Normalizer()
data = pd.DataFrame(normalizer.fit_transform(data))

title = str(no_clusters) + ' clusters'

figure = plt.figure(figsize=(4, 3))
ax = Axes3D(figure, elev=48, azim=134)
kmeans = KMeans(n_clusters=no_clusters).fit(data)
labels = kmeans.labels_
ax.scatter(data[0], data[1], data[2],
           c=labels.astype(np.float), edgecolor='k')
ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(title)
ax.dist = 10

plt.show()