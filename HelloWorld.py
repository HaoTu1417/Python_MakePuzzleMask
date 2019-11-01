import random
print('abc hello world')
 
matrixWidth = 4
matrixHeight = 3

resolutionWidth = 1920
resolutionHeight = 1080

cols = matrixWidth -1
rows = matrixHeight -1

result = list()

index = 0
for i in range(matrixHeight+2):
    for j in range(cols + (i%2)):
        index +=1
        result.append(random.randint(0,1))

print(result)