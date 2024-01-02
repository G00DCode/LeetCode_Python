class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng=len(nums)
        for i in range(leng):
            x= target-nums[i]
            for j in range(i+1,leng):
                if(nums[j]==x):
                    return [i,j]
        
