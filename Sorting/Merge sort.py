def merge_sort(arr):
    # Nếu mảng chỉ chứa 1 phần tử hoặc không có phần tử nào, trả về mảng đó
    if len(arr) <= 1:
        return arr
    
    # Tìm chỉ số giữa của mảng
    mid = len(arr) // 2
    
    # Gọi đệ quy để sắp xếp từng nửa của mảng
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Kết hợp hai mảng đã sắp xếp để tạo mảng kết quả
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # So sánh từng phần tử trong hai mảng và chọn phần tử nhỏ hơn để thêm vào mảng kết quả
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Thêm các phần tử còn lại của mỗi mảng vào mảng kết quả
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

arr = [3, 6, 8, 10, 1, 2, 4]
print("Sorted array using Merge Sort:", merge_sort(arr))
