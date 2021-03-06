import curses



def init():

    # on initialise la fenetre curses
    curses.initscr()
    win = curses.newwin(30, 80, 0, 0)
    curses.noecho()
    curses.curs_set(0)
    win.nodelay(0)
    curses.curs_set(1)
    win.move(10,10)
    
    return win




def loadNew():

    # on ouvre un niveau vide
    fichier = open("template.txt", 'r')
    chaine = fichier.read()
    linesLevel = chaine.split("\n")
    level = []
    
    for i in linesLevel:
        level.append(list(i))
    
    return level




def showLevel(win, level):
    
    (y, x) = win.getyx()
    
    # Affiche chaque caractere de level
    for i in range(len(level)):
        for j in range(len(level[i])):
            win.addstr(i, j, level[i][j])
    
    win.addstr(23, 20, str(x) +", "+str(y)+" ")
    
    win.move(y, x)
    
    return



def action(win, level, key, trace):
    (y, x) = win.getyx()
    
    if key == ord('q') and x>1 :
        x -= 1
    if key == ord('d') and x<67 :
        x += 1
    if key == ord('z') and y>1 :
        y -= 1
    if key == ord('s') and y<19 :
        y += 1
        
    win.move(y, x)
    
    
    if key == ord(' '):
        trace = not(trace)
        
    if trace:
        #char = changeTile(win, level)
        if level[y][x] != ' ':
            level[y][x] = ' '
        else:
            level[y][x] = '+'
            
        changeAllTiles(win, level)


    return trace


def changeAllTiles(win, level):
    
    for x in range(69):
        for y in range(21):
            if level[y][x] != ' ':
            
            
                c1, c2, c3, c4 = ' ', ' ', ' ', ' '
            
            
                if y > 0 :
                    c1 = level[y-1][x]
                if x < 68 :
                    c2 = level[y][x+1]
                if y < 20 :
                    c3 = level[y+1][x]
                if x > 0 :
                    c4 = level[y][x-1]
        
                if (c1 != ' ' and (c2 != ' ' or c4 != ' ')) or (c3 != ' ' and (c2 != ' ' or c4 != ' ')) or c1+c2+c3+c4 == '    ' :
                    char = '+'
                if (c1 != ' ' and c2 == ' ' and c4 == ' ') or (c3 != ' ' and c2 == ' ' and c4 == ' '):
                    char = '|'
                if (c2 != ' ' and c1 == ' ' and c3 == ' ') or (c4 != ' ' and c1 == ' ' and c3 == ' '):
                    char = '-'
                level[y][x] = char
    return




# inutilise, remplacee par chageAllTiles()
"""
def changeTile(win, level):

    (y, x) = win.getyx()
    
    for i in range(5):
        
        # chagement de case suivant le numero de la boucle
        if i == 1:
            y -= 1
        if i == 2:
            y += 2
        if i == 3:
            y -= 1
            x -= 1
        if i == 4:
            x += 2
        
        
        if i == 0 and level[y][x] != ' ':
            char = ' '
        
        if level[y][x] != ' ' or (i == 0 and level[y][x] == ' '):
            
            
            c1, c2, c3, c4 = ' ', ' ', ' ', ' '
            
            
            if y > 1 :
                c1 = level[y-1][x]
            if x < 67 :
                c2 = level[y][x+1]
            if y < 19 :
                c3 = level[y+1][x]
            if x > 1 :
                c4 = level[y][x-1]
        
            if (c1 != ' ' and (c2 != ' ' or c4 != ' ')) or (c3 != ' ' and (c2 != ' ' or c4 != ' ')) or c1+c2+c3+c4 == '    ' :
                char = '+'
            if (c1 != ' ' and c2 == ' ' and c4 == ' ') or (c3 != ' ' and c2 == ' ' and c4 == ' '):
                char = '|'
            if (c2 != ' ' and c1 == ' ' and c3 == ' ') or (c4 != ' ' and c1 == ' ' and c3 == ' '):
                char = '-'
            level[y][x] = char
    
    return
"""
        
        

def saveLevel(level):

    fichier = open("levels.txt", 'r')
    chaine = fichier.read()
    levels = chaine.split("level")
    levelNumber = len(levels)+1
    fichier.close()
    
    fichier = open("levels.txt", 'a')
    m = len(level)
    n = len(level[1])
    
    fichier.write("level\n")
    for i in range(m-1):
        s = ""
        for j in range(n):
            s = s + level[i][j]
        fichier.write(s + "\n")
    return









def quit(win):

    # Restore la fenetre du terminal
    win.erase()
    curses.echo()
    curses.endwin()
    return
    
    
    

def main():

    trace = False
    win = init()
    level = loadNew()
    stop = 0
    while not(stop) :
        showLevel(win, level)
        key = win.getch()
        if key == ord('\n'):
            stop = 1
        trace = action(win, level, key, trace)
    saveLevel(level)
    quit(win)
    return
    
    
main()

