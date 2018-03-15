from graphics import *
from msdie import MultiSidedDie
from die_view import DieView

class SumCounterView:
    def __init__(self, window, sum, counter):
        self.window = window
        self.sum = sum
        self.counter = counter
        
    def getSum(self):
       return self.sum

    def handleRoll(self, counter):
        sum = self.getSum()
        totalCounter = self.counter
        boxNumber = 0
        xChange = 95
        yChange = 20
        CenterPoint = Point(300, 40)
        currentNumber = 7
        while boxNumber < 4:
            topLeft = Point(CenterPoint.getX()-xChange, CenterPoint.getY()-yChange)
            bottomRight = Point(CenterPoint.getX()+xChange,CenterPoint.getY()+yChange)

            currentCounter = totalCounter[boxNumber]

            currentBox = Rectangle(topLeft,bottomRight)
            currentBox.draw(self.window)
            currentBox.setFill('white')

            self.text = Text( CenterPoint, 'Total of {0} counted {1} times'.format(currentNumber, currentCounter) )
            self.text.draw(self.window)
            CenterPoint = Point(300, bottomRight.getY()+yChange)
            currentNumber += 1

            boxNumber += 1
