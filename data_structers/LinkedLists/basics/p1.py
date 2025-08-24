#A linkedList is a linear collection of data elements.
#These data elements are called Nodes, and they point to the next Node.




#class Node(object):
 #   def __init__(self):
  #      return object

class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node



class Linkedlist(object):
    def __init__(self, head=None):
        self.head = head

    def Display(self):
        temp=self.head
        while(temp):
            print(temp.head,"->",end='')
            temp=temp.next_node
        print(" ")



    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    # %%
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def get_next_node(self, node):
        return node.next_node.data


llist = Linkedlist()
llist.head=Node(2)
s = Node(3)
t =Node(4)
llist.head.next_node=s
s.next_node = t

llist.Display()
print(llist.size())
llist.insert_at_head(6)
print(llist.get_next_node(s))