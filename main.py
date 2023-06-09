# Class for each individual node

class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference


node1 = Node(5)
node2 = Node(11)
node1.reference = node2
# print(node1.reference)

# Class for linked list


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print('The linked list is empty')
        else:
            c_node = self.head
            linked_list_string = ''
            while c_node:
                linked_list_string += f'{c_node.data} --> '
                c_node = c_node.reference
            print(linked_list_string)

    def add_to_start(self, data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node


linked_list1 = LinkedList()
linked_list1.add_to_start(83)
linked_list1.add_to_start(12)
linked_list1.add_to_start(node1.data)
# linked_list1.print_linked_list()

linked_list2 = LinkedList(node2)
linked_list2.add_to_start(25)
linked_list2.add_to_start(26)
linked_list2.print_linked_list()
