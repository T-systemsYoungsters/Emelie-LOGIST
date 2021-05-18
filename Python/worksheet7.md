1)
string: Hi
float: 2.456
integer: 1
boolean: True/False

2)
print(my lisr[1]) = gibt 2 aus (2. Stelle von der Liste)
print(my list[4]) = gibt 101 aus (5. Stelle von der Liste)
print(my list[5]) = gibt einen Fehler aus, da die list nur 5 Stellen hat und keine 6

3)
Er gibt alle Elemente der Liste aus

4)
Es ergibt sich ein Fehler, weil my list2 ein Tupel ist und somit nach der aufstellung nicht noch einmal verändert werden kann.

5)
Er gibt einmal die Rechnung aus der Liste aus, sprich (3*5)=15 und beim zweiten gibt er 5 mal die 3 aus, da die drei diesmal als einziges Element der Liste gilt und die Liste mit 5 multipliziert wird.

6)
er gibt die Liste aus (in diesem fall nur die 5) und danach fügt er durch die Schleife die Zahlen 0-4 an, da die Schleife in range(5) ist

7)
Er gibt die jeweilige Länge der Strings aus, da die 2 ein integer ist, hat diese keine Länge und es wird ein Fehler ausgegeben

8)
print("Simpson" + "College") : Gibt beides zusammengeschrieben aus
print("Simpson" + "College"[1]) : gibt Simpson und von dem zweiten Wort die zweite stelle aus (o)
print( ("Simpson" + "College")[1] ) : gibt die zweite Stelle von dem ersten Wort aus, sprich i

9)
Er gibt alle Buchsctaben untereinander aus

10)
Er hängt an das Wort Simpson noch drei mal(durch die Schleife) das Wort College an 

11)
Er gibt drei mal das Wort Hi hintereinander aus

12)
Es gibt die beiden Sätze aus fügt jedoch nichts nach dem doppelpunkt ran

13)
Die erte Zeile gibt die zweite Stelle aus, sprich 1
Die zweite Zeile gibt die ersten 3 Stellen aus, sprich 012
Die dritte Zeile gibt die Stellen nach der dritten stelle aus, sprich 3456789

14)
```Python
mylist=[]
for i in range(5):
    x=int(input("Welche Zahl soll in dein Array: "))
    mylist.append(x)
print (mylist)
```

15)
```Python
mylist=[]
list_total = 0
average=0
for i in range(5):
    x=int(input("Welche Zahl soll in dein Array: "))
    mylist.append(x)
for item in mylist:
    list_total += item
average=list_total/len(mylist)
print ("Meine Liste:", mylist)
print("Insgesamt:", list_total)
print("Länge:" ,len(mylist))
print("Durchschnitt:" ,average)
```