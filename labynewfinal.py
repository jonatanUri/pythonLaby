import sys, getch, random, time, os
select = ''
column, lines=os.get_terminal_size()
number_of_levels, basic_size, size_growth, color_wall, color_path = 5, 10, 5, "37", "40"

def print_middle(szoveg):
    print('{: ^{c}}'.format(szoveg, c=column))


def credits():
    print('{:*^{c}}'.format('*', c=column))
    print_middle('Credits')
    print('{:*^{c}}'.format('*', c=column))
    print_middle("      ___           ___           ___                                                   ___     ")
    print_middle("     /\__\         /\  \         /\__\         _____                                   /\__\    ")
    print_middle("    /:/  /        /::\  \       /:/ _/_       /::\  \       ___           ___         /:/ _/_   ")
    print_middle("   /:/  /        /:/\:\__\     /:/ /\__\     /:/\:\  \     /\__\         /\__\       /:/ /\  \  ")
    print_middle("  /:/  /  ___   /:/ /:/  /    /:/ /:/ _/_   /:/  \:\__\   /:/__/        /:/  /      /:/ /::\  \ ")
    print_middle(" /:/__/  /\__\ /:/_/:/__/___ /:/_/:/ /\__\ /:/__/ \:|__| /::\  \       /:/__/      /:/_/:/\:\__\\")
    print_middle(" \:\  \ /:/  / \:\/:::::/  / \:\/:/ /:/  / \:\  \ /:/  / \/\:\  \__   /::\  \      \:\/:/ /:/  /")
    print_middle("  \:\  /:/  /   \::/~~/~~~~   \::/_/:/  /   \:\  /:/  /   ~~\:\/\__\ /:/\:\  \      \::/ /:/  / ")
    print_middle("   \:\/:/  /     \:\~~\        \:\/:/  /     \:\/:/  /       \::/  / \/__\:\  \      \/_/:/  /  ")
    print_middle("    \::/  /       \:\__\        \::/  /       \::/  /        /:/  /       \:\__\       /:/  /   ")
    print_middle("     \/__/         \/__/         \/__/         \/__/         \/__/         \/__/       \/__/    ")
    print_middle(" ")                                                                                               
    print_middle("Produced by:")
    print_middle("Uri Jonatán")
    print_middle("Kalló Dávid")
    print_middle("Pető Réka")
    print_middle("")
    

def menu():
    print("\033[H\033[J")
    print('{:*^{c}}'.format('*', c=column))
    print_middle('Labyrinth')
    print('{:*^{c}}'.format('*', c=column))
    print_middle('Press the number you want to select!')
    print_middle('You can move with the keys: WASD and you can go back to the main menu with M')
    print_middle('')
    print_middle('1. New Game')
    print_middle('2. Options')
    print_middle('3. Credits')
    print_middle('0. Quit')

