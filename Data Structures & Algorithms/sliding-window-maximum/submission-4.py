from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices, values decreasing front to back
        l = r = 0

        while r < len(nums):
            # pop smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove the front if it's slid out of the window
            if l > q[0]:
                q.popleft()

            # once the window is size k, record the max
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output