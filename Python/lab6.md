Part1
```Python
row=10
column=10
i=10
for row in range(9):
    for column in range(row+1):
        print (i,end=" ")
        i=i+1
 
    # Print a blank line
    # to move to the next row
    print()
    ```
   Part2
   ```Python
    i=int(input("Wie viele Reihen soll das Viereck haben?"))
j=int(input("Wie viele Spalten soll das Viereck haben?"))
for row in range(i):
    for column in range(j):
        if row==0 or row==i-1 or column==0 or column==j-1:
            print("o", end=" ")
        else:
            print(" ", end=" ")
        
    
    print()
    
```
