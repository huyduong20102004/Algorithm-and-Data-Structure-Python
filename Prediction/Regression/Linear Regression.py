from sklearn.linear_model import LinearRegression
import numpy as np

# Dữ liệu giả lập
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.2, 2.3, 2.9, 4.1, 4.8])

# Khởi tạo mô hình
model = LinearRegression()

# Huấn luyện mô hình
model.fit(X, y)

# Dự đoán
predictions = model.predict(X)

print("Hệ số hồi quy:", model.coef_)
print("Hằng số hồi quy:", model.intercept_)
print("Dự đoán:", predictions)
