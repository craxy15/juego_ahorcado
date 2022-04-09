import random
palabra_secreta =[]
with open('./data.txt','r',encoding='utf-8') as f:
        for line in f:
            palabra_secreta.append(line)
        

print('Bienvenido al juego')

letrap=''
palabra_secreta=random.choice(palabra_secreta)   
vidas=5

while vidas>0:

    fallas=0
    for letra in palabra_secreta:
        if letra in letrap:
            print(letra,end='')
        else:
            print('_', end=' ')
            fallas+=1
    if fallas==0:
        print('Felicidades,ganaste')
        break

    tuletra=input('Entroduce una letra: ')
    letrap+=tuletra
    if tuletra in letrap:
        print("Ya has usado esta letra,prueba con otra!")

    if tuletra not in palabra_secreta:
        vidas-=1
        print('Te has equvocado')
        print("Te queda " + str(vidas) + " vidas")
    if vidas==0:
        print('Perdiste')
else:
    print('Gracias por participar!')

    




def run():
    pass






if __name__ =='__main__':
    run()