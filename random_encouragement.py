# TASK: Write a function that returns a random encouragement message.

# Import the random module
import random
# Define a function with no parameters that returns a string
def rand_encrgmnt():
# Create four different message variables
    mess_1 = print("Never give up")
    mess_2 = print("Sebastion believes in you")
    mess_3 = print("Jovan believes in you")
    mess_4 = print("Arsalan believes in you")
# Generate a random number from 1 to 4
    rand_num = random.randint(1, 4)
# Use if-elif statements to return the corresponding message
# Call the function and print the result
rand_encrgmnt()