import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Tạo mô hình CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # 32 bộ lọc 3x3
    MaxPooling2D((2, 2)),                                             # Tầng giảm mẫu
    Conv2D(64, (3, 3), activation='relu'),                            # 64 bộ lọc 3x3
    MaxPooling2D((2, 2)),                                             # Tầng giảm mẫu
    Flatten(),                                                        # Chuyển đổi dữ liệu thành dạng một chiều
    Dense(64, activation='relu'),                                    # 64 nút
    Dense(10, activation='softmax')                                  # 10 nút đầu ra cho phân loại
])

# Biên dịch mô hình
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Tóm tắt mô hình
model.summary()
