class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr = []
        p = 1
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                p *= nums[i]

        for j in range(len(nums)):
            if count > 1:
                arr.append(0)
            elif count == 1:
                if nums[j] == 0:
                    arr.append(p)
                else:
                    arr.append(0)
            else:
                arr.append(p // nums[j])
        return arr