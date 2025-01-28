num = int(input("Enter a 4 or more digit number: "))
t = num
numLen = 0

while t > 0:
    numLen += 1
    t = int(t/10)

if numLen >= 4:
    numLen  = int(numLen/2)
    chk = 0
    
    while num > 0:
        rem = num % 10
        
        if chk == numLen:
            midOne = rem

        elif chk == (numLen + 1):
            midTwo = rem

        num = int(num/10)
        chk += 1
    prod = midOne * midTwo
    print("\nProduct of mid digits (" + str(midOne) + "*" + str(midTwo),") =", prod)

else:
    print("You're number is not a more than 4 digit number!")