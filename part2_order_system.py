# =========================================
# RESTAURANT ORDER MANAGEMENT SYSTEM
# =========================================

import copy

# ---------------- DATA ----------------
menu = {
    "Paneer Tikka": {"category": "Starters", "price": 180.0, "available": True},
    "Chicken Wings": {"category": "Starters", "price": 220.0, "available": False},
    "Veg Soup": {"category": "Starters", "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains", "price": 320.0, "available": True},
    "Dal Tadka": {"category": "Mains", "price": 180.0, "available": True},
    "Veg Biryani": {"category": "Mains", "price": 250.0, "available": True},
    "Garlic Naan": {"category": "Mains", "price": 40.0, "available": True},
    "Gulab Jamun": {"category": "Desserts", "price": 90.0, "available": True},
    "Rasgulla": {"category": "Desserts", "price": 80.0, "available": True},
    "Ice Cream": {"category": "Desserts", "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka": {"stock": 10, "reorder_level": 3},
    "Chicken Wings": {"stock": 8, "reorder_level": 2},
    "Veg Soup": {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka": {"stock": 20, "reorder_level": 5},
    "Veg Biryani": {"stock": 6, "reorder_level": 3},
    "Garlic Naan": {"stock": 30, "reorder_level": 10},
    "Gulab Jamun": {"stock": 5, "reorder_level": 2},
    "Rasgulla": {"stock": 4, "reorder_level": 3},
    "Ice Cream": {"stock": 7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Veg Soup"], "total": 120.0},
    ]
}

# ---------------- TASK 1: MENU DISPLAY ----------------
print("\n===== MENU =====")

categories = set(item["category"] for item in menu.values())

for cat in categories:
    print(f"\n--- {cat} ---")
    for name, details in menu.items():
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:<15} ₹{details['price']:<6} [{status}]")

print("\nTotal items:", len(menu))
print("Available items:", sum(1 for i in menu.values() if i["available"]))

expensive = max(menu.items(), key=lambda x: x[1]["price"])
print("Most expensive item:", expensive[0], "₹", expensive[1]["price"])

print("\nItems under ₹150:")
for name, d in menu.items():
    if d["price"] < 150:
        print(name, "₹", d["price"])

# ---------------- TASK 2: CART SYSTEM ----------------
cart = []

def add_item(name, qty):
    if name not in menu:
        print("❌ Item not found:", name)
        return
    if not menu[name]["available"]:
        print("❌ Item unavailable:", name)
        return

    for item in cart:
        if item["item"] == name:
            item["quantity"] += qty
            return

    cart.append({"item": name, "quantity": qty, "price": menu[name]["price"]})

def remove_item(name):
    for item in cart:
        if item["item"] == name:
            cart.remove(item)
            return
    print("❌ Item not in cart")

# Sample actions
add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1)
add_item("Mystery Burger", 1)  # invalid
add_item("Chicken Wings", 1)   # unavailable
remove_item("Gulab Jamun")

print("\n===== ORDER SUMMARY =====")
subtotal = 0

for item in cart:
    total = item["quantity"] * item["price"]
    subtotal += total
    print(f"{item['item']:<15} x{item['quantity']} ₹{total}")

gst = round(subtotal * 0.05, 2)
total_pay = subtotal + gst

print("Subtotal:", subtotal)
print("GST (5%):", gst)
print("Total Payable:", total_pay)

# ---------------- TASK 3: INVENTORY (DEEP COPY) ----------------
inventory_backup = copy.deepcopy(inventory)

# Update stock
inventory["Paneer Tikka"]["stock"] -= 3

print("\n===== INVENTORY CHECK =====")
print("Original:", inventory["Paneer Tikka"])
print("Backup :", inventory_backup["Paneer Tikka"])

# Low stock alert
print("\nLow Stock Items:")
for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(item, "needs restock")

# ---------------- TASK 4: SALES ANALYSIS ----------------
print("\n===== SALES REPORT =====")

for date, orders in sales_log.items():
    total_sales = sum(order["total"] for order in orders)
    print(date, "Total Sales:", total_sales)

# Top order
all_orders = [order for orders in sales_log.values() for order in orders]
top_order = max(all_orders, key=lambda x: x["total"])

print("\nTop Order ID:", top_order["order_id"])
print("Top Order Value:", top_order["total"])