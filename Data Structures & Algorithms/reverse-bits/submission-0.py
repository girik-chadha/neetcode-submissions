class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, '032b')
        n=list(n)
        n.reverse()

        for i in range(len(n)):
            n[i]=int(n[i])

        final=0
        j=0
        for i in range(31,-1,-1):
            final+=n[i]*(2**j)
            j+=1
        return final