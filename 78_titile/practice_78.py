# class Solution:
#     def subsets(self,nums):
#         self.res=[]
#         for i in range(len(nums)+1):
#             self.backtracking(nums,i,0,[])
#         return self.res
#     def backtracking(self,nums,length,index,cur):
#         if length==len(cur):
#             self.res.append(cur[:])
#             return
#         for i in range (index,len(nums)):
#             cur.append(nums[i])
#             self.backtracking(nums,length,i+1,cur)
#             cur.pop()

# cc=Solution()
# ff=cc.subsets([1,2,3])
# print(ff)

class S:
    def sub(self, nums):
        self.res = []
        for i in range(len(nums) + 1):
            self.backtrackff(nums, i, 0, [])
        return self.res

    def backtrackff(self, nums, length, index, cur):
        if length == len(cur):
            self.res.append(cur[:])
            return
        for i in range(index, len(nums)):
            cur.append(nums[i])
            self.backtrackff(nums, length, i + 1, cur)
            cur.pop()


cc = S()
ff = cc.sub([1, 2, 3])
print(ff)


class answer:
    def funcSub(self, nums):
        self.res = []
        for i in range(len(nums) + 1):
            self.bac(nums, i, 0, [])
        return self.res

    def bac(self, nums, length, index, cur):
        if length == len(cur):
            self.res.append(cur[:])
            return
        for i in range(index, len(nums)):
            cur.append(nums[i])
            self.bac(nums, length, i + 1, cur)
            cur.pop()


fes = answer()
hh = fes.funcSub([1, 2, 3])
print(hh)
