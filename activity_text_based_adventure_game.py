import sys, random, time

# testing
# hero, name, weapon, items, health_points = '', '', '', [], ''

#main start function to run game
def start():
    print(f"Welcome to the Chaos Chambers")
    print("You hear spooky sounds echoing off the chamber walls..")
    choose_hero()

#choose from heroes: archer, mage or warrior with uniqe items, weapon and health points
def choose_hero():
    global hero, name, weapon, items, health_points
    choose = input("Choose you hero: Archer, Mage or Warrior: ")
    heroes = {
        'mage' : {
            'name' : 'Electra',
            'weapon' : 'Wand',
            'items' : ['10 gold pieces', '1x health potion', '2x mana potion'],
            'health points' : 10
            },
        'warrior' : {
            'name' : 'Zeus',
            'weapon' : 'Battle Axe',
            'items' : ['15 gold pieces', '2x health potion', 'shield', 'sword'],
            'health points' : 20
            },
        'archer' : {
            'name' : 'Laergo',
            'weapon' : 'bow',
            'items' : ['arrows', '3x health potion', 'anti-poison', 'diamond'],
            'health points' : 15
            }
        }
    if choose.lower() == 'mage':
        hero = list(heroes.keys())[0]
    elif choose.lower() == 'warrior':
        hero = list(heroes.keys())[1]
    elif choose.lower() == 'archer':
        hero = list(heroes.keys())[2]
    else:
        choose_hero()
    
    name = heroes[choose]['name']
    weapon = heroes[choose]['weapon']
    items = heroes[choose]['items']
    health_points = heroes[choose]['health points']

    print(f"\nYou chose the {hero.capitalize()}!")
    print(f'Your name is: {name}, Your weapon of choice is a {weapon} and you have {health_points} health points.')
    print(f'Your backpack contains the following items: ')
    for i in items:
        print(f'\t{i}')
    math_room()

#answer a single math question, after youve chosen your difficulty. using match case.
def math_room():
    # questions = ''
    print(f"\nI hope you brushed up on your maths skills.. noone has ever been able to defeat the Arithmetic Golem!")
    print(f"I feel bad for you.. so i'm going to let you choose your difficulty.")
    questions_e = [f'Golem: What is 2 * 2? ', 'Golem: What is 4 / 2? ', 'Golem: What is 10 * 5? ', 'What is the 5 + 5? ']
    questions_n = [f'Golem: What is 5 * 8? ', 'Golem: What is 21 / 3? ', 'Golem: What is 12 * 12? ' , 'What is the square root of 64? ']
    questions_h = [f'Golem: What is 12 * 13? ', 'Golem: What is 44 % 7? ', 'Golem: What is 300 * 12? ', 'What is the square root of 196? ']
    difficulty = ''
    while difficulty not in ['easy', 'normal', 'hard']:
        difficulty = input("Do you want it easy, normal or hard? ")
    if difficulty.lower() == 'normal':
        questions = questions_n
    elif difficulty.lower() == 'easy':
        questions = questions_e
    elif difficulty.lower() == 'hard':
        questions = questions_h
    else:
        difficulty = input("Do you want it easy, normal or hard? ")
    question = random.choice(questions)

    match question:
        case 'Golem: What is 5 * 8? ':
            answer = 40
        case 'Golem: What is 21 / 3? ':
            answer = 7
        case 'Golem: What is 12 * 12? ':
            answer = 144
        case 'What is the square root of 64? ':
            answer = 8
        case 'Golem: What is 2 * 2? ':
            answer = 4
        case 'Golem: What is 4 / 2? ':
            answer = 2
        case 'Golem: What is 10 * 5? ':
            answer = 50
        case 'What is the 5 + 5? ':
            answer = 10
        case 'Golem: What is 12 * 13? ':
            answer = 156
        case 'Golem: What is 44 % 7? ':
            answer = 2
        case 'Golem: What is 300 * 12? ':
            answer = 25
        case 'What is the square root of 196? ':
            answer = 14
    ask = int(input(question))
    if ask == answer:
        print("Golem: It appears we have a cheater! not to worry, i'll let you pass this time.. i dont expect you to get far ha ha ha")
        word_room()
    else:
        print("Incorrect")
        end()

