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
#derfor printer den først hei også funksjon


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
liste=[]

k=0
for i in liste:
    print(liste[k])
    k=k+1

print("Lagene som har vunnet minst ett seriemesterskap:")
for lag in eliteserielag:
    if lag["seriemesterskap"]:
        print(lag["lag"])

x = 0
for x in liste:
     print(liste[x])
     x=x+1
     print("lagene som har vunnet minst ett seriemesterskap og ett norgemesterskap")
     



# %%
#oppgave 4
