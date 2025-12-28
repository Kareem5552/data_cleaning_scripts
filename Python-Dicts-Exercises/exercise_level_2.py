"""
Exercise 3 – Medium: Normalize + Safe Add + Simple Flatten

Starting data (messy keys):
raw_contacts = {
    " Alice ": {"email": "alice@work.com"},
    "bob jones": {"email": "bob@gmail.com"},
    "Bob Jones ": {"phone": "555-9999"}
}

Tasks:
1. Normalize keys: lowercase + strip spaces (create new dict)
   → If duplicate after normalize → keep the first one, add missing keys from second
2. Add "active": True to every contact if missing
3. Flatten each contact to just their email (or "N/A" if missing)
4. Print final flat dict and total number of contacts
"""

# Solution
raw_contacts = {
    " Alice ": {"email": "alice@work.com"},
    "bob jones": {"email": "bob@gmail.com"},
    "Bob Jones ": {"phone": "555-9999"}
}

# 1. Normalize + merge duplicates
cleaned_contacts = {}
for name, info in raw_contacts.items():
    new_name = name.strip().lower()
    if new_name in cleaned_contacts:
        existing = cleaned_contacts[new_name]
        for k, v in info.items():
            if k not in existing:
                existing[k] = v
    else:
        cleaned_contacts[new_name] = info.copy()

# 2. Add "active": True if missing
for info in cleaned_contacts.values():
    info.setdefault("active", True)

# 3. Flatten to emails only
flat_emails = {name: info.get("email", "N/A") for name, info in cleaned_contacts.items()}

# 4. Print result
print("Final flat emails:")
print(flat_emails)
print("Total contacts:", len(flat_emails))
