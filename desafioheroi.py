nome = input('Nome do Herói: ')
xp = int(input('Quantidade XP: '))
nivel = ''
if xp < 1000:
    nivel ='FERRO'
elif xp >= 1001 and xp <= 2000:
    nivel = 'BRONCE'
elif xp >= 2001 and xp <= 5000:
    nivel = 'PRATA'
elif xp >= 5001 and xp <=7000:
    nivel = 'OURO'
elif xp >= 7001 and xp <= 8000:
    nivel = 'PLATINA'
elif xp >= 8001 and xp <= 9000:
    nivel = 'ASCENDENTE'
elif xp >= 9001 and xp <= 10000:
    nivel = 'INMORTAL'
elif xp >= 10001:
    nivel = 'RADIANTE'

print(f'O Herói de nome {nome} está no nível de {nivel}')
