class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.root = None  

    def insert_at_beginning(self, data): 
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position < 1:
            print("Invalid position")
            return

        if position == 1:  
            new_node.next = self.root
            self.root = new_node
            return

        current = self.root
        count = 1
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if not current:  
            print(f"Position {position} out of range.")
            return

        new_node.next = current.next
        current.next = new_node
    
    def display(self, reverse=False):
        if reverse:
            self.reverse_display(self.root) 
        else:
            current = self.root
            while current:
                print(current.data, end=" -> ")
                current = current.next 
        print() 
    
    def reverse_display(self, node):
        if node is None:
            return
        self.reverse_display(node.next)  
        print(node.data, end=" -> ") 

    def delete_at_position(self, position):
        if position < 1:
            print("Invalid position")
            return
        current = self.root
        if position == 1:  
            if self.root:
                self.root = current.next
                current = None
            return
        count = 1
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current or not current.next:
            print(f"Position {position} out of range.")
            return
        current.next = current.next.next 
        current = None


ll = LinkedList()
    
while True:
    print("\nMenu:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Delete at position")
    print("5. Display list in reverse")
    print("6. Exit")
        
    choice = int(input("Enter your choice: "))
        
    if choice == 1:
        data = int(input("Enter data to insert at beginning: "))
        ll.insert_at_beginning(data)
        
    elif choice == 2:
        data = int(input("Enter data to insert at end: "))
        ll.insert_at_end(data)
        
    elif choice == 3:
        data = int(input("Enter data to insert: "))
        position = int(input("Enter position to insert: "))
        ll.insert_at_position(data, position)
        
    elif choice == 4:
        position = int(input("Enter position to delete: "))
        ll.delete_at_position(position)
        
    elif choice == 5:
        print("Reversed linked list:")
        ll.display(reverse=True)
        
    elif choice == 6:
        print("End of program")
        break
  
    else:
        print("Invalid choice! Please try again.")
