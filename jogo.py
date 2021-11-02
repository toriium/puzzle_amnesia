p = 0
op = 0

# listas a serem testadas
valor1 = [1, 5, 6, 5, 2, 2]
valor2 = [3, 3, 5, 1, 2, 4]

# listas de binarios
b1 = []
b2 = []

while True:
    # copia da lista
    l1 = valor1[:]
    l2 = valor2[:]

    # gerador de binario em lista
    n = str(bin(p))
    n = n.replace('0b', "")
    for c in range(0, len(n)):
        b1.append(int(n[c]))

    # condicional de alternancia e parada
    if len(b1) > len(l1) and op == 0:
        op = 1
        p = 0
        b1.clear()
        b1.append(0)
        print('\n\nAgora se o primeiro numero não for usado\n\n')
    if len(b1) > len(l1) and op == 1:
        break

    # lista binaria inversa
    for c in range(0, len(b1)):
        if b1[c] == 1:
            b2.append(0)
        else:
            b2.append(1)

    # aplicando os binarios na lista
    if op == 0:
        for c in range(0, len(b1)):
            l1[c] = l1[c] * b1[c]
            l2[c] = l2[c] * b2[c]
    if op == 1:
        for c in range(0, len(b1)):
            l1[c] = l1[c] * b2[c]
            l2[c] = l2[c] * b1[c]

    # igualdade na soma das lista
    if sum(l1) == sum(l2):
        print('===' * 10)
        print(f'numero {p}')
        print(f'binario {n}')
        print(f'binario 1 {b1}')
        print(f'binario 2 {b2}')
        print(f'lista 1   {l1}')
        print(f'lista 2   {l2}')
        print(f'soma lista 1 {sum(l1)}')
        print(f'soma lista 2 {sum(l2)}')
        print('===' * 10)
    else:
        print(p)
    # as listas devem ser apagadas pois estão com valores alterados
    b1.clear()
    b2.clear()
    l1.clear()
    l2.clear()
    # incremento do numero a ser usado como binario no proximo teste
    p = p + 1

print('tentativas esgotadas')
