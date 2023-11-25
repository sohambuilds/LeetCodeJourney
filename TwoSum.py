#TimeComplexitity O(n)
class Solution(object):
  def twoSum(self,nums,target):
   
   seen = {}

   for i,num in enumerate(nums):
       if target-num in seen:
         return [seen[target-num],i]

       elif num not in seen:
            seen[num]=i
#OR

#TimeComplexity O(n^2)

class Solution2(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)-1):
           for j in range(i+1,len(nums)):
               if nums[i]+nums[j]==target:
                 return [i,j]
    
