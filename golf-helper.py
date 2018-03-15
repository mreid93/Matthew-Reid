try:
    print('Welcome to the Golf Club Helper! \n Tell me your situation, and Ill recommend a club.')
    Ans = input('Did you hit it on the green (y/n)?')
    Dist = int(input('How many yards is the ball from the hole?'))
                     
#Ensures we have correct input to begin program
    while Ans != 'y' and Ans != 'n' or Dist <= 0:
        Ans = input('Invalid input. \nDid you hit it on the green (y/n)? ')
        Dist = int(input('How many yards is the ball from the hole? '))
        print('')

# if ball is on the green, no need to test Dist. Then, begin checking ranges for Dist.
    if Ans == 'y':
        print('I recommend using your Putter')
    elif Dist >=200:
        print('I recommend using your Driver')
    elif Dist < 200 and Dist >= 140:
        print('I recommend using your 5-Iron')
    elif Dist < 140 and Dist >= 100:
        print('I recommend using your 9-Iron')
    else:
        print('I recommend using your Pitching Wedge')

except ValueError:
     print('Invalid value(s) entered')  