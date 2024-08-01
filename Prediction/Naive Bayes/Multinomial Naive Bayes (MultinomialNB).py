from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dữ liệu văn bản
data = fetch_20newsgroups(subset='all')
X = data.data
y = data.target

# Chuyển đổi văn bản thành đặc trưng tần suất
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.3, random_state=42)

# Khởi tạo và huấn luyện mô hình
model = MultinomialNB()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
