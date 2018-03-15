from button import Button
from die_view import DieView
from sum_counter_view import SumCounterView
from graphics import *

def main():
    win = GraphWin("Double Die Roller", 400, 200)
    win.setBackground( 'dark green' )
    dieView1 = DieView( win, Point( 50, 60 ), 80 )
    dieView2 = DieView( win, Point( 150, 60 ), 80 )
    rollButton = Button( win, Point( 100, 160), 100, 40, "Roll!" )
    
    sumCounter = [0,0,0,0]
    possibleSums = [7,8,9,10]
    currentSum = 0
    
    while True:
        mouseClick = win.getMouse()
        i = 0
        if rollButton.wasClickedIn( mouseClick ):

            dieView1.roll()
            dieView2.roll()
            
            currentSum = dieView1.getValue() + dieView2.getValue()
            Counter = SumCounterView(win, currentSum, sumCounter)
            currentSum = Counter.getSum()
            while i < 4:
                if currentSum == possibleSums[i]:
                    sumCounter[i] += 1
                i += 1
            Counter.handleRoll(sumCounter)
main()