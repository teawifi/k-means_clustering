import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from settings import DATASET_DIR_PATH

np.random.seed(42)

data = pd.read_csv(DATASET_DIR_PATH + '/' + '3d_dataset_clustering.csv')
normalizer = preprocessing.Normalizer()
data = pd.DataFrame(normalizer.fit_transform(data))

# Elbow Criterion
sse = {}
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, max_iter=1000).fit(data)
    sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center
plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel("Number of cluster")
plt.ylabel("SSE")
plt.title('Elbow Criterion')
plt.show()


# Silhouette Analysis
for n_cluster in range(2, 11):
    kmeans = KMeans(n_clusters=n_cluster).fit(data)
    label = kmeans.labels_
    sil_coeff = silhouette_score(data, label, metric='euclidean', sample_size=1000)
    print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))