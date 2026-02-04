import json
import os

# 1. SETUP: Check if the file exists, if not, create an empty one
if not os.path.exists('inventory.json'):
    with open('inventory.json', 'w') as f:
        json.dump({}, f)

# 2. LOAD: Read the current inventory from the file
with open('inventory.json', 'r') as f:
    inventory = json.load(f)

# 3. ADD/UPDATE: Modify the data in Python
# Adding a new item
name = "Apple"
inventory[name] = {"quantity": 10, "price": 0.50}

# Updating quantity (Add 5 more apples)
inventory["Apple"]["quantity"] += 5

# 4. SAVE: Write the updated data back to the file
with open('inventory.json', 'w') as f:
    json.dump(inventory, f, indent=4)

print("Inventory updated and saved!")