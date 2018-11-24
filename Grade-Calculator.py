x = int (input ("Enter your score"))
if x > 0 and x < 39:
    print ("F")
elif x > 39 and x < 44:
    print ("E")
elif x > 44 and x < 50:
    print ("D")
elif x > 50 and x < 60:
    print ("C")
elif x > 60 and x < 70:
    print ("B")
elif x > 70 and x < 100:
    print ("A")
else:
    print ("Please enter marks between 0-100! Thanks")

