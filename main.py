
# Importerer random-biblioteket
import random                                           

            

# Lager ett tilfeldig tall mellom 0-2 
lodd = random.randint(0, 3)



poengsum=0
                                                                   

svar = ""

while svar != "99":
    svar = input("Gjett ett tall mellom 0 og 10 (skriv 99 for å avslutte spillet): ")
    if int(svar) == int(lodd):
        poengsum +=1
        print ("Riktig, din poensum er nå: " + str(poengsum))
        lodd = random.randint(0, 2)
    else:
        print("Desverre feil, gjett igjen")
