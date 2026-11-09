from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output=[]
        index_nums = defaultdict(list)
        for i in range(0,len(nums)):
            index_nums[nums[i]].append(i)
        for i in range(0,len(nums)):
            temp = target-nums[i]
            index_nums[nums[i]].pop(0)
            if temp in index_nums.keys() and index_nums[temp] != []:
                output.append(i)
                output.append(index_nums[temp][0])
                break
        if output[0]>output[1]:
            return [output[1],output[0]]
        else:
            return [output[0],output[1]]