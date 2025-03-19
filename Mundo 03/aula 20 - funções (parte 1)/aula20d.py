def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
        cont +=1
    print(lst)

valores = [2,5,7,1,4,6]
print(valores)
dobra(valores[:])
