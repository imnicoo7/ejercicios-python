# Ejercicio Recursive Digit Sum
# Nicolas Gutierrez

# ------------------------------------------------------------------------------------------------------------
def super_digit(n, k):
    def recursive_super_digit(num):
        if len(num) == 1:
            return int(num)
        else:
            digit_sum = sum(int(digit) for digit in num)
            return recursive_super_digit(str(digit_sum))
    
    # Calculate the super digit of the original number n
    initial_super_digit = recursive_super_digit(n)
    
    # Calculate the super digit of the number concatenated k times
    repeated_super_digit = recursive_super_digit(str(initial_super_digit * k))
    
    return repeated_super_digit

# ------------------------------------------------------------------------------------------------------------
# Sample Input 0
n1, k1 = "148", 3
print(super_digit(n1, k1))

# Sample Input 1
n2, k2 = "9875", 4
print(super_digit(n2, k2))

# Sample Input 
n3, k3 = "123", 3
print(super_digit(n3, k3))
