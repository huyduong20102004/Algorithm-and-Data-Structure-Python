from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Tải dữ liệu
data = load_iris()
X, y = data.data, data.target

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Khởi tạo mô hình AdaBoost với DecisionTreeClassifier mặc định là bộ phân loại cơ sở
model = AdaBoostClassifier(n_estimators=50, random_state=42)

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán và đánh giá
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy of AdaBoost: {accuracy:.2f}')




