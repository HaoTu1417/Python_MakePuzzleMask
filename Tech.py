from PIL import Image

img = Image.open('Duc.png')

img = img.resize((500,500), Image.ANTIALIAS)
img.save('testThu.png')

def tech():
    mage1 = Image.open(r"Duc.png")
    # image1.show()width, height
    width, height = image1.size

    image2  = Image.new("RGBA", (1971+width, height), "#000000")
    image2.paste(image1,(1972,0))

    pixdata = image2.load()

    for y in range(image2.size[1]):
        for x in range(image2.size[0]):
            if pixdata[x, y] != (0, 0, 0, 255):
                pixdata[x, y] = (0, 0, 0, 0)
           
    image2.show()
    image2.save(r"C:\Users\HaoTu\Desktop\KetQUa.png") 