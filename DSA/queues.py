import sys

class queue:
    def __init__(self, size=5):
        self.stk = []
        self.size = size
        print('Empty queue is created')
    
    def insert(self):
        if len(self.stk) == self.size:
            print('queue is full')
            return
        element = input('Enter the element to be inserted: ')
        self.stk.insert(self.size-1, element)

    def delete(self):
        if not self.stk:
            print('queue is empty')
            return
        print(f'Deleted element is {self.stk[0]}')
        del self.stk[0]

    def list_queue(self):
        if not self.stk:
            print('queue is empty')
            return
        print('The queue is \n', self.stk) # stk[::-1]

class Menu:
    def get_menu(self, queue):
        menu = {
            1 : queue.insert,
            2 : queue.delete,
            3 : queue.list_queue,
            4 : self.end_of_program
        }
        return menu
    
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def run_menu(self):
        queue = queue()
        while True:
            choice = int(input('1: insert 2:delete 3:Display 4:Exit. Your choice: '))
            menu = self.get_menu(queue)
            menu.get(choice, self.invalid_choice)()
    
menu = Menu()
menu.run_menu()