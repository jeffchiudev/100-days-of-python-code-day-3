print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

l_or_r = input("You find yourself at a fork in the road. Where do you want to go? Type 'left' or 'right'\n").lower()

if l_or_r == "left":
  swim_or_wait = input("You come to a lake with an island and a tower in the middle. You could swim or wait for a boat. Type 'swim' or 'wait'\n").lower()
  if swim_or_wait == "wait":
    door_choice = input("You arrive on the island and the tower.  At the base of the tower there are three doors. Choose 'red', 'blue' or 'yellow' \n").lower()
    if door_choice == "red":
      print("It was a trap, you're consumed by a fireball. Game Over.")
    elif door_choice == "blue":
      print("This door was packed with beasts that tear you limb from limb. Game Over.")
    elif door_choice == "yellow":
      print("You cautiously open the door to find a treasure chest full of gold. Congrats you're rich.")
    else:
      print('You choose poorly. You whither away to dust. Game Over!')
  else:
    print("you're eaten by sharks. Game Over!")
else:
  print("You fall in a hole, Game Over!")
