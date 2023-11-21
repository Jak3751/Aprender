lockdown = False
status = 'Em casa' if lockdown else 'Uhuuuu'
#Por que ternario? porque é divido em 3 partes, "em casa" = verdadeiro, "lockdown" é a expressão lógica e "Uhuuuu" = falso.
print(status)
print(f'O status é: {status}')


lockdown = True
grana = 99
status = 'Em casa' if lockdown and grana <=100 else 'Uhuuuu'
print(f'O status é: {status}')

