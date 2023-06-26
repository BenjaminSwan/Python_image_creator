from graphics import *

#This function is used for drawing a line on the 
def drawLine(point1, point2, win, colour):
    dL = Line(point1,point2)
    dL.draw(win)
    dL.setOutline(colour)

#This is a function that is used to draw triangles
def drawRectangle(topLeft, bottomRight,win,colour):
    dR = Rectangle(topLeft, bottomRight)
    dR.draw(win)
    dR.setFill(colour)
    dR.setOutline(colour)

#This will get the center of the circle, you need this for when you are trying to draw a circle
def CentreOfCircle(topLeft,dimension):
    x1 = topLeft.getX()
    y1 = topLeft.getY()
    x2 = x1 + dimension/2
    y2 = y1 + dimension/2
    centre = Point(x2,y2)
    return centre

#This function is used to draw a circle
def drawCircle(topLeft, dimension, radius,win,colour):
    centre = CentreOfCircle(topLeft,dimension)
    dC = Circle(centre,radius)
    dC.draw(win)
    dC.setFill(colour)

#This function is used to creat polygons
def drawPolygon(point1,point2,point3,point4, win, colour):
    dP = Polygon(point1,point2,point3,point4)
    dP.draw(win)
    dP.setFill(colour)
    dP.setOutline(colour)

#This patch is your square, pollygon and circle patch that is the mainly used design in your assingment it also allocates the base x/y
def patchPen(base, win, colour):
    x = base.getX()
    y = base.getY()

#This loop was made to creat the dimonds in the pattern 
    for h in range (10, 100, 20):
        for w in range (10, 100, 20):
            point1 = Point(x+w, y+h+10)
            point2 = Point(x+w+10, y+h)
            point3 = Point(x+w, y+h-10)
            point4 = Point(x+w-10, y+h)
            drawPolygon(point1,point2,point3,point4, win, colour)

#this section is used to creat the colloms in pattern 
    for i in range(0,100,40):
        topLeft = Point(x+i,y)
        bottomRight = Point((x+i+20),y+100)
        drawRectangle(bottomRight,topLeft, win, colour)
    
#this creats the extra boxes to creat the plad pattern
    for i in range(20,100,40):
        topLeft = Point(x,y+i)
        bottomRight = Point(x+100, y+i+20)
        drawRectangle(topLeft,bottomRight, win, colour)

#This will draw white circles in a set pattern across the patch
    for h in range(10,100,20):
        for w in range(10,100,20):
            topLeft = Point(x+w, y+h)
            drawCircle(topLeft,0,5,win,"white")
    
#This is the spiral patch that is used for the diagonal going accross the screen
def patchFin(base, win, colour):
    x = base.getX()
    y = base.getY()
    for i in range(0,100,10):
        point1 = Point(x+0,y+i+0)
        point2 = Point(x+i+ 10,y+100)
        drawLine(point1, point2, win, colour)
        point3 = Point(x+i+0,y+0)
        point4 = Point(x+100,y+i+10)
        drawLine(point3, point4, win, colour)

#This is where the size of the window is created to the users size choice 
def program():

#This section is used to ask the user what size they want the patch to be
    while True:
        try:
            PWsize = int(input("[5][7][9] \nEnter patch size: "))
            if PWsize == 5 or PWsize == 7 or PWsize == 9:
                break
            else:
                print("Your input was invalid, please enter, \n[5][7][9] ")
                continue
        except ValueError:
            print("Your input was invalid, please enter, \n[5][7][9] ")
            continue

