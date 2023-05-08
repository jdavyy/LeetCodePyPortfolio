
#Shuffle a list


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l1 = nums[:n]
        l2 = nums[n:]
        shuffled = []
        for i in range(len(l1)):
            shuffled.append(l1[i])
            shuffled.append(l2[i])
        
        return shuffled
    
numba = [1,2,3,4,5,6,7,8]
nn = 4
solution = Solution()
print(solution.shuffle(numba, nn))