# iterate the array
# -> keep each value (key) with its index (value) in a hashmap
# -> if the same value occurs again, ignore it (we return the first occuring, smaller index)
# -> for each array element, check if target - element is present in hashmap
# -> return this pair of indices
# -> else return empty array 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dic:
                return [dic[diff], i]
            
            dic[nums[i]] = i
            print(dic)
        
        return []
