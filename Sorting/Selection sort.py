def selection_sort(arr):
    n = len(arr)  # Lấy độ dài của mảng
    for i in range(n):  # Lặp qua tất cả các phần tử trong mảng
        min_idx = i  # Giả sử phần tử hiện tại là nhỏ nhất
        for j in range(i+1, n):  # Tìm phần tử nhỏ nhất trong phần chưa sắp xếp
            if arr[j] < arr[min_idx]:  # So sánh các phần tử và cập nhật chỉ số của phần tử nhỏ nhất
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Đổi chỗ phần tử nhỏ nhất với phần tử đầu tiên trong phần chưa sắp xếp


arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array using Selection Sort:")
for i in range(len(arr)):
    print(arr[i], end=" ")