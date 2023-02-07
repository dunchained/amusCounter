from glob import glob
from collections import Counter
import pandas
# Importi, instaliraš sve što je uvezeno sa: pip install -r requirements.txt

#Praviš listu fajlova u folederu input, u taj folder metneš sve one txtove gdje su pjesme.
file_list = glob('input/*.txt')
#Otvaraš praznu listu
song_list = []
#For petlja za item koji je file na listi fajlova koju so gore napravio
for item in file_list:
    #Otvoriš svaki file
    with open(item, 'rb') as f:
        # u data upišeš svaku liniju
        data = f.readlines()
        # sad za svaku liniju u ovom fajlu otkidaš s početka ono vrijeme i sa zada imaju nake oznake
        for line in data:
            # ovdje decodiraš tekst u txt jer dodje u bytes formatu i otkidaš 
            # s lijeve strane po 8 znakova, vrijeme i onu crticu, a desne strane po dva naka znaka koja dodju,
            # nemam pojma šta su, helem, otkineš i njih
            strip_line = line.decode("cp1255")[8:-2]
            # txt za svaku pjesmu, čist tekst dodaješ na listu pjesama koju so gore napravio praznu
            song_list.append(strip_line)

# counter je brojanje istih itema na listi, odnosno praviš dictionary za svaki item na listi pjesama, key je
# pjesma, a vrijednost je broj ponavljanja na listi pjesama           
counter = dict(Counter(song_list))
# zapis je pandas dataframe od te counter dictionarija
zapis = pandas.DataFrame(data=counter, index=[0])
# transponovanje u kolonu
zapis = zapis.T
# zapis u excel file
zapis.to_excel('prebrojano.xlsx', index=[0])