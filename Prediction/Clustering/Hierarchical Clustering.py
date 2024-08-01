import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.datasets import make_blobs

# Tạo dữ liệu giả lập
X, _ = make_blobs(n_samples=50, centers=3, cluster_std=0.60, random_state=0)

# Tính toán liên kết Hierarchical
linked = linkage(X, method='ward')

# Vẽ dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()

# Phân cụm dữ liệu
labels = fcluster(linked, t=3, criterion='maxclust')
print("Hierarchical Clustering labels:", labels)

