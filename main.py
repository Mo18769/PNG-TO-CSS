import cv2 as cv
import os
string = "body {\n     background: black;\n     }\n  #image {\n      position: absolute;\n      top: 30px;\n      left: 50%;\n      margin-left: -200px;\n      width: 0;\n      height: 0;\n      box-shadow:\n"

img = cv.imread(f"input.png", -1)
rows,cols,_ = img.shape


x = 0
y = -1

#print(cols)
for i in range(rows): #|
    y+= 1
    x = -1
    for j in range(cols): # ----
            x+=1
            k = img[i,j]
            k = str(k)
            k = k.replace("[","")
            k = k.replace("]","")
            
            #print(k)
            k = k.split()

            b = int(k[0])
            g = int(k[1])
            r = int(k[2])
            
            hex = '#%02x%02x%02x' % (r, g, b)
            #print(k)
            string += f"        {x}px {y}px 1px 1px {hex},\n" #rgb({r},{g},{b})


string = string[:-1]
string = string[:-1]
string+="}"

os.remove("main.css")

f = open("main.css", "a")
f.write(string)

