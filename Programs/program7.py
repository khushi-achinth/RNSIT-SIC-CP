class Event:
    def __init__(self):
        pass
    def monday(self):
        print('Monday event')
    def tuesday(self):
        print('Tuesday event')
    def wednesday(self):
        print('Wednesday event')
    def thursday(self):
        print('Thursday event')
    def friday(self):
        print('Friday event')
    def other_day(self):
        print('Invalid choice')

class Menu:
    def __init__(self):
        pass
    def get_menu(self, event):
        menu = {
            1 : event.monday,
            2 : event.tuesday,
            3 : event.wednesday,
            4 : event.thursday,
            5 : event.friday,
        }
        return menu
    
    def run_menu(self):
        pass
    
menu = Menu()
menu.run_menu()