def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Nếu phần tử ở giữa là target, trả về chỉ số của nó
        if arr[mid] == target:
            return mid
        
        # Nếu target nhỏ hơn phần tử ở giữa, loại bỏ nửa phải của mảng
        elif arr[mid] > target:
            right = mid - 1
        
        # Nếu target lớn hơn phần tử ở giữa, loại bỏ nửa trái của mảng
        else:
            left = mid + 1
    
    # Trả về -1 nếu không tìm thấy target trong mảng
    return -1

# Ví dụ sử dụng
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
target = 11
result = binary_search(arr, target)

if result != -1:
    print(f"Phần tử {target} được tìm thấy tại vị trí {result}.")
else:
    print(f"Phần tử {target} không được tìm thấy trong mảng.")
