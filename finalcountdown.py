from PIL import Image

im = Image.open('meme_met_tekst.jpg')

for x in range(1000, -1, -1):
    print(x)

    if x < 1:
        im.show()
    
