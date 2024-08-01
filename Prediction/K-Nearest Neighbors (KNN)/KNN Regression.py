import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

# Tạo dữ liệu giả lập
X = np.random.rand(100, 1)  # 100 mẫu, 1 đặc trưng
y = 3 * X.squeeze() + np.random.randn(100)  # Mối quan hệ hồi quy tuyến tính với nhiễu

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo mô hình KNN hồi quy
model = KNeighborsRegressor(n_neighbors=5)

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Dự đoán cho dữ liệu mới
new_data = np.array([[0.5], [0.8]])
predictions = model.predict(new_data)
print(f"Predictions for new data: {predictions}")
