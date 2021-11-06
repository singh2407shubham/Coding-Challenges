def hammingDistance(self, x: int, y: int) -> int:
    X, Y = x, y
    binaryX, binaryY = [0]*32, [0]*32
    i,j=0,0
    count = 0
    while X > 0:
        binaryX[i] = X%2
        X=X//2
        i+=1
    while Y > 0:
        binaryY[j] = Y%2
        Y=Y//2
        j+=1

    for m in range(32):
        if binaryX[m]!=binaryY[m]:
            count+=1
    return count    
