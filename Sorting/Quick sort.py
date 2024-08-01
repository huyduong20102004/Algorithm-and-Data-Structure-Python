def quick_sort(arr):
    # Kiểm tra nếu mảng chỉ chứa 1 phần tử hoặc không có phần tử nào
    if len(arr) <= 1:
        return arr
    
    # Chọn phần tử trung vị làm pivot
    pivot = arr[len(arr) // 2]
    
    # Tách mảng thành các phần tử nhỏ hơn, bằng và lớn hơn pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Kết hợp các mảng con và pivot để tạo mảng kết quả
    return quick_sort(left) + middle + quick_sort(right)

arr = [6, 3, 8, 7, 1, 5, 10, 9, 2, 4]
print("Sorted array using Quick Sort:", quick_sort(arr))