def options(number_of_levels, basic_size, size_growth, color_wall, color_path):
    options_choice = "k"
    while options_choice != "5":
        print('{:*^{c}}'.format('*', c=column))
        print_middle('Options')
        print('{:*^{c}}'.format('*', c=column))
        print_middle(f"1. Number of levels: {number_of_levels} ")
        print_middle(f"2. Basic size: {basic_size} ")
        print_middle(f"3. Level size growth: {size_growth}")
        print_middle(f"               4. Colors: \x1b[6;{color_wall};{color_path}m\u2588\u2588  \x1b[0m")
        print_middle("5. Exit")
        options_choice = getch.getch()
        try:
            
            if options_choice == "1":
                print()
                print_middle("How many levels do you want to play?")
                number_of_levels = int(getch.getch())
            if options_choice == "2":
                print()    
                print_middle("How big do you want the first level to be?")
                input_basic_size = int(input())
                while input_basic_size < 6:
                    print()
                    print_middle("Basic size must be at least 6!")
                    print_middle("How big do you want the first level to be?")
                    input_basic_size = int(input())
                basic_size = input_basic_size
            if options_choice == "3":
                print()
                print_middle("How much do you want the next level to grow?")
                size_growth = int(getch.getch())
            if options_choice == "4":
                print()    
                print_middle("What color do you want the walls to be?")
                print_middle("1. \x1b[6;31;40m\u2588\u2588\x1b[0m")
                print_middle("2. \x1b[6;32;40m\u2588\u2588\x1b[0m")
                print_middle("3. \x1b[6;33;40m\u2588\u2588\x1b[0m")
                print_middle("4. \x1b[6;37;40m\u2588\u2588\x1b[0m")
                input_color_wall = getch.getch()
                while not ("0" < input_color_wall < "5"):
                    print()
                    print_middle("Invalid input!")
                    print()    
                    print_middle("What color do you want the walls to be?")
                    print_middle("1. \x1b[6;31;40m\u2588\u2588\x1b[0m")
                    print_middle("2. \x1b[6;32;40m\u2588\u2588\x1b[0m")
                    print_middle("3. \x1b[6;33;40m\u2588\u2588\x1b[0m")
                    print_middle("4. \x1b[6;37;40m\u2588\u2588\x1b[0m")
                    input_color_wall = getch.getch()
                print()
                print_middle("What color do you want the paths to be?")
                print_middle("1. \x1b[6;30;41m  \x1b[0m")
                print_middle("2. \x1b[6;30;42m  \x1b[0m")
                print_middle("3. \x1b[6;30;43m  \x1b[0m")
                print_middle("4. \x1b[6;30;47m  \x1b[0m")
                print_middle("5. \x1b[6;30;40m  \x1b[0m")
                input_color_path = getch.getch()
                while (not "0" < input_color_path < "6"):
                    print()
                    print_middle("Ivalid input!")
                    print()
                    print_middle("What color do you want the paths to be?")
                    print_middle("1. \x1b[6;30;41m  \x1b[0m")
                    print_middle("2. \x1b[6;30;42m  \x1b[0m")
                    print_middle("3. \x1b[6;30;43m  \x1b[0m")
                    print_middle("4. \x1b[6;30;47m  \x1b[0m")
                    print_middle("5. \x1b[6;30;40m  \x1b[0m")
                    input_color_path = getch.getch()
                while input_color_wall == input_color_path:
                    print()
                    print()
                    print_middle("Please select different colors for the walls and the paths!")
                    print()    
                    print_middle("What color do you want the walls to be?")
                    print_middle("1. \x1b[6;31;40m\u2588\u2588\x1b[0m")
                    print_middle("2. \x1b[6;32;40m\u2588\u2588\x1b[0m")
                    print_middle("3. \x1b[6;33;40m\u2588\u2588\x1b[0m")
                    print_middle("4. \x1b[6;37;40m\u2588\u2588\x1b[0m")
                    input_color_wall = getch.getch()
                    while not ("0" < input_color_wall < "5"):
                        print()
                        print_middle("Invalid input!")
                        print()    
                        print_middle("What color do you want the walls to be?")
                        print_middle("1. \x1b[6;31;40m\u2588\u2588\x1b[0m")
                        print_middle("2. \x1b[6;32;40m\u2588\u2588\x1b[0m")
                        print_middle("3. \x1b[6;33;40m\u2588\u2588\x1b[0m")
                        print_middle("4. \x1b[6;37;40m\u2588\u2588\x1b[0m")
                        input_color_wall = getch.getch()
                    print()
                    print_middle("What color do you want the paths to be?")
                    print_middle("1. \x1b[6;30;41m  \x1b[0m")
                    print_middle("2. \x1b[6;30;42m  \x1b[0m")
                    print_middle("3. \x1b[6;30;43m  \x1b[0m")
                    print_middle("4. \x1b[6;30;47m  \x1b[0m")
                    print_middle("5. \x1b[6;30;40m  \x1b[0m")
                    input_color_path = getch.getch()
                    while (not "0" < input_color_path < "6"):
                        print()
                        print_middle("Ivalid input!")
                        print()
                        print_middle("What color do you want the paths to be?")
                        print_middle("1. \x1b[6;30;41m  \x1b[0m")
                        print_middle("2. \x1b[6;30;42m  \x1b[0m")
                        print_middle("3. \x1b[6;30;43m  \x1b[0m")
                        print_middle("4. \x1b[6;30;47m  \x1b[0m")
                        print_middle("5. \x1b[6;30;40m  \x1b[0m")
                        input_color_path = getch.getch()
                if input_color_wall == "1":
                    color_wall = "31"
                elif input_color_wall == "2":
                    color_wall = "32"
                elif input_color_wall == "3":
                    color_wall = "33"
                elif input_color_wall == "4":
                    color_wall = "37"   
                if input_color_path == "1":
                    color_path = "41"
                elif input_color_path == "2":
                    color_path = "42"
                elif input_color_path == "3":
                    color_path = "43"
                elif input_color_path == "4":
                    color_path = "47"
                elif color_path == "5":
                    color_path = "40"  
            print("\033[H\033[J")
        except ValueError:
            print("\033[H\033[J")
            print_middle("Invalid input!")
    return number_of_levels, basic_size, size_growth, color_wall, color_path

