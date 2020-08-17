class Solution:
    '''这道题的关键思路就是倒着来，从大到小，倒着填入列表，和归并是反过来的'''
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m and n:
            if nums1[m-1]<=nums2[n-1]:
                nums1[m+n-1]=nums2[n-1]
                n-=1
            else:
                nums1[m+n-1]=nums1[m-1]
                m-=1
        if n:
            nums1[:n]=nums2[:n]
            
    
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):       
        index_total = m + n - 1
        indexA = m-1
        indexB = n-1   
        while indexA >= 0 and indexB >= 0 :
            if A[indexA] > B[indexB]:
                A[index_total] = A[indexA]
                indexA -= 1
            else:
                A[index_total] = B[indexB]
                indexB -= 1
            index_total -= 1
            
        if indexA >= 0:
            while indexA >= 0:
                A[index_total] = A[indexA]
                indexA -= 1
                index_total -= 1
        else:
            while indexB >= 0:
                A[index_total] = B[indexB]
                indexB -= 1
                index_total -= 1
