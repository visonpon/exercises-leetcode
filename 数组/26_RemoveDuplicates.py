class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        else:
            left = 0
            right = 1
            while right<len(nums):
                if nums[right] != nums[right-1]:
                    left += 1
                    nums[left] = nums[right]
                    right += 1
                else:
                    right += 1
            return left+1
	   
	   
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1
	
#替换和开辟空间放入思想！！！！
class Solution:
    def removeDuplicates(self, nums):
        lastIndex = 0
        lastNum = None
        for num in nums:
            if lastNum != num:
                lastNum = num
                nums[lastIndex]=lastNum
                lastIndex+=1
        return lastIndex

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r,curVal=0,0,None
        while r<len(nums):
            if nums[r]!=curVal:
                curVal=nums[r]
                nums[l]=curVal
                l+=1
            r+=1 #像这样，每次while都保证一次r的自增，就可以把while换成for循环了！所以这个答案和第二个答案是一样的。
        return l
