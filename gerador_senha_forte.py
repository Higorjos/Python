import random, string

'''
Para o tamanho da senha é aconselhavel ter no mínimo 16 caracteres para
ser considerada uma senha forte.
'''
tamanho = 16


character = string.ascii_letters + string.digits + '!@#$%&*()-+=?/'

rnd = random.SystemRandom()

print('A senha gerada foi: ')
print(''.join(rnd.choice(character) for i in range(tamanho)))