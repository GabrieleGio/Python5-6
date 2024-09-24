"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 22222455

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Example 2:

Input: nums = [1,1,1]
Output: 0

 

Constraints:

    n == nums.length
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    The answer is guaranteed to fit in a 32-bit integer.


"""
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        if len(nums)>1:
            numeridacambiare = len(nums)-1
            numeromax = max(nums)
        elif len(nums)==1:
            return nums
        elif len(nums) == 0:
            return "Errore la lista è vuota"
        t = True
        for n in range(0,len(nums)-2):
            if t == True:
                if nums[n]!=nums[n+1]:
                    t = False 
                    break
    
        if t==True:
            return nums
               
        else:
            mosse = 0
            z = True
            while numeridacambiare != 0:
                for n in nums:
                    if n < numeromax and numeridacambiare != 0:
                        nums[n] = nums[n]+1
                        numeridacambiare -= 1
                    
                    if n == numeromax and numeridacambiare != 0:
                        nums[n] = nums[n]+1
                        numeridacambiare -= 1

                    if numeridacambiare == 0:
                        mosse+=1
                        z = True
                        for n in range(0,len(nums)-2):
                            if z == True:
                                if nums[n]!=nums[n+1]:
                                    z = False 
                                    
                    if z==True: 
                        break
                        
        return f"lista{nums}, numero mosse{mosse}"
classe1=Solution()
print(classe1.minMoves([2,3,2,2,5,3,5]))
                    
    
       
                


                
        
        