class construct_item():
    def __init__(self, item):
        self.item_name = item 
    
    def print_original_item(self):
        print(f'Original items: {self.item_name}')
        
class shorten_itemANDchar(construct_item):
    def shorten(self):
        print(f'Shortened items: {self.item_name[0:3]}')


class shorten_dict(construct_item):
    def shorten(self):
        input_dict = self.item_name
        print(f'Printing dict values directly: {self.item_name}')
        print(f'Printing dict values using item method: {self.item_name.items()}')
        counter = 0
        result_dict = {}

        for k, v in input_dict.items():
            if(counter < 3):
                result_dict.update({k: v})
                counter = counter + 1
        print(f'Shortened item: {result_dict}')



item1 = shorten_itemANDchar("Hello")
item1.print_original_item()
item1.shorten()

item2 = shorten_itemANDchar([1,2,3,4])
item2.print_original_item()
item2.shorten()


my_dict = shorten_dict({1: 'mike', 2: 'satz', 3: 'nariya', 4: 'leo', 5: 'namdi'})
my_dict.print_original_item()
my_dict.shorten()