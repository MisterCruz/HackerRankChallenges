class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
        if head == None:
            head = Node(data)
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
        return head
