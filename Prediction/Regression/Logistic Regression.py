from sklearn.linear_model import LogisticRegression
import numpy as np

# Dữ liệu giả lập
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 0, 1, 1])

# Khởi tạo mô hình
model = LogisticRegression()

# Huấn luyện mô hình
model.fit(X, y)

# Dự đoán
predictions = model.predict(X)
probabilities = model.predict_proba(X)

print("Hệ số hồi quy:", model.coef_)
print("Hằng số hồi quy:", model.intercept_)
print("Dự đoán:", predictions)
print("Xác suất dự đoán:", probabilities)
