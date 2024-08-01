def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Tạo thùng và phân phối các phần tử vào các thùng tương ứng
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Phân phối các phần tử vào thùng
    for num in arr:
        # Tính chỉ số thùng và đảm bảo nó là số nguyên
        index = int((num - min_val) * (bucket_count - 1) / (max_val - min_val))
        buckets[index].append(num)
    
    # Sắp xếp từng thùng và hợp nhất kết quả
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Ví dụ sử dụng
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.68, 0.84, 0.73, 0.50]
sorted_arr = bucket_sort(arr)
print("Sắp xếp thùng:", sorted_arr)

