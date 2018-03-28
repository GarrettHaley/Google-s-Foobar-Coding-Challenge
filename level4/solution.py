from itertools import permutations

def answer(times,time_limit):
    paths = []
    pathDistances = [] 
    matrixDimensions = len(times)
    for i in range(matrixDimensions-1):
        paths.extend(permutations(range(1,matrixDimensions-1),i))
    paths = [[0] + list(path) + [matrixDimensions-1] for path in paths]
    distanceMatrix = GetDistanceGraphMatrix(times)
    if distanceMatrix == -1:
        return range(0,matrixDimensions-2) 
    for path in paths:
        pathLength = GetPathLength(distanceMatrix,path)
        if pathLength <= time_limit:
            pathDistances.append([path,pathLength])
    maxLength = max([len(p[0]) for p in pathDistances]) 
    pathDistances = [p for p in pathDistances if len(p[0]) == maxLength]
    fastestPaths = [p[0] for p in pathDistances]
    for p in fastestPaths:
        p.sort()
    fastestPaths.sort()
    bunnies = fastestPaths[0][1:-1]
    bunnies = [i-1 for i in bunnies]
    return bunnies
    
def GetDistanceGraphMatrix(weightedMatrix):
    vertexInt = len(weightedMatrix)
    dMatrix = [[0 for i in range(vertexInt)] for j in range(vertexInt)]
    for i in range(vertexInt):
        for j in range(vertexInt):
            dMatrix[i][j] = weightedMatrix[i][j]
    for x in range(vertexInt):
        for i in range(vertexInt):
            for j in range(vertexInt):
                if dMatrix[i][j] > dMatrix[i][x] + dMatrix[x][j]:
                    dMatrix[i][j] = dMatrix[i][x] + dMatrix[x][j]
                    if dMatrix[j][j] < 0:
                        return -1
    return dMatrix

def GetPathLength(weightedMatrix,path):
    pathLength = 0
    for i in range(len(path)-1):
        pathLength += weightedMatrix[path[i]][path[i+1]]
    return pathLength
