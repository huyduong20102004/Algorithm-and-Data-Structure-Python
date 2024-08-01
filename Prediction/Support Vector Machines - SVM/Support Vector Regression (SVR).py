import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# Tạo dữ liệu giả lập
X = np.arange(1, 11).reshape(-1, 1)  # Các giá trị đầu vào
y = np.array([1.5, 1.8, 2.3, 2.6, 3.1, 3.5, 4.0, 4.4, 5.1, 5.5])  # Các giá trị mục tiêu

# Khởi tạo mô hình SVR
svr = SVR(kernel='rbf', C=100, epsilon=0.1)
svr.fit(X, y)

# Dự đoán
X_pred = np.linspace(1, 10, 100).reshape(-1, 1)
y_pred = svr.predict(X_pred)

# Vẽ đồ thị
plt.scatter(X, y, color='red', label='Dữ liệu gốc')
plt.plot(X_pred, y_pred, color='blue', label='Dự đoán SVR')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Support Vector Regression (SVR)')
plt.legend()
plt.show()
