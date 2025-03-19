from time import sleep

def maior(*num):
    for c in num:
        print(c, end = ' | ')
        sleep(0.3)
    print()
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor é {max(num)}.')
    print('-'*30)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
