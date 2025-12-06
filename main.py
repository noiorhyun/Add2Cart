# main.py
from collections import deque
from data import PRODUCT_CATALOG, PRODUCTS_BY_ID
from algorithms import quicksort, linear_search, binary_search
from models import Order

# --- Global State ---
shopping_cart = {}  # {product_id: quantity}
order_queue = deque() # FIFO queue for Order objects

# --- Helper Functions ---

def display_catalog(catalog):
    """Prints the current state of the product catalog."""
    print("\n--- Product Catalog ---")
    if not catalog:
        print("Catalog is empty.")
        return
        
    print(f"{'ID':<4} {'Name':<25} {'Price':<8} {'Rating':<6}")
    print("-" * 43)
    for product in catalog:
        print(f"{product.id:<4} {product.name:<25} ${product.price:6.2f} {product.rating:5.1f}")
    print("-" * 43)

def view_cart():
    """Prints the contents and total of the shopping cart."""
    print("\n--- Shopping Cart ---")
    if not shopping_cart:
        print("Your cart is empty.")
        return [], 0.0
    
    total_cost = 0
    print(f"{'ID':<4} {'Name':<25} {'Qty':<4} {'Price':<8} {'Subtotal':<8}")
    print("-" * 50)
    
    items_list = []
    for p_id, qty in shopping_cart.items():
        product = PRODUCTS_BY_ID[p_id]
        subtotal = product.price * qty
        total_cost += subtotal
        items_list.append({'product': product, 'quantity': qty})
        print(f"{p_id:<4} {product.name:<25} {qty:<4} ${product.price:6.2f} ${subtotal:7.2f}")
    
    print("-" * 50)
    print(f"{'Total Cost:':>41} ${total_cost:7.2f}")
    return items_list, total_cost

def validate_product_input(prompt):
    """Handles product ID input and validation."""
    p_id = input(prompt).strip()
    if p_id not in PRODUCTS_BY_ID:
        print(f"Error: Product ID {p_id} not found.")
        return None
    return p_id

# --- Main Logic Functions ---

def add_item_to_cart():
    """Prompts user to add an item to the cart."""
    p_id = validate_product_input("Enter Product ID to add: ")
    if not p_id: return
    
    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("Error: Quantity must be a positive number.")
            return
    except ValueError:
        print("Error: Invalid quantity entered.")
        return

    # Update or add item
    shopping_cart[p_id] = shopping_cart.get(p_id, 0) + qty
    print(f"Added {qty}x {PRODUCTS_BY_ID[p_id].name} (ID: {p_id}) to cart.")

def remove_item_from_cart():
    """Prompts user to remove an item from the cart."""
    if not shopping_cart:
        print("Your cart is already empty.")
        return
        
    p_id = validate_product_input("Enter Product ID to remove: ")
    if not p_id: return

    if p_id not in shopping_cart:
        print(f"Error: Product ID {p_id} is not in your cart.")
        return
        
    try:
        qty_to_remove = int(input(f"Enter quantity to remove (Current: {shopping_cart[p_id]}): "))
        if qty_to_remove <= 0:
            print("Error: Quantity must be a positive number.")
            return
    except ValueError:
        print("Error: Invalid quantity entered.")
        return

    current_qty = shopping_cart[p_id]
    if qty_to_remove >= current_qty:
        del shopping_cart[p_id]
        print(f"Removed all {current_qty} units of {PRODUCTS_BY_ID[p_id].name} from cart.")
    else:
        shopping_cart[p_id] -= qty_to_remove
        print(f"Removed {qty_to_remove} units of {PRODUCTS_BY_ID[p_id].name}. Remaining: {shopping_cart[p_id]}.")

