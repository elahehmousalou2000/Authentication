import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        users[username] = hash_password(password)
        print("Registered.")
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        if users.get(username) == hash_password(password):
            print("Login successful.")
        else:
            print("Invalid credentials.")
    elif choice == "3":
        break
