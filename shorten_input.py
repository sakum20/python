class construct_item():
    def __init__(self, item):
        self.item_name = item 
    
    def print_original_item(self):
        print(self.item_name)
        
class shorten_itemANDchar(construct_item):
    def shorten(self):
        print(self.item_name[0:3])

item1 = shorten_itemANDchar("Hello")
item1.print_original_item()
item1.shorten()

item2 = shorten_itemANDchar([1,2,3,4])
item2.print_original_item()
item2.shorten()