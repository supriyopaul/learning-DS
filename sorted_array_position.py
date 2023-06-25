class Solution():
    def __init__(self, arr, x):
        self.arr = arr
        self.x = x
        self.first_pos = -1
        self.last_pos = -1
        self.length = len(arr)

    def find_positions(self, start, end):
        #print(start, end)
        arr_len = end - start
        #print(self.arr[start:end])
        #import pdb; pdb.set_trace()
        mid = int((start+end)/2)
        mid_value = self.arr[mid]

        if  arr_len > 1:
            if self.x <= mid_value:
                return self.find_positions(start, int((start+end)/2))
            elif self.x > mid_value:
                return self.find_positions(int((start+end)/2)+1, end)
            else: return mid
        print(start, end)
        if self.arr[start] == self.x: return start
        return -1
    
if __name__ == '__main__':
    sol = Solution(arr=[1, 1, 2, 2, 2, 3, 4, 7, 8, 9], x=2)
    print(sol.find_positions(start=0, end=9)) # [1,7]