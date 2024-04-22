def findPoint(distanceMatrix):
    x, y = 0,0
    x = distanceMatrix[0][0]
    y = distanceMatrix[x][0]
    if (distanceMatrix[x][y] == 0):
        return(x,y)
    
    else:
        y = distanceMatrix[0][0]
        x = distanceMatrix[0][y]
        return(x,y)


distanceMatrix = [
[5, 5, 5, 5, 5, 5, 5, 5],
[4, 4, 4, 4, 4, 4, 4, 4],
[3, 3, 3, 3, 3, 3, 3, 4],
[3, 2, 2, 2, 2, 2, 3, 4],
[3, 2, 1, 1, 1, 2, 3, 4],
[3, 2, 1, 0, 1, 2, 3, 4],
[3, 2, 1, 1, 1, 2, 3, 4],
[3, 2, 2, 2, 2, 2, 3, 4],
]

print(findPoint(distanceMatrix))

testCase2 = [
    [3, 3, 3, 3, 4, 5, 6],
    [2, 2, 2, 3, 4, 5, 6],
    [1, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [1, 1, 2, 3, 4, 5, 6],
    [2, 2, 2, 3, 4, 5, 6],
    [3, 3, 3, 3, 4, 5, 6],
]

print(findPoint(testCase2))

