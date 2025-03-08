valores = list(range(4,11))
print(valores)

num = [8,2,5,4,9,3,0]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

print(f'essa lista tem {len(num)} valores')

num.pop(0)
print(num)
