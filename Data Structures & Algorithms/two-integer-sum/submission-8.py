from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = defaultdict(list)
        for i in range(0,len(nums)):
            index[nums[i]].append(i)
        index2 = index.copy() 

        for i in range(0,len(nums)):
            k = target-nums[i]
            if len(index2[nums[i]])<2:
                del index2[nums[i]]
            else:    
                index2[nums[i]].remove(i)

            if k in index2 and index[k][0] != i:
                if i>index[k][0]:
                    return [index[k][0], i]
                else:
                    return [i, index[k][0]]
            index2 = index.copy()