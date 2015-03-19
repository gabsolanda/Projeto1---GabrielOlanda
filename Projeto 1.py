# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ('Vamos começar? O jogo é basicamente um pedra-papel-tesoura mas agora acrescentamos os personagens Spock e Lagarto.\n')

j = 0 
jpc = 0
jplayer = 0

while (jpc<3 and jplayer<3): #Delimitando o limite de jogadas válidas para 3.
    import random
    pc=random.randint(0,4) #Selecionando aleatoriamente as escolhas para o computador
    j=j+1
    
    print ('Faça sua escolha considerando: 0 - Pedra; 1 - Papel; 2 - Tesoura; 3 -Spock e 4 - Lagarto\n')
    player = int(input('Digite o número equivalente a sua escola:\n'))
    
    if player == 0:
        if pc == 0:
            print ('Você empatou com o computador\n')
        elif pc == 1:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 2:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 3:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 4:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        else:
            print ('Essa entrada não é valida. Escolha um núemro entre 0 e 4\n')
            
    if player == 1:
        if pc == 0:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 1:
            print ('Você empatou com o computador\n')
        elif pc == 2:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 3 :
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 4:
            print ('O computador ganhou, não desista\n')
        else:
            print ('Essa entrada não é valida. Escolha um núemro entre 0 e 4\n')
            
    if player == 2:
        if pc == 0:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 1:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 2:
            print ('Você empatou com o computador\n')
        elif pc == 3:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 4:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
            
    if player == 3:
        if pc == 0:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 1:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 2:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 3:
            print ('Você empatou com o computador\n')
        elif pc == 4:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
            
    if player == 4:
        if pc == 0:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 1:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 2:
            print ('O computador ganhou, não desista\n')
            jpc = jpc + 1
        elif pc == 3:
            print ('Parabéns, você ganhou essa\n')
            jplayer = jplayer + 1
        elif pc == 4:
            print ('Você empatou com o computador\n')
            
    if jpc == 3:
        print ('Que pena o computador ganhou, mas não desista')
        
    if jplayer == 3:
        print ('Você é fera, ganhou dessa máquina, continue assim')
            
            
            
            
            
            
            
            
        
    