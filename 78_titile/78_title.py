class Solution:
    def subsets(self, nums):
        res = []
        for i in range(len(nums) + 1):  # 0 1 2 3
            self.backtracking(nums, i, 0, [], res)
        return res

    def backtracking(self, nums, length: int, index: int, cur, res):
        if len(cur) == length:
            res.append(cur[:])
            return
        for i in range(index, len(nums)):
            cur.append(nums[i])
            self.backtracking(nums, length, i + 1, cur, res)
            cur.pop()


ss = Solution()
cc = [1, 2, 3]

dd = ss.subsets(cc)
print(dd)
