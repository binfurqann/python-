# Creating a Python Program to convert decimal number into octal numbers

def decimal_to_octal(decimal_num):
    octal_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num = str(remainder) + octal_num
        decimal_num //= 8
    return octal_num

# Taking Input
decimal_input = int(input("Enter a decimal number: "))

# Converting decimal numbers into octal numbers
octal_output = decimal_to_octal(decimal_input)

# Output of converted decimal numbers to output numbers
print("Octal representation:", octal_output)