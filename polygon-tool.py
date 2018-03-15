import graphics as g

winX = 400
winY = 300
Win = g.GraphWin('Polygon Maker', winX, winY)

topLeft = g.Point(winX - 50,0)
bottomRight = g.Point(winX, 50)

exitButton = g.Rectangle(topLeft,bottomRight)
exitButton.setFill('dark green')
exitButton.draw(Win)

exitText = g.Text(g.Point (winX - 25,25), "DONE?")
exitText.setTextColor('white')
exitText.draw(Win)

firstPoint = Win.getMouse()
lastPoint = firstPoint
lastPoint.draw(Win)

while True:
    nextPoint = Win.getMouse()

    if not( nextPoint.x >= (winX - 50) and nextPoint.y <= 50):
        polyEdge = g.Line(lastPoint, nextPoint)
        polyEdge.setFill('red')
        polyEdge.draw(Win)
        lastPoint = nextPoint
        
    else:    
        polyEdge = g.Line(firstPoint, lastPoint)
        polyEdge.setFill('blue')
        polyEdge.draw(Win)
        break

Win.getMouse()
Win.close()
