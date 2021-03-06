class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,0
        minlength = len(nums)+1
        sums = 0
        while right<len(nums):
            while sums<s and right<len(nums):
                sums += nums[right]
                right+=1
            while sums>=s:
                sums -= nums[left]
                left+=1
            minlength = min(minlength, right-left+1)
			#注：这个时候，滑动窗口整体向前移了一格，即sums是由[left-1,right-1]区间内的元素累加而得。
        if minlength == len(nums)+1:
            return 0
        return minlength
		
#这题细节挺坑的。
一定要考虑清楚如果所有元素加起来还是比s小的情况。这种情况下，right-left+1=len(nums)+1
为什么会加个1，就是因为如果出现上述情况，那么r虽然加了1，但是l并没有，即，19行所说的整体向前在这种情况下是错误的，只有r向前了
因此，r-l就已经等于len(nums)了
所以，我们的minlen初始化必须是大于等于len(nums)+1的，这样20 21两行才会起作用。

def solution(arr,s):
    n = len(arr)
    start = 0
    sum = 0
    minlength = n+1
    for i in range(n):
        sum +=arr[i]
	while(sum>=s):
	    minlength  = min(minlength , i-start+1)
	    sum -=arr[start]
	    start +=1
    return minlength == n+1?0:minlength
