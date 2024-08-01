def heapify(arr, n, i):
    # Khởi tạo largest là vị trí của nút hiện tại
    largest = i
    left = 2 * i + 1  # Vị trí của nút con bên trái
    right = 2 * i + 2  # Vị trí của nút con bên phải
    
    # So sánh giá trị của nút con bên trái với nút hiện tại
    if left < n and arr[left] > arr[largest]:
        largest = left
    # So sánh giá trị của nút con bên phải với nút hiện tại
    if right < n and arr[right] > arr[largest]:
        largest = right 

    # Nếu largest đã thay đổi, thực hiện hoán đổi giữa nút hiện tại và nút có giá trị lớn nhất
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Tiếp tục thực hiện heapify trên nút con có giá trị lớn nhất đã thay đổi
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)      

    # Xây dựng heap tối ưu
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Trích xuất các phần tử từ heap một cách tuần tự để sắp xếp mảng
    for i in range(n-1, 0, -1):
        # Hoán đổi phần tử cuối cùng với phần tử đầu tiên của heap
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify lại heap với kích thước giảm đi 1 và nút gốc là 0
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array using Heap Sort:", arr)













0

