from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs] 
        output_dict=defaultdict(list)
        output=[]
        for i in strs:
            temp_dict={}
            for j in i:
                temp_dict[j] = temp_dict.get(j, 0) + 1
            k=tuple(sorted(temp_dict.items()))
            output_dict[k].append(i)
        
        for i in output_dict:
            output.append(output_dict[i])
        
        return output
