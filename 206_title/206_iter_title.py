def Solution(head):
    pre=None
    cur=head
    while cur:
        temp=head.next
        cur.next=pre
        pre=cur
        cur=temp
    return pre