#word room based on wordle, you have 5 attempts or you will rot here.
def word_room():
    letters = ['u', 'o', 'c', 't', 's', 't', 'a', 'e', 'l']
    attempts = 6
    word = 'castle'
    print(f"\nYou appear to have bumped your head.. openeing your eyes slowly")
    print(f'You see a chest in the middle of the room, intrigued.. you walk over and look inside..')
    print(f'Inside there are 8 tiles, with blood carvings.. they appear to be letters.. ')
    for l in letters:
        print(f'{l.upper()}',end ='  ')
    print('\nYou hear a roar in the distance..\n')
    while attempts != 0:
        guess = str(input("Word Worgen: Guess the 6 letter word and you may pass: "))
        if len(guess) != 6:
            print("Enter a 6 letter word, dummy!")
            print(f"You have {attempts-1} tries left.")
            attempts -= 1
            if attempts == 0:
                #dead()
                print('you are dead')
        else:
            if guess == word:
                print("Word Worgen: wait.. what?! how did you do that?!\n")
                final_room()
                break
            else:
                attempts += 1
                print(f"You have {attempts} tries left.")
                for hidden_c, guess_c in zip(word, guess):
                    if guess_c in word and guess_c in hidden_c:
                        print(guess_c+ u' \u2713 ')
                    elif guess_c in word:
                        print(guess_c + ' + ')
                    else:
                        print(' X ')
            if attempts == 0:
                print('you are dead')
                time.sleep(5)
                dead()


#the final room you will face a dragon in a life or death scenario
def final_room():
    global weapon, health_points, items
    name = 'bob'
    drink = ''
    choice = ''
    old_health = health_points
    dragon = {
        'name' : 'Nuved, Destroyer Of Life',
        'health points' : 40,
        'loot' : ['health potion', 'Dragon Skull', 'Legendary Weapon', 'Key']
    }
    
    print(f"You have finally made it.. you see the door to freedom in sight and the key just laying there in the middle of the room..")
    print(f"It all just seems a little too easy.. until you hear the roar from above.")
    print(f"The legend of Nuved, Destroyer Of Life is real!, flapping its wings as it lands, guarding the key.")
    print(f"You look up in awe of the huge dragon as it grunts.. there is only one way out of here. You draw your {weapon}.")
    while choice.lower() != 'run' or choice.lower() != 'fight':
        choice = input("\nAre you going to run or fight? ")
        print('\n')
        if choice.lower() == 'fight':
            x = (random.randint(20, 40))
            y = int(dragon['health points'])
            z = y - x
            dragon['health points'] = str(z)
            print(f"You hit dragon with your {weapon} for " + str(x) + " damage. ")
            print(f"The dragon has {z} health points left!")
            print("The dragon strikes back! clawing you across the chest as you start to bleed.")
            health_points = int(health_points / 2)
            print(f"You have {health_points} health points remaining.\n")
            backpack = input("..you hear a whisper from behind *if that dragon hits you again you are done for!, check your 'backpack' for help* : ")
            if backpack.lower() == 'backpack':
                print(f"You open your backpack to reveal:")
                for i in items:
                    print(f'\t{i}')
            drink = input("hint: you look thirsty.. maybe you could 'drink' something? ")
            while 'health' not in drink.lower():
                drink = input("hint: you look thirsty.. maybe you could 'drink' something? ")
            print("*You drink the health potion*")
            health_points = old_health
            print(f"You now have {health_points} health points again!")
            print(f"You attack the dragon again, sending it crashing to the ground!\n")
            print(f"You walk over to the dragon, examining its ashes.. you find: ")
            for item in dragon['loot']:
                print(f'\t{item}')
            print("You quickly grab the key and run to the door!")
            win()

        elif choice.lower() == 'run':
            print(f"You can't run from a dragon! {dragon['name']} claws at you as you try to escape.")
            dead()

    




        
def dead():
    print("That dragon sure hurts, doesnt he?")
    print("YOU ARE DEAD. ENJOY YOUR TIME IN THE AFTERLIFE.")
    time.sleep(5)
    sys.exit()
    #if life counter == 0 die
    #would you like to try again?

#lost function printed anytime you dont pass a challenge
def end():
    print("You just aren't cut out for the challenge of Chaos Chambers..")
    time.sleep(3)
    print('You are going to rot in here.')
    time.sleep(3)
    sys.exit()

#escape function, only run if you escape the chambers
def win():
    print(f"You managed to escape Chaos Chambers, from here on out you will be known as {name} the Dragon Slayer!")
    print('''
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"
                        ''')
    exit()


#welcome function, whole program runs off this function
start()
