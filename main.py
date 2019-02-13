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

def glLine (x1,y1, x2,y2):
    img.line(x1, y1, x2, y2)

def newX(x):
    img.getNormXCoord(math.floor(x))

def newY(y):
    img.getNormYCoord(math.floor(y))

#Show new image 
def glFinish():
    img.writeFile("img.bmp")

def menu(): 
    os.system('cls')
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
        glLine(10,10,510,10)
        glLine(10,10,462,191)
        glLine(10,10,354,354)
        glLine(10,10,191,462)
        glLine(10,10,10,510)
        glFinish()

    elif menuOption == "2":
        print("----")
        input ("Has ingresado a la opción 2...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(790,590,790,90)
        glLine(790,590,609,138)
        glLine(790,590,446,246)
        glLine(790,590,338,409)
        glLine(790,590,290,590)
        glFinish()
    
    elif menuOption == "3":
        print("----")
        input ("Has ingresado a la opción 3...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(10,590,510,590)
        glLine(10,590,462,409)
        glLine(10,590,354,246)
        glLine(10,590,191,138)
        glLine(10,590,10,90)
        glFinish()
    
    elif menuOption == "4":
        print("----")
        input ("Has ingresado a la opción 4...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(790,10,790,510)
        glLine(790,10,609,462)
        glLine(790,10,446,354)
        glLine(790,10,338,191)
        glLine(790,10,290,10)
        glFinish()
    
    elif menuOption == "5":
        print("----")
        input ("Has ingresado a la opción 5...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(100, 100, 200, 100)
        glLine(100, 100, 100, 200)
        glLine(200, 100, 200, 200)
        glLine(100, 200, 200, 200)
        glLine(150, 150, 250, 150)
        glLine(150, 150, 150, 250)
        glLine(250, 150, 250, 250)
        glLine(150, 250, 250, 250)
        glLine(100, 100, 150, 150)
        glLine(100, 200, 150, 250)
        glLine(200, 100, 250, 150)
        glLine(200, 200, 250, 250)

        glFinish()
    
    elif menuOption == "6":
        print("----")
        input ("Has ingresado a la opción 6...\npulsa una tecla para continuar")
        glViewPort(0,0,700,500)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        glLine(200, 200, 287, 250)
        glLine(200, 200, 113, 250)
        glLine(200, 200, 200, 300)
        glLine(287, 250, 287, 350)
        glLine(113, 250, 113, 350)
        glLine(200, 300, 287, 350)
        glLine(200, 300, 113, 350)
        glLine(287, 350, 200, 400)
        glLine(113, 350, 200, 400)       
        glFinish()

    elif menuOption == "0":
        break 
    else: 
        print("")
        input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")