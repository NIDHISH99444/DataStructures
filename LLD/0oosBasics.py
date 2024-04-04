class ShoppingCart(object):

    def __init__(self):
      self.total = 0
      self.items = {}

    def add_item(self, item_name, quantity, price):
        self.total += (quantity * price)
        self.items[item_name]= quantity
        print(self.items)


    def remove_item(self, item_name, quantity, price):
        if quantity > self.items[item_name]:
           return "cant remove the existing quantity"
        else:
            self.items[item_name]-=quantity
            if quantity==0:
                del self.items[item_name]
            else: 
                self.total-=quantity*price


    def checkout(self, cash_paid):
        balance = 0
        if cash_paid < self.total:
          return "You paid {} but cart amount is {}".format(cash_paid, self.total))
        balance = cash_paid - self.total
        return "Exchange amount: {}".format(balance)
    



# Driver code
cart = ShoppingCart()

cart.add_item('A', 10, 50)
cart.add_item('B', 5, 20)

cart.remove_item('B', 5, 20)

cart_res = cart.checkout(600)

print('Total cart amount:', cart.total)
print('Cart items:', cart.items)

print(cart_res)