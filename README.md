# Puzzle-Amnesia
solução de puzzle do jogo amnesia usando programação

Esse script foi feito para solucionar um desafio, que é feito em um jogo (amnesia)
ele se baseava em: existiam números na parte de cima e na parte de baixo , entre eles havia uma 
alavanca, se a alavanca estivesse apontada para parte de cima o numero de cima seria 
escolhido, se estivesse para a parte de baixo o numero de baixo 
seria escolhido, no final os números que ficaram em cima 
deveriam se somar e dar o resultado 8 e os debaixo também.

os número eram :

3  3  5  1  2  4


1  5  6  5  2  2

a ordem certa é:

005120 = 8

150002 = 8

(o zero indica que a alavanca foi colocada para o lado oposto)

Me baseando nisso, elaborei um programa que realiza esse processo sozinho, testando todas
as possiblidades possiveis.

nele eu considero os numeros não usados como zero e os que são usados continuam iguais
então fiz um codigo que fizesse varios binarios em uma lista e depois essa lista 
seria multiplicada nos valores das listas problema 
