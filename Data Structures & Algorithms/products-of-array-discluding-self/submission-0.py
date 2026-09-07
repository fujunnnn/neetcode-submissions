class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total : int = 1
        zero = []
        res = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(i)
            else:
                total *= nums[i]

        for i in range(len(nums)):
            if len(zero) > 1:
                res.append(0)
            elif len(zero) == 1:
                if i == zero[0]:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append((int)(total/ nums[i]))

        return res
        