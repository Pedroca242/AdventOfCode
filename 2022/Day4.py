def result(file):
    count = 0
    for f in file:
        f = f.replace('\n', '')
        interval1, interval2 = f.split(',')
        interval1 = interval1.split('-')
        interval2 = interval2.split('-')

        n1 = [i for i in range(int(interval1[0]), int(interval1[-1])+1)]
        n2 = [i for i in range(int(interval2[0]), int(interval2[-1])+1)]

        check = [n for n in n1 if n in n2]

        if len(check) != 0:
            count += 1
    return count

file = open('Day4Input.txt')
print(result(file))

