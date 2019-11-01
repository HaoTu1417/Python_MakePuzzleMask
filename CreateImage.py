from PIL import Image
import numpy as np
import math 
import random
import os.path


#tinh resolution tu 1 hinh va 4 huong xem co huong nao la canh ko
def GetTargetResolution(source,edges):
    width = source[0] + (matchPixelH * 2)
    height = source[1] + (matchPixelW * 2)
    # if edges[0] != 0 :
    #     width += matchPixelH
    # if edges[1] != 0 :
    #     height += matchPixelW
    # if edges[2] != 0 :
    #     width += matchPixelH
    # if edges[3] != 0 :
    #     height += matchPixelW
    
    return width, height
# tinh do phan giai cho scale
def CalculateMathPixel(baseSize , pieceSize):
    return math.floor(pieceSize[0] * baseSize[0] / baseSize[1]), math.floor(pieceSize[1] * baseSize[0] / baseSize[1])
# tinh index cho ca 4 canh
def Get4Index(index,cols,rows):
    rowNumber = math.floor(index/cols)
    result = [0,0,0,0]
    result[3] =  ((rowNumber+1) * (cols-1)) +index
    result[2] =  rowNumber * (cols -1) +index 
    result[1] = (rowNumber * cols)-rowNumber -cols + index 
    result[0] = ((rowNumber+1) * (cols))-(rowNumber+1) -(cols) +index

    if index/cols < 1 :
        result[1] = -2
    if index/(cols) >= rows-1 :
        result[3] = -2
    if index % cols == 0 :
        result[0] = -2
    if (index+1) % cols == 0:
        result[2] = -2


    # if index % 3 == 0
    #     return -11
    return  result

#ghep 4 canh vao
def CombineImage(sourceImage,edge,edgeInfos):
    if edgeInfos[edge] ==-2 :
        return

    tmp = [edgeInfos[0],edgeInfos[1],edgeInfos[2],edgeInfos[3]]
    addImage = sourceImage

    if edge == 2 :
        x =  pieceResolution[0] + matchPixelH
        y = matchPixelW

        if pieceTarget[edgeInfos[edge]] == -1:
            addImage = imgCai
            x -= matchPixelH
        if pieceTarget[edgeInfos[edge]] == 1:
            addImage = imgDuc
        
        newSize = (matchPixelH,pieceResolution[1])
        tmpImge =  addImage.resize(newSize,Image.NEAREST)

        sourceImage.paste(tmpImge,(x,y))


    if(edge == 0):
        x = 0
        y = matchPixelW

        if pieceTarget[edgeInfos[edge]] == -1:
            addImage = imgDuc.rotate(-180)
        if pieceTarget[edgeInfos[edge]] == 1:
            addImage = imgCai.rotate(-180)
            x += matchPixelH
        
        newSize = (matchPixelH,pieceResolution[1])
        tmpImge =  addImage.resize(newSize,Image.NEAREST)
       
        sourceImage.paste(tmpImge,(x,y))


    if(edge == 1):
        y = 0
        x = matchPixelH

        if pieceTarget[edgeInfos[edge]] == -1:
            addImage = imgDucNgang
            

        if pieceTarget[edgeInfos[edge]] == 1:
            addImage = imgCaiNgang
            y+=matchPixelW

        newSize = (pieceResolution[0],matchPixelW)
        tmpImge =  addImage.resize(newSize,Image.NEAREST)
        
        sourceImage.paste(tmpImge,(x,y))

    if(edge == 3):
        x = matchPixelH
        y = pieceResolution[1] + matchPixelW
       
        if pieceTarget[edgeInfos[edge]] == -1:
            addImage = imgCaiNgang.rotate(180)
            y -= matchPixelW
        if pieceTarget[edgeInfos[edge]] == 1:
            addImage = imgDucNgang.rotate(180)
        
        newSize = (pieceResolution[0],matchPixelW)
        tmpImge =  addImage.resize(newSize,Image.NEAREST)

        
        sourceImage.paste(tmpImge,(x,y))



    

  

    

    
    
    
   


