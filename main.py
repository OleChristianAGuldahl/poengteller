
# Importerer random-biblioteket
import random                                           

            

# Her lager koden ett tilfeldig tall mellom 0-3
tilfeldig_tall = random.randint(0, 3)


# Begynner med at poensummen til spilleren er null
poengsum=0
                                                                   

# Begynner med blankt svar
svar = ""

# Lager en løkke, hvor spilleren kan skrive inn tall

#Hvis svaret er ikke 99 sjekkes svaret mot det tilfeldige tallet. 
while svar != "99":
    svar = input("Gjett ett tall mellom 0 og 10 (skriv 99 for å avslutte spillet): ")
    if int(svar) == int(tilfeldig_tall):
        # legger til ett poeng til poeng summen hvis riktig 
        poengsum +=1
        print ("Riktig, din poensum er nå: " + str(poengsum))
        tilfeldig_tall = random.randint(0, 2)
        #Hvis spillern gjettet feil
    else:
        print("Desverre feil, gjett igjen")
