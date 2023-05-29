def pass_generator():
    from string import ascii_letters, digits, punctuation
    from random import choice
    caracteres = ascii_letters + digits + punctuation
    password = ''
    for caracter in range(0, 15):
        password += choice(caracteres)
    return password
