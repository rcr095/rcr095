import time, tkinter, random
from tkinter import font
class Snake():

    def __init__(self, width, height):
        self.foodTime = 0
        self.width = width
        self.height = height
        self.start()
        self.size = 0
        self.bodyList = []
        self.frame.update()
        self.startGameC()
        self.startBt()


    def start(self):
        self.window = tkinter.Tk()
        self.window.title('Snake by rcr095')
        self.style = tkinter.font.Font(size = 20, weight = 'bold')
        self.frame = tkinter.Canvas(self.window, width = self.width,
                                    height = self.height, bg = 'white')
        self.frame.create_rectangle(0, 0, 18, self.height, fill = 'black')
        self.frame.create_rectangle(0, 0, self.width, 18, fill = 'black')
        self.frame.create_rectangle(0, self.height - 18, self.width,
                                    self.height, fill = 'black')
        self.frame.create_rectangle(self.width - 18, 0, self.width,
                                    self.height, fill = 'black')
        self.head = self.frame.create_rectangle(40, 60, 60, 80, fill = 'yellow', outline = 'blue')

        self.frame.pack()

    def startBt(self):
        self.startBt = tkinter.Button(self.frame, text = 'Press to Play', bg = 'white',
                         font = self.style)
        self.startBt.configure(command = self.startGame)
        self.startBt.place(x = self.width//2, y = self.height//2,
                           anchor = tkinter.CENTER, width = self.width - 36,
                           height = self.height - 36)      

    def body(self):
        bodyID = 'body' + str(self.size)
        self.bodyList.append(bodyID)
        self.bodyList[self.size] = self.frame.create_rectangle(40, 40, 60, 60, fill = 'black',
                                                               outline = 'white')
        self.size += 1

    def move(self):
        i = 20
        if self.direction == 'up':
            for x in range(len(self.bodyList) - 1, 0, -1):
                x1, y1, x2, y2 = self.frame.coords(self.bodyList[x - 1])
                self.frame.coords(self.bodyList[x], x1, y1, x2, y2)
            x1, y1, x2, y2 = self.frame.coords(self.head)
            self.frame.coords(self.head, x1, y1 - i, x2, y2 - i)
            self.frame.coords(self.bodyList[0], x1, y1, x2, y2)
            self.frame.update()

        elif self.direction == 'down':
            for x in range(len(self.bodyList) - 1, 0, -1):
                x1, y1, x2, y2 = self.frame.coords(self.bodyList[x - 1])
                self.frame.coords(self.bodyList[x], x1, y1, x2, y2)
            x1, y1, x2, y2 = self.frame.coords(self.head)
            self.frame.coords(self.head, x1, y1 + i, x2, y2 + i)
            self.frame.coords(self.bodyList[0], x1, y1, x2, y2)
            self.frame.update()

        elif self.direction == 'left':
            for x in range(len(self.bodyList) - 1, 0, -1):
                x1, y1, x2, y2 = self.frame.coords(self.bodyList[x - 1])
                self.frame.coords(self.bodyList[x], x1, y1, x2, y2)
            x1, y1, x2, y2 = self.frame.coords(self.head)
            self.frame.coords(self.head, x1 - i, y1, x2 - i, y2)
            self.frame.coords(self.bodyList[0], x1, y1, x2, y2)
            self.frame.update()

        elif self.direction == 'right':
            for x in range(len(self.bodyList) - 1, 0, -1):
                x1, y1, x2, y2 = self.frame.coords(self.bodyList[x - 1])
                self.frame.coords(self.bodyList[x], x1, y1, x2, y2)
            x1, y1, x2, y2 = self.frame.coords(self.head)
            self.frame.coords(self.head, x1 + i, y1, x2 + i, y2)
            self.frame.coords(self.bodyList[0], x1, y1, x2, y2)
            self.frame.update()

    def startFoodC(self, x, y):
        nameX = str(int(x)) + str(int(y))
        self.food1 = self.frame.create_rectangle(x + 2, y + 2, x + 18, y + 18,
                                                 fill = 'red')
        self.foodCount = 1
        self.foodDic = {nameX:self.food1}

    def newFood(self, x, y):
        
        if self.foodCount == 0:
            nameX = str(int(x)) + str(int(y))
            self.food1 = self.frame.create_rectangle(x + 2, y + 2, x + 18, y + 18,
                                                 fill = 'red')
            self.foodCount += 1
            self.foodDic[nameX] = self.food1

        elif self.foodCount == 1:
            nameX = str(int(x)) + str(int(y))
            self.food2 = self.frame.create_rectangle(x + 2, y + 2, x + 18, y + 18,
                                                 fill = 'red')
            self.foodCount += 1
            self.foodDic[nameX] = self.food2

        elif self.foodCount == 2:
            nameX = str(int(x)) + str(int(y))
            self.food3 = self.frame.create_rectangle(x + 2, y + 2, x + 18, y + 18,
                                                 fill = 'red')
            self.foodCount += 1
            self.foodDic[nameX] = self.food3

    def eaten(self, eaten):
        self.frame.delete(eaten)
        self.foodCount -= 1

    def startGameC(self):
        self.state = 'on'
        self.direction = 'down'
        self.control()
        self.vel = 0.1
        self.possPos()

    def game(self, event):
        if self.state == 'off':
            self.state = 'on'

        elif self.state == 'on':
            self.state = 'off'
        self.play()

    def up(self, event):
        if self.direction != 'down' and self.checkBody0('up') == 0:
            self.direction = 'up'
            

    def down(self, event):
        if self.direction != 'up' and self.checkBody0('down') == 0:
            self.direction = 'down'        

    def right(self, event):
        if self.direction != 'left' and self.checkBody0('right') == 0:
            self.direction = 'right'

    def left(self, event):
        if self.direction != 'right' and self.checkBody0('left') == 0:
            self.direction = 'left'

    def checkBody0(self, direction):
        try:
            x1,y1,x2,y2 = self.frame.coords(self.bodyList[0])
            hx1,hy1,hx2,hy2 = self.frame.coords(self.head)
            if direction == 'up':
                if hy1 - 20 == y1:
                    return 1
                return 0
                
            elif direction == 'down':
                if hy2 + 20 == y2:
                    return 1
                return 0
                
            elif direction == 'right':
                if hx2 + 20 == x2:
                    return 1
                return 0
                
            elif direction == 'left':
                if hx1 - 20 == x1:
                    return 1
                return 0
        except IndexError:
            return 0
        
    def control(self):
        self.frame.bind('<Up>', self.up)
        self.frame.bind('<Down>', self.down)
        self.frame.bind('<Right>', self.right)
        self.frame.bind('<Left>', self.left)
        self.frame.bind('<Return>', self.game)
        self.frame.focus_set()

    def possPos(self): #create list of possible positions for 'food'
        self.possX = []
        self.possY = []
        x = 0
        y = 0
        
        while x < self.width - 40:
            x += 20
            self.possX.append(x)

        while y < self.height - 40:
            y += 20
            self.possY.append(y)

    def play(self):
        try:
            while self.state == 'on':
                self.move()
                time.sleep(self.vel)
                self.foodTime += 1
                if self.foodTime > 20:
                    self.newFood(random.choice(self.possX), random.choice(self.possY))
                    self.foodTime = 0
                self.frame.update()
                self.killCheck()
        except:
            return 0
    def killCheck(self):
        x1, y1, x2, y2 = self.frame.coords(self.head)
        for id in self.frame.find_overlapping(x1 + 8, y1 + 8, x2 - 8, y2 - 8):
            color = self.frame.itemcget(id, 'fill') 
            if color == 'black':
                self.kill()
            elif color == 'red':
                self.body()
                x1, y1, x2, y2 = self.frame.coords(self.head)
                nameX = str(int(x1)) + str(int(y1))
                self.eaten(self.foodDic[nameX])
                if self.vel > 0.04:
                    self.vel -= 0.0001

    def kill(self):
        self.game('<Return>')
        self.frame.delete(self.head)
        for entry in self.bodyList:
            self.frame.delete(entry)
        self.bodyList = []
        self.size = 0
        for key in self.foodDic:
            self.eaten(self.foodDic[key])
        self.restartBt = tkinter.Button(self.frame, text = 'Gameover \n Press to Play',
                         bg = 'white', command = self.restartGame,
                         font = self.style)
        self.restartBt.place(x = self.width//2, y = self.height//2,
                           anchor = tkinter.CENTER, width = self.width - 36,
                           height = self.height - 36)

    def restartGame(self):
        self.restartBt.destroy()
        self.foodTime = 0
        self.size = 0
        self.head = self.frame.create_rectangle(40, 60, 60, 80, fill = 'yellow', outline = 'blue')
        self.bodyList = []
        self.frame.update()
        self.startGameC()
        self.body()
        self.move()
        self.startGameC()
        self.startFoodC(random.choice(self.possX), random.choice(self.possY))
        self.play()

    def startGame(self):
        self.startBt.destroy()
        self.body()
        self.move()
        self.startGameC()
        self.startFoodC(random.choice(self.possX), random.choice(self.possY))
        self.play()


def playSnake(width, height):
    game = Snake(width, height)
    game.window.mainloop()

playSnake(500,500)


    
        
