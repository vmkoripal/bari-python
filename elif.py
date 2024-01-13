john = int(input("Enter John age"))
peter = int(input("Enter Peter age"))
kane = int(input("Enter kane age"))

if john > peter and john > kane:
    print("John is eldest")
elif peter > kane:
    print("peter is elder")
else:
    print("kane is eldest")
