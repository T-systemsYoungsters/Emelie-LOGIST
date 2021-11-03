#1. What is a Python library?
    # eine Sammling von Funktionen und Klassen die in einem seperaten Dokument untergracht sind und für das eigenen Programm verwendet werden können.
    #Sie dienen zur Erleicherung und müssen nicht unbedingt von dem selben Programmierer verfasst worden sein

#2. What are some of the reasons why a programmer would want to create his/her own library file?
    # Zeitsparend
    #Code wird durch die Benutzung küzer
    #unterstützend, andere können zur selben Zeit mitarbeiten

#3. There are two ways to import library files in Python. Give an example of each.
    #Bsp 1:
    from my_functions import *
    foo()

    #Bsp 2:
    import my_functions
    my_functions.foo()

#4. How do calls to functions and classes differ depending on how the library is imported?
    #Bei dem ersten Beispiel wird kein namespace benötigt um die richtige Funktion auszuführen. Bei der zweiten jedoch schon

#5. Can library files import other library files?
    #Nein

#6. What is a ``namespace?''
    my_functions.foo()
    # my_functions ist der namespace von .foo()
