```Python
current_room=0
room_list= []
next_room=0
done=False
n=0
s=0
w=0
o=0
room=['Du bist in einem Raum, da sind Türen in Richtung: Norden, Osten und Westen', 2, 4, None, 1]
room_list.append(room)
room=['Du bist in einem Raum, da ist eine Tür in Richtung: Osten', None, 2, None, None]
room_list.append(room)
room=['Du bist in einem Raum, da sind Türen in Richtung: Osten, Süden und Westen', None,3, 0, 1]
room_list.append(room)
room=['Du bist in einem Raum, da sind Türen in Richtung:Norden, Süden und Westen',5, None, 4, 2]
room_list.append(room)
room=['Du bist in einem Raum, da sind Türen in Richtung: Norden und Westen', 3, None, None, 0]
room_list.append(room)
room=['Du bist in einem Raum, da ist eine Tür in Richtung:Westen', None, None, 3, None]
room_list.append(room)

current_room=room_list[0]
print(current_room)

while done==False:
    print()
    x=int(input("Wo möchtest du hingehen? Richtung: (1) Norden, (2) Süden, (3)Westen oder (4) Osten?"))
    
    if x==1:
        next_room=room_list[2]
        current_room=next_room
        print(next_room)
        
    elif x==2:
        print("Du kannst nicht hier lang gehen")
        
    elif x==3:
        next_room=room_list[1]
        current_room=next_room
        print(current_room)
        
    elif x==4:
        next_room=room_list[4]
        current_room=next_room
        print(current_room)
        
        
    else:
        print("Tut mir leid, das habe ich nicht verstanden")
    
```