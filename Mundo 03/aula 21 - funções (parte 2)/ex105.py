def notas(*num, sit=False):
    '''
    :param num: Mostra as notas
    :param sit: (opcional) Mostra a situação da turma com base na média geral
    :return: Dicionário com total de alunos, maior nota, menor nota, média e situação
    '''
    dici = dict()
    dici['total'] = len(num)
    dici['maior'] = max(num)
    dici['menor'] = min(num)
    dici['média'] = sum(num)/len(num)
    if sit:
        if dici['média'] < 5:
            dici['situação'] = 'péssima'
        elif 5 <= dici['média'] < 7:
            dici['situação'] = 'regular'
        elif 7 <= dici['média'] < 9:
            dici['situação'] = 'boa'
        else:
            dici['situação'] = 'ótima'
    return dici


resp = notas(4.5, 3.2, 9.5, 7.8, sit = True)
print(resp)
print('-' * 30)
for k, v in resp.items():
    print(f'{k} é {v}')
