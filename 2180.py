import math 
def primo(n):
    primo = 0
    save = int(math.sqrt(n))
    for i in range(1, save):
        if (n%i == 0):
            return False

    return True

peso = int(input())
velocidade_max = 0
i = 0
while i < 10:
    if (primo(peso)):
        velocidade_max += peso
        i+=1
    peso += 1
print("{}  km/h".format(velocidade_max))
res = 60000000/velocidade_max
res = res//24
print("{} h / {} d".format(60000000/velocidade_max, res))
