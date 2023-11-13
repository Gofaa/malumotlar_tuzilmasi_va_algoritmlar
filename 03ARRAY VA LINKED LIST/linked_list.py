# class Node:
#     """tugun Node obyekti"""
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __int__(self):
#         self.head = None
#
#     def PrintList(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next
#
#
# # Linked List yaratamiz
#
# llist = LinkedList()
#
# # 3 ta tugun yaratamiz
# llist.head = Node('Dushanba')
# tuesday = Node("Seshanba")
# wednesday = Node("Chorshanba")
#
# llist.head.next = tuesday
# tuesday.next = wednesday

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
#
#
#
# print(faktorial(3))

def sonlar(i=11):
    print(i)
    if i<=1:
        return
    else:
        sonlar(i-1)


sonlar()