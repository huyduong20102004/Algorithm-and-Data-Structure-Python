import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_classification

# Tạo dữ liệu phân loại giả lập
X, y = make_classification(n_samples=100, 
                           n_features=2, 
                           n_informative=2, 
                           n_redundant=0, 
                           n_clusters_per_class=1, 
                           random_state=42)

# Khởi tạo mô hình SVC
svc = SVC(kernel='linear', C=1.0)
svc.fit(X, y)

# Vẽ quyết định biên
def plot_decision_boundary(X, y, model):
    h = .02  # Độ phân giải của lưới
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Support Vector Classification (SVC)')
    plt.show()

plot_decision_boundary(X, y, svc)

