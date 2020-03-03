# Ben Lizza
# 02/19/20

# Making a driver to use the linked list and node

from linked_lists import SingleLinkedList

my_list = SingleLinkedList()
print(my_list)

my_list.prepend(24)
my_list.prepend(49)
my_list.prepend(69)
my_list.prepend('Hello')
my_list.prepend('Good morning')

print(my_list)

print(SingleLinkedList.add_tail())
