class Solution:
    def purchasePlans( nums, target):
        nums.sort()
        ans = 0
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                ans += (j-i)
                i += 1
        if ans<=1000000007:
            return ans
        else:
            return ans%1000000007

    i = purchasePlans([1,2,3,4],3)
    print(i)