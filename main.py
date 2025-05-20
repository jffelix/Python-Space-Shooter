from mainGame import startGame

print("Welcome to Space Shooter!")

userMenuInput = input("Type 'Start Game' to begin: ")

if (userMenuInput.lower() == 'start game'):
    startGame()
else:
    print("Invalid input. Try again")