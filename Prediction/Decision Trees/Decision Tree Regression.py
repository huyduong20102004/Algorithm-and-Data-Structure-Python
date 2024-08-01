from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([1.1, 1.9, 3.1, 3.9, 5.1, 6.1, 6.9, 8.1, 9.1, 10.1])

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Khởi tạo và huấn luyện mô hình Decision Tree Regressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

# Dự đoán trên tập kiểm tra
y_pred = regressor.predict(X_test)

# Đánh giá mô hình
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Vẽ đồ thị
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.title('Decision Tree Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