def draw_fog(level, x, y):
    i=0
    while level[x-i][y]!=1 and x-i-1>0:
        if level[x-i+1][y]==1:
            level[x-i+1][y]=2
        if level[x-i-1][y]==1:
            level[x-i-1][y]=2
        if level[x-i][y+1]==1:
            level[x-i][y+1]=2
        if level[x-i][y-1]==1:
            level[x-i][y-1]=2
        i+=1
    i=0

    while level[x+i][y]!=1 and x+i+1<len(level):
        if level[x+i+1][y]==1:
            level[x+i+1][y]=2
        if level[x+i-1][y]==1:
            level[x+i-1][y]=2
        if level[x+i][y+1]==1:
            level[x+i][y+1]=2
        if level[x+i][y-1]==1:
            level[x+i][y-1]=2
        i+=1
    i=0

    while level[x][y-i]!=1 and y-i-1>0:
        if level[x+1][y-i]==1:
            level[x+1][y-i]=2
        if level[x-1][y-i]==1:
            level[x-1][y-i]=2
        if level[x][y+1-i]==1:
            level[x][y+1-i]=2
        if level[x][y-1-i]==1:
            level[x][y-1-i]=2
        i+=1
    i=0

    while level[x][y+i]!=1 and y+i+1<len(level):
        if level[x+1][y+i]==1:
            level[x+1][y+i]=2
        if level[x-1][y+i]==1:
            level[x-1][y+i]=2
        if level[x][y+1+i]==1:
            level[x][y+1+i]=2
        if level[x][y-1+i]==1:
            level[x][y-1+i]=2
        i+=1

    sor = 0
    while sor<len(level1):
        elem = 0
        line=""
        while elem<len(level1[sor]):
            if level1[sor][elem]==1:
                line += '  '
            if level1[sor][elem]==2:
                line += '\u2588\u2588'
            elif level1[sor][elem] == 0:
                line += '  '
            elif level1[sor][elem] == 'z':
                line += '\u25e2\u25e3'
            elif level1[sor][elem] == 'x':
                line += 'XX'
            elem += 1
        print_middle(f'\x1b[6;{color_wall};{color_path}m{line}\x1b[0m')          
        sor += 1
    
def draw(level1):
    sor = 0
    while sor<len(level1):
        elem = 0
        line=""
        while elem<len(level1[sor]):
            if level1[sor][elem]==1:
                line += '\u2588\u2588'
            elif level1[sor][elem] == 0:
                line += '  '
            elif level1[sor][elem] == 'z':
                line += '\u25e2\u25e3'
            elif level1[sor][elem] == 'x':
                line += 'XX'
            elem += 1
        print_middle(f'\x1b[6;{color_wall};{color_path}m{line}\x1b[0m')          
        sor += 1

