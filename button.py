from graphics import *

class Button:
    def __init__( self, window, centerPt, width, height, text ):
        self.minX = centerPt.getX() - width / 2.0
        self.maxX = centerPt.getX() + width / 2.0
        
        self.minY = centerPt.getY() - height / 2.0
        self.maxY = centerPt.getY() + height / 2.0
        
        ulPt = Point( self.minX, self.minY)
        lrPt = Point( self.maxX, self.maxY)
        
        self.rect = Rectangle( ulPt, lrPt )
        self.rect.setFill( 'light gray' )
        self.rect.draw( window )
        
        self.text = Text( centerPt, text )
        self.text.draw( window )
        
        self.enable()
        
    def enable( self ):
        self.isEnabled = True
        self.text.setFill ('black')
        self.rect.setWidth( 2 )
    
    def disable( self ):
        self.isEnabled = False
        self.text.setFill ('dark gray' )
        self.rect.setWidth( 1 )
    
    def wasClickedIn( self, clickPoint ):
        return self.isEnabled and clickPoint.getX() >= self.minX and clickPoint.getX() <= self.maxX and clickPoint.getY() >= self.minY and clickPoint.getY() <= self.maxY