import graphics as g

Win = g.GraphWin('Gradient', 400, 150)

#Allow user to decide how many rectangles are drawn
Scale = int(input('How expansive do you want your gradient? Enter a number from 1 - 5 with 1 being less expansive and 5 being most expansive :'))
NumOfRec = 6 * Scale
AddedWidth = 400 / NumOfRec #This tells us how much we need to move in the x direction for each new triangle


#These variables will keep track of changing x coordinates in our loop
TL_x = 0
BR_x = AddedWidth

#Initialize variables to change color
CurrentColor = 0
AddedColor = int(255 / NumOfRec)

#Loop to draw each rectangle
for N in range(0,NumOfRec):
    TopLeft = g.Point(TL_x,0)
    BottomRight = g.Point(BR_x, 400)
    
    #Create, add and color current rectangle
    CurrentRectangle = g.Rectangle(TopLeft,BottomRight)
    CurrentRectangle.draw(Win)
    CurrentRectangle.setFill(g.color_rgb(int(CurrentColor/2),0,CurrentColor))
    CurrentRectangle.setOutline(g.color_rgb(int(CurrentColor/2),0,CurrentColor))
    
    #Increment our x coordinates
    TL_x = TL_x + AddedWidth
    BR_x = BR_x + AddedWidth

    #Add color for next rectangle
    CurrentColor = CurrentColor + AddedColor