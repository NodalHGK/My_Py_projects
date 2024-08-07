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
print("Welcome to Treasure Iland. Your misson is to find the treasure.")
print("Your misson is to find the treasure.")



choice1 = input('You\'re at a cross road. Where dou want to go?  Type "left" or "right"\n').lower()
    
if choice1 == "left":
    choice2 = input('You\'ve сome to a lake. There is an island in the middle of the lake. Type "wait" for a boat. Type "swim" to swim across \n').lower()
    
    if choice2 == "wait":
        print('''
                                           
                                   |>>>                   
                    |>>>       _  _|_  _        |>>>              
                    |         |;| |;| |;|       |
                _  _|_  _     \.    .  /    _  _|_  _
               |;|_|;|_|;|     \:. ,  /    |;|_|;|_|;|
               \..      /     ||;   . |    \.    .  /
                \.  ,  /     ||:  .   |     \:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       \,/
                 ||:   ||:  ,  _______   .   ||: , |            
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~''')
        choice3 = input('You arrived on the island by boat. As you move deeper into the island, you came across an old fortress. Type "enter" inside through the gate. Type "crawl" through a crack in the wall \n').lower()
        
        if choice3 == "enter":
            print("Inside the castle the treasure is guarded by a sphinx, he will ask you 2 riddles")
            choice4 = input('Guess the riddle, guess the question, what shoots in the heel, hits the nose? Type "socks", "farting", or "Chuck Norris" \n').lower()
            
            if choice4 == "farting":
                print("Congratulations!!! little fart, the next riddle is going to be harder.")
                print("Solve an example for me,  ? * ? / 100 = 8. Name two number correctly and the treasure is yours ")
                choice5 = input('name the first number \n')
                choice6 = input('name the second number \n')
                
                solution = int(choice5) * int(choice6) / 100
                
                if solution == 8: 
                    print("Congratulations!!! You have received your treasures")
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
                else:
                    print("The answer is incorrect, Merry Christmas and Happy New Year, dirty animal, gratatatata. Game Over.")
            elif choice4 == "socks":
                print("The answer is incorrect, now you yourself will become a sock. Game Over.")
            
            elif choice4 == "Chuck Norris":
                print("Hey chuck, some loser here said you have a weak punch.")
                print("Chuck Norris showed you what a real punch, Game Over.")
            else:
                print("You didn't choose any of the answer options, the sphinx turned you into stone. Game Over.")
        else:
            print("A rock fell on your head. Game over.")
    else:
        print("You were eaten by a big lake shark. Game over.")
        print('''
                                 ,-
                               ,'::|
                              /::::|
                            ,'::::o\                                      _..
         ____........-------,..::?88b                                  ,-' /
 _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
<. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
 `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
     """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
         ""--.__     P(       \               ` ``:`:``:::: .   .;'
                ""--.:-.     `.                             .: /
                  \. /    `-._   `.""-----.,-..::(--"".""`.  ` 
                   `P         `-._ \          `-:\          `. `:
                                   ""            "            `-._)''')
        

else:
    print("You Fall into a hole. Game Over.")
    print('''        _       
                    (_)      
                _ __ _ _ __  
               | '__| | '_ \ 
               | |  | | |_) |
               |_|  |_| .__/ 
                      | |    
                      |_|   ''')


        
    
        
        
