class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:

            L, R = 0, len(i) - 1
            while L<=R:
                mid = (L+R)//2
                if target > i[mid]:
                    L = mid + 1
                elif target < i[mid]:
                    R = mid - 1
                elif target == i[mid]:
                    return True
        return False