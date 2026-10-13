class Solution:
    def countBits(self, n: int) -> List[int]:
        output_list=[]

        for i in range(0,n+1):
            output_list.append(i)

        L=0
        count=0
        while L<len(output_list):
            if output_list[L]<=0:
                output_list[L]=count
                count=0
                L+=1
                
            if L>=len(output_list):
                break

            if output_list[L]>0 and output_list[L]%2 == 1:
                count+=1
                output_list[L]=output_list[L]//2
            else:
                output_list[L]=output_list[L]//2

        return output_list

