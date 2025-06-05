from mainGame import startGame

print("Welcome to Space Shooter!")

userMenuInput = input("Type 'Start' to begin: ")

if (userMenuInput.lower() == 'start'):
    startGame()
else:
    print("Invalid input. Try again")