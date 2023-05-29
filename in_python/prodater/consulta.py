from funcs import *

res = menu(['Consultar data atual', 'Inserir data manual'])
if res == 1:
    tempo = int(input('Válido por quantos dias? '))
    validade(dias=tempo)

elif res == 2:
    hoje = str(input('Insira a data (formato: 19/05/2023): '))
    tempo = int(input('Válido por quantos dias? '))
    validade(hoje, tempo) # type: ignore
