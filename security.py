location = str(input()) #like xxxxxxxGxxxTxxx$

thief = location.find("T")
first_guard = location.find("G")
last_guard = location.rfind("G")
money = location.find("$")

if money < last_guard and money > first_guard:
    if thief > last_guard or thief < first_guard:
        print("quiet")
    else:
        print("ALARM")

elif money < last_guard and thief > last_guard:
    print("quiet")

elif money > last_guard and thief < last_guard:
    print("quiet")
elif "T" not in location:
    print("quiet")

elif thief > first_guard and thief < last_guard:
    print("quiet")


else:
    print("ALARM")




