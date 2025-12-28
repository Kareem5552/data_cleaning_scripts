"""
Exercise 2 – Easy: Update & Add New Contact

Starting data:
contacts = {
    "alice": {"email": "alice@work.com", "active": True},
    "bob": {"email": "bob@gmail.com", "active": True}
}

Tasks:
1. Change Alice's email to "alice.new@work.com" (safe check first)
2. Add a new contact "sara" with email "sara@home.com" and "active": True
3. Print all contacts in one line each:
   Name: Alice | Email: alice.new@work.com | Active: True
"""

# Solution
contacts = {
    "alice": {"email": "alice@work.com", "active": True},
    "bob": {"email": "bob@gmail.com", "active": True}
}

# 1. Update Alice safely
if "alice" in contacts:
    contacts["alice"]["email"] = "alice.new@work.com"

# 2. Add Sara safely
contacts["sara"] = {"email": "sara@home.com", "active": True}

# 3. Print
for name, info in contacts.items():
    print(f"Name: {name.capitalize()} | Email: {info['email']} | Active: {info['active']}")
