from linkedlist import LinkedList
from produto import Product

class Stock:

    def __init__(self):
        self.stock = LinkedList()

    #
    # Get product if exists, else return None
    #
    def get_product(self, id):

        ## Get all existent products in stock
        all_products = self.stock.get_all()

        ## Find existent product in stock by ID
        for product in all_products:
            if id == product.id:
                return product
            
        return None
    
    #
    # Order by quantity if stock is not empty
    #
    def order_by_quantity(self):

        if self.stock.is_empty():
            return None

        ## Get all existent produts in stock
        all_products = self.stock.get_all()

        ## Initialize ordered list
        ordered_list = []

        ## Search in all of the products list and return
        for i in range(len(all_products)):
            highest = None

            for product in all_products:
                if highest == None:
                    highest = product
                
                if product.quantity >= highest.quantity:
                    highest = product
                    print(f"O produto atual é {product.quantity}")
                    print(f"O highest {highest.quantity} foi atribuido como produto")

            print(f"O highest que será feito o append e removido é: {highest.quantity}")
                
            ordered_list.append(highest)
            all_products.remove(highest)

        return ordered_list
    
teste = Stock()

teste.stock.add(Product(1, 'iago', 'legal', 1, 1))
teste.stock.add(Product(2, 'hertz', 'interessante', 3, 2))
teste.stock.add(Product(3, 'caua', 'opressor', 5, 7))
teste.stock.add(Product(4, 'luana', 'opressor', 4, 9))


for product in teste.stock.get_all():
    print(product.name, product.quantity, sep=',')
for product in teste.order_by_quantity():
    print(product.name, product.quantity)