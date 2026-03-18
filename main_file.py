from tabulate import tabulate

def inventory_system():
  inventory = [
    {'id':'764', 'name':"AD", "quantity":2, "price": 60000  },
    {'id':'74', 'name':"zinq", "quantity":3, "price": 6000  }           
  ]
  print (tabulate(inventory, headers="keys", tablefmt="grid"))

def main():
  inventory_system()

if __name__ == "__main__":
  main()


#for item in inventory:
 #   for key, value in i.items(): print (f"The {key} is {value}")

  #print (f'ID:{item["id"]}| name:{item['name']}|quan: {item["quantity"]}| price: {item["price"]}')