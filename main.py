import libs 
import struct
import math
import os 
from libs import Bitmap
from libs import word

#Objet to draw 
img = None

#Constructor 
def glInit():
    return None

#Init FrameBuffer
def glCreateWindow(width, height):
    global img 
    img = Bitmap(width,height) 

#Delete actual image 
def glClear(): 
    img.clear()
#Image area can draw
def glViewPort(x,y,widht, height):
    img.viewPort(x,y,widht, height)

#Get Color 
def glColor(r,g,b):
    img.color(r,g,b)

#Init canvas with new color 
def glClearColor(r,g,b):
    img.clearColor(0,0,0) 

#Get new x,y points 
def glVertex(x,y):
    img.vertex(x,y)

def getNewX(x): 
    return img.getNormXCoord(x)

def getNewY(y): 
    return img.getNormYCoord(y)

def glLine (x1,y1, x2,y2):
    img.line(x1, y1, x2, y2)

#Show new image 
def glFinish():
    img.writeFile("img.bmp")

def menu(): 
  #  os.system('cls')
    print ('0. Salir')
    print('1. Por renderizar una imagen negra con las siguientes líneas')
    print('2. Por una imagen negra con las siguientes líneas (parte dos)')
    print('3. Por renderizar por renderizar una imagen negra con las siguientes líneas (parte tres)')
    print('4. Por renderizar por renderizar una imagen negra con las siguientes líneas (parte 4)')
    print('5. Por renderizar un cubo')
    print('6. Por llenar un cubo isométrico')

glCreateWindow(800,600)

option = True 
while option: 
    menu()
    menuOption = input("Ingresa una opción del menú  >> ")

    if menuOption == "1":
        print("----")
        input ("Has ingresado a la opción 1...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(getNewX(10),getNewY(10),getNewX(510),getNewY(10))
        glLine(getNewX(10),getNewY(10),getNewX(462),getNewY(191))
        glLine(getNewX(10),getNewY(10),getNewX(354),getNewY(354))
        glLine(getNewX(10),getNewY(10),getNewX(191),getNewY(462))
        glLine(getNewX(10),getNewY(10),getNewX(10),getNewY(510))
        glFinish()

    elif menuOption == "2":
        print("----")
        input ("Has ingresado a la opción 2...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(getNewX(790),getNewY(590),getNewX(790),getNewY(90))
        glLine(getNewX(790),getNewY(590),getNewX(609),getNewY(138))
        glLine(getNewX(790),getNewY(590),getNewX(446),getNewY(246))
        glLine(getNewX(790),getNewY(590),getNewX(338),getNewY(409))
        glLine(getNewX(790),getNewY(590),getNewX(290),getNewY(590))
        glFinish()
    
    elif menuOption == "3":
        print("----")
        input ("Has ingresado a la opción 3...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(getNewX(10),getNewY(590),getNewX(510),getNewY(590))
        glLine(getNewX(10),getNewY(590),getNewX(462),getNewY(409))
        glLine(getNewX(10),getNewY(590),getNewX(354),getNewY(246))
        glLine(getNewX(10),getNewY(590),getNewX(191),getNewY(138))
        glLine(getNewX(10),getNewY(590),getNewX(10),getNewY(90))
        glFinish()
    
    elif menuOption == "4":
        print("----")
        input ("Has ingresado a la opción 4...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(getNewX(790),getNewY(10),getNewX(790),getNewY(510))
        glLine(getNewX(790),getNewY(10),getNewX(609),getNewY(462))
        glLine(getNewX(790),getNewY(10),getNewX(446),getNewY(354))
        glLine(getNewX(790),getNewY(10),getNewX(338),getNewY(191))
        glLine(getNewX(790),getNewY(10),getNewX(290),getNewY(10))
        glFinish()
    
    elif menuOption == "5":
        print("----")
        input ("Has ingresado a la opción 5...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(getNewX(100), getNewY(100), getNewX(200), getNewY(100))
        glLine(getNewX(100), getNewY(100), getNewX(100), getNewY(200))
        glLine(getNewX(200), getNewY(100), getNewX(200), getNewY(200))
        glLine(getNewX(100), getNewY(200), getNewX(200), getNewY(200))
        glLine(getNewX(150), getNewY(150), getNewX(250), getNewY(150))
        glLine(getNewX(150), getNewY(150), getNewX(150), getNewY(250))
        glLine(getNewX(250), getNewY(150), getNewX(250), getNewY(250))
        glLine(getNewX(150), getNewY(250), getNewX(250), getNewY(250))
        glLine(getNewX(100), getNewY(100), getNewX(150), getNewY(150))
        glLine(getNewX(100), getNewY(200), getNewX(150), getNewY(250))
        glLine(getNewX(200), getNewY(100), getNewX(250), getNewY(150))
        glLine(getNewX(200), getNewY(200), getNewX(250), getNewY(250))

        glFinish()
    
    elif menuOption == "6":
        print("----")
        input ("Has ingresado a la opción 6...\npulsa una tecla para continuar")
        glViewPort(0,0,700,500)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(getNewX(200), getNewY(200), getNewX(287), getNewY(250))
        glLine(getNewX(200), getNewY(200), getNewX(113), getNewY(250))
        glLine(getNewX(200), getNewY(200), getNewX(200), getNewY(300))
        glLine(getNewX(287), getNewY(250), getNewX(287), getNewY(350))
        glLine(getNewX(113), getNewY(250), getNewX(113), getNewY(350))
        glLine(getNewX(200), getNewY(300), getNewX(287), getNewY(350))
        glLine(getNewX(200), getNewY(300), getNewX(113), getNewY(350))
        glLine(getNewX(287), getNewY(350), getNewX(200), getNewY(400))
        glLine(getNewX(113), getNewY(350), getNewX(200), getNewY(400))       
        glFinish()

    elif menuOption == "0":
        break 
    else: 
        print("")
        input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")