
def achar_maior(file):
    valores = []
    atual = 0
    maiores = [0, 0, 0]

    for f in file:
        print(maiores)
        if f != '\n':
            valores.append(int(f))
        else:
            atual = sum(valores)
            valores = []
        if min(maiores) <= atual and atual not in maiores:
            maiores[maiores.index(min(maiores))] = atual

    return sum(maiores)

file = open('Day1Input')


print(achar_maior(file))



