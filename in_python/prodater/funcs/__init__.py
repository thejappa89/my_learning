from datetime import date, datetime, timedelta


def linha(tam=42):
    print('-' * tam)


def titulo(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    op = leiaint('Sua opção: ')
    return op


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m\nEntrada de lib interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def validade(data=date.today(), dias=0):
    hoje = None
    if type(data) is str:
        hoje = datetime.strptime(data, '%d/%m/%Y')
    if type(data) is date:
        hoje = data
    validade = hoje + timedelta(days=dias) # type: ignore
    print(linha())
    print(f'Fabricação: {hoje.strftime("%d/%m/%Y")}') # type: ignore
    print(f'Validade: {validade.strftime("%d/%m/%Y")}')
