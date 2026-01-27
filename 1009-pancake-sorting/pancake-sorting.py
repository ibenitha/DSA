class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
    
        # Start from the largest number and go down
        for size in range(n, 1, -1):
            # Find the index of the largest number in the unsorted portion
            max_idx = arr.index(size)
        
            # If it's not already in the correct position
            if max_idx != size - 1:
                # Step 1: Flip it to the front if needed
                if max_idx != 0:
                    arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                    res.append(max_idx + 1)
            
                # Step 2: Flip it to its correct position
                arr[:size] = arr[:size][::-1]
                res.append(size)
    
        return res

        

    