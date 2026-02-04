import json
import os

FILENAME = 'inventory.json'

def load_inventory():
    """Loads inventory from JSON file, or returns an empty dict if not found."""
    if not os.path.exists(FILENAME):
        return {}
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Error reading file. Starting with an empty inventory.")
        return {}

def save_inventory(inventory):
    """Saves the current inventory dictionary to the JSON file."""
    try:
        with open(FILENAME, 'w') as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully.")
    except IOError as e:
        print(f"Failed to save inventory: {e}")

def add_item(inventory, name, quantity, price):
    """Adds a new item or updates the price if it already exists."""
    inventory[name] = {
        "quantity": quantity,
        "price": price
    }
    print(f"Added {name} to inventory.")

def update_quantity(inventory, name, quantity_change):
    """Updates the quantity of an existing item."""
    if name in inventory:
        inventory[name]['quantity'] += quantity_change
        print(f"Updated {name} quantity to {inventory[name]['quantity']}.")
    else:
        print(f"Error: Item '{name}' not found in inventory.")

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Load existing data
    my_inventory = load_inventory()

    # 2. Add some items
    add_item(my_inventory, "Widget", 50, 19.99)
    add_item(my_inventory, "Gadget", 20, 45.50)
    add_item(my_inventory, "Mouse", 5, 23.00)

    # 3. Update an existing item
    update_quantity(my_inventory, "Widget", -5) # Sold 5 widgets

    # 4. Save back to file
    save_inventory(my_inventory)