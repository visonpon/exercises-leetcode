#0,1,2 for red/while/blue.
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        pointer = 0
        right = len(nums)-1
        while pointer<=right:# =?
            if nums[pointer]==0:
                nums[left],nums[pointer]=nums[pointer],nums[left]
                left+=1
                pointer+=1
            elif nums[pointer]==1:
                pointer+=1
            else:
                nums[right],nums[pointer]=nums[pointer],nums[right]
                right-=1
                
    
class Solution {
    public:
        void sortColors(vector<int>& nums) {
            int red = 0, blue = (int)nums.size() - 1;
            for (int i = 0; i <= blue; ++i) {
                if (nums[i] == 0) {
                    swap(nums[i], nums[red++]);
                } else if (nums[i] == 2) {
                    swap(nums[i--], nums[blue--]);
                } 
            }
        }
    }
    
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0, right = (int)nums.size() - 1, cur = 0;
        while (cur <= right) {
            if (nums[cur] == 0) {
                swap(nums[cur++], nums[left++]);
            } else if (nums[cur] == 2) {
                swap(nums[cur], nums[right--]);
            } else {
                ++cur;
            }
        }
    }
}
