from graphics import *
from msdie import MultiSidedDie

class DieView:
    def __init__( self, window, centerPoint, size ):
        self.die = MultiSidedDie( 6, 1 )
        self.window = window
        
        minX = centerPoint.getX() - size / 2.0
        maxX = centerPoint.getX() + size / 2.0
        
        minY = centerPoint.getY() - size / 2.0
        maxY = centerPoint.getY() + size / 2.0
        
        ulPt = Point( minX, minY)
        lrPt = Point( maxX, maxY)
        
        self.dieOutline = Rectangle( ulPt, lrPt )
        self.dieOutline.setFill( 'white' )
        self.dieOutline.draw( window )
    
        pipRadius = size / 7 / 2
        column1X = centerPoint.getX() - size / 4
        column3X = centerPoint.getX() + size / 4
        row1Y = centerPoint.getY() - size / 4
        row3Y = centerPoint.getY() + size / 4

        self.pip1_1 = self.__makePip( column1X, row1Y, pipRadius )
        self.pip1_3 = self.__makePip( column3X, row1Y, pipRadius )
        
        self.pip2_1 = self.__makePip( column1X, centerPoint.getY(), pipRadius )
        self.pip2_2 = self.__makePip( centerPoint.getX(), centerPoint.getY(), pipRadius )
        self.pip2_3 = self.__makePip( column3X, centerPoint.getY(), pipRadius )
        
        self.pip3_1 = self.__makePip( column1X, row3Y, pipRadius )
        self.pip3_3 = self.__makePip( column3X, row3Y, pipRadius )
        
     
    def __makePip( self, x, y, r ):
        pip = Circle( Point( x, y ), r )
        pip.setFill( 'black' )
        return pip
    
    def __clearPips( self ):
        self.pip1_1.undraw()
        self.pip1_3.undraw()
        self.pip2_1.undraw()
        self.pip2_2.undraw()
        self.pip2_3.undraw()
        self.pip3_1.undraw()
        self.pip3_3.undraw()
    
    def __updatePips( self, dieValue ):
        self.__clearPips()
        
        if dieValue == 1 or dieValue == 3 or dieValue == 5:
            self.pip2_2.draw( self.window )
        
        if dieValue >= 2 and dieValue <= 6:
            self.pip1_1.draw( self.window )
            self.pip3_3.draw( self.window )
            
        if dieValue >= 4 and dieValue <= 6:
            self.pip1_3.draw( self.window )
            self.pip3_1.draw( self.window )
            
        if dieValue == 6:
            self.pip2_1.draw( self.window )
            self.pip2_3.draw( self.window )
        
    
    def roll( self ):
        self.die.roll()
        self.__updatePips( self.die.getValue() )
        
    def getValue( self ):
        return self.die.getValue()