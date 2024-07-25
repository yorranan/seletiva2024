import math

def recursao(k, inicial, lista_elementos):
    print("Elemento inicial")
    print(inicial)
    while(lista_elementos):
        print("Lista de elementos ainda nao acabou")
        # print(lista_elementos)
        tamanho_lista = len(lista_elementos)
        for i in lista_elementos:
            if abs(i*i - k) % (2 * N + 1) == 0:
                lista_elementos.pop(lista_elementos.index(i))
                print("Entrou no if")
                if lista_elementos:
                    print("K REMOVE DA LISTA?")
                    k = lista_elementos.pop(0)
                print("IMPOSSÍVEL QUE NAO TENHA ENTRADOOOOOOOOO")
        print("Tamanho lista_elementos")
        print(len(lista_elementos))
        print("Tamanho inicial")
        print(tamanho_lista)
        if len(lista_elementos) == tamanho_lista:
            print("Quebrou")
            return 0
    return inicial

lista_elementos = []
lista_solucoes = []
N = int(input())
for i in range(1, N*2+1):
    lista_elementos.append(i)
# print(lista_elementos)
K = int(input())
lista_elementos.pop(int(math.sqrt(K))-1)
for i in lista_elementos:
    print("Em que elemento da lista ele está?")
    print(i)
    print(i*i - K)
    print(2 * N + 1)
    if abs(K - i*i) % (2 * N + 1) == 0:
        print("Ele entra nesse if?")
        print("Quais elementos sobraram?")
        # print(lista_elementos)
        if lista_elementos:
            value = recursao(K, i, lista_elementos)
            print("Saiu da recursao")
            print(value)
            if value != 0:
                lista_solucoes.append(value)
                print("achou algum valor?")
        else:
            lista_solucoes.append(i)

lista_solucoes.sort(reverse=True)
print(lista_solucoes)
print(lista_solucoes[0] * lista_solucoes[0])
