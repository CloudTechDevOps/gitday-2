# Request input from user
user_input = input("Enter a number: ")

# Convert text input to an integer
number = int(user_input)

# Check if the number is divisible by 6
if number % 6 == 0:
    print(f"{number} is divisible by 6.")
else:
    print(f"{number} is not divisible by 6.")

