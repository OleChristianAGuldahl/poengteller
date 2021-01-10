# poengteller
Løsningsforslag på oppgave Poengteller. Lagd i Python

Spille går ut på at man skal gjette tall mellom 0-3.

Spilleren får poeng for hvert tall som gjettes riktig.

Åpne main.py filen for å se brukerveiledningen. 


#Anvisning
Først begynner vi med å importere nødvendige biblioteker
Deretter opprettes verdiene vi trenger

`
# Importerer random-biblioteket
import random                                           

# Oppretter ett tilfeldig tall mellom 0-3
tilfeldig_tall = random.randint(0, 3)
# Begynner med at poensummen til spilleren er null
poengsum=0

# Begynner med blankt svar
svar = ""
`

Så starter man en løkke ved hjelp av kommandoen `while`.

Inne i while-løkken har vi først feilhåndteringsrutiner.

Så tar vi imot svaret fra brukeren med kommandorn `input`. 


`
# Lager en løkke, hvor spilleren kan skrive inn tall
# Hvis svaret er ikke 99 sjekkes svaret mot det tilfeldige tallet
# Løkken forsetter helt til spilleren skriver inn 99
while svar != "99":
    # Legger på feilhåndtering, så programmet ikke avsluttes viss spillern skriver en bokstav
    try:
        svar = input("Gjett ett tall mellom 0 og 3(skriv 99 for å avslutte spillet): ")
        
        if int(svar) == int(tilfeldig_tall):
            # Merk vi konverterer både svar tilfeldig tall til heltall
            # Legger til ett poeng til poeng summen hvis riktig 
            poengsum +=1
            print ("Riktig, din poensum er nå: " + str(poengsum))
            # Merk vi konverterer poengsummen til string når den skal skrives ut
            tilfeldig_tall = random.randint(0, 2)

            # Hvis spiler skriver 99. Skriver hadet bra
        elif int(svar) == int(99):
            print("Avslutt")
            exit()

            # Hvis spillern gjettet feil
        else:
            print("Desverre feil, gjett igjen")

    # Ved feil gis tilbakemelding til spillern
    except ValueError:
        print("SKRIV TALL!!")
        
    
`