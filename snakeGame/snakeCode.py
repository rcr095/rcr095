from tkinter import *
import time
import random

window = Tk()
mapa = Canvas(window, width = 1280, height = 720, bg = 'white')
mapa.pack()
style = font.Font(size = 40, weight= 'bold')

timeGone=0

# Creates list of values between 20 and 1240
x = 0
possibleX = []
while x < 1240:
    x = x + 20
    possibleX.append(x)


# Creates list of values between 20 and 680
y = 0
possibleY = []
while y < 680:
    y = y + 20
    possibleY.append(y)

class Snake:
    ''' Main class For Snake, allows movement controll and incresing the snake size. '''
    def __init__(self, x1, y1):
        global snake, tailist, size
        snake = mapa.create_rectangle(x1, y1, x1+20, y1+20, fill = 'yellow')
        size = 0
        tailist = []
        
    def update(self, xs, ys):
        x1,y1,x2,y2 = mapa.coords(snake)
        mapa.coords(snake, x1+xs, y1+ys, x2+xs, y2+ys)
    # Increses Size
    def tail(self, x1,y1):
        global tailist, size
        name = 'tail'+str(size)
        tailist.append(name)
        tailist[size] = mapa.create_rectangle(x1, y1, x1+20, y1+20, fill = 'black')
        size = size + 1
    # Movement Controll
    def mv(self,direction ,i):
        global tailist, snake
               
        if direction == 'up':
            for x in range(len(tailist)-1,0,-1):
                x1,y1,x2,y2 = mapa.coords(tailist[x-1])
                mapa.coords(tailist[x],x1,y1,x2,y2)
            x1,y1,x2,y2 = mapa.coords(snake)
            mapa.coords(snake,x1,y1-i,x2,y2-i) 
            mapa.coords(tailist[0],x1,y1,x2,y2)
            mapa.update()
                
        elif direction == 'down':
            for x in range(len(tailist)-1,0,-1):
                x1,y1,x2,y2 = mapa.coords(tailist[x-1])
                mapa.coords(tailist[x],x1,y1,x2,y2)
            x1,y1,x2,y2 = mapa.coords(snake)
            mapa.coords(snake,x1,y1+i,x2,y2+i) 
            mapa.coords(tailist[0],x1,y1,x2,y2)
            mapa.update()
                
        elif direction == 'left':
            for x in range(len(tailist)-1,0,-1):
                x1,y1,x2,y2 = mapa.coords(tailist[x-1])
                mapa.coords(tailist[x],x1,y1,x2,y2)
            x1,y1,x2,y2 = mapa.coords(snake)
            mapa.coords(snake,x1-i,y1,x2-i,y2) 
            mapa.coords(tailist[0],x1,y1,x2,y2)
            mapa.update()
        elif direction == 'right':
            for x in range(len(tailist)-1,0,-1):
                x1,y1,x2,y2 = mapa.coords(tailist[x-1])
                mapa.coords(tailist[x],x1,y1,x2,y2)
            x1,y1,x2,y2 = mapa.coords(snake)
            mapa.coords(snake,x1+i,y1,x2+i,y2) 
            mapa.coords(tailist[0],x1,y1,x2,y2)
            mapa.update()
     
class Food(Snake):
    '''Food class inherits Snake class, spawns new food, deletes food used and 
        check if snake went through any food.'''
    def __init__(self, x1, y1):
        global food1, foodCount,foodDic
        nameX = str(int(x1))+str(int(y1))
        foodCount = 0
        food1 = mapa.create_rectangle(x1+2, y1+2, x1+18, y1+18, fill = 'red')
        foodCount = foodCount + 1
        foodDic = {}
        foodDic[nameX]=food1
    #Creates New Food
    def newFood(self, x1, y1):
        global food1, food2, food3, foodCount,foodDic
        nameX = str(int(x1))+str(int(y1))
        if foodCount == 0:
            food1 = mapa.create_rectangle(x1+2, y1+2, x1+18, y1+18, fill = 'red')
            foodCount = foodCount + 1
            foodDic[nameX] = food1
        elif foodCount == 1:
            food2 = mapa.create_rectangle(x1+2, y1+2, x1+18, y1+18, fill = 'red')
            foodCount = foodCount + 1
            foodDic[nameX] = food2
        elif foodCount == 2:
            food3 = mapa.create_rectangle(x1+2, y1+2, x1+18, y1+18, fill = 'red')
            foodCount = foodCount + 1
            foodDic[nameX] = food3
    # Deletes Food   
    def eaten(self, eaten):
        global tailist, foodCount
        mapa.delete(eaten)
        foodCount = foodCount - 1       

