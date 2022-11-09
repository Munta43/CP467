from math import sqrt

# Inputs
classA = [[1, 1], [1, 2]]
classB = [[2, 1], [3, 1]]

# classA = [[1, 1], [1, 2]]
# classB = [[2, 1]]

# Minimum distance
def dMin(classA, classB):
    min = 9999
    lenA = len(classA)
    lenB = len(classB)
    for i in range(lenA):
        for j in range(lenB):
            calc = 0
            for m in range(2):
                calc += (classB[j][m] - classA[i][m]) ** 2
            calc = sqrt(calc)
            if calc <= min:
                min = calc
    return min


# Maximum distance
def dMax(classA, classB):
    max = -9999
    lenA = len(classA)
    lenB = len(classB)
    for i in range(lenA):
        for j in range(lenB):
            calc = 0
            for m in range(2):
                calc += (classB[j][m] - classA[i][m]) ** 2
            calc = sqrt(calc)
            if calc >= max:
                max = calc
    return max


# Average distance (FIX)
def dAvg(classA, classB):
    avg = 0
    lenA = len(classA)
    lenB = len(classB)
    for i in range(lenA):
        for j in range(lenB):
            calc = 0
            for m in range(2):
                calc += (classB[j][m] - classA[i][m]) ** 2
            calc = sqrt(calc)
            avg += calc
    avg = avg / (lenA * lenB)
    return avg


# Mean distance (FIX)
def dMean(classA, classB):
    mean = 0
    lenA = len(classA)
    lenB = len(classB)
    xMean1 = 0
    yMean1 = 0
    xMean2 = 0
    yMean2 = 0
    for i in range(lenA):
        xMean1 += classA[i][0]
        yMean1 += classA[i][1]
    xMean1 = xMean1 / lenA
    yMean1 = yMean1 / lenA
    for i in range(lenB):
        xMean2 += classB[i][0]
        yMean2 += classB[i][1]
    xMean2 = xMean2 / lenB
    yMean2 = yMean2 / lenB
    mean = sqrt((xMean2 - xMean1) ** 2 + (yMean2 - yMean1) ** 2)
    return mean


# Print/function calls
print("dMin: {:.2f}".format(dMin(classA, classB)))
print("dMax: {:.2f}".format(dMax(classA, classB)))
print("dAvg: {:.2f}".format(dAvg(classA, classB)))
print("dMean: {:.2f}".format(dMean(classA, classB)))
