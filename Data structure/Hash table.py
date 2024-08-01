class HashTable:
    def __init__(self, size):
        self.size = size  # Kích thước của bảng băm
        self.hash_table = [[] for _ in range(size)]  # Khởi tạo bảng băm với danh sách rỗng

    def _hash_function(self, key):
        return hash(key) % self.size  # Sử dụng hàm băm tích hợp của Python

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        for pair in self.hash_table[hash_key]:
            if pair[0] == key:  # Nếu khóa đã tồn tại, cập nhật giá trị mới
                pair[1] = value
                return
        self.hash_table[hash_key].append([key, value])  # Thêm cặp (khóa, giá trị) mới

    def search(self, key):
        hash_key = self._hash_function(key)
        for pair in self.hash_table[hash_key]:
            if pair[0] == key:  # Nếu khóa được tìm thấy, trả về giá trị tương ứng
                return pair[1]
        return None  # Nếu không tìm thấy, trả về None

    def delete(self, key):
        hash_key = self._hash_function(key)
        for i, pair in enumerate(self.hash_table[hash_key]):
            if pair[0] == key:  # Nếu khóa được tìm thấy, xóa cặp (khóa, giá trị)
                del self.hash_table[hash_key][i]
                return

# Sử dụng bảng băm
hash_table = HashTable(10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
hash_table.insert("orange", 15)

print("Value for 'apple':", hash_table.search("apple"))  # In ra giá trị tương ứng với khóa "apple"
print("Value for 'banana':", hash_table.search("banana"))  # In ra giá trị tương ứng với khóa "banana"
print("Value for 'orange':", hash_table.search("orange"))  # In ra giá trị tương ứng với khóa "orange"

hash_table.delete("banana")  # Xóa cặp (khóa, giá trị) có khóa là "banana"

print("Value for 'banana' after deletion:", hash_table.search("banana"))  # In ra giá trị tương ứng với khóa "banana" sau khi đã xóa


