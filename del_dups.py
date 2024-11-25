def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # Handle empty list
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node

        return head