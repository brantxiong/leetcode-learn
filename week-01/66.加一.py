# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        result = []
        carry = 0
        added = False
        while i >= 0:
            temp = digits[i] + carry
            if not added:
                temp += 1
                added = True
            # 处理进位
            if temp >= 10:
                temp %= 10
                carry = 1
            else:
                carry = 0
            
            result.insert(0, temp)
            
            i -= 1
        if carry == 1:
            result.insert(0, carry)

        return result
# @lc code=end

