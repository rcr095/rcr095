import random
import tkinter as tk
from tkinter import font

class Board:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Sudoku by rcr095')
        self.createFrame()
        for i in range(3):
            for j in range(3):
                self.createQuad(i, j)

    def createFrame(self):
        self.boldStyle = tk.font.Font(size = 20, weight = 'bold')
        self.frame = tk.Canvas(self.window, height = 540, width = 540,
                                    bg = 'black')
        self.frame.grid(columnspan = 3, rowspan = 3,
                        sticky = tk.N+tk.E+tk.S+tk.W)

    def createQuad(self, row, column):
        self.quad = tk.Canvas(self.window, width = 90, height = 90)
        self.quad.grid(column = column, row = row, sticky = tk.N+tk.E+tk.S+tk.W)
        self.quad.config( highlightbackground = 'black')
        self.quad.cellwidth = 30
        self.quad.cellheight = 30



if __name__ == '__main__':
    a = Board()
    a.window.mainloop()
