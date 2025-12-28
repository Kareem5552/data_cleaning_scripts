"""
Exercise 1 – Easy: Basic Contact List + Add Active Flag

Starting data:
contacts = {
    "alice": {"email": "alice@work.com"},
    "bob": {"email": "bob@gmail.com"}
}

Tasks:
1. Use .setdefault() to add "active": True to every contact
2. Print each contact like this (simple format):
   Alice → Email: alice@work.com → Active: True
"""

# Solution
contacts = {
    "alice": {"email": "alice@work.com"},
    "bob": {"email": "bob@gmail.com"}
}

# 1. Add "active" safely
for info in contacts.values():
    info.setdefault("active", True)

# 2. Simple print
for name, info in contacts.items():
    print(f"{name.capitalize()} → Email: {info['email']} → Active: {info['active']}")
