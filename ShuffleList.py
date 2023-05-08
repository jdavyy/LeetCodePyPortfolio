
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
    
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return nums
        else: 
            stack = []
            stack.append(0)
            x = 0
            for item in nums:
                print(x)
                a = stack[x] + nums[x]
                stack.append(a)
                x += 1
        
        stack.pop(0)
        return stack
    
nums = [1,2,3,4]
nums2 = [1,1,1,1,1]
nums3 = [3,1,2,10,1]
print(solution.runningSum(nums))
print(solution.runningSum(nums2))
print(solution.runningSum(nums3))
    
numba = [1,2,3,4,5,6,7,8]
nn = 4
solution = Solution()
print(solution.shuffle(numba, nn))
