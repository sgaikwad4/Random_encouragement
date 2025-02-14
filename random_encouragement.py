# TASK: Write a function that returns a random encouragement message.

# Import the random module
import random
# Define a function with no parameters that returns a string
def rand_encrgmnt():
# Create four different message variables
    mess_1 = "Never give up"
    mess_2 = "Sebastion believes in you"
    mess_3 = "Jovan believes in you"
    mess_4 = "Arsalan believes in you"
# Generate a random number from 1 to 4
    rand_num = random.randint(1, 4)
# Use if-elif statements to return the corresponding message
    if rand_num == 1:
        return mess_1 
    elif rand_num == 2:
        return mess_2 
    elif rand_num == 3:
        return mess_3 
    else:
        return mess_4 
# Call the function and print the result
print(rand_encrgmnt())