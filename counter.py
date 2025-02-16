def update_inventory(cur_stock, new_stock):
    inventory_dict = {}

    # Initialize inventory dictionary with current stock
    for quantity, item_name in cur_stock:
        inventory_dict[item_name] = quantity

    # Update inventory dictionary with new stock
    for quantity, item_name in new_stock:
        if item_name in inventory_dict:
            inventory_dict[item_name] += quantity
        else:
            inventory_dict[item_name] = quantity

    # Convert the dictionary back to a list of tuples and sort it
    updated_inventory = [(quantity, item_name) for item_name, quantity in inventory_dict.items()]
    updated_inventory.sort(key=lambda item: item[1])  # Sort by item name

    return updated_inventory