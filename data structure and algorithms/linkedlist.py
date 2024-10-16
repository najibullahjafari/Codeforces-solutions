class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        less_head = ListNode(0)
        greater_head = ListNode(0)

        less = less_head
        greater = greater_head

        current = head
        while current:
            if current.val < x:
                less.next = current  # Link current node to the "less" list
                less = less.next  # Move the pointer forward
            else:
                greater.next = current  # Link current node to the "greater" list
                greater = greater.next  # Move the pointer forward
            current = current.next  # Move to the next node

        # Connect the less list with the greater list
        greater.next = None  # End the greater list
        # Link the end of less list to the head of greater list
        less.next = greater_head.next

        return less_head.next  # Return the head of the new partitioned list


def linked_list_to_list(head):
    """Convert a linked list to a Python list."""
    numbers = []
    current = head
    while current:
        numbers.append(current.val)
        current = current.next
    return numbers


# Example usage
head = ListNode(1, ListNode(4, ListNode(
    3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3

solution = Solution()
new_head = solution.partition(head, x)

# Convert the new linked list to a Python list for easy verification
output_list = linked_list_to_list(new_head)
print(output_list)  # Expected output: [1, 2, 2, 4, 3, 5]
