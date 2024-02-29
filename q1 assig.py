# Function to convert an integer to Indian currency notation
def convert_to_curr(num):
    # Convert the number to a string for easy manipulation
    num = str(num)
    
    # If the length of the number is less than or equal to 3, return the number as is
    if len(num) <= 3:
        return num
    
    # Initialize the result string with a comma
    result = ","
    
    # Start iterating from the third digit from the end of the number
    i = len(num) - 3
    
    # Initialize a count to keep track of digits inserted
    count = 0
    
    # Iterate through the number in reverse
    while i > 0:
        i -= 1
        count += 1
        # Insert a comma after every second digit, except for the last two digits
        result += num[i]
        if count == 2 and i:
            result += ","
            count = 0
    
    # Reverse the result string and add the last three digits
    result = result[::-1] + num[-3:]
    
    # Return the result
    return result

# Take user input for the integer
num = int(input("Enter the input:"))

# Call the function to convert the integer to Indian currency notation
result=convert_to_curr(num)
print(result)

#Time complexity is O(N) since its a while loop that traverses the string once, where N is the length of the number.
#Space Complexity is also O(N) since we are using a string of length N to save the result.