#This section is used to find out the colours the user wants to use    
    userColourSelection = []    
    for i in range(3):
        while True:
            print("colours = [red = r][green = g][blue = b][magenta = m][orange = o][cyan = c]")
            UCS = input("Enter colour:\n").lower()
            if UCS == "r":
                userColourSelection.append("red")
                i+1
                break
            elif UCS == "g":
                userColourSelection.append("green")
                i+1
                break
            elif UCS == "b":
                userColourSelection.append("blue")
                i+1
                break
            elif UCS == "m":
                userColourSelection.append("magenta")
                i+1
                break
            elif UCS == "o":
                userColourSelection.append("orange")
                i+1
                break
            elif UCS == "c":
                userColourSelection.append("cyan")
                i+1
                break
            else:
                print("Invalid input please enter one of the listed colours:\n")
                continue

#This will initialize the GUI 
    win = GraphWin("PatchCW",PWsize*100, PWsize*100)   
    win.getMouse()

#tThis section is used to make the size of the window to the size that the user wanted 
    edge = PWsize*100 - 100
    for y in range(0,PWsize*100,100):
        for x in range(0,PWsize*100,100):
            base = Point(x,y)

#This section is the different scales that the user can choose from this means that depending on the user input it will display the correct scaled pattern
            if PWsize == 5:
                if x == 100 and y == 100 or x == 200 and y == 200 or x == 300 and y == 300:
                    patchFin(base, win, userColourSelection[0])
                elif x == 0 and y == 200 or x == 0 and y == 400 or x == 200 and y == 0 or x == 400 and y == 0 or x == 400 and y == 200 or x == 200 and y == 400: 
                    patchPen(base, win, userColourSelection[1])
                elif x == 0 and y == 0 or x == 400 and y == 400:
                    patchFin(base, win, userColourSelection[1])
                else:
                    patchPen(base, win, userColourSelection[0])
                    if y == 0 or y == edge or x ==0 or x == edge:
                        patchPen(base, win,userColourSelection[2])
                    else:
                        patchPen(base, win,userColourSelection[0]) 
            elif PWsize == 7: 
                if x == 100 and y == 100 or x == 200 and y == 200 or x == 300 and y == 300 or x == 400 and y == 400 or x == 500 and y == 500:
                    patchFin(base, win, userColourSelection[0])
                elif x == 200 and y == 0 or x == 400 and y == 0 or x == 600 and y == 0 or x == 600 and y == 200 or x == 600 and y == 400 or x == 0 and y == 200 or x == 400 and y == 600 or x == 200 and y == 600 or x == 0 and y == 600:
                    patchPen(base, win, userColourSelection[1])
                elif x == 0 and y == 0 or x == 600 and y == 600:
                    patchFin(base, win, userColourSelection[1])
                else:
                    patchPen(base, win, userColourSelection[0])
                    if y == 0 or y == edge or x ==0 or x == edge:
                        patchPen(base, win,userColourSelection[2])
                    else:
                        patchPen(base, win,userColourSelection[0])
            elif PWsize == 9: 
                if x == 100 and y == 100 or x == 200 and y == 200 or x == 300 and y == 300 or x == 400 and y == 400 or x == 500 and y == 500 or x == 600 and y == 600 or x == 700 and y == 700:
                    patchFin(base, win, userColourSelection[0])
                elif x == 200 and y == 0 or x == 400 and y == 0 or x == 600 and y == 0  or x == 800 and y == 0 or x == 800 and y == 200 or x == 800 and y == 400 or x == 800 and y == 600 or x == 600 and y == 800 or x == 400 and y == 800 or x == 200 and y == 800 or x == 0 and y == 800 or x == 0 and y == 600 or x == 0 and y == 400 or x == 0 and y == 200:
                    patchPen(base, win, userColourSelection[1])
                elif x == 0 and y == 0 or x == 800 and y == 800:
                    patchFin(base, win, userColourSelection[1])
                else:
                    patchPen(base, win, userColourSelection[0])
                    if y == 0 or y == edge or x ==0 or x == edge:
                        patchPen(base, win,userColourSelection[2])
                    else:
                        patchPen(base, win,userColourSelection[0])

#This will run the main program                    
program()

#I have put this here so the program doesnt close instantly when it has finished running
input("Please press enter to close the program:\n")