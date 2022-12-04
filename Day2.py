file = open('Day2Input')

gabarito1 = {'A':1, 'B': 2, 'C': 3}
# gabarito2 = {'X':1, 'Y': 2, 'Z': 3}
gabarito2 = {'X':0, 'Y': 3, 'Z': 6}

pont2 = 0

# Parte 1
# for f in file:
#     if gabarito1[f.split()[0]] == gabarito2[f.split()[1]]:
#         pont2 += gabarito2[f.split()[1]] + 3
#     elif f.split()[0] == 'A' and f.split()[1] == 'Y':
#         pont2 += gabarito2[f.split()[1]] + 6
#     elif f.split()[0] == 'B' and f.split()[1] == 'Z':
#         pont2 += gabarito2[f.split()[1]] + 6
#     elif f.split()[0] == 'C' and f.split()[1] == 'X':
#         pont2 += gabarito2[f.split()[1]] + 6
#     else:
#         pont2 += gabarito2[f.split()[1]]

# Parte 2
for f in file:
    if f.split()[1] == 'Y':
        pont2 += gabarito1[f.split()[0]] + gabarito2[f.split()[1]]
    elif f.split()[1] == 'X':
        if f.split()[0] == 'A':
            pont2 += gabarito1['C']
        elif f.split()[0] == 'B':
            pont2 += gabarito1['A']
        else:
            pont2 += gabarito1['B']
    elif f.split()[1] == 'Z':
        if f.split()[0] == 'A':
            pont2 += gabarito1['B'] + 6
        elif f.split()[0] == 'B':
            pont2 += gabarito1['C'] + 6
        else:
            pont2 += gabarito1['A'] + 6

print(pont2)

