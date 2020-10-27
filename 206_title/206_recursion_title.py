class Solution:
    def recursion(self,head):
        if not head or not head.next:
            return head
        p=self.recursion(head.next)
        head.next.next=head
        head.next=None
        return p
