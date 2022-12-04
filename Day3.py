class Day3:
    def __init__(self, file):
        self.file = file

    def partone(self):
        minusculos = 'abcdefghijklmnopqrstuvwxyz'
        maiusculos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
                prio += (maiusculos.index(semelhantes[0]) + 27)
            else:
                prio += (minusculos.index(semelhantes[0]) + 1)

        return prio

    def parttwo(self):
        content = file.readlines()
        minusculos = 'abcdefghijklmnopqrstuvwxyz'
        maiusculos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
                prio += (maiusculos.index(semelhantes[0]) + 27)
            else:
                prio += (minusculos.index(semelhantes[0]) + 1)

        return prio


file = open('Day3Input')

obj = Day3(file)
print(obj.parttwo())
