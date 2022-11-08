from math import sqrt

# Inputs
# assumption is that both class (A, B) sizes are the same.
# (code is based off this assumption therefore changes may be required for a flexible class size)
classA = [[1, 1], [1, 2]]
classB = [[2, 1], [3, 1]]

# Minimum distance
def dMin(classA, classB):
    min = 9999
    n = len(classA)
    for i in range(n):
        calc = 0
        for j in range(2):
            calc += (classB[i][j] - classA[i][j]) ** 2
        calc = sqrt(calc)
        if calc <= min:
            min = calc
    return min


# Maximum distance
def dMax(classA, classB):
    max = -9999
    n = len(classA)
    for i in range(n):
        calc = 0
        for j in range(2):
            calc += (classB[i][j] - classA[i][j]) ** 2
        calc = sqrt(calc)
        if calc >= max:
            max = calc
    return max


# Average distance
def dAvg(classA, classB):
    avg = 0
    n = len(classA)
    for i in range(n):
        for j in range(n):
            calc = 0
            for m in range(2):
                calc += (classB[j][m] - classA[i][m]) ** 2
            calc = sqrt(calc)
            avg += calc
    avg = avg / (n * n)
    return avg


# Mean distance
def dMean(classA, classB):
    mean = 0
    n = len(classA)
    xMean1 = 0
    yMean1 = 0
    xMean2 = 0
    yMean2 = 0
    for i in range(n):
        xMean1 += classA[i][0]
        yMean1 += classA[i][1]
    xMean1 = xMean1 / n
    yMean1 = yMean1 / n
    for i in range(n):
        xMean2 += classB[i][0]
        yMean2 += classB[i][1]
    xMean2 = xMean2 / n
    yMean2 = yMean2 / n
    mean = sqrt((xMean2 - xMean1) ** 2 + (yMean2 - yMean1) ** 2)
    return mean


# Print/function calls
print("dMin: {:.2f}".format(dMin(classA, classB)))
print("dMax: {:.2f}".format(dMax(classA, classB)))
print("dAvg: {:.2f}".format(dAvg(classA, classB)))
print("dMean: {:.2f}".format(dMean(classA, classB)))
