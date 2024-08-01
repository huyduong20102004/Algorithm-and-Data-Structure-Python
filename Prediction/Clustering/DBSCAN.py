from sklearn.cluster import DBSCAN
import numpy as np

# Dữ liệu giả lập
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

# Khởi tạo và huấn luyện mô hình DBSCAN
dbscan = DBSCAN(eps=1, min_samples=2).fit(X)

# Dự đoán nhãn cụm
labels = dbscan.labels_
print("DBSCAN labels:", labels)
