import libs 
import struct
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

glCreateWindow(800,400)

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
        glLine(299,200,100,100)
        glFinish()

    elif menuOption == "2":
        print("----")
        input ("Has ingresado a la opción 2...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
       
        glFinish()
    
    elif menuOption == "3":
        print("----")
        input ("Has ingresado a la opción 3...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
        
        glFinish()
    
    elif menuOption == "4":
        print("----")
        input ("Has ingresado a la opción 4...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
       
        glFinish()
    
    elif menuOption == "5":
        print("----")
        input ("Has ingresado a la opción 5...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
       
        glFinish()
    
    elif menuOption == "6":
        print("----")
        input ("Has ingresado a la opción 6...\npulsa una tecla para continuar")
        glViewPort(0,0,799,599)
        glClear()
        glColor(1, 0, 0)
        glVertex(0,0)
       
        glFinish()
    

    
    
   

    elif menuOption == "0":
        break 
    else: 
        print("")
        input("No has ingresado ninguna opción correcta...\npulsa una tecla para continuar")