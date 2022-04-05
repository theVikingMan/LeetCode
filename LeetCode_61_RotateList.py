# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    # edge case of no or just one node given
    if not head or not head.next:
        return head

    # Find the length of the linked list and to set up the circular LL
    lastElem = head
    length = 1
    while lastElem.next:
        lastElem = lastElem.next
        length += 1

    # Mathy but tells you in a effiecent way how many times to rotate
    # based on length and desired rotations
    k = k % length

    # Create circular LL
    lastElem.next = head

    # Find where to break the LL by getting the node right before the one we want
    # Example: In 1->2->3->4->5, and k = 2
    #   we need to get to the Node(3)
    tempNode = head
    for _ in range(length - k - 1):
        tempNode = tempNode.next

    # Grab the node that will be the new head node
    answer = tempNode.next
    # Break the LL
    tempNode.next = None

    return answer
