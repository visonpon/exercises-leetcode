class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k=self.findKthLargestHelper(nums,len(nums)-k,0,len(nums)-1)#注意这里的转换，从小到大排序，第k大的元素，其索引是len(arr)-k.
        return k
        
    def findKthLargestHelper(self,nums,k,first,last):
        splitpoint = self.partition(nums,first,last)
        if k<splitpoint:
            return self.findKthLargestHelper(nums,k,first,splitpoint-1)
        elif k>splitpoint:
            return self.findKthLargestHelper(nums,k,splitpoint+1,last)
        else:
            return nums[splitpoint]
        
    def partition(self,nums,first,last):
        pivotvalue = nums[first]
        left = first+1
        right = last
        done = False
        while not done:
            while left<=right and nums[left]<pivotvalue:
                left+=1
            while left<=right and nums[right]>pivotvalue:
                right-=1
            if left>right:
                done=True
            else:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        nums[first],nums[right]=nums[right],nums[first]
        return right

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: in
        """
        heap = []
        for i,j in enumerate(nums):
            if i < k:
                heapq.heappush(heap, j)
            else:
                heapq.heappushpop(heap, j)
        return heapq.heappop(heap)
		
'''
第一个算法是On，第二个算法是Onlogm，只是第一个算法的常数项太大，在数据很少的时候，效率比不过第二个函数。
第二个算法老师也讲过，就是堆的妙用。但是第二个算法求出了前m个最大项，而我只需要取第m大的项，所以第二个算法是浪费效率的。
'''
