attempts = 3
while attempts > 0:
    user = input("Enter UserID: ")
    Pass = input("Enter Password: ")

    if user == "Jayesh.12" and Pass == "Jayesh@12":
        print("Logged in!")
        break
    else:
        attempts -= 1
        print(f"Wrong. Attempts left: {attempts}")

if attempts == 0:
    print("Locked Program terminated.")