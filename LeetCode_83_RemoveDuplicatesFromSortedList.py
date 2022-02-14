
class Solution(object):
    def deleteDuplicates(self, head):
        current_node = head
        while current_node!=None and current_node.next!=None:
            if (current_node.val == current_node.next.val):
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head

"""

    if not head:
        return None
            curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr=curr.next
    return head

""""