def sort_catalog():
    """Prompts user to sort the catalog."""
    global PRODUCT_CATALOG
    
    print("\n--- Sort Options ---")
    print("1. Sort by Price (Low to High)")
    print("2. Sort by Rating (High to Low)")
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == '1':
        # Quicksort: Price (Ascending: reverse=False)
        PRODUCT_CATALOG = quicksort(PRODUCT_CATALOG, 'price', reverse=False)
        print("\nCatalog sorted by Price (Low to High).")
    elif choice == '2':
        # Quicksort: Rating (Descending: reverse=True)
        PRODUCT_CATALOG = quicksort(PRODUCT_CATALOG, 'rating', reverse=True)
        print("\nCatalog sorted by Rating (High to Low).")
    else:
        print("Invalid sort option.")

def search_products():
    """Allows user to search by name (linear) or ID (binary)."""
    print("\n--- Search Options ---")
    print("1. Search by Name (partial match)")
    print("2. Search by ID (exact match)")
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == '1':
        # Linear Search
        term = input("Enter name or partial name: ").strip()
        results = linear_search(PRODUCT_CATALOG, term)
        print(f"\nFound {len(results)} product(s) matching '{term}':")
        display_catalog(results)
        
    elif choice == '2':
        # Binary Search (Requires sorted IDs)
        target_id = input("Enter exact Product ID: ").strip()
        
        # Binary Search Preparation (O(n log n) setup, but O(log n) search)
        sorted_id_list = sorted(PRODUCTS_BY_ID.keys(), key=int)
        
        found_id = binary_search(sorted_id_list, target_id)
        
        if found_id:
            product = PRODUCTS_BY_ID[found_id]
            print(f"\nFound product by ID {found_id}:")
            display_catalog([product])
        else:
            print(f"Error: Product ID {target_id} not found.")
            
    else:
        print("Invalid search option.")

def checkout():
    """Creates an Order object and enqueues it."""
    global order_queue
    items_list, total_cost = view_cart()
    
    if not items_list:   # cart effectively empty
        print("\nCheckout Failed: Your cart is empty.")
        return
        
    # Create the Order object (Model)
    new_order = Order(items_list, total_cost)
    
    # Enqueue the order (Queue/FIFO)
    order_queue.append(new_order)
    
    # Reset the cart
    shopping_cart.clear() 
    
    print("\n--------------------------------")
    print(f"✅ CHECKOUT SUCCESSFUL!")
    print(f"Order ID: {new_order.order_id} | Total: ${new_order.total_cost:.2f}")
    print("Your order has been placed in the processing queue.")
    print("--------------------------------")

def process_next_order():
    """Simulates processing the next order in the queue (FIFO)."""
    if not order_queue:
        print("\nOrder processing queue is empty. No orders to process.")
        return
        
    # Dequeue the next order (Queue/FIFO)
    order_to_process = order_queue.popleft()
    
    print("\n--- Processing Order ---")
    print(f"Order ID: {order_to_process.order_id}")
    print(f"Total Items: {len(order_to_process.items)} distinct products")
    print(f"Total Cost: ${order_to_process.total_cost:.2f}")
    print("Status: Successfully processed and shipped.")
    print(f"Orders remaining in queue: {len(order_queue)}")
    print("-" * 25)

def display_menu():
    """Prints the main menu options."""
    print("\n==================================")
    print("🛒 Add2Cart: Backend Simulator")
    print("==================================")
    print("1. View Product Catalog")
    print("2. Sort Catalog (Price/Rating)")
    print("3. Search Products (Name/ID)")
    print("4. Add Item to Cart")
    print("5. Remove Item from Cart")
    print("6. View Shopping Cart")
    print("7. Checkout (Create Order)")
    print("8. Process Next Order (Queue)")
    print("9. Exit")
    print("----------------------------------")
    print(f"Orders Waiting: {len(order_queue)}")
    
def main():
    """Main application loop."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            display_catalog(PRODUCT_CATALOG)
        elif choice == '2':
            sort_catalog()
        elif choice == '3':
            search_products()
        elif choice == '4':
            add_item_to_cart()
        elif choice == '5':
            remove_item_from_cart()
        elif choice == '6':
            view_cart()
        elif choice == '7':
            checkout()
        elif choice == '8':
            process_next_order()
        elif choice == '9':
            print("Exiting Add2Cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
