# Remove duplicates from linked List

# Q1 : What type of values are stored in each node? are they numbers or string?
# Q2 : Is the linked is sorted or not
# Q3 : Should I do this in place?
# Q4 : What should be the value of the pointer for last node?

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(N) TIME where N is the no of elements in the ll
# o(M) SPACE where M is the no of unique elements in the ll
def removeDuplicatesFromLinkedList(header_node):

    value_and_count = {}
    current_node = header_node
    
    while current_node:
        value_and_count[current_node.value] = value_and_count.get(current_node.value, 0) + 1
        current_node = current_node.next
    
    current_node = header_node
    while current_node.next is not None:
        count = value_and_count[current_node.value]
        if count == 1:
            current_node = current_node.next
        else:
            next_node = current_node
            for _ in range(count):
                next_node = next_node.next
            current_node.next = next_node
            if next_node is not None:
                current_node = next_node
    return header_node

# O(N) time
# O(1) space
def removeDuplicatesFromLinkedList(header_node):
    current_node = header_node
    next_node = header_node.next

    while next_node:
        if current_node.value == next_node.value or next_node.next is None:
            current_node.next = None
        else:
            current_node.next = next_node
            current_node = next_node
        next_node = next_node.next
    return header_node

def removeDuplicatesFromLinkedList(header_node):
    current_node = header_node

    while current_node:
        next_distinct_node = find_next_distict_node(current_node)
        current_node.next = next_distinct_node
        current_node = next_distinct_node
    return header_node

def find_next_distict_node(current_node):
    next_distinct_node = current_node.next
    while next_distinct_node:
        if current_node.value == next_distinct_node:
            next_distinct_node = next_distinct_node.next
    return next_distinct_node

def build(array):
	header = LinkedList(array[0])
	current_node = header
	idx = 1
	while idx < len(array):
		node = LinkedList(array[idx])
		current_node.next = node
		current_node = node
		idx += 1
	return header

def print_ll(header):
	
	cn = header
	while cn:
		print(str(cn.value) + "-->", end=" ")
		cn = cn.next

def print_linked_list(header):
    node = header
    while node:
        print(str(node.value) + "-->", end=" ")
        node = node.next
    print("null")




s = build([1, 2, 2, 2, 3, 3])
print_linked_list(s)
d = removeDuplicatesFromLinkedList(s)
print_linked_list(d)

# 1--> 2--> 2--> 2--> 3--> 3--> null
# 1--> 2--> 3--> null