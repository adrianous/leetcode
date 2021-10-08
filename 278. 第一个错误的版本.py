# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        if isBadVersion(0):
            return 1

        while low <= high:
            mid = (low + high) // 2
            res = isBadVersion(mid)
            if res:
                if mid > 1 and  not isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1