# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or not head.next: # edge case of no or just one node given
        return head

    lastElem, length = head, 1 # Find the length of the LL + set up the circular LL
    while lastElem.next:
        lastElem = lastElem.next
        length += 1

    # effiecent way how many times to rotate based on length and desired rotations
    k = k % length
    lastElem.next = head # Create circular LL

    # Find where to break the LL by getting the node right before the head of new LL
    # Example: In 1 -> 2 -> 3 -> 4 -> 5, and k = 2
    #   we need to get to the Node(2)
    tempNode = head
    for _ in range(length - k - 1):
        tempNode = tempNode.next

    answer = tempNode.next # Grab the node that will be the new head node
    tempNode.next = None # Break the LL

    return answer