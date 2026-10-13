import string
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        count_t = {}
        count_s = {}
        index_sn={} # no dupe index
        index_sd={} # dupe index
        dupecheck = set(t) # set to check if dupes are there or no
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        output = s + " "

        temp1=0
        temp2=0
        count = 0
        x=str()
        if len(dupecheck) == len(t):
            for R in range(len(s)):
                if s[R] in dupecheck:
                    count_s[s[R]] = count_s.get(s[R], 0) + 1
                    index_sn[s[R]] = R
                if count_s.keys() == count_t.keys():
                    output =min(output, s[min(index_sn.values()):max(index_sn.values())+1], key=len)
        else:
            # to get count of all the chars that we need throughout the str
            for R in range(len(s)):
                if s[R] in dupecheck:
                    count_s[s[R]] = count_s.get(s[R], 0) + 1
                if count_t.items()<=count_s.items():
                    x=s[:R+1]
                    for L in range(len(x)):
                        if s[L] in count_s and count_s[s[L]]<=count_t[s[L]]:
                            temp1=L
                            break
                        elif s[L] in count_s and count_s[s[L]]>count_t[s[L]]:
                            count_s[s[L]]-=1
                            temp1=L                        
                    for L in range(len(x)-1, -1, -1):
                        if s[L] in count_s and count_s[s[L]]<=count_t[s[L]]:
                            temp2=L
                            break
                        elif s[L] in count_s and count_s[s[L]]>count_t[s[L]]:
                            count_s[s[L]]-=1
                            temp2=L                         
                    output = min(output,s[temp1:temp2+1], key=len)  

            # to check if the substring answer is even existing
            for R in count_s:
                if count_s[R]>=count_t[R]:
                    count += 1
            if count != len(count_t):
                return ""
            else:
                for L in range(len(s)):
                    if s[L] in count_s and count_s[s[L]]<=count_t[s[L]]:
                        temp1=L
                        break
                    elif s[L] in count_s and count_s[s[L]]>count_t[s[L]]:
                        count_s[s[L]]-=1
                        temp1=L                        
                for L in range(len(s)-1, -1, -1):
                    if s[L] in count_s and count_s[s[L]]<=count_t[s[L]]:
                        temp2=L
                        break
                    elif s[L] in count_s and count_s[s[L]]>count_t[s[L]]:
                        count_s[s[L]]-=1
                        temp2=L                         
                output = min(output,s[temp1:temp2+1], key=len)               


        if output == s + " ":
            return ""
        else:
            return output
                

