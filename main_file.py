from tabulate import tabulate

class Inventory():
  def __init__ (self, id, name, quantity, price):
    self.id = id
    self.name = name
    self.quantity = quantity
    self.price = price

class InventoryManager():
         
  def input_inv (self):
    inventory = [
    {'id':'764', 'name':"AD", "quantity":2, "price": 60000  },
    {'id':'74', 'name':"zinq", "quantity":3, "price": 6000  } 
    ]
    print(tabulate(inventory, headers= "keys", tablefmt="grid"))


    while True:
      answer = input('add?')
      if answer == "yes":
          id = input("what's the id?")
          name = input("What is the name")
          quantity = input("what is the q")
          price = input("what is the price?")

          Inventory(id, name, quantity, price)

          add_inventory = {
          "id": id,
          "name":name,
          "quantity": quantity,
          "price": price
         }
          inventory.append(add_inventory)
          print(tabulate(inventory, headers= "keys", tablefmt="grid"))

      else: break
    

def main():
  energy = InventoryManager()
  energy.input_inv()

if __name__ == "__main__":
  main()

