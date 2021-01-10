# poengteller
Løsningsforslag på oppgave Poengteller. Lagd i Python

Spille går ut på at man skal gjette tall mellom 0-3.

Spilleren får poeng for hvert tall som gjettes riktig.

Åpne main.py filen for å se brukerveiledningen. 


# Anvisning

Først begynner vi med å importere nødvendige biblioteker
```
# Importerer random-biblioteket
import random
```

Deretter opprettes verdiene vi trenger

```
 
# Oppretter ett tilfeldig tall mellom 0-3
tilfeldig_tall = random.randint(0, 3)
# Begynner med at poensummen til spilleren er null
poengsum=0

# Begynner med blankt svar
svar = ""
```

Så starter man en løkke ved hjelp av kommandoen `while`.

Inne i while-løkken har vi først feilhåndteringsrutiner med kommandoen `try`.

Så tar vi imot svaret fra brukeren med kommandoen `input`. 


```
# Lager en løkke, hvor spilleren kan skrive inn tall
# Hvis svaret er ikke 99 sjekkes svaret mot det tilfeldige tallet
# Løkken forsetter helt til spilleren skriver inn 99
while svar != "99":
    # Legger på feilhåndtering, så programmet ikke avsluttes viss spillern skriver en bokstav
    try:
        svar = input("Gjett ett tall mellom 0 og 3(skriv 99 for å avslutte spillet): ")
```
Vi konverterer svaret fra bruken og det tilfeldige tallet til heltall.

Hvis spilleren har gjettet riktig legges det til ett poeng til poensummen
 ```
        if int(svar) == int(tilfeldig_tall):
            # Merk vi konverterer både svar tilfeldig tall til heltall
            # Legger til ett poeng til poeng summen hvis riktig 
            poengsum +=1
            print ("Riktig, din poensum er nå: " + str(poengsum))
```
Vi lager nytt tilfeldig tall hvis spilleren har gjettet riktig med kommandoen random. randint betyr at det skal lages ett heltall. I parantesen skriver man inn intervallet man ønsker tallet fra.
```
            # Merk vi konverterer poengsummen til string når den skal skrives ut
            tilfeldig_tall = random.randint(0, 3)
```
Vi sjekker om spillern vill avslutte. Hvis spilleren avslutter bruker vi komandoen `exit()`
```
            # Hvis spiler skriver 99. Skriver hadet bra
        elif int(svar) == int(99):
            print("Avslutt")
            exit()
```
Hvis vi spilleren gjetter alt annet en riktig - eller 99 sier vi at spilleren har gjettet feil
```            # Hvis spillern gjettet feil
        else:
            print("Desverre feil, gjett igjen")
```
Legg merke til at på slutten av løkken er kommandoen `except` som viser tilbakemelding til spilleren hvis det oppstår en feil.
```
  # Ved feil gis tilbakemelding til spillern
    except ValueError:
        print("SKRIV TALL!!")
 ```
        
    

