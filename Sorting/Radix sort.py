def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    # Lặp qua các chữ số của các phần tử
    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        
        # Phân phối các phần tử vào các bucket dựa trên chữ số tương ứng
        for i in arr:
            # Tính chỉ số bucket cho phần tử hiện tại
            tmp = int((i / placement) % RADIX)
            # Đặt phần tử vào bucket tương ứng
            buckets[tmp].append(i)
        
        # Hợp nhất các bucket thành mảng mới
        a = 0
        for b in range(RADIX):
            # Duyệt qua từng bucket
            buck = buckets[b]
            for i in buck:
                # Gán phần tử từ bucket vào mảng ban đầu
                arr[a] = i
                a += 1
        # Di chuyển đến chữ số tiếp theo
        placement *= RADIX

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array using Radix Sort:", arr)

