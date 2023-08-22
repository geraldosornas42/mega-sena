# numeros
import random

lista_mega = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]

def jogo_um():
    lista_jogo_um = [3,14,19,23,35,38]
    print(f"mesmo jogo:{lista_jogo_um}")

def jogo_dois():
    lista_jogo_dois = [8,13,23,32,47,53]
    print(f"mesmo jogo:{lista_jogo_dois}")

def jogo_tres():
    lista_jogo_tres = [1,5,15,21,34,46]
    print(f"mesmo jogo:{lista_jogo_tres}")


def aposta():
    b = 0
    lista_aposta = []
    while b < 6:
        a = int(input("digite um valor: "))
        lista_aposta.append(a)
        b = b + 1
        if b == 6:{
            print(f"numeros escolhidos:{lista_aposta}")
        }


def mega_sena():
    a = 0
    lista_mega_sorteada = []
    while a < 6:
        m = random.choice(lista_mega)
        lista_mega_sorteada.append(m)
        a = a + 1
        if a == 6:{
            print(f"numeros sorteados:{lista_mega_sorteada}")
        }

# jogo 

#aposta()
jogo_um()

mega_sena()
contador = 0

while jogo_um != mega_sena: 
    jogo_um()
    mega_sena()
    contador = contador + 1
    if jogo_um == mega_sena:{
        print(contador)
    }

