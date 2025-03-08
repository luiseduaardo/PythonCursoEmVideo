times = ['Corinthians', 'Atlético-MG', 'Grêmio', 'São Paulo', 'Internacional', 'Sport',
         'Santos', 'Cruzeiro', 'Palmeiras', 'Atlético-PR', 'Ponte Preta', 'Flamengo', 'Fluminense',
         'Chapecoense', 'Coritiba', 'Figueirense', 'Avaí', 'Vasco da Gama', 'Goiás', 'Joinville']

posicao = int(input('Me diga a posição que eu direi o time que ficou nessa posição no Brasileirão 2015: '))
while posicao > 20 or posicao <= 0:
    posicao = int(input('Me diga a posição que eu direi o time que ficou nessa posição no Brasileirão 2015: '))

print(f'O time na {posicao}ª posição foi o {times[posicao-1]}')