def CreateSinglePiece(pieceIndex,cols,rows,pieceSize):

    # do phan giai cho 1 mieng
    edgesDefine = Get4Index(pieceIndex,cols,rows)
    
    targetpieceResolution = GetTargetResolution(pieceSize,edgesDefine)
    

   
    #tao  phan o giua
    imgBlackMid = Image.new("RGBA",(pieceSize[0],pieceSize[1]),"#000000")
    imgMid = Image.new("RGBA",targetpieceResolution,"#FF0000")
    
    x = matchPixelH
    y = matchPixelW
        
    imgMid.paste(imgBlackMid,(x,y))
    
    #ghep 4 canh vao 
   
    CombineImage(imgMid,0,edgesDefine)
    CombineImage(imgMid,1,edgesDefine)
    CombineImage(imgMid,2,edgesDefine)
    CombineImage(imgMid,3,edgesDefine)

    # xoa phan du
    pixdata = imgMid.load()
    for y in range(imgMid.size[1]):
        for x in range(imgMid.size[0]):
            #if pixdata[x,y]==(255,0,0,255) : #or (pixdata[x, y][0] > 150 and (pixdata[x, y][1]>=0 or pixdata[x, y][2]>=0))
            if pixdata[x,y][0] >= 250 and pixdata[x,y][1] == 0 and pixdata[x,y][2] ==0 : #or (pixdata[x, y][0] > 150 and (pixdata[x, y][1]>=0 or pixdata[x, y][2]>=0))
                #pixdata[x,y] = pixdata[x,y]
                pixdata[x,y] = (0,0,0,0)


    #imgMid.show()
    imgMid.save(strPath+'/'+str(pieceIndex)+'.png')


    
print('Hello man')
#do phan giai
width = 0
height =0
while 1==1:
    strResolution = input('Hay nhap do phan giai cach bang dau x: ').split('x')
    if len(strResolution) != 2:
        print('Nhap sai cau truc , mau 1920x1080, hay nhap lai')
        continue
    try:
        print(strResolution[0])
        width = int(strResolution[0])
        height = int(strResolution[1])
        break
    except :
        print('Hay nhap 2 so cach bang dau x')
        continue
   
   
sourceResolution = (width,height)
# so dong va cot
cols = 4
rows = 3

while 1==1:
    strResolution = input('Hay nhap cot va dong cach bang dau x: ').split('x')
    if len(strResolution) != 2:
        print('Nhap sai cau truc , mau 4x3, hay nhap lai')
        continue
   
    try:
        colIp = int(strResolution[0])
        rowIp = int(strResolution[1])
        cols = colIp
        rows = rowIp
        break
    except :
        print('Hay nhap 2 so cach bang dau x')
        continue

    
print('Do phan giai')
print(sourceResolution)
print('So cot va so dong')
print(str(cols)+" x "+str(rows))
print('Processing..........')

#kiem tra va tao folder
strPath = str(sourceResolution[0])+"X"+str(sourceResolution[1])+"_"+str(cols)+"x"+str(rows)
if not os.path.exists(strPath):
    os.makedirs(strPath)


# do phan giai cho 1 mieng 
pieceResolution = (math.floor(sourceResolution[0]/cols),math.floor(sourceResolution[1]/rows))

# image 2 mieng duc va cai
imgDuc = Image.open(r"Duc.png")
imgCai = Image.open(r"Cai.png")
imgDucNgang = Image.open(r"DucNgang.png")
imgCaiNgang = Image.open(r"CaiNgang.png")

# do trung cua 2 mieng
matchPixelW,matchPixelH = CalculateMathPixel((imgDuc.size),pieceResolution)



#array duc cai quyet dinh phan loi lom cua cac mieng
total = (cols-1) * rows + cols * (rows-1)

pieceTarget = [None] * total

index =0
for i in range(total):
    tmp = random.randint(0,1)
    if tmp == 0:
        tmp = -1
    pieceTarget[i] = tmp
for i in range(cols*rows ):
    CreateSinglePiece(i, cols,rows,pieceResolution)

print('Done')
print('Ket qua trong folder:'+strPath)
