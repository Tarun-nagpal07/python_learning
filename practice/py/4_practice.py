'''Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. 
The gun beats the snake, the water beats the gun, and the snake beats the water.
 Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.'''

import random

# m = {
#     '0' : 'snake',
#     '1' : 'water',
#     '2' : 'gun'
# }

# r = random.choice(['0','1','2'])

# print(m[r])


class SWG:
    def __init__(self,g):
      self.rule  = {
            '0' : 'snake',
            '1' : 'water',
            '2' : 'gun'
        }
      self.user_points = 0
      self.ai_points = 0
      self.g = g

    def startgame(self):
       print("Wlc to Snake, Water, Gun game!!!")
       try:
            while True:
                if self.user_points == self.g:
                    print("User wins")
                    break
                elif self.ai_points == self.g:
                    print("Ai wins")
                    break
                elif self.ai_points == self.user_points:
                    if self.user_points == self.g:
                        print("DRAW")
                        break
                
                inp = input("Your chance , write from ['snake','water','gun'] : ")

                if inp not in ['snake','water','gun']:
                  raise Exception("Wrong Input")
            
                ai = random.choice(['0','1','2'])
                ai = self.rule[ai]

                if inp == 'snake' and ai == 'water':
                    print("User get the point")
                    self.user_points += 1
                elif inp == 'gun' and ai == 'snake':
                    print("User get the point")                   
                    self.user_points += 1
                elif inp == 'water' and ai == 'gun' :
                    print("User get the point")
                    self.user_points += 1
                elif inp == 'water' and ai == 'snake':
                    print("AI get the point")
                    self.ai_points += 1
                elif inp == 'snake' and ai == 'gun':
                    print("AI get the point")
                    self.ai_points += 1
                elif inp == 'gun' and ai == 'water':
                    print("AI get the point")
                    self.ai_points += 1
                else :
                    print("No score on same guess") 

       except Exception as e:
          print(e)
          

s = SWG(3)

s.startgame()