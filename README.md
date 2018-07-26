# k-means_clustering
#### k-means algorithm from scikit-learn is used for the clustering. 
#### Due to the fact that the dataset doesn't contain true object labels 
#### to select the number of clusters are used two methods: elbow criterion and silhouette analysis.
***
# Selection of the number of clusters
#
#### Elbow criterion
![Elbow criterion](https://github.com/teawifi/k-means_clustering/blob/master/resources/elbow_criterion_labeled.JPG)
***
#### Silhouette analysis output:
##### For n_clusters=2, The Silhouette Coefficient is 0.5935667167833373
##### For n_clusters=3, The Silhouette Coefficient is 0.5572336399772229
##### For n_clusters=4, The Silhouette Coefficient is 0.579064767127141
##### For n_clusters=5, The Silhouette Coefficient is 0.5851502535228933
##### For n_clusters=6, The Silhouette Coefficient is 0.5666556731479311
##### For n_clusters=7, The Silhouette Coefficient is 0.5410459326241673
##### For n_clusters=8, The Silhouette Coefficient is 0.5526697602383583
##### For n_clusters=9, The Silhouette Coefficient is 0.5408851438579928
##### For n_clusters=10, The Silhouette Coefficient is 0.5624750474483997
***
### Final number of clusters is 5
***
### Result of clustering
![Result of clustering](https://github.com/teawifi/k-means_clustering/blob/master/resources/clustering_result_plot.png)
