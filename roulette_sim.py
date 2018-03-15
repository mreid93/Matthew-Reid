# start w/ method try/except for 3 ints
from random import *

def userBets():
    
    try:
        startingDollars = int(input('Enter the number of dollars you start with as a whole number : '))
        numOfSpins = int(input('Enter the number of spins you will play : '))
        spinBet = int(input('Enter how many dollars you will bet for each spin as a whole number : '))
        
    except ValueError:
        print('\nInvalid value(s) entered')
        startingDollars = int(input('Enter the number of dollars you start with as a whole number : '))
        numOfSpins = int(input('Enter the number of spins you will play : '))
        spinBet = int(input('Enter how many dollars you will bet for each spin as a whole number : '))
        
    while startingDollars < 0 or numOfSpins < 0 or spinBet < 0:
        print('\nPlease enter positive numbers')
        startingDollars = int(input('Enter the number of dollars you start with as a whole number : '))
        numOfSpins = int(input('Enter the number of spins you will play : '))
        spinBet = int(input('Enter how many dollars you will bet for each spin as a whole number : '))

    return startingDollars, numOfSpins, spinBet

def userStrategy():
    print('Choose one of the following strategy choices')
    print('- Bet on a (s)ingle number (pays 35 to 1)')
    print('- Bet on (e)ven or odd numbers (pays 1 to 1)')
    print('- Bet on a (d)ozen numbers (pays 2 to 1)')
    selectedStrategy = input('Enter your strategy choice (s, e, or d) : ')
    
    if selectedStrategy != 's' and selectedStrategy != 'e' and selectedStrategy != 'd':
        print('{0} is not a choice.'.format(selectedStrategy))
        selectedStrategy = input('Enter your strategy choice (s, e, or d) : ')
        
    return selectedStrategy

def rouletteSim(startingDollars, numOfSpins, spinBet, selectedStrategy):
    
    currentBalance = startingDollars
    Wins = 0
    Losses = 0
    totalSpins = 0
    
    
    if selectedStrategy == 's':
        #rangeOfResults = 36
        try:
            winningBet = int(input('Enter the single number you want to bet on (1 to 36) : '))
        except ValueError:
            print('\nInvalid input')
            winningBet = int(input('Enter the single number you want to bet on (1 to 36) : '))
        while winningBet > 36 or winningBet < 1:
            print('\nNumber not in range')
            winningBet = int(input('Enter the single number you want to bet on (0 to 36) : '))
            
        for spin in range(0, numOfSpins):
            
            currentNumber = randrange(1,37)
            
            if currentNumber == winningBet:
                Wins += 1
                currentBalance += 35*spinBet
            else:
                Losses += 1
                currentBalance -= spinBet
            totalSpins += 1
            if currentBalance < spinBet:
                break;
                
    elif selectedStrategy == 'e':
        winningBet = input('Enter if you want to bet on (e)ven or (o)dd numbers : ')
        while winningBet != 'e' and winningBet != 'o':
            print('\nInvalid input')
            winningBet = input('Enter if you want to bet on (e)ven or (o)dd numbers : ')
        
        for spin in range(0, numOfSpins):
            currentNumber = randrange(1,37)
            
            if winningBet == 'e' and currentNumber % 2 == 0:
                Wins += 1
                currentBalance += spinBet
            else:
                Losses += 1
                currentBalance -= spinBet
                
            totalSpins += 1
            
            if currentBalance < spinBet:
                break;
    else:
        try:
            winningBet = int(input('Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36 : '))
        except ValueError:
            print('\nInvalid input')
            winningBet = int(input('Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36 : '))
        while winningBet != 1 and winningBet != 2 and winningBet != 3:
            print('\nInvalid number entered')
            winningBet = int(input('Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36 : '))
        
        for spin in range(0, numOfSpins):
            #This generates 1, 2, or 3, which is much easier to coorespond to the user's selection above.
            currentNumber = randrange(1,4)
            
            if winningBet == currentNumber:
                Wins += 1
                currentBalance += 2*spinBet
            else:
                Losses += 1
                currentBalance -= spinBet
                
            totalSpins += 1
            
            if currentBalance < spinBet:
                break;
    netAmount = currentBalance - startingDollars
    
    print()
    print('After {0} spins'.format(totalSpins))
    print('Wins : {0} ({1:.2f}%)'.format(Wins, 100*Wins/totalSpins))
    print('Losses : {0} ({1:.2f}%)'.format(Losses, 100*Losses/totalSpins))
    print('Ending bank : ${0}'.format(currentBalance))
    print('Net winnings : ${0}'.format(netAmount))
        
def main():
    startingDollars, numOfSpins, spinBet = userBets()
    selectedStrategy = userStrategy()
    rouletteSim(startingDollars, numOfSpins, spinBet, selectedStrategy)

main()