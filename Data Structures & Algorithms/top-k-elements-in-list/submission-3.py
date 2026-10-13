from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums=defaultdict(int)
        nums_sett=set(nums)
        for i in nums_sett:
            count_nums[i]=0
            output_list=[i]

        for i in nums:
            count_nums[i]+=1
        
        output_list=output_list*k
        exception_list=[]

        #edge cases
        if len(nums_sett)==1:
            return [nums[0]]

        #edge cases
        if k==len(nums_sett):
            for i in count_nums:
                exception_list.append(i)
            return exception_list

        for i in range(k):
            best = max(count_nums, key=count_nums.get)
            output_list[i] = best
            count_nums.pop(best)
        return output_list
