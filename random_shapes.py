#Variables with 'Format' at the end were created after initial testing had a bug where the output still had parentheses and the text 'Point'. Removal is necessary for this program to cooperate with shape_painter.py

from random import *
from graphics import *

def userInput():
    try:
        fileName = input('Enter the drawing file name to create : ')
        numOfShapes = int(input('Enter the number of shapes to make (1-100) : '))
    except ValueError:
        print('\nInvalid input')
        numOfShapes = int(input('Enter the number of shapes to make (1-100) : '))
    while numOfShapes<1 or numOfShapes>100:
        print('Value too small/large')
        numOfShapes = int(input('Enter the number of shapes to make (1-100) : '))
    return fileName, numOfShapes

def createShapes(fileName, numOfShapes):
    outputFile = open(fileName, 'w')
    shapesDrawn = 0
    
    while shapesDrawn < numOfShapes:
        
        #Gives either 0 for Circle or 1 for Rectangle
        determineShape = randrange(0,2)
        
        RGB = randrange(0,256), randrange(0,256), randrange(0,256)
        RGBFormat = format(str(RGB).strip('()'))
        
        #We need 1 point for Circle and 2 for Rectangle. Generating a point here reduces some redundancy
        firstPointX = str(randrange(0,501))
        firstPointY = str(randrange(0,501))
        firstPointFormat = firstPointX + ', ' + firstPointY
        
        if determineShape == 0:
            shapeType = 'Circle'
            # 100 was chosen so we wouldn't have enormous circles taking up most of the screen
            radius = randrange(1,100)
            print('{0}; {1}; {2}; {3}'.format(shapeType, firstPointFormat, radius, RGBFormat), file=outputFile)
        else:
            shapeType = 'Rectangle'
            secondPointX = str(randrange(0,501))
            secondPointY = str(randrange(0,501))
            secondPointFormat = secondPointX + ', ' + secondPointY
            print('{0}; {1}; {2}; {3}'.format(shapeType, firstPointFormat, secondPointFormat, RGBFormat), file=outputFile)
            
        shapesDrawn += 1
        
    outputFile.close()
    print('Done creating all {0} shapes'.format(numOfShapes))
    
def main():
    fileName, numOfShapes = userInput()
    createShapes(fileName, numOfShapes)

main()