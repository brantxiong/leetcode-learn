# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        protect = ans
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                protect.next = l1
                l1 = l1.next
            else:
                protect.next = l2
                l2 = l2.next
            protect = protect.next
            self.printNodeList("l1", l1)
            self.printNodeList("l2", l2)
            self.printNodeList("protect", protect)
            self.printNodeList("ans", ans)
        if l1:
            protect.next = l1
        else:
            protect.next = l2
        return ans.next

    def printNodeList(self, name, l):
        print(name+":", end="")
        while l != None:
            print(l.val, end="->")
            l = l.next
        print("")

# @lc code=end

