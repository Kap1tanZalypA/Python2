#KAUPPATEHTÄVÄ
#On yleinen tapa, että luokkien nimet alkavat isolla alkukirjaimella
#Sinulla on kauppa, kaupassa on osastoja, osastoilla on tavaroita
#tarvitset kolme luokkaa: Kauppa, Osasto, Tuote
#osasto-luokalla on lista siihen kuuluvista tuotteista
#tee seuraavat osastot: "Maito", "Suurimot", "Proteiinit"
        
#tee 100 kappaletta Tuote-olioita, joilla on
#satunnainen paino ja koko, Tuotteessa on tieto mihin osastoon se kuuluu. Laita nämä listaan "kuorma"
        
#tee Kauppaan metodi "lajittele_tuotteet" joka ottaa kuorma-listan ja laittaa kunkin tuotteen omalle osastolleen
#tee Osastoon metodi, joka laskee kuinka monta Tuotteita osastolla on laitettu
#tee Tuote-olioon metodi, joka vertaa tuotteen vanhenemispäivää ja   Kaupan kalenteria. Jos tuotteen vanhenemispäivä on vanhempi kuin kaupan kalenteri, tuote merkitsee itsensä poistettavaksi. Kaupan kalenteri etenee päivän kerrallaan. Kalenteri voi olla joko aito PYthonin date/time olio tai vain kasvava kokonaisluku.  (jokaisella tuotteella on viittaus
#kauppaan ja sen omaan osastoon)
import random                                          

class Kauppa:
    def osastoja(self):
        self.maito = []
        self.suurimot = []
        self.proteiinit = []
        self.kuukausi = 10  

class tuote:
    def __init__(self):
        self.letter = random.choice(['Maito','Suurimot', 'Proteiini' ])
        self.month = random.randint(1, 12)  
        self.size = random.randint(1, 20)

        
    def __repr__(self):
       return f"{self.letter} month: {self.month} size: {self.size}"

class Kuorma:
    def kuorma(self,k):
        for _ in range(100):
            t = tuote()
            if t.letter == 'Maito':
                k.maito.append(t)
            if t.letter == 'Suurimot':
                k.suurimot.append(t)
            if t.letter == 'Proteiini':
                k.proteiinit.append(t)
    def paivays(self,k):
        tulos1 = []
        for i in range(len(k.maito)):
            if k.maito[i].month > k.kuukausi:
                tulos1.append(k.maito[i])
        k.maito = tulos1

        tulos2 = []
        for q in range(len(k.proteiinit)):
            if k.proteiinit[q].month > k.kuukausi:
                tulos2.append(k.proteiinit[q])
        k.proteiinit = tulos2

        tulos3 = []
        for i in range(len(k.suurimot)):
            if k.suurimot[i].month > k.kuukausi:
                tulos3.append(k.suurimot[i])
        k.suurimot = tulos3

            
        
        
        

k = Kauppa()
k.osastoja()

kuor = Kuorma()
kuor.kuorma(k)
kuor.paivays(k)
count1 = len(k.suurimot)
count2 = len(k.maito)
count3 = len(k.proteiinit)


print("Suurimot:")
for a in range(len(k.suurimot)):
    print(k.suurimot[a])

print("Maitotuotteet:")
for i in range(len(k.maito)):
    print(k.maito[i])
    
print("\nProteiinit:")
for x in range (len(k.proteiinit)):
    print(k.proteiinit[x])

