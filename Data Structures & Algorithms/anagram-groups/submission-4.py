from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict=defaultdict(list)
        for i in strs:
            count_dict={}
            if i.strip() != "":
                for j in i:
                    count_dict[j]=count_dict.get(j,0)+1
            else:
                strs_dict[""].append("")
            if count_dict != {}:
                strs_dict[tuple(sorted(count_dict.items()))].append(i)
        output=[]
        for i in strs_dict:
            output.append(strs_dict[i])
        return output