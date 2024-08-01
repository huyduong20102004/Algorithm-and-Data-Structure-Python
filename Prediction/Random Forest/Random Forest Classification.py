from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

# Giả sử bạn có một DataFrame `df` với các cột 'feature1', 'feature2', ..., 'target'
# df = pd.read_csv('your_data.csv')

# Tạo dữ liệu giả lập
np.random.seed(0)
X = np.random.rand(100, 2)  # 100 mẫu, 2 đặc trưng
y = np.random.randint(0, 2, 100)  # Nhãn nhị phân

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Khởi tạo và huấn luyện mô hình Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Dự đoán và đánh giá mô hình
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
