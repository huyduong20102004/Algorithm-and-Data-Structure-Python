import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Tạo mô hình MLP
model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),  # 64 nút, kích thước đầu vào 784
    Dense(32, activation='relu'),                      # 32 nút
    Dense(10, activation='softmax')                    # 10 nút đầu ra cho phân loại
])

# Biên dịch mô hình
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Tóm tắt mô hình
model.summary()
