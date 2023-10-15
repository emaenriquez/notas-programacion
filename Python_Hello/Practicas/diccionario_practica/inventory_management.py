# Inventory Management
# Create a dictionary to represent an inventory of products in a store. Each product should have attributes like name, price, and quantity. Implement functions to add a new product, update product details, check if a product exists, and remove a product from the inventory.

inventory_management_store = {}

def add_new_product(name,price,quantity):
    inventory_management_store[name] = {
        'price':price,
        'quantity': quantity
    }

def update_product(name,price=None,quantity=None):
    if name in inventory_management_store:
        if price is not None:
            inventory_management_store[name]['price'] = price
        if quantity is not None:
            inventory_management_store[name]['quantity'] = quantity
        else:
            print('the product does not exist in the inventory')
    
def check_product_exists(name):
    return name in inventory_management_store
def remove_product(name):
    if name in inventory_management_store:
        del inventory_management_store[name]
        return 'el producto a sido eliminado {name}'
    else:
        return 'el producto no existe'

add_new_product("lechuga",10,90)
add_new_product("Tomate",10,90)
add_new_product("Pezacado",10,90)
add_new_product("Zanahoria",10,90)

update_product("lechuga",15,40)

if check_product_exists('lechuga'):
    print('El producto existe actualmente')
else:
    print('el producto no existe')

remove = remove_product("lechuga")
print(remove)
print(inventory_management_store)
