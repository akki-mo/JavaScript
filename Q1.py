class Solution:
    def count_swaps(self, arr):
        n = len(arr)
        if n <= 1:  
            return 0
        
        swaps_asc = 0
        swaps_desc = 0
        
       
        arr_asc = arr[:]
        arr_desc = arr[:]
        
        for i in range(n):
            for j in range(n - 1):
                if arr_asc[j] > arr_asc[j + 1]:
                    arr_asc[j], arr_asc[j + 1] = arr_asc[j + 1], arr_asc[j]
                    swaps_asc += 1
        
        
        for i in range(n):
            for j in range(n - 1):
                if arr_desc[j] < arr_desc[j + 1]:
                    arr_desc[j], arr_desc[j + 1] = arr_desc[j + 1], arr_desc[j]
                    swaps_desc += 1
        
        return min(swaps_asc, swaps_desc)



if __name__ == "__main__":
    N = int(input().strip()) 
    arr = list(map(int, input().strip().split())) 
    
    
    solution = Solution()
    

    result = solution.count_swaps(arr)
    
  
    print(result)
