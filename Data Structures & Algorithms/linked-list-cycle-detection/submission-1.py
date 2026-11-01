class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_set = set()

        current = head

        while current:
            if current in my_set:
                return True

            my_set.add(current)
            current = current.next

        return False