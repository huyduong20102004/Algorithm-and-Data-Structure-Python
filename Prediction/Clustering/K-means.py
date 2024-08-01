from sklearn.cluster import KMeans
import numpy as np

# Dữ liệu giả lập
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Khởi tạo và huấn luyện mô hình K-means
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Dự đoán nhãn cụm
labels = kmeans.labels_
print("K-means labels:", labels)

# Tọa độ tâm cụm
centroids = kmeans.cluster_centers_
print("Centroids:", centroids)
