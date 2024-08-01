import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Tạo dữ liệu giả lập
X = np.random.rand(100, 2)  # 100 mẫu, 2 đặc trưng
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Phân loại dựa trên tổng của các đặc trưng

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo mô hình KNN phân loại
model = KNeighborsClassifier(n_neighbors=5)

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Dự đoán cho dữ liệu mới
new_data = np.array([[0.6, 0.7], [0.2, 0.3]])
predictions = model.predict(new_data)
print(f"Predictions for new data: {predictions}")
