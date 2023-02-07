# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_num = 0
        l2_num = 0
        i = 0
        while l1.next != None:
            l1_num += l1.val*(10**i)
            i += 1
            l1 = l1.next
        else:
            l1_num += l1.val*(10**i)
        i = 0
        while l2.next != None:
            l2_num += l2.val*(10**i)
            i += 1
            l2 = l2.next
        else:
            l2_num += l2.val*(10**i)

        total = str(l2_num + l1_num)
        answer = [int(i) for i in total]

        final_answer = []

        for num in range(len(answer)):
            if num == 0:
                final_answer.append(ListNode(val=answer[num]))
            else: 
                final_answer.append(ListNode(answer[num], final_answer[num-1]))
        return final_answer[-1]
