from tabulate import tabulate

class Inventory():
  def __init__ (self, id, name, quantity, price):
    self.id = id
    self.name = name
    self.quantity = quantity
    self.price = price



class InventoryManager():
  def __init__ (self):
    self.inventory = [
    {'id':'764', 'name':"AD", "quantity":2, "price": 60000  },
    {'id':'74', 'name':"zinq", "quantity":3, "price": 6000  } 
    ]
    print(tabulate(self.inventory, headers= "keys", tablefmt="grid"))

  def input_inv (self):
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
          self.inventory.append(add_inventory)
          print(tabulate(self.inventory, headers= "keys", tablefmt="grid"))
 
      else: 
        break
    
  def input_del (self):
    while True:
      answer_del = input('do you want to delete an item?')
      if answer_del == "yes":
        delete = str(input('which id you want to delete?'))

        found = False

        for i in self.inventory:
            if i['id'] == delete:
              self.inventory .remove(i)
              found = True
              break

        if found == False:
          print('Error, id was not found')
 #like a list not dic

          print(tabulate(self.inventory, headers= "keys", tablefmt="grid"))
      else: 
        break


def main():
  energy = InventoryManager()

  energy.input_inv()
  energy.input_del()

if __name__ == "__main__":
  main()

