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
