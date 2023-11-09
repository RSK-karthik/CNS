def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)


num1 = int(input("Enter Value of a: "))
num2 = int(input("Enter Value of b: "))

gcd_val= gcd(num1, num2)

print("GCD using Euclidean Algorithm "+str(num1)+" and " +str(num2)+": ", gcd_val)

def advanced_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = advanced_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y

# Example Usage
num1 = int(input("Enter Value of a: "))
num2 = int(input("Enter Value of b: "))
gcd, x, y = advanced_euclidean_algorithm(num1, num2)
print(f"GCD using Advanced Euclidean Algorithm: {gcd}, x = {x}, y = {y}")
