class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._heapify_down(0)
        return min_val

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _heapify_down(self, idx):
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            smallest_idx = idx

            if (left_child_idx < len(self.heap) and
                    self.heap[left_child_idx] < self.heap[smallest_idx]):
                smallest_idx = left_child_idx

            if (right_child_idx < len(self.heap) and
                    self.heap[right_child_idx] < self.heap[smallest_idx]):
                smallest_idx = right_child_idx

            if smallest_idx != idx:
                self.heap[idx], self.heap[smallest_idx] = self.heap[smallest_idx], self.heap[idx]
                idx = smallest_idx
            else:
                break

# Sử dụng heap
heap = MinHeap()
heap.insert(5)
heap.insert(10)
heap.insert(3)
heap.insert(8)
heap.insert(1)

print("Extracted min:", heap.extract_min())  # In ra giá trị nhỏ nhất từ heap
print("Extracted min:", heap.extract_min())  # In ra giá trị nhỏ nhất từ heap
print("Extracted min:", heap.extract_min())  # In ra giá trị nhỏ nhất từ heap
