
def partone(file):
    prio = 0
    for f in file:
        letras = str(f)
        primeira = letras[0:int(len(letras)/2)]
        segunda = letras[int(len(letras)/2):len(letras)]

        semelhantes = []
        for i in primeira:
            for j in segunda:
                if i == j and i not in semelhantes:
                    semelhantes.append(i)
                else:
                    pass
        if semelhantes[0].isupper():
            prio += (ord(semelhantes[0])-ord('A') + 27)
        else:
            prio += (ord(semelhantes[0])-ord('a') + 1)

    return prio

def parttwo(file):
    content = file.readlines()
    prio = 0

    for i in range(2,len(content),3):
        terceira = content[i]
        segunda = content[i-1]
        primeira = content[i-2]

        semelhantes = []
        for m in primeira:
            for n in segunda:
                for p in terceira:
                    if m == n == p and m not in semelhantes and m != '\n':
                        semelhantes.append(m)
                    else:
                        pass

        if semelhantes[0].isupper():
            prio += (ord(semelhantes[0]) - ord('A') + 27)
        else:
            prio += (ord(semelhantes[0]) - ord('a') + 1)

    return prio

file = open('2022/Day3Input')
print(partone(file))
file = open('2022/Day3Input')
print(parttwo(file))
