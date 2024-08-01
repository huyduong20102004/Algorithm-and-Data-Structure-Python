def counting_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Tìm giá trị lớn nhất và nhỏ nhất trong danh sách
    max_val = max(arr)
    min_val = min(arr)
    
    # Tạo mảng đếm với kích thước đủ để chứa tất cả các giá trị
    count = [0] * (max_val - min_val + 1)
    
    # Đếm số lần xuất hiện của từng giá trị
    for num in arr:
        count[num - min_val] += 1
    
    # Xây dựng danh sách đã sắp xếp từ mảng đếm
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i + min_val] * cnt)
    
    return sorted_arr

# Ví dụ sử dụng
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sắp xếp đếm:", sorted_arr)
