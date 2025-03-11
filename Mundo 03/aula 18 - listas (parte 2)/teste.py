import random

nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Gabriela", "Henrique", "Isabela", "João",
    "Karen", "Lucas", "Mariana", "Nathan", "Olivia", "Paulo", "Quésia", "Rafael", "Sofia", "Tiago",
    "Ursula", "Vinícius", "Wellington", "Xavier", "Yasmin", "Zaqueu", "Alice", "Bernardo", "Camila", "Diego",
    "Elaine", "Fábio", "Giovana", "Hugo", "Ingrid", "Juliano", "Kátia", "Leonardo", "Melissa", "Nelson",
    "Oscar", "Priscila", "Quirino", "Rebeca", "Samuel", "Talita", "Ulisses", "Vera", "William", "Zilda"
]

qnt = int(input('Quantos nomes você deseja? '))

for c in range(qnt):
    print(random.choice(nomes))
    print(f'nota 1: {random.randint(0,10)}')
    print(f'nota 2: {random.randint(0,10)}')