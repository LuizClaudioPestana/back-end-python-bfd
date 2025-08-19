tupla1 = (1, 2, 3, 4)
for num in tupla1:
    print(num + 5)
    
print("==================")

tupla2 = ("Fred", "João", "Maria", "Fred")

print(tupla2.count("Fred"))

print("==================")

frutas = {"banana", "manga", "Pêra", "tomate"}
legumes = {"Cenoura", "Couve-flor", "tomate"}

print(legumes.difference(frutas))
print(legumes.intersection(frutas))