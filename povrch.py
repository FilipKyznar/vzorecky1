print ("Vitejte v aplikaci pro výpočet obvodu obdelníku")

r = input ("zadejte proměnou r: ")

r = int(r)

if r>0:
    vysledek = 3.14*(r**2)
    print("vysledek je: ", vysledek)
else:
    print ("nemůžeš zadat 0 nebo záporné číslo")
