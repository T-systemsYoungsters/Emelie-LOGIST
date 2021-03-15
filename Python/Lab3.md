print("It is Quiz Time")
score=0
question_one= float(input("Wie alt ist die Telekom?"))
if question_one == 26:
    print("Correct")
    score = score+1
else:
    print("Das ist leider falsch")

question_two= float(input(Wie groß ist der Fernsehturm (in Meter) ?"))
if question_two == 368
    print("Correct!")
    score = score +1
else:
    print("Das ist leider falsch!")

question_three= float(input("Was ergibt 3*5+9:"))
if question_three == 24:
    print("Correct!")
    score =score+1
else:
    print("Das ist leider falsch")

question_four=int(input("Wie viele Tage hat der Juli?"))
if question_four == 31:
    print("Correct!")
    score=score+1
else:
    print("Das ist leider falsch")

question_five=int("Wie viele Sekunden hat ein Tag?")
if question_five == 86400:
    print("Correct")
    score = score+1
else:
    print("Das war leider falsch")

print("Du hast", score, "fragen richtig beantwortet")
prozent = (score*100)/5
print("Das sind", prozent )