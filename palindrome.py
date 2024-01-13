n = int(input("Enter n"))
m = n

rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r
    
if m == rev:
    print("Number is Palindrome")
else:
    print("Not a Palindrome")
    
    
    