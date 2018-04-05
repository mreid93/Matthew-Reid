from random import *

class player:
    def __init__(self, name, health, points, day):
        self.name = name
        self.health = health
        self.points = points
        self.day = day
        
    def takeDamage(self, amount):
        self.health = self.health - amount

    def earnPoints(self, amount):
        self.points = self.points + amount
    
    def nextDay(self):
        self.day = self.day + 1
    
    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health
    
    def getPoints(self):
        return self.points
    
    def getDay(self):
        return self.day
    
    def getStats(self):
        print('Welcome to Day {0}, {1}. You have {2} Health remaining and have accumulated {3} Points'.format(self.getDay(), self.getName(),self.getHealth(),self.getPoints()))
        print(' (1) Do research in your ship.\n (2) Look for samples nearby.\n (3) Look for rare samples in the far away wilderness.')
        print()
        
    def determineDay(self, decision):
         outcome = randrange(0,10)
         risk = 0
         if decision == '1':
             self.earnPoints(10)
             print('You do research in your ship, afraid of the outdoors. You earn 10 points.')
             if outcome == 0:
                 self.takeDamage(2)
                 print('While doing research, you were attacked by a swarm of vicious alien ants! You struggle against the mighty ants and take 2 damage')
           
         elif decision == '2':
            self.earnPoints(30)
            print('You search the area nearby your ship for new samples, finding several. You earn 30 points.')
            if outcome % 3 == 0:
                self.takeDamage(3)
                print('A mutant from Total Recall body slams you! You take 3 damage.')
            risk = 1
                
         elif decision == '3':
             self.earnPoints(100)
             print('You risk your life searching for rare specimens in an alien forest. You earn 100 points.')
             if outcome % 2 == 0:
                 self.takeDamage(5)
                 print('Predator lurks in this mysterious forest, ambushing you without being seen! You suffer serious injuries and take 5 damage.')
             risk = 2
         else:
             self.takeDamage(5)
             print('{0} is not an option. Your indecisivensss costs you greatly. You waste your day and are attacked by a group of klingons! \nYou take 5 damage.'.format(decision))
             
         if outcome == 9:
             self.takeDamage(-5)
             print('You find a peanut butter and jelly sandwich on this alien planet. You restore 5 health!')
                
         print()
    
    def playGame(self):
        
        while self.day < 8 and self.health > 0:
            self.getStats()
            userDecision = input('What will you do? ')
            self.determineDay(userDecision)
            if self.day == 7:
                print('=============================================================')
                print('Having survived the horrors of an alien planet for a full week, {0} escapes and returns to Earth a hero!'.format(self.name))
                print()
                print('End score : {0}'.format(self.getPoints()))
                print('End health : {0}'.format(self.getHealth()))
                
            if self.health <= 0:
                print('=============================================================')
                print('The puny {0} succumbs to the evil of this alien planet, only surviving for {1} full days!'.format(self.getName(), self.getDay()-1))
                print('All of Earth laughs at you!')
                print()
                print('End score : {0}'.format(self.getPoints()))
                print('End health : {0}'.format(self.getHealth()))
                print('=============================================================')
            self.day += 1
                      
def gameInfo():
    print('=============================================================')
    print('Welcome to Planet Quest! You are trying to collect samples of materials on an alien planet for one week before returning to Earth')
    print('The more samples you can collect, the more successful your journey has been, but beware - the further away from your ship you are, the more dangerous this planet becomes.')
    print('During your week, you have 3 options: \n1. Stay in your ship to work on samples. There is low chance for attack here, but low sample payoff.\n2. Explore the nearby area for samples. You have a slightly higher chance of being attacked here, but will find more samples.\n3. Finally, you may venture into the alien wilderness several miles away. Your payoff will be immense, but you risk a great chance of being attacked by powerful alien lifeforms. Beware!')
    print('\nIf you are attacked, you will lose your research for that day and some of your health points')
    print('=============================================================')

def main():
    gameInfo()
    name = input('What is your name? ')
    Player = player(name, 15, 0, 1)
    Player.playGame()

main()