while True:
    user_input = input("Enter your age: ")

    if user_input.isdigit():  # checks if it's a whole number
        age = int(user_input)

        if 0 <= age <= 120:
            print("Your age is:", age,"years old meaning you are human")
            break
        else:
            print("Error: Age must be between 0 and 120 if above or bellow you are an alien or you are not born yet.")
    

    else:
        print("Error: Please enter a valid integer.")