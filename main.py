from PIL import Image
from PIL import ImageColor

def rozdelenie (row:str):
    skupiny = []
    row = row.strip()
    for i in range(0,len(row),6):
        skupina = row[i:i+6]
        skupiny.append(skupina)
    return skupiny

fr = open("result.txt", "r", encoding="UTF-8")
fl = fr.readline().strip().split(" ")
picture = Image.new("RGB", (int(fl[0]),int(fl[1])), "white")
pixels = picture.load()

y = 0

for row in fr:
    x = 0
    temp = rozdelenie(row)
    for i in range(len(temp)):
        hexa = "#" + temp[i]
        color = ImageColor.getcolor(hexa,"RGB")
        pixels[x,y] = (color[0],color[1],color[2])
        x+=1
    y+=1
picture.show()
uhfaukh