class Game(Food):
    
    '''Game class inherits Food class, allows the game to be paused, controlls through the keyboard,
        starts the game and checks if the position of the snake, ends the game.'''
    def __init__(self):
        self.state = 'on'
        self.direction = 'down'
        self.bind()
        self.vel=0.40
        
    def game(self, event):
        if self.state == 'off':
            self.state = 'on'
        elif self.state == 'on':
            self.state = 'off'
        self.play()

    def direct(self, now):
        self.direction = now
    
    def up(self,event):
        if self.direction != 'down':
            self.direct('up')
    def down(self,event):
        if self.direction != 'up':
            self.direct('down')
    def right(self,event):
        if self.direction != 'left':
            self.direct('right')
    def left(self,event):
        if self.direction != 'right':
            self.direct('left')

    def bind(self):
        mapa.bind('<Up>', self.up)
        mapa.bind('<Down>', self.down)
        mapa.bind('<Right>', self.right)
        mapa.bind('<Left>', self.left)
        mapa.bind('<Return>', self.game)
        mapa.focus_set()
    # Moves Snake, while cheking snake position
    def play(self):
        global timeGone, possibleX, possibleY, tailist, foodDic
        while self.state == 'on':
            self.mv(self.direction,20)
            time.sleep(self.vel)
            timeGone = timeGone + 1
            if self.killCheck() == 'black':
                self.kill()
            elif self.killCheck() == 'red':
                x1,y1,x2,y2 = mapa.coords(tailist[len(tailist)-1])
                #self.newFood(random.choice(possibleX), random.choice(possibleY))
                self.tail(x1-20,y1-20)
                x1,y1,x2,y2 = mapa.coords(snake)
                nameX = str(int(x1))+str(int(y1))
                self.eaten(foodDic[nameX])
                if self.vel >0.05:
                    self.vel = self.vel - 0.01
            mapa.update()
            if timeGone == 10:
                timeGone = 0
                self.newFood(random.choice(possibleX), random.choice(possibleY))
        
    def killCheck(self):
        global snake,strt
        x1,y1,x2,y2=mapa.coords(snake)
        for id in mapa.find_overlapping(x1+8,y1+8,x2-8,y2-8):
            callcolor = mapa.itemcget(id, 'fill')

        return callcolor
    def kill(self):
        global tailist,snake, restart, food1, food2, food3
        self.game('<Return>')
        mapa.delete(snake)
        for entry in tailist:
            mapa.delete(entry)
        for key in foodDic:
            self.eaten(foodDic[key])
        restart = Button(mapa, text = 'GAMEOVER \n Press To Play Again', bg = 'white', command = strt,
                         font = style)
        restart.place(x=640, y=360, anchor = CENTER, height = 400, width = 800)

# Function that allows game start.
def strt():
    global restart, tailist,possibleX,possibleY
    try:
        restart.destroy()
        snake = Snake(40,60)
        snake.tail(40,40)
        play = Game()
        snake.mv(play.direction,20)
        g = Food(random.choice(possibleX), random.choice(possibleY))
        mapa.create_rectangle(0, 0, 18, 720, fill = 'black')
        mapa.create_rectangle(0, 0, 1280, 18, fill = 'black')
        mapa.create_rectangle(0, 702, 1280, 720, fill = 'black')
        mapa.create_rectangle(1262, 0, 1280, 720, fill = 'black')
        play.play()

    except NameError:
        snake = Snake(40,60)
        snake.tail(40,40)
        play = Game()
        snake.mv(play.direction,20)
        g = Food(random.choice(possibleX), random.choice(possibleY))
        mapa.create_rectangle(0, 0, 18, 720, fill = 'black')
        mapa.create_rectangle(0, 0, 1280, 18, fill = 'black')
        mapa.create_rectangle(0, 702, 1280, 720, fill = 'black')
        mapa.create_rectangle(1262, 0, 1280, 720, fill = 'black')
        play.play()

# Automatically starts game.
strt()

window.mainloop()
