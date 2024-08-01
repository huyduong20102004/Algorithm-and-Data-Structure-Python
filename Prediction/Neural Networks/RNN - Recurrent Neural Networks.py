import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Tạo mô hình RNN
model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(None, 10)),  # 50 nút RNN, đầu vào có kích thước (None, 10)
    Dense(20, activation='relu'),                               # 20 nút
    Dense(1, activation='sigmoid')                              # Nút đầu ra cho phân loại nhị phân
])

# Biên dịch mô hình
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Tóm tắt mô hình
model.summary()
