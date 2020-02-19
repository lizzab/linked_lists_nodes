# Ben Lizza
# 02/19/20

# Making a driver to use the linked list and node

from linked_lists import SingleLinkedList

mylist = SingleLinkedList()
print(mylist)

mylist.prepend(24)
mylist.prepend(49)
mylist.prepend(69)
mylist.prepend('Hello')
mylist.prepend('Good morning')

print(mylist)
