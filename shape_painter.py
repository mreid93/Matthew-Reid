from graphics import *

def getPoint( pointString ):
    pointString = pointString.strip()
    x, y = pointString.split(',')
    return Point( int( x ), int( y ))

def getRadius( radiusString ):
    return int( radiusString.strip() )

def getColor( colorString ):
    colorString = colorString.strip()
    if colorString.isalpha() :
        return colorString
    elif len( colorString.split( ',' ) ) == 3:
        r, g, b = colorString.split( ',' )
        return color_rgb( int(r), int(g), int(b) )
    else:
        return 'white'

def parseRectangleProperties( rectangleLine ):
    tokens = parseShapeLine( rectangleLine )
    if len( tokens ) == 4:
        shape, upperLeftPtString, lowerRightPtString, colorString = tokens
        return upperLeftPtString, lowerRightPtString, colorString
    else:
        shape, upperLeftPtString, lowerRightPtString = tokens
        colorString = ''
        return centerPtString, radiusString, colorString     

def getRectangleFromLine( rectangleLine ):
    upperLeftPtString, lowerRtPtString, colorString = parseRectangleProperties( rectangleLine )
    
    upperLeftPoint = getPoint( upperLeftPtString )
    lowerRightPoint = getPoint( lowerRtPtString )
    color = getColor( colorString )
    
    rectangle = Rectangle( upperLeftPoint, lowerRightPoint )
    rectangle.setFill( color )
    return rectangle

def parseCircleProperties( circleLine ):
    tokens = parseShapeLine( circleLine )
    if len( tokens ) == 4:
        shape, centerPtString, radiusString, colorString = tokens
        return centerPtString, radiusString, colorString
    else:
        shape, centerPtString, radiusString = tokens
        colorString = ''
        return centerPtString, radiusString, colorString 
    
def parseShapeLine( line ):
    return line.split(';')
    

def getCircleFromLine( circleLine ):
    centerPtString, radiusString, colorString = parseCircleProperties( circleLine )

    centerPoint = getPoint( centerPtString )
    radius = int( radiusString )
    color = getColor( colorString )
    
    circle = Circle( centerPoint, radius )
    circle.setFill( color )
    return circle

def getDrawingFile():
    drawingFileName = input("Enter drawing file name: ")
    drawingFile = open( drawingFileName, 'r' )
    return drawingFileName, drawingFile

def getShape( line ):
    return line.split(';')[0].strip()


def drawShapesInWindow( window, shapes ):
    for shape in shapes:
        shape.draw( window )

def getShapesFromFile( drawingFile ):
    lineCount = 0
    shapes = []
    for line in drawingFile:
        lineCount = lineCount + 1
        
        shapeName = getShape( line )
        shape = None
        if shapeName.casefold() == "circle":
            shape = getCircleFromLine( line )
        elif shapeName.casefold() == "rectangle":
            shape = getRectangleFromLine( line )
        else:
            raise ValueError( "ERROR on line {0}: Invalid shape '{1}'".format( lineCount, shapeName ) )
 
        shapes.append( shape )
    return shapes

def main():
    drawingFileName, drawingFile = getDrawingFile()
    shapes = getShapesFromFile( drawingFile )
 
    win = GraphWin( drawingFileName, 500, 500 )
    drawShapesInWindow( win, shapes )
    
main()
    
    

