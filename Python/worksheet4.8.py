sum=0
total_positiv=0
total_zero=0
total_negativ=0
for i in range(7):
    x=int(input("Enter a number: "))
    sum= sum + x
    if x > 0:
        total_positiv = total_positiv +1
    elif x == 0:
        total_zero= total_zero +1
    else:
        total_negativ= total_negativ +1

        
print("The total is:", sum)
print("You entered a total of positiv numbers of:", total_positiv)
print("You entered a total of zeros of:", total_zero)
print("you entered a total of negativ numbers of: ", total_negativ)
        
