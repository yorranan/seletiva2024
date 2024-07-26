import math

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

peso = int(input())
velocidade_max = 0
count = 0

while count < 10:
    if primo(peso):
        velocidade_max += peso
        count += 1
    peso += 1

print(f"{velocidade_max} km/h")
res = 60000000 / velocidade_max
days = res // 24
print(f"{int(res)} h / {int(days)} d")
