jogador = dict()


jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
jogador['gols'] = list()

for c in range(jogador['partidas']):
    jogador['gols'].append(int(input(f'     - Quantos gols na partida {c+1}? ')))

jogador['total'] = sum(jogador['gols'])

print('-=' * 30)

print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.')

soma = 0
for i, v in enumerate(jogador['gols']):
    print(f'     - Na partida {i+1}, fez {v} gols')

print(f'No total, foram feitos {jogador['total']} gols em {jogador['partidas']} jogos, com uma média de {jogador['total']/jogador['partidas']:.2f} gols por partida')
