from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score

# Tải dữ liệu ví dụ
data = load_iris()
X = data.data
y = data.target

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Khởi tạo mô hình LightGBM
model = lgb.LGBMClassifier(objective='multiclass', num_class=3, metric='multi_logloss')

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá
accuracy = accuracy_score(y_test, y_pred)
print(f'LightGBM Accuracy: {accuracy}')


