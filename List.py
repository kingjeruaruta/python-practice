accounts = {
    "John": "abc123",
    "Alenere": "123abc",
    "David": "hahatdog"
}

user = input("Enter your username: ")
passw = input("Enter your password: ")


while True:
    if user in accounts and passw in accounts[user] == passw:
        print(f"Welcome, {user}!")
        break
    else:
        print("Incorrect username or password. Try again.")
        user = input("Enter your username: ")
        passw = input("Enter your password: ")