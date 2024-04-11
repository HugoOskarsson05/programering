'''
1. skapa 5 olika tärningar
2. skapa ett poängblock (börja med 1-6 )
3. skapa olika kombinationer som funkar med tärningarna
4. skapa ett poängsystem
'''
import random

tärningar = []

for i in range(5):
    # lägg till slumptal, 1 till 4, i listan tärningar
    tärningar.append(random.randint(1,6))

print(tärningar)
print("min", min(tärningar))
print("max", max(tärningar))
print("summa", sum(tärningar))
print("antal fyror", tärningar.count(6))

# räkna antal ettor
antal_ettor = 0
for tärning in tärningar:
    if tärning == 1:
        antal_ettor = antal_ettor + 1

print("antal ettor", antal_ettor)

# fungerar inte om vi vill ändra på värden i listan
for tärning in tärningar:
    tärning = 7 - tärning

print(tärningar)

# create dictionary
dictionary = {"ettor": "-", "tvåor": "-", "treor": "-" 
, "fyror": "-", "femmor": "-", "Sexor": "-"}
print(dictionary)
# print output is shown below each print statement
# {'key 1': 'value 1', 'key 2': 'value 2'}

for i in range(2):
    print("välj vilka tärningar som ska slås om (_"+str(i+1)+"/2)")
        
    Byta = input("byt första tärningen j/n")
    if Byta == "j" : 
        tärningar [0] = random.randint(1,6) 

    Byta = input("byt andra tärningen j/n")
    if Byta == "j" : 
        tärningar [1] = random.randint(1,6) 

    Byta = input("byt tredje tärningen j/n")
    if Byta == "j" : 
        tärningar [2] = random.randint(1,6) 

    Byta = input("byt fjärde tärningen j/n")
    if Byta == "j" : 
        tärningar [3] = random.randint(1,6) 

    Byta = input("byt femte tärningen j/n")
    if Byta == "j" : 
        tärningar [4] = random.randint(1,6) 

    print(tärningar)



print("välj")
print("ettor")
print("tvåor")
print("treor")
print("fyror")
print("femmor")
print("sexor")
