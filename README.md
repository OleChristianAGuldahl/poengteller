# poengteller
Løsningsforslag på oppgave Poengteller.

Spille går ut på at man skal gjette tall mellom 0-9.

Spilleren får poeng for hvert tall som gjettes riktig.

Starter med at programmet finner ett tilfeldig tall

`tilfeldig_tall = random.randint(0, 3)`

Brukeren skriver inn ett tall:

 ` svar = input("Gjett ett tall mellom 0 og 10 (skriv 99 for å avslutte spillet): ") `

Sjekker om brukeren har gjettet riktig tall:

 ` if int(svar) == int(tilfeldig_tall):`
 
 Hvis riktig tall er gjettet, får spilleren ett nytt poeng og nytt gjettetall lages:
 ```poengsum +=1
        print ("Riktig, din poensum er nå: " + str(poengsum))
        tilfeldig_tall = random.randint(0, 2)
 ```
