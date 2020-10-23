#含重置的回溯
# class Solution:
#     def subsets(self, nums):
#         res = []
#         for i in range(len(nums) + 1):  # 0 1 2 3
#             self.backtracking(nums, i, 0, [], res)
#         return res
#
#     def backtracking(self, nums, length: int, index: int, cur, res):
#         if len(cur) == length:
#             res.append(cur[:])
#             return
#         for i in range(index, len(nums)):
#             cur.append(nums[i])
#             self.backtracking(nums, length, i + 1, cur, res)
#             cur.pop()
#
#
# ss = Solution()
# cc = [1, 2, 3]
#
# dd = ss.subsets(cc)
# print(dd)

#.顺序考虑，仅考虑选择的元素
class Solution:
    def subsets(self, nums) :
        self.res = []
        self.backtrack([], 0, nums)

        return self.res

    def backtrack(self, sol, index, nums):
        self.res.append(sol)

        for i in range(index, len(nums)):
            self.backtrack(sol + [nums[i]], i + 1, nums)

ss = Solution()
cc = [1, 2, 3]

dd = ss.subsets(cc)
print(dd)

#全部考虑，选或不选
class Solution:
    def subsets(self, nums) :
        self.res = []
        self.backtrack([], 0, nums)
        return self.res

    def backtrack(self, sol, index, nums):
        if index == len(nums):
            self.res.append(sol)
            return

        self.backtrack(sol + [nums[index]], index + 1, nums)
        self.backtrack(sol, index + 1, nums)


