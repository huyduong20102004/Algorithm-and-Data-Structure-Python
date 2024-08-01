def bubble_sort(arr):
    n = len(arr)  # Lấy độ dài của mảng
    for i in range(n):  # Lặp qua tất cả các phần tử trong mảng
        for j in range(0, n-i-1):  # Lặp qua tất cả các phần tử chưa được sắp xếp
            if arr[j] > arr[j+1]:  # So sánh hai phần tử liền kề
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Nếu phần tử trước lớn hơn, đổi chỗ hai phần tử

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array using Bubble Sort:")
for i in range(len(arr)):
    print(arr[i], end=" ")