from typing import List

def twoSum(nums: List[int], target: int) -> List[int]
        sizeOfNums = len(nums)
        result = ""
        for i in range(0, sizeOfNums, 1):
            for j in range(i, sizeOfNums, 1):
                if(nums[i]+nums[j] == target):
                  result = "[" + i +"," + j + "]"
        
        return result   