def makeLevel(size):
    level = [[1 for coordx in range(size)] for coordy in range(size)]
    startX=0
    startY=0
    stack=[]

    rand=random.randint(1,size-1)

    while rand%2==0:
        rand=random.randint(2,size-1)
    startX = rand

    rand=random.randint(2,size-1)

    while rand%2==0:
        rand=random.randint(2,size-1)
    startY = rand

    stack.append([startX,startY])

    goodstep=0
    triedUp=0
    triedRight=0
    triedDown=0
    triedLeft=0

    #0: Up, 1: Right, 2: Down, 3: Left
    direction = random.randint(0,3)

    level[startX][startY]=0
    while len(stack) >= 1:
        goodstep=0
        triedUp=0
        triedRight=0
        triedDown=0
        triedLeft=0
        direction = random.randint(0,3)
        while goodstep!=1:
            if direction==0:
                if startY>1 and level[startX][startY-2]==1:
                    level[startX][startY-1]=0
                    level[startX][startY-2]=0
                    stack.append([startX,startY])
                    startY-=2
                    goodstep=1
                    break
                else:
                    triedUp=1
                    direction = random.randint(0,3)


            if direction==1:
                if startX<size-2 and level[startX+2][startY]==1:
                    level[startX+1][startY]=0
                    level[startX+2][startY]=0
                    stack.append([startX,startY])
                    startX+=2
                    goodstep=1
                    break
                else:
                    triedRight=1
                    direction = random.randint(0,3)
                
            if direction==2:
                if startY<size-2 and level[startX][startY+2]==1:
                    level[startX][startY+1]=0
                    level[startX][startY+2]=0
                    stack.append([startX,startY])
                    startY+=2
                    goodstep=1
                    break
                else:
                    triedDown=1
                    direction = random.randint(0,3)
                    
            if direction==3:
                if startX>1 and level[startX-2][startY]==1:
                    level[startX-1][startY]=0
                    level[startX-2][startY]=0
                    stack.append([startX,startY])
                    startX-=2
                    goodstep=1
                    break
                else:
                    triedLeft=1
                    direction = random.randint(0,3)
                
            if (triedDown==1 and triedLeft==1 and triedRight==1 and triedUp==1):
                startX = stack[-1][0]
                startY = stack[-1][1]
                del stack[-1]
                break
        if goodstep==1:
            print("\033[H\033[J")
            draw(level)
            time.sleep(0.05)
    goodstep = 0
    while goodstep != int(size/8):
        startX = random.randint(3,size-3)
        startY = random.randint(3,size-3)
        if (startX%2==1 and startY%2==1) or startX%2==0 and startY%2==0:
            startX+=1

        if level[startX][startY]==1:
            level[startX][startY]=0
            goodstep+=1
            print("\033[H\033[J")
            draw(level)
            time.sleep(0.05)
    return level

while select != '0':    
    menu()
    goToMenu=0
    select=getch.getch()
    if select == '1':
        for l in range(number_of_levels):
            coordx=1
            coordy=1
            if (basic_size+(l*size_growth))%2==0:
                level1 = makeLevel(1+basic_size+(l*size_growth))
            else:
                level1 = makeLevel(basic_size+(l*size_growth))
            print("\033[H\033[J")
            level1[coordx][coordy] ='z'
            level1[-2][-2] ='x'
            draw(level1)
            while not (level1[-2][-2] == 'z'):
                mozg =getch.getch()
                print("\033[H\033[J")
                level1[coordx][coordy]=0
                if mozg == 'a':
                    if level1[coordx][coordy-1] != 1:
                        coordy=coordy-1          
                if mozg == 's':
                    if level1[coordx+1][coordy] != 1: 
                        coordx=coordx+1 
                if mozg == 'd':
                    if level1[coordx][coordy+1] != 1:
                        coordy=coordy+1 
                if mozg == 'w':
                    if level1[coordx-1][coordy] != 1:
                        coordx=coordx-1 
                if mozg == 'm':
                    goToMenu=1
                    break    
                level1[coordx][coordy]='z'
                draw(level1)
            if goToMenu==1:
                break
            else:
                print("\033[H\033[J")
            if l==number_of_levels-1 and level1[-2][-2] == 'z':
                print_middle('Congratulations! You escaped all the labyrinths!')
                print_middle('Press any key to return to the menu.')
                getch.getch()
                print("\033[H\033[J")
                menu()
    if select == '2':
        print("\033[H\033[J")
        number_of_levels, basic_size, size_growth, color_wall, color_path = options(number_of_levels, basic_size, size_growth, color_wall, color_path)
    if select == '3':
        print("\033[H\033[J")
        credits()
        print_middle('Press any key to return to the menu.')
        getch.getch()
        print("\033[H\033[J")
else:
    quit() # break

# MAIN!!!!
# Kisebb fügvények!
