#%%
#oppgave 1 
# a)
print("Why did the programmer quit his job? Because he didn't get arrays")

#b
def dagens_vits():
    vits = "Why did the programmer quit his job? Because he didn't get arrays"
    print(vits)

    #c
dagens_vits()


#d
def dagens_vits2(vits):
    print(vits)

#E
dagens_vits2("a")

#F
def dagens_vits3(vits):
    print(vits)
    return("Because he didn't get arrays")

#G 
dagens_vits3("Why did the programmer quit his job? Because he didn't get arrays")
    

    
# %% 
# oppgave 2 
ord = "funksjon"
def minfunksjon(tekst):
    ord = tekst 
    return ord
print(minfunksjon("hei"))
print(ord)

#fordi ord blir definert som funksjon i starten av programmet
#derfor printer den først hei også funksjon 0g ikke hei 2 ganger


# %%
#oppgave 3
#%%
eliteserielag = [
  { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
  { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
  { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
  { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
  { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
  { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
  { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
  { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
  { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
  { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
  { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
]
#A
print("Lagene som har vunnet minst ett seriemesterskap:")
for lag in eliteserielag:
    if lag["seriemesterskap"]:
        print(lag["lag"])

    
#B
print("Lagene som har vunnet minst ett seriemesterskap og ett norgesmesterskap:")
for lag in eliteserielag:
    if lag["seriemesterskap"] and lag["norgesmesterskap"]:
        print(lag["lag"])

#C
mest_vinnendelag = 0
mest_seriemesterskap = 0

for lag in eliteserielag:
    antall_seriemesterskap = len(lag["seriemesterskap"])
    if antall_seriemesterskap > mest_seriemesterskap:
        mest_seriemesterskap = antall_seriemesterskap
        mest_vinnendelag = lag["lag"]
        
if mest_vinnendelag:
    print(f"Laget med flest seriemesterskap er {mest_vinnendelag} med {mest_seriemesterskap} mesterskap.")
else:
    print("Ingen lag har vunnet serien.")

#D
tidligste_vinner_lag = 0
tidligste_vinner_år = float('inf')  # Setter året til et høyt tall som en startverdi

for lag in eliteserielag:
    seriemesterskap = lag["seriemesterskap"]
    if seriemesterskap:
        tidligste_år = min(seriemesterskap)
        if tidligste_år < tidligste_vinner_år:
            tidligste_vinner_år = tidligste_år
            tidligste_vinner_lag = lag["lag"]

if tidligste_vinner_lag:
    print(f"Laget som vant serien første gang er {tidligste_vinner_lag} i år {tidligste_vinner_år}.")
else:
    print("Ingen lag har vunnet serien.")

#E
siste_vinnerlag = 0
siste_vinnerår = 0  # Setter året til null som en startverdi

for lag in eliteserielag:
    seriemesterskap = lag["seriemesterskap"]
    if seriemesterskap:
        siste_år = max(seriemesterskap)
        if siste_år > siste_vinnerår:
            siste_vinnerår = siste_år
            siste_vinnerlag = lag["lag"]

if siste_vinnerlag:
    print(f"Laget som vant serien sist er {siste_vinnerlag} i år {siste_vinnerår}.")
else:
    print("Ingen lag har vunnet serien.")







# %%
#oppgave 4
import random as rn 
 
# a)
def trekke_vinnertall():
    tallListe = list(range(1, 35)) # en liste fra 1 til 35
    vinnertall = [] 
    while len(vinnertall) <= 7:
        tall = tallListe[rn.randint(1,len(tallListe)-1)] #velger et tilfeldig tall fra lista med 34 tall
        vinnertall.append(tall) #legger et tilfeldig tall inn i  vinnertall listen
        tallListe.remove(tall) #fjerner det tilfeldige tallet fra lista sånn at mann ikke kan trekke det to ganger
   
    tillegstall = tallListe[rn.randint(1,len(tallListe)-1)] #tilfeldig tillegstall fra tallista
 
    return vinnertall, tillegstall #returnerer lista med vinnertall, og tillegstall
 
trekke_vinnertall() #kaller funksjonen
 
# b)
def sjekk_kupong(bruker_kupong, bruker_tillegs):
    total = 0
    tillegs = False
    vinnerkupong, tillegstall = trekke_vinnertall() 
    for vinnertall in vinnerkupong: #går gjennom alle vinnertall
        for bruker_tall in bruker_kupong: #går gjennom kupongen til brukeren
            if vinnertall == bruker_tall:
                tot += 1 #totalen blir 1 større for hvert samsvarende tall mellom bruker kupongen og vinnertallene
    if bruker_tillegs == tillegstall:
        tillegs = True #Tillegstall blir True hvis det stememr
 
    return(total, tillegs)
 
sjekk_kupong([4, 2, 5, 3, 6, 1], 19)
 
# c)
def generer_rekker(ant_rekker):
    rekker = []
    for i in range(1, ant_rekker+1): #kjører løkka like mange ganger parameteren sier
        rekker.append(trekke_vinnertall()) #adderer et sett med vinnertall og tillegstall som funksjonen trekk_vinnertall() lager
     
    return rekker
 
generer_rekker(4)




#%%
#oppgave 5
import turtle  
import time    
import random  

# Definer konstanter for vindusstørrelse og fargevalg for skilpaddene
WIDTH, HEIGHT = 700, 600  # Størrelsen på vinduet
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']  # farger til skilpaddene 

# Funksjon for å be brukeren om antall 
def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():  # Sjekker om inndata er numerisk
            racers = int(racers)
        else:
            print('Input is not numeric... Try Again!')  # Hvis inndata ikke er numerisk, gi en feilmelding
            continue

        if 2 <= racers <= 10:  # Sjekker om antallet deltakere er innenfor akseptabelt område
            return racers
        else:
            print('Number not in range 2-10. Try Again!')  # Hvis antallet ikke er i riktig område, gi en feilmelding

# Funksjon for racet 
def race(colors):
    turtles = create_turtles(colors)  # Oppretter skilpaddene

    while True:
        for racer in turtles: 
            distance = random.randrange(1, 20)  # Generer en tilfeldig avstand å bevege seg
            racer.forward(distance)  # Flytte skilpaddene fremover

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:  # Sjekk om skilpadden har nådd eller overskredet en bestemt høyde
                return colors[turtles.index(racer)]  # Returner fargen på vinneren

# Funksjon for å opprette skilpaddene
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)  # Beregn avstanden mellom skilpaddene horisontalt
    for i, color in enumerate(colors):
        racer = turtle.Turtle()  # Opprett en ny skilpadde
        racer.color(color)  # Angi fargen på skilpadden
        racer.shape('turtle')  # Angi formen til skilpadden
        racer.left(90)  # Snu skilpadden for å peke oppover
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)  # Plasser skilpadden i startposisjonen
        racer.pendown()
        turtles.append(racer)  # Legg skilpadden til listen

    return turtles  # Returner listen med skilpadder

# Funksjon for å åpne Turtle Graphics-vinduet
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)  # Sett opp vindusstørrelsen
    screen.title('Turtle Racing!')  # Angi tittelen på vinduet

# Spør brukeren om antall deltakere
racers = get_number_of_racers()

# åpner Turtle Graphics-vinduet
init_turtle()

# Bland fargene til deltakerne og begrenset til antall deltakere
random.shuffle(COLORS)
colors = COLORS[:racers]

# Start racet og vis vinneren
winner = race(colors)
print("The winner is the turtle with color:", winner)  # Skriv ut vinneren

# Vent i 5 sekunder før programmet avsluttes
time.sleep(5)

#%%
#oppgave 6


#%%
#oppgave 7
navn = ['Robert', 'Boris', 'Brad', 'George', 'David']
 
n = 5
k = 0
while k < n-2:
    temp = navn[k]
    navn[k] = navn[n-k-1]
    navn[n-k-1] = temp
    k = k+1

 
#%% # Oppgave 8
def fordeling(spillere, biler, plasser):
    spillere_i_bil = spillere // biler
    spillere_fordelt = [spillere_i_bil] * biler
    rest = spillere % biler

    for i in range(rest):
        spillere_fordelt[i] += 1

    return spillere_fordelt

spillere = int(input('Skriv antall spillere: '))
biler = int(input('Skriv antall biler: '))
plasser = int(input('Skriv antall plasser i hver bil: '))

fordelt_spillere = fordeling(spillere, biler, plasser)

for i, antall in enumerate(fordelt_spillere):
    print(f'I bil {i + 1}, er det {antall} spillere.')

# %%
