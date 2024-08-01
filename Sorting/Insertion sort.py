def insertion_sort(arr):
    for i in range(1, len(arr)):  # Bắt đầu từ phần tử thứ hai đến hết mảng
        key = arr[i]  # Lưu giữ giá trị của phần tử hiện tại
        j = i - 1  # Vị trí của phần tử trước đó trong dãy đã sắp xếp
        while j >= 0 and key < arr[j]:  # Di chuyển các phần tử lớn hơn khóa về phía trước
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Chèn phần tử vào vị trí đúng trong dãy đã sắp xếp


arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array using Insertion Sort:")
for i in range(len(arr)):
    print(arr[i], end=" ")