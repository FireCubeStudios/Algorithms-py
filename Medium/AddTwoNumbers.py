from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution:
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        return







# Cursed non-recursive solution
class SolutionCursed:  
    # Initialise x and y with head value of each LinkedList node
    # Loop both LinkedLists in while loop starting from the next node
    # For each iteration multiply by (10 * i) where i = 0 to represent placeholder positions and increment i *= 10
    # Add the values then convert to a reverse LinkedList
    # The runtime should be O(n) linear to linked list size
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = self.LinkedListToInt(l1) 
        y = self.LinkedListToInt(l2) 
        num = x + y

        # Loop over digits to convert to LinkedList
        placeholder = 10
        head = list = ListNode(num % placeholder)
        lastDigit = num % placeholder
        while True:
            if(num / placeholder >= 1):
                list.next = ListNode((int)(((num % (placeholder * 10)) - lastDigit) / placeholder))
                lastDigit = num % (placeholder * 10)
                list = list.next   
                placeholder *= 10 # Move to next placeholder
            else: 
                break # Digits ended
            
        return head # Return start of LinkedList
    
    # Convert a LinkedList with digits stored in a reverse order into an integer e.g [2,4,3] = 342
    def LinkedListToInt(self, list: Optional[ListNode]) -> int:
        x = list.val
        i = 1 # For placeholders, start it at 1 as we already put the unit place value for x
        while list.next != None:
            list = list.next
            x += list.val * (i * 10)
            i *= 10
        return x