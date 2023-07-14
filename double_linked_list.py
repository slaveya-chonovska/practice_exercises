class Node:
    def __init__(self,value) -> None:
        self.next = None
        self.prev = None
        self.value = value

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_start(self,value):
        new_node = Node(value)

        if self.find_node_by_value(value):
            raise Exception("Cannot add values that already exist in the list!")

        new_node.next = self.head
        new_node.prev = None

        #if the list already had a head
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_end(self,value):
        new_node = Node(value)

        if self.find_node_by_value(value):
            raise Exception("Cannot add values that already exist in the list!")

        last = self.head

        # if the head is empty just insert a new head
        if last is None:
            self.insert_start(value)
            return

        #find the last element
        while last.next != None:
            last = last.next

        new_node.next = None
        last.next = new_node
        new_node.prev = last

    def insert_after_node(self,prev_value,new_value):
        prev_node = self.find_node_by_value(prev_value)

        if not prev_node:
            return "No such node exists."

        new_node = Node(new_value)

        if self.find_node_by_value(new_value):
            raise Exception("Cannot add values that already exist in the list!")
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        # if it is not the last element
        if new_node.next is not None:
            new_node.next.prev = new_node
        
    def delete_node(self,value):
        node_to_delete = self.find_node_by_value(value)
        if not node_to_delete:
            return "No node with that value"
        
        # if it is the head
        if node_to_delete == self.head:
            self.head = node_to_delete.next
        # if it is not the last node change next node
        if node_to_delete.next != None:
            next_node = node_to_delete.next
            next_node.prev = node_to_delete.prev
            #node_to_delete.next.prev = node_to_delete.prev
        # if it is not the first node change prev node
        if node_to_delete.prev != None:
            previous_node = node_to_delete.prev
            previous_node.next = node_to_delete.next
            #node_to_delete.prev.next = node_to_delete.next


    #check if a value already exists
    def find_node_by_value(self,value):
        nodes = self.head
        while nodes !=None:
            if nodes.value == value:
                return nodes
            nodes = nodes.next
        return False
    
    #display the whole list
    def display(self):
        nodes = self.head
        while nodes !=None:
            print(nodes.value)
            nodes = nodes.next

    @property
    def length(self):
        count_nodes = 0
        nodes = self.head
        while nodes !=None:
            count_nodes = count_nodes+1
            nodes = nodes.next
        return count_nodes


linked_list = DoubleLinkedList()
linked_list.insert_start(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_after_node(2,5)
#linked_list.insert_start(6)
linked_list.delete_node(2)
#linked_list.delete_node(3)
#linked_list.insert_end(2)
#linked_list.insert_start(3)

linked_list.display()
print("------------------------")
print(linked_list.length)